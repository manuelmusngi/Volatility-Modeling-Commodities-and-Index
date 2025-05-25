#### Volatility-Modeling-Commodities-and-Index

This project is about the study of the volatility models used in a research paper that aimed to model and forecast the volatility of key energy and equity index markets using advanced GARCH-family models. Leveraging the research paper’s methodology, this development implements a suite of volatility models including EGARCH, FIGARCH, and others to capture the dynamic and nonlinear behavior of financial returns in markets like crude oil (WTI), natural gas (Henry Hub), and the S&P 500 Index. 

The core functionality includes:

- Forecasting conditional volatility:\
  Utilizing models such as EGARCH and FIGARCH, the functionality provides rolling out-of-sample forecasts of volatility, adapting to market shifts and clustering effects that standard models may overlook. 

- Evaluating model performance:\
  The forecasting models are quantitatively assessed using Mean Squared Error (MSE) and Mean Absolute Error (MAE), in line with the paper’s methodology for determining the most accurate model under various market conditions. 

- Comparing behavior across asset classes:\
  By running the same GARCH variants on different markets (energy commodities and equity index), this enables comparative analysis of volatility structures and sensitivities across asset classes, reflecting the paper’s multi-market approach. 

- Supporting hedging and risk management:\
  Forecasted volatilities can be used to derive optimal hedge ratios, assisting traders, policymakers, and risk managers in making informed decisions—mirroring the practical insights provided in the original study. 

In essence, this translates the empirical modeling approach of the original research into a computational tool that allows users to explore, visualize, and evaluate volatility patterns in major financial markets using GARCH-family models. By combining robust econometric modeling with real-time financial data, it supports both academic exploration and real-world financial decision-making.

#### Models applied

For practical implications, I have selected the following models, since investors and fund managers can use EGARCH or FIGARCH models to develop risk-minimizing hedge strategies in the energy markets or index.
 
- GARCH (baseline)

- EGARCH (exponential, asymmetric)

- FIGARCH (fractionally integrated)

#### Project architecture

volatility_model_app/\
│
├── [main.py](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/main.py)                            
├── config/\
│   └── [settings.py](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/config/settings.py)                    
├── data/\
│   └── [loader.py](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/data/loader.py)                      
├── models/\
│   └── [model_factory.py](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/models/model_factory.py)               
│   └── [forecasting.py](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/models/forecasting.py)                 
├── evaluation/\
│   └── [metrics.py](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/evaluation/metrics.py%20python%20Copy%20Edit)                     
├── utils/\
│   └── [logger.py](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/utils/logger.py)                      
│   └── [plotter.py](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/utils/plotter.py)                     
├── reports/\
│   └── results.csv
\
|   └── [requirements.txt](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/requirements.txt)

#### Dependencies
- [requirements.txt](https://github.com/manuelmusngi/Volatility-Modeling-Index-and-Commodities/blob/main/requirements.txt)

#### Reference
- [Volatility Modelling in Crude Oil and Natural Gas Prices](https://www.sciencedirect.com/science/article/pii/S2212567116302192)

#### License
This project is licensed under the [MIT License](https://github.com/manuelmusngi/regime_switching_models/edit/main/LICENSE).  
