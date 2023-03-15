import requests
from bs4 import BeautifulSoup


for n in range(7):
    url = f'https://scrapingclub.com/exercise/list_basic/?page={n+1}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml' )
    link_1 = soup.find_all('h4', class_ = 'card-title')

    for links in link_1:

        for link_inf in links.find_all('a'): 
            link = link_inf.get('href') 
            url2 = f'https://scrapingclub.com{link}'
            response2 = requests.get(url2)
            soup2 = BeautifulSoup(response2.text, 'lxml' )
            title = soup2.find_all('h3', class_='card-title')
            price = soup2.find_all('h4', class_='')
            description = soup2.find_all('p', class_='card-text')

            for i in range(0, len(title)):
                print(title[i].text)
                print('price= ' + price[i].text)
                print(description[i].text)
                print('\n')
