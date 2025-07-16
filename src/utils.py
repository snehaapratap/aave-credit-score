def extract_amount(df):
    def parse_amount(row):
        data = row.get("actionData", {})
        if isinstance(data, dict) and "amount" in data:
            try:
                return float(data["amount"])
            except Exception:
                return 0
        return 0
    df["amount"] = df.apply(parse_amount, axis=1)
    return df
