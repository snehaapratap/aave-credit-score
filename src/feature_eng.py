import pandas as pd

_TX_TYPES = ["deposit", "borrow", "repay",
             "redeemunderlying", "liquidationcall"]

def make_features(df: pd.DataFrame) -> pd.DataFrame:
    TX_TYPES = ["deposit", "borrow", "repay", "redeemunderlying", "liquidationcall"]
    g = df.groupby("userWallet")
    feats = pd.DataFrame(index=g.size().index)

    for t in TX_TYPES:
        feats[f"{t}_cnt"] = df[df["action"] == t].groupby("userWallet").size()

    for t in TX_TYPES:
        mask = df["action"] == t
        feats[f"{t}_vol"] = df[mask].groupby("userWallet")["amount"].sum()

    feats["borrow_repay_ratio"] = feats["repay_vol"] / feats["borrow_vol"].replace(0, 1)
    feats["liquidation_rate"] = feats["liquidationcall_cnt"] / g.size()

    df["block_ts"] = pd.to_datetime(df["timestamp"], unit="s", errors="coerce")
    lifespan = df.groupby("userWallet")["block_ts"].agg(["min", "max"])
    feats["lifetime_days"] = (lifespan["max"] - lifespan["min"]).dt.days.clip(lower=1)

    feats["tx_per_day"] = g.size() / feats["lifetime_days"]

    return feats.fillna(0)
