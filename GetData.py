import requests
from bs4 import BeautifulSoup
import pandas as pd
from TickersList import tickers
import re

column_names = ['Ticker','Company Name','BusinessType','Date','Open','High','Low','Beta',
                'VWAP','Market Cap All Classes', 'Dividend',
                'Div Freq', 'P/E Ratio', 'EPS','Yield',
                'P/B Ratio','Exchange']

# df = pd.DataFrame(columns = column_names)

tickerDict = {}
for i in column_names:
    tickerDict[i]=[None]*len(tickers)

for i in range(len(tickerDict['Ticker'])):
    tickerDict['Ticker'][i]=tickers[i]
    results = requests.get('https://web.tmxmoney.com/quote.php?qm_symbol=' + tickers[i])
    src = results.content
    soup = BeautifulSoup(src, 'lxml')
    dq_card = soup.find_all('div', class_="dq-card")
    for dq in range(len(dq_card)):
        if 'Open' in dq_card[dq].text :
            tickerDict['Open'][i] = dq_card[dq].find('strong').string
        if 'High' in dq_card[dq].text :
            tickerDict['High'][i] = dq_card[dq].find('strong').string
        if 'Low' in dq_card[dq].text :
            tickerDict['Low'][i] = dq_card[dq].find('strong').string
        if 'Beta' in dq_card[dq].text :
            tickerDict['Beta'][i] = dq_card[dq].find('strong').string
        if 'All Classes' in dq_card[dq].text :
            tickerDict['Market Cap All Classes'][i] = dq_card[dq].find('strong').string
        if 'DIVIDEND' in dq_card[dq].text :
            tickerDict['Dividend'][i] = dq_card[dq].find('strong').string
        if 'DIV. FREQUENCY' in dq_card[dq].text :
            tickerDict['Div Freq'][i] = dq_card[dq].find('strong').string
        if 'P/E Ratio' in dq_card[dq].text :
            tickerDict['P/E Ratio'][i] = dq_card[dq].find('strong').string
        if 'EPS' in dq_card[dq].text :
            tickerDict['EPS'][i] = dq_card[dq].find('strong').string
        if 'Yield' in dq_card[dq].text :
            tickerDict['Yield'][i] = dq_card[dq].find('strong').string
        if 'P/B Ratio' in dq_card[dq].text :
            tickerDict['P/B Ratio'][i] = dq_card[dq].find('strong').string
        if 'Exchange' in dq_card[dq].text :
            t = dq_card[dq].find('strong').string
            tickerDict['Exchange'][i] = re.sub('\s','',t)

print(tickerDict)

