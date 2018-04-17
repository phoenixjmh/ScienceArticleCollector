
from bs4 import BeautifulSoup
import requests
import os


def main():
    """This function grabs all of the scraped articles, from scraper.py, given to the index.html page
    and stores all of the articles from them as .txt files in the SavedArticles directory
    """


    url = 'http://127.0.0.1:8000/'

    response=requests.get(url)

    soup= BeautifulSoup(response.text, 'html.parser')


    links=soup.find_all('a')

    content=[]

    for i in links[1:]:
        articleContent=[]
        link = i.get('href')
        newResponse = requests.get(link)
        newSoup = BeautifulSoup(newResponse.text, 'html.parser')
        headline=newSoup.find('h1', class_='article__headline').text
        body = newSoup.find('div', class_='article__body')
        paragraphs=body.find_all('p')
        for p in paragraphs:
            paragraph=p.text
            articleContent.append(paragraph)
            print(paragraph)
#This prevents the program from creating duplicate articles..
        if not os.path.exists(os.path.dirname(os.path.abspath(__file__))+'/SavedArticles/'+ headline+'.txt'):
#Write to the Science Articles folder..
            with open(os.path.dirname(os.path.abspath(__file__))+'/SavedArticles/' + headline+'.txt', 'w', encoding = 'utf-8') as doc:
                for p in paragraphs:
                    paragraph=p.text
                    doc.write(paragraph)
