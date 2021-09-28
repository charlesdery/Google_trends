
"""
Created on Sun Jun 13 10:17:43 2021

@author: -
"""

import os
import glob
import pandas as pd
import sys

base_path = os.getcwd()
stamp = pd.to_datetime("today").strftime("%Y-%m-%d %H:%M:%S")
date = pd.to_datetime("today").strftime("%Y-%m-%d")

processed_data_path = base_path + r"\output\processed"
Cleaned_data_file = r"Google_trends_dataset.csv"

Output_path = base_path + r"\output\raw"



files = os.listdir(Output_path)




"""
#combine all files in the list
for file in files:
    #print(file)
    df_temp = pd.read_csv(Output_path +'\\'+ file)
    
    
  #  = [i for i in glob.glob('*.{}'.format(extension))]
   #combined_csv = pd.concat(df_temp) 
    df_temp.to_csv(processed_data_path + file, index=False, encoding='utf-8-sig')
"""

#all_filenames mes])
#export to csv
extension = 'csv'
#dataset_location = os.chdir(r'D:\investing_programs\datasets\CoinMetrics')
all_filenames = [i for i in glob.glob(Output_path + '\*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
#export to csv

combined_csv.to_csv(processed_data_path +'\\'+ Cleaned_data_file, index=False, encoding='utf-8-sig')



#load csv file into a dataframe
#combined_csv.to_csv( "coin_metrics_full_dataset.csv", index=False, encoding='utf-8-sig')

print("Coin Metrics Dataset Created!")
#create column with name of CSV file


sys.exit()