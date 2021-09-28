# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 15:03:39 2021

@author: -

https://github.com/GeneralMills/pytrends
"""

from pytrends.request import TrendReq
import pandas as pd
import os
import csv
import time
from tqdm import tqdm

stamp = pd.to_datetime("today").strftime("%Y-%m-%d %H:%M:%S")
date = pd.to_datetime("today").strftime("%Y-%m-%d")
base_path = os.getcwd()
Output_path = base_path + r"\output\raw"


pytrend = TrendReq()


filename = 'keyword_searches.csv'
df = pd.DataFrame()

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in tqdm(datareader, desc='Name', leave=False, position=2):
        pytrend.build_payload(kw_list=row)
        df = pytrend.interest_over_time()
        
        file_Name = ''.join(row) + '_' + date + '.csv'
        df.to_csv(Output_path +'\\' + file_Name, encoding='utf-8')
        time.sleep(1)



