import requests
from bs4 import BeautifulSoup
import pandas as pd
from TickersList import tickers
import re

# Column names that are needed in the pandas dataframe
column_names = ['Ticker','Company Name','BusinessType','Date','Open','High','Low','Beta',
                'VWAP','Market Cap All Classes', 'Dividend',
                'Div Freq', 'P/E Ratio', 'EPS','Yield',
                'P/B Ratio','Exchange']

# Create dictionary and fill with empty lists
tickerDict = {}
for i in column_names:
    tickerDict[i]=[None]*len(tickers)

# Extract the data from web for each ticker
for i in range(len(tickerDict['Ticker'])):
    tickerDict['Ticker'][i]=tickers[i]
    results = requests.get('https://web.tmxmoney.com/quote.php?qm_symbol=' + tickers[i])
    src = results.content
    soup = BeautifulSoup(src, 'lxml')
    texts = soup.find_all(text=True)
    # Get company name
    compName = soup.find_all('div', class_="quote-company-name")
    tickerDict['Company Name'][i] = compName[0].find('h4').text
    # Get the date
    dateTick = compName[0].find('p').text
    dateTick = dateTick.split('|')
    tickerDict['Date'][i] = re.sub('\s', '', dateTick[1])
    # most of the info is in the dq_card div class
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
        if 'Dividend' in dq_card[dq].text :
            dividend = dq_card[dq].find('strong').string
            dividend = dividend.replace("\xa0", " ")
            tickerDict['Dividend'][i] = dividend
        if 'Div. Frequency' in dq_card[dq].text :
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

