# Open Jupyter Notebook and run the following commands
import requests 
# import requests is a command to allow you to send HTTP/1.1 requests using Python. 
from bs4 import BeautifulSoup
# Beautfiul Soup is a fascinating Python Library by legendary Leonard Richardson, make sure you check his other work: https://www.crummy.com/software/
response = requests.get('HTML you want to use')
# Creating a variable called response to get requests from HTMl which we want to scrape.  
doc = BeautifulSoup(response.text, 'html.parser')
# Creating a variable called doc where we assign BeautifulSoup to read text from response (the variable we just created). HTML.parser helps analyzing the text in HTML format, it depends which one you'd want to use. For instance you can use lxml or HTML5 parser but it depends in which situation you'd want to use that. 
elements1 = doc.find_all('type', {'class':'nameofclass'})
# Here we are creating a variable which would find all the headlines from the class which you'd like to specify.  
for element in elements:
    print(element.string)
# In this For statement, we are looking for element in elements that will give us the strings associated with it. 
import pandas as pd
# Now after getting the data, putting it into dataframe would be important. 
data = []
elements2 = doc.find_all('a', {'class':'name of class'})
# putting the elements 2 in the document type.
for element in nkelements:
    datapoint = {}
    datapoint['Headlines'] = element.text
    datapoint['Link'] = element['name of class']
    print(datapoint)
    data.append(datapoint)
#Here we are using the text headline data and adding links along with. 
    
df = pd.DataFrame(data)
# converting data to dataframe
df.to_csv('nk_news.csv', index=False)
# Saving dataframe to csv. 
