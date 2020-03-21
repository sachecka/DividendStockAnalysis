import requests
from bs4 import BeautifulSoup

results = requests.get("https://web.tmxmoney.com/quote.php?qm_symbol=XDV")

# print(results.status_code)

# print(results.headers)

src = results.content

soup = BeautifulSoup(src, 'lxml')

dq_card = soup.find_all('div', class_= "dq-card")

print(dq_card)

# print(dq_card[1].find('strong').string)
print(dq_card[1].text)
print(type(dq_card))

if 'High' in dq_card[1].text:
    print("Yes")