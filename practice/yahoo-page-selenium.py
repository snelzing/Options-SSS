from selenium import webdriver
import time
import pandas as pd

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://finance.yahoo.com/quote/AAPL/options?p=AAPL")

html = driver.page_source

driver.close()

df_list = pd.read_html(html) # this parses all the tables in webpages to a list
print(df_list)




