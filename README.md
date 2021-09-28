# Scaling Google Trends

## Description

*Disclaimer: this project is messy and I have increased my knowledge of projects best practices since… Nevertheless, until I have a more structured project to showcase, feel free to review what I did and reach out if you have any questions.*

## Motivation

Google Trends provide key behavioural insights into the digital community of investors. However, scaling the analytics to thousands of searches is key when overseeing the entire crypto space. This program aims to scale the searches of string keywords such that it can be incorporatedIt into your workflow.


## Solution

Leveraging the [PyTrends](https://github.com/GeneralMills/pytrends)  package, this program loads a table of strings to be searched by Google Trends and then generates those searches in a loop, saving each search results timeseries as a CSV file.
 
 Meanwhile, the program stores the searched strings in a log in case we get disconnected. This ensures you do not rerun all searches if we end up getting disconnected.
 
 Finally, The program aggregates all search results CSV files into a single file to be saved in AWS S3.
 
 
date|Score|isPartial|ID|Timestamp|Source
--- | --- | --- | --- | --- | ---
2019-06-16|0|False|ILV.Illuvium|2021-08-21 13:27:52|Google Trends
2019-06-23|0|False|ILV.Illuvium|2021-08-21 13:27:52|Google Trends
2019-06-30|0|False|ILV.Illuvium|2021-08-21 13:27:52|Google Trends
2019-07-07|0|False|ILV.Illuvium|2021-08-21 13:27:52|Google Trends
2019-07-14|0|False|ILV.Illuvium|2021-08-21 13:27:52|Google Trends
2019-07-21|0|False|ILV.Illuvium|2021-08-21 13:27:52|Google Trends
