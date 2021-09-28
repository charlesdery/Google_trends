# Scaling_Google_Trends

## Description

*Disclaimer: this project is messy and I have increased my knowledge of projects best practices since… Nevertheless, until I have a more structured project to showcase, feel free to review what I did and reach out if you have any questions.*

## Motivation

Google Trends provide key behavioural insights into the digital community of investors. However, scaling the research is not something we are often seeing. This program aims to scale the searches of string keywords such that it can be incorporatedIt into your workflow.


## Solution

Leveraging the [PyTrends](https://github.com/GeneralMills/pytrends)  package, this program loads a table of strings to be searched by Google Trends and then generates those searches in a loop, saving each search results timeseries as a CSV file.
 
 Meanwhile, the program stores the searched strings in a log in case we get disconnected. This ensures you do not rerun all searches if we end up getting disconnected.
 
 Finally, The program aggregates all search results CSV files into a single file to be saved in AWS S3.
 
 
