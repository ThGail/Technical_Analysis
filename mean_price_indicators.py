def typical_price(df, save = False):
    
    if save :
        df['Typical Price'] = (df['High'] + df['Low'] + df['Close'])/3
    
    return (df['High'] + df['Low'] + df['Close'])/3


def median_price(df, save = False):
    
    if save :
        df['Median Price'] = (df['High'] + df['Low'])/2
    
    return (df['High'] + df['Low'])/2


def weight_close(df, save = False):
    
    if save :
        print('hello')
        df['Weight Close'] = (df['Close']*2 + df['High'] + df['Low'])/4
    
    return (df['Close']*2 + df['High'] + df['Low'])/4


def total_price(df, save = False):
    
    if save :
        df['Total Price'] = (df['Open'] + df['High'] + df['Low'] + df['Close'])/4
    
    return (df['Open'] + df['High'] + df['Low'] + df['Close'])/4