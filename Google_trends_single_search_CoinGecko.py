"""

Article For not getting caught: https://juanluisrto.medium.com/scraping-google-search-without-getting-caught-e43bb91b363e

Normalizing Keywords 
    – Replace  ".", \, / With an escape  to ensure script still works
    – File Naming, spaces and replace with _
    – Rotate IP address through the cloud
"""

from pytrends.request import TrendReq
import pandas as pd
import os
from tqdm import tqdm
import time
import sys

# old_stdout = sys.stdout

stamp = pd.to_datetime("today").strftime("%Y-%m-%d %H:%M:%S")
date = pd.to_datetime("today").strftime("%Y-%m-%d")
base_path = os.getcwd()
Output_path = base_path + r"\output\raw"
log_Path = base_path + r"\log"

log_file = open(log_Path + "\\" + "log_" + date + ".csv", "a")

log_list = pd.DataFrame()
log_list = pd.read_csv(log_Path + "\\" + "log_" + date + ".csv")
log_list = log_list['List'].tolist()
sys.stdout = log_file

pytrend = TrendReq()

filename = 'coin_gecko_token_list.csv'

df = pd.DataFrame()

df = pd.read_csv(filename)
# df2 = pd.DataFrame(columns=['Score','isPartial', 'Ticker','ID','Timestamp','Source'])
# df2.columns = ['Score','isPartial', 'Ticker','ID','Timestamp','Source#']

for index, row in tqdm(df.iterrows(), desc='Extracting', leave=False, position=2):
    # print(row)

    if row[1] in log_list:
        continue

    if row[1] not in log_list:
        # df2 = pd.DataFrame()
        df2 = pytrend.build_payload(kw_list=[row[1]])
        df2 = pytrend.interest_over_time()

        # df3['Ticker'] = row[0]
        # df3['Join'] = df2['date']
        df2['ID'] = row[8]
        df2['Timestamp'] = stamp
        df2['Source'] = 'Google Trends'

        # result = df3.merge(df2,how='right', left_on = 'Ticker', right_on = 'Ticker')
        # header=['Score','isPartial', 'Ticker','ID','Timestamp','Source']
        # header=['Score','isPartial', 'Ticker','ID','Timestamp','Source']
        file_Name = 'GoogleTrends__' + str(row[1]) + '(' + str(row[0]) + ')' + '.csv'
        df2.to_csv(Output_path + '\\' + file_Name, header=['Score', 'isPartial', 'ID', 'Timestamp', 'Source'],
                   encoding='utf-8')

        print(row[1])
        time.sleep(1)

token = pd.read_csv(filename)

for index, row in tqdm(token.iterrows(), desc='Extracting', leave=False, position=2):
    # print(row)

    if row[1] in log_list:
        continue

    if row[1] not in log_list:
        pytrend.build_payload(kw_list=[row[1]])

        df2 = pytrend.interest_over_time()

        df2['Ticker'] = row[0]
        df2['ID'] = row[8]

        df2['Timestamp'] = stamp
        df2['Source'] = 'Google Trends'
        df.columns = ['Date', 'Score', 'isPartial', 'Ticker', 'ID', 'Timestamp', 'Source']
        file_Name = 'GoogleTrends__' + row[1] + ' (' + row[0] + ')' + '__' + date + '.csv'
        df2.to_csv(Output_path + '\\' + file_Name, encoding='utf-8')
        time.sleep(1)

        print(row[1])

log_file.close()
sys.exit()
