from jupyterthemes import jtplot
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

jtplot.style(theme = 'monokai', context = 'notebook', ticks = True, grid = False)

stock_df = pd.read_csv('stock_data.csv')
daily_return_df = pd.read_csv('stocks_daily_returns.csv')
fig, axs = plt.subplots(2, 3, figsize=(17,8),tight_layout={'w_pad': 1.0})
axs[0, 0].plot(stock_df['Date'], stock_df['FB'], label = 'Facebook Stock Price')
axs[0, 0].set_ylabel('Price [$]')
axs[0, 0].set_title('FB Stock Price')
axs[0, 0].legend(loc = 'upper right')
ticks = np.linspace(0, len(stock_df['Date']) - 1, 5, dtype=int)
axs[0, 0].set_xticks(ticks)
axs[0, 0].set_xticklabels(stock_df['Date'].iloc[ticks], rotation=20)
axs[0, 0].tick_params(axis='x', labelsize=8)
axs[0, 0].grid()

axs[0, 1].plot(stock_df['Date'], stock_df['NFLX'], label = 'Netflix Stock Price', color = 'r')
axs[0,1].set_ylabel('Price [$]')
axs[0,1].set_title('Netflix Stock Price')
axs[0,1].legend(loc = 'upper right')
ticks = np.linspace(0, len(stock_df['Date']) - 1, 5, dtype=int)
axs[0, 1].set_xticks(ticks)
axs[0, 1].set_xticklabels(stock_df['Date'].iloc[ticks], rotation=20)
axs[0, 1].tick_params(axis='x', labelsize=8)
axs[0, 1].grid()


mu = daily_return_df['FB'].mean()
sigma = daily_return_df['FB'].std()
num_bins = 40
axs[1,0].hist(daily_return_df['FB'], num_bins, facecolor = 'blue'); # ; is to get rid of extra text printing
axs[1,0].set_ylabel('Frequency')
axs[1, 0].set_title('Histogram: mu = {:.2f}, sigma = {:.2f}'.format(mu, sigma))
axs[1,0].grid()

axs[1,1].plot(stock_df['Date'], stock_df[['NFLX', 'FB', 'TWTR']])
axs[1,1].set_ylabel('price [$]')
axs[1,1].set_title('NFLX, FB, TWTR Stock Prices')
axs[1,1].legend(loc = 'upper right')
ticks = np.linspace(0, len(stock_df['Date']) - 1, 5, dtype=int)
axs[1, 1].set_xticks(ticks)
axs[1, 1].set_xticklabels(stock_df['Date'].iloc[ticks], rotation=20)
axs[1, 1].tick_params(axis='x', labelsize=8)
axs[1,1].grid()
fig.delaxes(axs[0, 2])
fig.delaxes(axs[1, 2])
fig.text(0.67, 0.5,
'''Stock price plays a crucial role
in creating valuation of an organ-
ization where it is used by the
investor as a performance indicator. An
increasing stock price of any company in the
market justifies its good performance and the
probability of investment also emerges. However,
various parameters of the market exist in a
dynamic nature which keep fluctuating the stock
price of the organization with the changing
time. The dataset chosen for visualization is
based-on stock price which reflects a 
consistent fluctuation of stock price of
the companies. These are renowned companies
like Facebook (FB), Twitter and Netflix whose
changing stock price in the market has been
studied thoroughly with the support of
visualization. 

'''
, fontsize=9, fontweight='light', fontfamily='serif')

fig.text(0.67, 0.01,
'''Total 4 visuals have been obtained as a result
which can be used further for analysis and
these are FB Stock Price, Netflix Stock Price,
Histogram and combination of stock prices of
all the three companies.It can be seen
in the FB stock price that it had cons-
istently increased from the year 2013
to year 2020.Despite a few downward fluct-
uations in stock price, Facebook had succes-
sfully reached the level of 300$ by the
year 2020. Likewise, the stock price
of Netflix kept on rising since the year
2013 and crossed the limit of 500$ by
the year it reached 2020. In order to
showcase the fluctuation, a linear graph
has been selected  for two companies
whereas a histogram has been developed for
Facebook. The fourth visualization shed
light on the status of all the stock
prices of three companies which allowed
the comparison of stock prices among these
companies. Subsequently, the stock price
of Facebook has been found to be the
highest among other companies. Hence,it
has been found that the performance of Fac-
ebook remains at the top out of three 
companies.
'''
, fontsize=9, fontweight='light', fontfamily='serif')

fig.text(0.8, 0.95,
'''Student id: 22075765 
Name : Hari Bahadur Gharti Magar'''
, fontsize=11, fontweight='light', fontfamily='serif')

plt.savefig('22075765',dpi=300)
#plt.show()