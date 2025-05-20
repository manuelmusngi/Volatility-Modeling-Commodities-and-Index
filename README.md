#### Volatility-Modeling-Index-and-Commodities

This application is a replication of the volatility models used in a research paper that aimed to model and forecast the volatility of key energy and equity markets using advanced GARCH-family models. Leveraging the research paper’s methodology, the application implements a suite of volatility models including EGARCH, FIGARCH, and others to capture the dynamic and nonlinear behavior of financial returns in markets like crude oil (WTI), natural gas (Henry Hub), and the S&P 500 Index. 

The core functionality of this application includes:

- Forecasting conditional volatility:\
  Utilizing models such as EGARCH and FIGARCH, the application provides rolling out-of-sample forecasts of volatility, adapting to market shifts and clustering effects that standard models may overlook. 

- Modeling asymmetry and long memory:\
  As demonstrated in the paper, natural gas and crude oil exhibit volatility asymmetry (leverage effects) and long memory. The application captures these features using asymmetric and fractionally integrated models like GJRGARCH and FIAPARCH. 

- Evaluating model performance:\
  The forecasting models are quantitatively assessed using Mean Squared Error (MSE) and Mean Absolute Error (MAE), in line with the paper’s methodology for determining the most accurate model under various market conditions. 

- Comparing behavior across asset classes:\
  By running the same GARCH variants on different markets (energy commodities and equity index), the application enables comparative analysis of volatility structures and sensitivities across asset classes, reflecting the paper’s multi-market approach. 

- Supporting hedging and risk management:\
  Forecasted volatilities can be used to derive optimal hedge ratios, assisting traders, policymakers, and risk managers in making informed decisions—mirroring the practical insights provided in the original study. 

In essence, this application translates the empirical modeling approach of the original research into a computational tool that allows users to explore, visualize, and evaluate volatility patterns in major financial markets using GARCH-family models. By combining robust econometric modeling with real-time financial data, it supports both academic exploration and real-world financial decision-making.

#### Models Applied

For practical implications, I have selected the following models, since investors and fund managers can use EGARCH or FIGARCH models to develop risk-minimizing hedge strategies in energy markets or index.
 
- GARCH (baseline)

- EGARCH (exponential, asymmetric)

- FIGARCH (fractionally integrated)


#### Performance Metrics for Evaluation

- Mean Squared Error (MSE)

- Mean Absolute Error (MAE)

#### Program Structure



#### Dependencies
-

#### Reference
- [Volatility Modelling in Crude Oil and Natural Gas Prices](https://www.sciencedirect.com/science/article/pii/S2212567116302192)
