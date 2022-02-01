import requests
from bs4 import BeautifulSoup

url = 'https://www.femmeactuelle.fr/'
#url2 = 'https://www.seloger.com/'
#url3 = 'https://www.leboncoin.fr/'
#url4 = 'https://www.pap.fr/'
#url5 = 'https://www.logic-immo.com/'
url6 = 'https://www.paruvendu.fr/immobilier/'
#url7 = 'https://www.avendrealouer.fr/'
url8 = 'https://www.orpi.com/'
url9 = 'https://www.century21.fr/'
url10 = 'https://www.iadfrance.fr/'

res = requests.get(url)

print(res)
