import quandl
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

# This is in example on how to query the Quandl API for financial data
# the quandl library will then parse the result and build a dataframe

df = pd.DataFrame(quandl.get("YALE/RBCI", api_key="you_key_here"))
df.to_csv("QuandlData.csv")

# Impostiamo una struttura per il nostro futuro grafico:

fig = plt.figure()
ax1 = plt.subplot2grid((2, 1), (0, 0))
ax2 = plt.subplot2grid((2, 1), (1, 0))

# Aggiungiamo un pizzico di pepe (moving standard deviation):

mstd = pd.rolling_std(df[["Cost Index", "Long Rate"]], window=12)

# Grafico (solo di ciò che ci interessa):

df[["Cost Index", "Long Rate"]].plot(ax=ax1)
mstd.plot(ax=ax2)
plt.legend()
plt.show()

# Osserviamo gli estremi del dataset:

print(df.head())
print(df.tail())