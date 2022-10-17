# import request module for news scraping purpose 

import requests
from bs4 import BeautifulSoup

from db_config import mydb

class ScrapeNews:
    def __init__(self,url):
        self.url = url
        self.mycursor = mydb.cursor()

    def scrape(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find('body').find_all('h3')
        for head in headlines:
            self.mycursor.execute(f'insert into news(url,news) values("{self.url}","{head.text.strip()}")')
        mydb.commit()
        return "Data inserted successfully"
        

if __name__== "__main__":
    obj = ScrapeNews("https://www.timeanddate.com/worldclock/india/hyderabad")
    print(obj.scrape())
