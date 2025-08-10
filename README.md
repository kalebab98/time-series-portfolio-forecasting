# 📈 Time Series Forecasting for Portfolio Management Optimization

### 🚀 Guide Me in Finance (GMF) Investments – Case Challenge

This project applies time series forecasting techniques to real financial data in order to optimize portfolio performance. The goal is to generate actionable insights using historical data from TSLA, SPY, and BND, and apply these insights to improve risk-adjusted returns for GMF Investments' clients.

---

## 📊 Interim Submission – Task 1: Data Exploration & Preprocessing

### ✅ Task Overview
- Collect and clean historical financial data (TSLA, BND, SPY)
- Perform exploratory data analysis (EDA)
- Calculate key financial metrics: daily returns, volatility, Value at Risk (VaR), Sharpe Ratio
- Conduct stationarity testing for modeling readiness

---

### 📅 Data Source & Period
- **API:** [YFinance](https://pypi.org/project/yfinance/)
- **Date Range:** `2015-07-01` to `2025-07-31`
- **Frequency:** Daily Trading Days
- **Assets:**
  - `TSLA` – High-growth stock
  - `BND` – Bond ETF (stability)
  - `SPY` – S&P 500 ETF (broad market exposure)

---

### 🧹 Data Preprocessing
- Cleaned malformed header rows
- Converted `Date` column to datetime format
- Set `Date` as time-based index
- Checked for missing values and handled them appropriately
- Combined TSLA, BND, and SPY datasets into a unified dataframe

---

### 📈 Descriptive Statistics (Closing Prices)

| Asset | Mean | Std Dev | Min | Max |
|-------|------|---------|-----|-----|
| TSLA  | 131.96 | 120.91 | 9.58 | 479.86 |
| BND   | 68.47  | 4.55   | 60.78 | 77.32 |
| SPY   | 334.19 | 126.43 | 155.87 | 637.10 |

---

### 🔁 Daily Returns Summary

| Metric | TSLA | BND | SPY |
|--------|------|-----|-----|
| Mean Daily Return | 0.1828% | 0.0078% | 0.0575% |
| Std Dev (Volatility) | 3.73% | 0.35% | 1.15% |
| Max Return | +22.69% | +4.22% | +10.50% |
| Min Return | -21.06% | -5.44% | -10.94% |

---

### 📉 30-Day Rolling Volatility (Mean)

| TSLA | BND | SPY |
|------|-----|-----|
| 3.48% | 0.29% | 0.98% |

---

### 🛡️ Risk Metrics

#### Value at Risk (VaR @ 95% confidence)

- **TSLA:** -5.47%
- **SPY:** -1.72%
- **BND:** -0.49%

#### Sharpe Ratios (Annualized)

| Asset | Sharpe Ratio |
|-------|--------------|
| TSLA  | 0.78 |
| SPY   | 0.79 |
| BND   | 0.36 |

---

### 🧪 Stationarity Tests

| Series | p-value | Stationary? |
|--------|---------|-------------|
| Close Prices | > 0.05 | ❌ No |
| Daily Returns | < 0.05 | ✅ Yes |

---

### 📂 Folder Structure

## 📁 Project Structure
```bash
time-series-portfolio-forecasting/
│
├── data/
│ ├── processed/ # Cleaned/merged data
│ ├── combined_cleaned.csv
│ └── daily_returns.csv
│
├── notebooks/
│ └── 01_data_exploration.ipynb # Full Task 1 notebook
│
├── reports/
│ └── interim_report.md # Optional short summary
│
├── src/
│ └── data_loader.py # Script to download YFinance data
│
├── .gitignore # Ignore large files, checkpoints
├── requirements.txt # List of required packages
├── README.md # Project overview
└── LICENSE # (Optional) License file
```
---

### 📌 Next Steps

- ✅ Finalize preprocessing pipeline
- 🚧 Develop ARIMA and LSTM models (Task 2)
- 🚧 Generate TSLA forecasts (Task 3)
- 🚧 Optimize portfolio using MPT (Task 4)
- 🚧 Backtest strategy vs benchmark (Task 5)

---


