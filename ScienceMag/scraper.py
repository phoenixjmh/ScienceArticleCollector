from bs4 import BeautifulSoup
import requests
from collections import OrderedDict

#The URL where articles will be found
url = "http://www.sciencemag.org/news"

response=requests.get(url)

soup=BeautifulSoup(response.text, 'html.parser')
#Initialize the lists that will be filled and passed to an OrderedDict for display
#on the index.html page.

names=[]
links=[]

latestNews_Container = soup.find('div', class_='view-article-lists-block-6')
latestNews_List = latestNews_Container.find('ul', class_='item-list')
latestNews_nameContainer = latestNews_List.find_all('div', class_='media__body')
latestNews_linkContainer = latestNews_List.find_all('div', class_='media__icon')

def Scrape():
	"""Fill the names/links list, for insertion into dictionary
	"""
	for article in latestNews_nameContainer:
	    name=article.find('span')
	    name=name["content"]
	    names.append(name)


	for linkRef in latestNews_linkContainer:
	    link=linkRef.find('a')
	    link=link['href']
	    trueLink = ('http://www.sciencemag.org'+link)
	    links.append(trueLink)
	    print(trueLink)


#Run the scraper on server load.
Scrape()
#Pass Elements into OrderedDict
listContainer=OrderedDict(zip(names,links))
