from yahoo_fin.stock_info import get_data
from datetime import datetime, timedelta
import requests
import pandas as pd

def is_pdufa_date(index_date, pdufa_date):
    return index_date.month == pdufa_date.month and index_date.day == pdufa_date.day and index_date.year == pdufa_date.year


daily= get_data("ABCL", start_date="09/10/2020", end_date="01/08/2021", index_as_date = True, interval="1d")
# daily['pdufa'] = daily.index
# daily['pdufa'] = daily.index.to_series().apply(lambda x: is_pdufa_date(x, datetime.strptime('2023-12-20', '%Y-%m-%d').date()))
# pdufa_date = daily[daily['pdufa']].index[0]

print(daily)

# def get_ticker(company_name):
#     yfinance = "https://query2.finance.yahoo.com/v1/finance/search"
#     user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
#     params = {"q": company_name, "quotes_count": 1, "country": "United States"}

#     res = requests.get(url=yfinance, params=params, headers={'User-Agent': user_agent})
#     data = res.json()
#     if len(data['quotes']) == 0:
#         return None
#     company_code = data['quotes'][0]['symbol']
#     return company_code

# # print(get_ticker("SHANDONG LUYE"))

# df = pd.read_csv("approved/DrugsFDA FDA-Approved Drugs (1).csv")
# company = df['Company'].tolist()
# for com in company:
#     print(get_ticker(com))
    


