import json
import re
from pathlib import Path

import pandas as pd

PROMPTS_PATH = Path("prompts/prompts.json")
RESPONSES_DIR = Path("responses")
RESULTS_DIR = Path("results")


def load_prompt_meta():
    """Load prompt metadata and return a dict keyed by prompt id."""
    prompts = json.loads(PROMPTS_PATH.read_text())
    meta = {
        p["id"]: {
            "hypothesis": p.get("hypothesis"),
            "condition": p.get("condition"),
        }
        for p in prompts
    }
    return meta


def extract_first_player(text: str):
    """
    Example match: 'Player G', 'Player L'
    """
    m = re.search(r"Player\s+([A-Z]{1,2})", text)
    if not m:
        return None
    return f"Player {m.group(1)}"


def main():
    print("=== Loading prompt metadata ===")
    prompt_meta = load_prompt_meta()
    print(f"Loaded {len(prompt_meta)} prompt entries.\n")

    if not RESPONSES_DIR.exists():
        print("[WARN] responses/ folder not found. Nothing to analyze.")
        return

    RESULTS_DIR.mkdir(exist_ok=True)

    rows = []
    for path in RESPONSES_DIR.glob("*.txt"):
        prompt_id = path.stem 
        meta = prompt_meta.get(prompt_id, {})

        text = path.read_text()
        chosen_player = extract_first_player(text)

        rows.append(
            {
                "prompt_id": prompt_id,
                "file": path.name,
                "hypothesis": meta.get("hypothesis"),
                "condition": meta.get("condition"),
                "chosen_player": chosen_player,
            }
        )

    df = pd.DataFrame(rows)
    print("=== Raw choices ===")
    print(df)

    out_path = RESULTS_DIR / "bias_summary.csv"
    df.to_csv(out_path, index=False)
    print(f"\nSaved per-prompt summary to {out_path}")


if __name__ == "__main__":
    main()

