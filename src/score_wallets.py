import argparse, pandas as pd, json
from pathlib import Path
from data_loading import load_tx
from feature_eng import make_features
from model import CreditScorer

def main(inp, outp):
    df = load_tx(inp)
    X = make_features(df)
    scorer = CreditScorer().fit(X)
    scores = scorer.predict(X)
    Path(outp).parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame({"wallet": X.index, "score": scores}) \
      .to_csv(outp, index=False)
    print(f"[✓] wrote {outp} ({len(X)} wallets)")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    main(**vars(p.parse_args()))
