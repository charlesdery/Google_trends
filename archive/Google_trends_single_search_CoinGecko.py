# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 15:03:39 2021

@author: -

https://github.com/GeneralMills/pytrends
"""

from pytrends.request import TrendReq
import pandas as pd
import os
from tqdm import tqdm
import time
import sys

#old_stdout = sys.stdout

stamp = pd.to_datetime("today").strftime("%Y-%m-%d %H:%M:%S")
date = pd.to_datetime("today").strftime("%Y-%m-%d")
base_path = os.getcwd()
Output_path = base_path + r"\output\raw"


log_file = open("log_"+ date + ".log","w")

sys.stdout = log_file

pytrend = TrendReq()

try:   
    with open("log_" + date) as f:
        content = f.read().splitlines()
except: pass
    
filename = 'coin_gecko_token_list.csv'

df = pd.DataFrame()



df = pd.read_csv(filename)
    
for index, row in tqdm(df.iterrows(), desc='Country', leave=False, position=2):
    #print(row)
    
    try: 
        if row[1] in content:
            break
    except: pass
    else :
        pytrend.build_payload(kw_list=[row[1]])
        
        df2 = pytrend.interest_over_time()
        
        df2['Ticker'] = row[0]
        df2['ID'] = row[8]
        df2['Timestamp'] = stamp
        df2['Source'] = 'Google Trends'
        
        file_Name = 'GoogleTrends__' + row[1] +' (' + row[0] + ')' + '__' + date + '.csv'
        df2.to_csv(Output_path +'\\' + file_Name, encoding='utf-8')
        time.sleep(1)
    
    
        print(row[1])

    

log_file.close()
