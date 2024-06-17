# Seasonal Investing Strategy

by Stefan Erben, DIFA 2022/23

## Introduction

In this project, I explored the concept of seasonal investing and test its potential success in the stock market. Seasonal investing is a strategy that involves buying and selling stocks based on the time of year, based on the belief that certain stocks tend to perform better during specific seasons.

## Seasonal Investing

Seasonal investing is based on the idea that certain sectors or stocks have predictable patterns of performance throughout the year. For example, retail and tourism stocks may perform better in summer, while energy stocks may perform better in winter. This strategy aims to take advantage of these patterns to optimize portfolio returns.

### Benefits:
- **Predictable Patterns:** Seasonal investing leverages predictable market trends.
- **Diversification:** By rotating investments through different sectors, it reduces the reliance on a single industry, potentially lowering risk.

### Drawbacks:
- **Market Unpredictability:** The stock market can be unpredictable, and seasonal trends may not always hold.
- **Research Required:** Thorough research and analysis are necessary to identify suitable investments.
- **Additional Costs:** Transaction fees, taxes, and the exclusion of dividends can impact overall returns.

## Goal

The goal of this project is to determine whether seasonal investing is a viable strategy for maximizing returns. The strategy involves investing in the general market (represented by the Dow Jones) during most of the year and switching to individual consumer-market stocks during the winter. This approach tests the hypothesis that a seasonal investing strategy can outperform the general market.

## Limitations

1. **Fractional Shares:** Not all brokers support fractional shares, limiting the applicability of results for some investors.
2. **Transaction Costs:** Transaction fees are not accounted for, which can significantly impact returns.
3. **Dividends:** This strategy does not consider dividends, potentially underestimating returns.
4. **Capital Taxes and Fees:** Taxes and fees incurred from selling positions are not considered.

## Code Structure

1. **Installing pip libraries**
2. **Definition of functions**: Each function is documented for clarity.
3. **Parameterization of the strategy**
4. **Trading Strategy**
5. **Visualization of the results**

## Installing pip libraries

```python
!pip install yfinance
!pip install yahoo-fin
```

## Definition of Functions

- **download_data:** Downloads historical stock data for all symbols and saves it in pickle files.
- **get_index:** Retrieves all stock symbols for a given index (e.g., S&P 500).
- **get_stock_type:** Returns the category of a given stock symbol.
- **get_price_for_symbol:** Returns the price of a stock for a given date.
- **buy_position:** Buys a stock and adds it to the portfolio.
- **sell_position:** Sells a stock and removes it from the portfolio.
- **liquidate_positions:** Sells all open positions in the portfolio.
- **buy_into_positions:** Buys specified amounts of stocks for each symbol.
- **calculate_portfolio_value:** Calculates the portfolio value for a given date.

## Parameterization of the Strategy

The strategy involves changing holdings twice a year:
- **Consumer Markets:** From November to March.
- **General Market:** From March to November.

### Initial Setup
- **Starting Date:** June 1, 2012
- **Ending Date:** Current date
- **Initial Portfolio Value:** $100,000

### Data Download
```python
all_symbols = get_index("dowjones")
all_symbols.extend(get_index("dowjones-consumer"))
download_data(all_symbols, starting_date)
```

## Trading Strategy

### Initial Investment
Invest in the general market initially.

### Monthly Evaluation
Evaluate and adjust holdings on the first of each month:
- **November 1:** Switch to consumer market stocks.
- **March 1:** Switch back to the general market.

## Visualization of the Results

### Results Summary
```python
end_balance_general = timeline["general"]["value"][-1]
end_balance_seasonal = timeline["seasonal"]["value"][-1]

diff_general = (end_balance_general - inital_portfolio_value) / inital_portfolio_value * 100
diff_seasonal = (end_balance_seasonal - inital_portfolio_value) / inital_portfolio_value * 100

years = (ending_date.year - starting_date.year) + (ending_date.month - starting_date.month) / 12
yearly_return_general = (end_balance_general / inital_portfolio_value) ** (1 / years) - 1
yearly_return_seasonal = (end_balance_seasonal / inital_portfolio_value) ** (1 / years) - 1

print("*** General portfolio ***")
print(f"Portfolio value: ${end_balance_general:.2f} USD")
print(f"Total return: {diff_general:.2f} %")
print(f"Yearly return: {yearly_return_general * 100:.2f} %\n")

print("*** Seasonal portfolio ***")
print(f"Portfolio value: ${end_balance_seasonal:.2f} USD")
print(f"Total return: {diff_seasonal:.2f} %")
print(f"Yearly return: {yearly_return_seasonal * 100:.2f} %")
```

### Final Output
- **General Portfolio:**
  - Portfolio value: $344,496.26 USD
  - Total return: 244.5%
  - Yearly return: 12.4%

- **Seasonal Portfolio:**
  - Portfolio value: $369,804.30 USD
  - Total return: 269.8%
  - Yearly return: 13.15%

## License

This project is licensed under the MIT License.
