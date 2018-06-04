import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from poloniex import Poloniex

polo = Poloniex()

def ExpMovingAverage(values, window):
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()
    a =  np.convolve(values, weights, mode='full')[:len(values)]
    a[:window] = a[window]
    return a


def calcalema():
  # period1 300, 900, 1800, 7200, 14400, and 86400
  rightnow=time.time()
  for period in [900,300,1800,14400]:
    charts = polo.returnChartData(
      currencyPair='BTC_ETH',
      period=period)
    lescloses=list()
    print(type(charts))
    df = pd.DataFrame(charts)
    df['date'] = pd.to_datetime(df['date'],unit='s')
    rows = 50
    for chart in charts:
      lescloses.append(chart['close'])
    # datelist = pd.date_range(pd.datetime(2017, 1, 1).strftime('%Y-%m-%d'), periods=rows).tolist()
    # df['dates'] = datelist 
    # df = df.set_index(['dates'])
    # df.index = pd.to_datetime(df.index)
    x = df['date']
    print(df.tail(10))
    yMa = ExpMovingAverage(lescloses, period)
    plt.plot(x[len(x)-len(yMa):],yMa)
  plt.show()
  return yMa 

def main():
  print(calcalema())

if __name__ == '__main__':
  main()