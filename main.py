from config.settings import ASSETS, START_DATE, END_DATE, VOLATILITY_MODELS, FORECAST_HORIZON
from data.loader import fetch_data
from models.model_factory import fit_model
from models.forecasting import forecast_volatility
from evaluation.metrics import evaluate_model
from utils.logger import log, log_error
import pandas as pd

def main():
    results = []

    for asset_name, ticker in ASSETS.items():
        log(f"Processing {asset_name}")
        data = fetch_data(ticker, START_DATE, END_DATE)
        returns = data['Return']

        for model_name in VOLATILITY_MODELS:
            log(f"Fitting {model_name} model")
            try:
                fitted_model = fit_model(model_name, returns)
                pred_vol = forecast_volatility(fitted_model, FORECAST_HORIZON)
                mse, mae = evaluate_model(returns[-FORECAST_HORIZON:], pred_vol)
                results.append({
                    'Asset': asset_name,
                    'Model': model_name,
                    'MSE': mse,
                    'MAE': mae
                })
            except Exception as e:
                log_error(f"{model_name} on {asset_name}: {e}")

    df = pd.DataFrame(results)
    df.to_csv('reports/results.csv', index=False)
    print(df)

if __name__ == '__main__':
    main()
