def forecast_volatility(fitted_model, horizon):
    forecast = fitted_model.forecast(horizon=horizon)
    return forecast.variance.iloc[-1].values.mean()
