# import libraries
import urllib
from bs4 import BeautifulSoup

def scrape(url):
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r, "html.parser")
    # print(soup.prettify()[0:1000])
    for link in soup.find_all(align="center"):
        print(link)


if __name__ == "__main__":

    scrape("http://www.dartmouth.edu/~reg/transcript/medians/17x.html")

    # print("Please input the webpage URL")
    # s = raw_input('--> ')
    #
    # while (s != 'quit' and s != 'q'):
    #     try:
    #         scrape(s)
    #
    #     except:                                   # anything else
    #         print("Unexpected error")
    #
    #     s = raw_input('--> ')
