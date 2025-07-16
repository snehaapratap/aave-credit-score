
# Aave Credit Scoring Engine 🏦

**Predictive Credit Scoring for DeFi Wallets on Aave V2**

This project builds a robust machine learning pipeline to analyze on-chain behavior of DeFi wallets and assign them a credit score between **0 and 1000**, where:
- **0** indicates highly risky or exploitative behavior (e.g., liquidation, no repayment)
- **1000** indicates trustworthy users with long-term, healthy financial activity

> Designed for large-scale scoring of wallets, this engine helps identify high-quality users for credit delegation, reward programs, or lending strategies in decentralized finance.

---

## 🚀 Project Highlights

- ✅ Processes raw Aave V2 transaction data (~87MB JSON)
- ✅ Feature engineering on borrow/deposit/repay actions, volumes, liquidation, activeness
- ✅ Trains a scaled, interpretable scoring model using unsupervised standardization
- ✅ Outputs ranked credit scores for 3,497 wallets
- ✅ Includes automated analysis and visualizations

---

## 📁 Folder Structure

```

aave-credit-score/
├── data/
│   └── user-wallet-transactions.json   # Raw Aave V2 data
├── outputs/
│   ├── wallet_scores.csv               # Final scored wallet CSV
│   └── score_distribution.png          # Score histogram
├── src/
│   ├── score_wallets.py                # Main scoring script
│   ├── data_loading.py                 # JSON parsing logic
│   ├── feature_engineering.py          # Feature extraction
│   ├── model.py                        # Credit scoring model logic
│   └── utils.py                        # Helper: amount extraction
├── README.md                           
└── analysis.md                         # Score insights + wallet behavior

````

---

## 📊 Methodology

### 1. **Feature Engineering**

We extract behavioral features per wallet based on:
- `deposit`, `borrow`, `repay`, `redeemunderlying`, `liquidationcall`
- Total and per-action transaction volume
- Lifetime in days
- Borrow-to-repay ratio
- Liquidation rate
- Daily transaction frequency

### 2. **Scoring Strategy**

Since we lack labeled credit outcomes, we use:
- **Standardized Z-score normalization**
- Weighted aggregation of positive (e.g., repay volume, tx_per_day) and negative indicators (e.g., liquidation rate)
- Final score scaled between **0–1000**

---

## 🛠 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
````

### 2. Run scoring script

```bash
python3 src/score_wallets.py \
    --input data/user-wallet-transactions.json \
    --output outputs/wallet_scores.csv
```


---

## 📈 Output Preview

| Wallet      | Score |
| ----------- | ----- |
| 0xabc...123 | 987   |
| 0xdef...456 | 215   |
| 0xghi...789 | 742   |

---

## 📑 Deliverables

* ✅ `wallet_scores.csv`: Final score for each wallet
* ✅ `analysis.md`: Score insights, behavioral band analysis
* ✅ `score_distribution.png`: Visual histogram of wallet scores
* ✅ `README.md`: This file – full methodology + usage

---

## 🧠 Future Extensions

* Fine-tune model using real repayment defaults if labeled data is introduced
* Support other DeFi protocols (Compound, MakerDAO)
* Use graph-based wallet clustering
* Integrate chain-agnostic scoring using cross-chain wallet identity

---

## 📬 Contact

Made by **Sneha Prem Pratap**
For any questions or extensions, feel free to connect.

---

