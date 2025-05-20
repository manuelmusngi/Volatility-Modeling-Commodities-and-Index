import matplotlib.pyplot as plt

def plot_volatility(data, title='Volatility Forecast'):
    plt.figure(figsize=(12, 6))
    plt.plot(data)
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Volatility')
    plt.grid()
    plt.show()
