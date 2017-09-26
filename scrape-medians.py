# import libraries
import urllib
import csv
from bs4 import BeautifulSoup

def scrape(url):
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r, "html.parser")
    data = []
    for link in soup.find_all('tr'):
        raw = link.text.strip()
        term, course, enrollment, grade = raw.split("\n")
        to_list = [str(term), str(course), str(enrollment), str(grade)]
        data.append(to_list)

    f = csv.writer(open("test.csv", "w"))
    for row in data:
        f.writerow((row[0], row[1], row[2], row[3]))

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
