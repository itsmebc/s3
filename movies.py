import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.afi.com/afis-100-years-100-movies/'
headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
page = requests.get(url, headers=headers)


soup = BeautifulSoup(page.text, 'html.parser')
res = soup.find_all('h6', class_='q_title')

def scrape_movies():
    total = soup.find_all('h6', class_='q_title')
    movies = []
    id = 1

    for i in total:
        movies.append({
            "id": id,
            "movies": i.text
        })
        id += 1
    
    return movies

movies = pd.DataFrame(scrape_movies())

movies['movies'] = movies['movies'].astype(str).str.extract(r'\d. (.*) \(\d{4}\)')
movies.to_csv('movies.csv')