import yfinance as yf
import pprint


msft = yf.Ticker("MSFT")
print(msft)

pprint.pprint(msft.info)

