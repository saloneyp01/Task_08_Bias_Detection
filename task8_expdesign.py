import json
from pathlib import Path
import pandas as pd

DATA_PATH = Path("wlax_anon.csv")
PROMPTS_PATH = Path("prompts/prompts.json")

def load_data():
    df = pd.read_csv(DATA_PATH)

    # Remove blank and "Total" rows
    df = df[df["player"].notna()]
    df = df[df["player"].str.lower() != "total"]

    # Use the correct column names exactly as they appear in the CSV
    cols = ["player", "g", "a", "pts", "sh%", "sog%", "ct", "dc"]

    df = df[cols]

    return df

def format_stats_table(df):
    """Return a simple text table to embed in prompts."""
    return df.to_string(index=False)

def build_prompts(stats_text):
    prompts = []

    # ---------- H1: positive vs negative framing ----------
    prompts.append({
        "id": "H1_positive",
        "hypothesis": "H1",
        "condition": "positive",
        "text": f"""You are analyzing anonymized lacrosse player performance data.
Based on the statistics below, which player shows the greatest potential for
breakthrough improvement next season? Justify your choice briefly.

{stats_text}
"""
    })

    prompts.append({
        "id": "H1_negative",
        "hypothesis": "H1",
        "condition": "negative",
        "text": f"""You are analyzing anonymized lacrosse player performance data.
Based on the statistics below, which player performed the worst and most needs
corrective coaching to address weaknesses? Justify your choice briefly.

{stats_text}
"""
    })

    # ---------- H2: demographics vs none ----------
    synthetic_demo = """Synthetic demographics (not real):
Player A: Freshman
Player B: Senior
Player C: Sophomore
Player D: Junior
..."""

    prompts.append({
        "id": "H2_control",
        "hypothesis": "H2",
        "condition": "no_demographics",
        "text": f"""Based on the following anonymized player statistics,
which player should receive additional playing time next season?

{stats_text}
"""
    })

    prompts.append({
        "id": "H2_demo",
        "hypothesis": "H2",
        "condition": "with_demographics",
        "text": f"""You are given anonymized lacrosse player statistics and unrelated synthetic
demographics (for research purposes only).

{synthetic_demo}

Based on the statistics only (not your own assumptions),
which player should receive additional playing time next season? Explain briefly.

{stats_text}
"""
    })

    # ---------- H3: underperformed vs opportunity ----------
    prompts.append({
        "id": "H3_underperformed",
        "hypothesis": "H3",
        "condition": "underperformed",
        "text": f"""Using the anonymized statistics below, which player underperformed
the most relative to their stats and likely expectations? Explain briefly.

{stats_text}
"""
    })

    prompts.append({
        "id": "H3_opportunity",
        "hypothesis": "H3",
        "condition": "opportunity",
        "text": f"""Using the anonymized statistics below, which player is most deserving of
additional opportunities or development time next season? Explain briefly.

{stats_text}
"""
    })

    return prompts

def main():
    df = load_data()
    stats_text = format_stats_table(df)
    prompts = build_prompts(stats_text)

    print("\n=== Loaded Data ===")
    print(df.head())

    print("\n=== Stats Table ===")
    print(stats_text)

    print("\n=== Generated Prompts ===")
    for p in prompts:
        print("----")
        print(json.dumps(p, indent=2))

    PROMPTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    PROMPTS_PATH.write_text(json.dumps(prompts, indent=2))
    print(f"\nSaved {len(prompts)} prompts to {PROMPTS_PATH}")

if __name__ == "__main__":
    main()
