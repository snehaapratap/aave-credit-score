import argparse, pandas as pd, json
from pathlib import Path
from data_loading import load_tx
from feature_eng import make_features
from utils import extract_amount
from model import CreditScorer

def main(input, output):
    df = load_tx(input)
    df = extract_amount(df)  
    X = make_features(df)
    scorer = CreditScorer().fit(X)
    scores = scorer.predict(X)
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame({"userWallet": X.index, "score": scores}) \
      .to_csv(output, index=False)
    print(f"wrote {output} ({len(X)} wallets)")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    main(**vars(p.parse_args()))
