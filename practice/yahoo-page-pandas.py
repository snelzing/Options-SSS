import pandas as pd

url = "https://finance.yahoo.com/quote/AAPL/options?p=AAPL"

dfs = pd.read_html(url)