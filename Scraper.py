import requests 
from bs4 import BeautifulSoup
response = requests.get('http://kcna.kp/kcna.user.home.retrieveHomeInfoList.kcmsf')
doc = BeautifulSoup(response.text, 'html.parser')
nkelements = doc.find_all('a', {'class':'titlebet'})
for element in nkelements:
    print(element.string)
    print(element['onclick'])
import pandas as pd
data = []
nkelements = doc.find_all('a', {'class':'titlebet'})
for element in nkelements:
    datapoint = {}
    datapoint['Headlines'] = element.text
    datapoint['Link'] = element['onclick']
    print(datapoint)
    data.append(datapoint)
    
df = pd.DataFrame(data)

df.to_csv('nk_news.csv', index=False)
