import numpy as np


def RSI(prices, n_steps=14):
    rsi_values = [None] * n_steps
    for i in range(n_steps, len(prices)):
        current_prices = prices[i - n_steps + 1 : i + 1]
        ups = []
        downs = []
        price_changes = current_prices[1:] - current_prices[:-1]
        for price_change in price_changes:
            if price_change >= 0:
                ups.append(price_change)
                downs.append(0)
            else:
                ups.append(0)
                downs.append(-price_change)
        avg_up = np.mean(ups)
        avg_down = np.mean(downs)

        rsi_val = 100 - 100 / (1 + avg_up / avg_down)
        rsi_values.append(rsi_val)

    return rsi_values


# making bollinger
def extract_bb(prices, n_steps: int = 14):
    bollinger_list = []

    for i in range(n_steps, len(prices)):
        mean_price = prices.iloc[i - n_steps : i + 1].mean()
        sigma = prices.iloc[i - n_steps : i + 1].std()
        current_price = prices.iloc[i]

        result = (current_price - mean_price) / sigma
        bollinger_list.append(result)
    return bollinger_list
