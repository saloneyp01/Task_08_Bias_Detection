import re
from pathlib import Path

import pandas as pd

DATA_PATH = Path("wlax_anon.csv")
RESPONSES_DIR = Path("responses")
RESULTS_DIR = Path("results")


def extract_player(text: str):
    """Return 'Player X' or None."""
    m = re.search(r"Player\s+([A-Z]{1,2})", text)
    if not m:
        return None
    return f"Player {m.group(1)}"


def extract_number(label: str, text: str):
    """
    Extract a number followed by a phrase, e.g.
    label='draw controls'  -> matches '39 draw controls'
    label='caused turnovers' -> matches '11 caused turnovers'
    """
    pattern = rf"(\d+)\s+{label}"
    m = re.search(pattern, text)
    return int(m.group(1)) if m else None


def main():
    if not DATA_PATH.exists():
        print(f"[WARN] Data file not found: {DATA_PATH}")
        return

    if not RESPONSES_DIR.exists():
        print("[WARN] responses/ folder not found.")
        return

    RESULTS_DIR.mkdir(exist_ok=True)

    stats = pd.read_csv(DATA_PATH)

    records = []
    for path in RESPONSES_DIR.glob("*.txt"):
        text = path.read_text()
        player = extract_player(text)
        if player is None:
            continue

        rec = {
            "file": path.name,
            "player": player,
        }

        # stats for that player
        gt = stats.loc[stats["player"] == player]
        if not gt.empty:
            gt_row = gt.iloc[0]
            rec["g_true"] = gt_row.get("g")
            rec["a_true"] = gt_row.get("a")
            rec["pts_true"] = gt_row.get("pts")
            rec["ct_true"] = gt_row.get("ct")
            rec["dc_true"] = gt_row.get("dc")
        else:
            rec["g_true"] = rec["a_true"] = rec["pts_true"] = None
            rec["ct_true"] = rec["dc_true"] = None

        # claimed numbers
        rec["ct_claimed"] = extract_number("caused turnovers", text)
        rec["dc_claimed"] = extract_number("draw controls", text)

        # consistency flags
        if rec["ct_true"] is not None and rec["ct_claimed"] is not None:
            rec["ct_matches"] = rec["ct_true"] == rec["ct_claimed"]
        else:
            rec["ct_matches"] = None

        if rec["dc_true"] is not None and rec["dc_claimed"] is not None:
            rec["dc_matches"] = rec["dc_true"] == rec["dc_claimed"]
        else:
            rec["dc_matches"] = None

        records.append(rec)

    df = pd.DataFrame(records)
    print("=== Claim checks ===")
    print(df)

    out_path = RESULTS_DIR / "claim_checks.csv"
    df.to_csv(out_path, index=False)
    print(f"\nSaved validation results to {out_path}")


if __name__ == "__main__":
    main()
