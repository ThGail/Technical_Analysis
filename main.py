import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

from brownian_motion import create_brownian_motion
from brownian_motion import underlying_asset
from technical_analysis import *

n = 1000

Wt, timerange = create_brownian_motion(1,255, n)
 
S0=100.0
mu=0.5
sigma=0.15
taux_r=0.05

St = underlying_asset(S0, mu, sigma, timerange, Wt)

#plt.figure()
#plt.subplot(1,2,1)
#plt.plot(Wt)
#plt.plot(Wt.mean(axis = 1), color = 'black', lw = 3)

#plt.subplot(1,2,2)
#plt.plot(St)
#plt.plot(St.mean(axis = 1), color = 'black', lw = 3)

#plt.show()

tte = yf.Ticker("TTE")
history_tte = tte.history(start='2021-12-21', end='2023-01-04')

df_history_tte = pd.DataFrame(history_tte)

plt.plot(rolling_mean(df_history_tte['Open'], 50))
plt.plot(df_history_tte['Open'])
plt.show()