import numpy as np


def RSI(prices, n_steps=14):
    prices = np.array(prices)
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
    bollinger_list = [None] * n_steps

    for i in range(n_steps, len(prices)):
        mean_price = prices.iloc[i - n_steps : i + 1].mean()
        sigma = prices.iloc[i - n_steps : i + 1].std()
        current_price = prices.iloc[i]

        result = (current_price - mean_price) / sigma
        bollinger_list.append(result)
    return bollinger_list


# making bollinger
def MFI(open, high, low, close, volume, n_steps: int = 14):
    mfi_list = [None] * n_steps

    for i in range(n_steps, len(close)):
        open_i = open.iloc[i - n_steps : i + 1]
        high_i = high.iloc[i - n_steps : i + 1]
        low_i = low.iloc[i - n_steps : i + 1]
        close_i = close.iloc[i - n_steps : i + 1]
        volume_i = volume.iloc[i - n_steps : i + 1]
        typical_price = (high_i + low_i + close_i) / 3
        raw_money_flow = typical_price * volume_i

        mask = (close_i - open_i) > 0
        positive_flow = (raw_money_flow[mask]).sum()
        negative_flow = (raw_money_flow[~mask]).sum()

        ratio = positive_flow / negative_flow
        mfi_val = 100 - 100 / (1 + ratio)

        mfi_list.append(mfi_val)
    return mfi_list


# making bollinger
def CMF(open, high, low, close, volume, n_steps: int = 14):
    cmf_list = [None] * n_steps

    for i in range(n_steps, len(close)):
        open_i = open.iloc[i - n_steps : i + 1]
        high_i = high.iloc[i - n_steps : i + 1]
        low_i = low.iloc[i - n_steps : i + 1]
        close_i = close.iloc[i - n_steps : i + 1]
        volume_i = volume.iloc[i - n_steps : i + 1]

        multiplier = ((close_i - low_i) - (high_i - close_i)) / (high_i - low_i)
        mf_vol = multiplier * volume_i

        cmf_val = mf_vol.sum() / volume_i.sum()

        cmf_list.append(cmf_val)
    return cmf_list
