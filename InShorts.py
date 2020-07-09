from bs4 import BeautifulSoup as beauty
import requests
import time
from termcolor import colored

source = requests.get('https://inshorts.com/en/read').text
soup = beauty(source,'lxml')

print("MAIN HEADLINES AT THIS HOUR // \n")
i=1

for news in soup.find_all('div',class_='news-card z-depth-1'):
    news_headline = news.find('div',class_='news-card-title news-right-box')
    news_headline = news_headline.a.span.text
    print(i,end=")  ")
    print(colored(news_headline, "green"), end="\n")

    news_content = news.find('div',class_='news-card-content news-right-box')
    news_content = news_content.div.text
    print(colored(news_content, "blue"))

    print()
    i+=1
    time.sleep(1.5)

input("Press enter to exit.")



