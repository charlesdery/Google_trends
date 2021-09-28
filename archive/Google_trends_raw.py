#@title Default title text
from pytrends.request import TrendReq

import matplotlib.pyplot as plt



# Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()

# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list=['CNBC','Coinmarketcap'])

# Interest Over Time
interest_over_time_df = pytrend.interest_over_time()
df=interest_over_time_df[-156:]

print(interest_over_time_df.tail(10))

# multiple line plot

plt.plot( 'CNBC', 'y1', data=df, marker='x', color='red', linewidth=2)
plt.plot( 'Coinmarketcap', 'y2', data=df, color='blue', linewidth=2)

# title
plt.title('Google Trends', loc='center',pad=10)

#plt.plot( 'Cosmos Crypto', 'y5', data=df, marker='x', color='red', linewidth=2)
plt.legend()



# title
plt.title('Google Trends (Past 36 months)', loc='center',pad=10)



interest_over_time_df.to_csv('layer_1.csv', encoding='utf-8')

