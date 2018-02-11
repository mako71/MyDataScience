import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

df = pd.read_csv('c:\Finance\Data\IBM.csv')
df[['High', 'Adj Close']].plot()
plt.xlabel('Session Number')
plt.ylabel('High Price')
plt.show()
