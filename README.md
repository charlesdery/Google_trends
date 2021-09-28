# Scaling_Google_Trends

## Description

**Disclaimer: this code is very messy and was created to proveI can do some work but it will not be a long-term project to be displayed since it's not really meant to be shared. Since creating that code, I have increased my knowledge of best practices and would structure/code very differently.**

 This program loads a table of strings to be searched by Google Trends and then generates those searches in a loop, saving each search results timeseries as a CSV file.
 
 Meanwhile, the program stores the searched strings in a log in case we get disconnected. This ensures you do not rerun all searches if we end up getting disconnected.
 
 Finally, The program aggregates all search results CSV files into a single file to be saved in AWS S3.
 
 
