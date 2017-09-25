# import libraries
import urllib2
from bs4 import BeautifulSoup

def scrape(url):
    print(url)

if __name__ == "__main__":

    print("Please input the webpage URL")
    s = input('--> ')

    while (s != 'quit' and s != 'q'):
        try:
            scrape(s)

        except:                                   # anything else
            print("Unexpected error")

        s = input('--> ')
