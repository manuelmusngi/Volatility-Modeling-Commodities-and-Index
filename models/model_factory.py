from arch import arch_model

def fit_model(model_name, returns):
    if model_name == 'GARCH':
        model = arch_model(returns, vol='GARCH', p=1, q=1)
    elif model_name == 'EGARCH':
        model = arch_model(returns, vol='EGARCH', p=1, q=1)
    elif model_name == 'FIGARCH':
        model = arch_model(returns, vol='FIGARCH', p=1, q=1)
    else:
        raise ValueError(f"Unsupported model: {model_name}")
    return model.fit(disp='off')
