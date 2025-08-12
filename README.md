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

# Task 2: Develop Time Series Forecasting Models

## Objective
To build and compare forecasting models for predicting Tesla (TSLA) stock prices using both classical (ARIMA) and deep learning (LSTM) methods.

---

## Steps Performed

1. **Data Split**
   - Training: July 1, 2015 – December 31, 2023
   - Testing: January 1, 2024 – July 31, 2025

2. **Model 1: ARIMA**
   - Performed stationarity testing (ADF Test).
   - Optimized parameters using `auto_arima`.
   - Evaluated metrics:
     - **MAE**: 62.96
     - **RMSE**: 78.04
     - **MAPE**: 24.04%

3. **Model 2: LSTM**
   - Created a sequential neural network.
   - Trained on scaled windowed sequences.
   - Evaluated metrics:
     - **MAE**: 13.33
     - **RMSE**: 17.31
     - **MAPE**: 5.26%

---

## Insights
- LSTM outperformed ARIMA in all metrics.
- LSTM was selected as the best model for forecasting.

---

## Outputs
- Trained LSTM model (`lstm_model.h5`)
- Evaluation plots (actual vs predicted)
# Task 3: Forecast Future Market Trends

## Objective
To use the trained LSTM model to forecast Tesla's stock prices over the next 6–12 months and analyze risks and opportunities.

---

## Forecasting

- Model: `lstm_model.h5`
- Forecast Range: August 2024 – July 2025
- Forecasted using 30-day windows recursively.
- Generated future prices and plotted with historical data.

---

## Trend Analysis
- Forecast indicates an **upward trend** with fluctuations.
- General trajectory supports growth, consistent with historical momentum.

## Volatility & Risk
- Confidence intervals widen over time, indicating increased uncertainty.
- Implies more reliable short-term predictions than long-term ones.

## Market Opportunities & Risks
- 📈 **Opportunity**: Expected price growth suggests possible gains.
- ⚠️ **Risk**: Forecast confidence drops with time horizon — possible volatility ahead.

---

## Output
- Forecast visualization plot
- JSON/CSV file with forecasted prices
# Task 4: Optimize Portfolio Based on Forecast

## Objective
To apply Modern Portfolio Theory (MPT) and use forecasted TSLA returns with historical BND and SPY data to build an optimal portfolio.

---

## Methodology

1. **Expected Returns**
   - TSLA: Derived from LSTM forecast.
   - BND & SPY: Historical annualized daily returns.

2. **Covariance Matrix**
   - Calculated from daily returns of TSLA, BND, SPY.

3. **Optimization**
   - Used `PyPortfolioOpt` to compute:
     - Efficient Frontier
     - Maximum Sharpe Ratio Portfolio
     - Minimum Volatility Portfolio

---

## Key Portfolios

📌 **Max Sharpe Ratio Portfolio**
- TSLA: 6.3%
- BND: 56%
- SPY: 37.7%
- Return: 8.95%
- Volatility: 10.11%
- Sharpe Ratio: 0.89

📌 **Minimum Volatility Portfolio**
- TSLA: 0%
- BND: 94.5%
- SPY: 5.5%
- Return: 2.65%
- Volatility: 5.4%
- Sharpe Ratio: 0.49

---

## Output
- Efficient Frontier plot
- Saved weights: `task_4_optimal_weights.json`
# Task 5: Strategy Backtesting

## Objective
To validate the forecast-driven optimized portfolio by simulating performance over the last year (August 2024 – July 2025) and comparing it with a benchmark.

---

## Methodology

- Backtest Period: Aug 1, 2024 – Jul 31, 2025
- Strategy Portfolio: From Task 4 Max Sharpe weights
- Benchmark: 60% SPY / 40% BND
- Held weights constant throughout the year

---

## Results

📊 **Strategy Total Return**: 17.10%  
📊 **Benchmark Total Return**: 12.47%

⚖️ **Strategy Sharpe Ratio**: 1.09  
⚖️ **Benchmark Sharpe Ratio**: 1.00

---

## Insights

✅ Strategy portfolio outperformed benchmark in both return and Sharpe Ratio.  
📌 Indicates value in using forecast-driven portfolio allocation.

---

## Outputs

- Cumulative return plot (strategy vs benchmark)
- Performance metrics (Sharpe, return)


