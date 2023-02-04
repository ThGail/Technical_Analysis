def rolling_mean(data, rolling_range):
    
    rolling_mean = data.rolling(rolling_range).mean()
    
    return rolling_mean