import pandas as pd
import numpy as np
rows = 50
df = pd.DataFrame(np.random.randint(90,110,size=(rows, 3)), columns=['BTC', 'ETH', 'DASH'])
datelist = pd.date_range(pd.datetime(2017, 1, 1).strftime('%Y-%m-%d'), periods=rows).tolist()
df['dates'] = datelist 
df = df.set_index(['dates'])
df.index = pd.to_datetime(df.index)

print(df.tail(10))