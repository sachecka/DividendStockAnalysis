import requests
from bs4 import BeautifulSoup
import pandas as pd
from TickersList import tickers

#for tick in tickers:
 #   print('https://web.tmxmoney.com/quote.php?qm_symbol=' + tick)

results = requests.get("https://web.tmxmoney.com/quote.php?qm_symbol=XDV")

src = results.content

soup = BeautifulSoup(src, 'lxml')

dq_card = soup.find_all('div', class_= "dq-card")

#print(dq_card)
#print(dq_card[14].find('strong').string)
#print(dq_card[14].text)
#print(len(dq_card))

#if 'High' in dq_card[1].text:
#    print(dq_card[1].find('strong').string)

column_names = ['Ticker','Company Name','Date','Open','High','Low','Beta',
                'VWAP','Market Cap','Market Cap All Classes', 'Dividend',
                'Div Freq', 'P/E Ratio', 'EPS','Yield',
                'P/B Ratio','Exchange']

# df = pd.DataFrame(columns = column_names)

#tickerDict = {}
#for i in column_names:
#    tickerDict[i]=[None]*len(tickers)

#print(len(tickerDict['Ticker']))

compName = soup.find_all('div', class_= "quote-company-name")
x = compName[0].find('p').text
x=x.split('|')
print(x[1])

