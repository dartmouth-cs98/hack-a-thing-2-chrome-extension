from scrape_medians import scrape
from analyze import *

def run(url_link):
    term, title = scrape(url_link)
    df = pandas.read_csv("csv_files/" + term + "_grades.csv", sep=',', na_values=".")
    convert_grades(df)
    add_depts(df)
    make_plot(df, title, term)

if __name__ == "__main__":
    # urls = ["http://www.dartmouth.edu/~reg/transcript/medians/17x.html",
    #         "http://www.dartmouth.edu/~reg/transcript/medians/17s.html",
    #         "http://www.dartmouth.edu/~reg/transcript/medians/17w.html",
    #         "http://www.dartmouth.edu/~reg/transcript/medians/16f.html"]
    # for url in urls:
    #     run(url)

    s = raw_input('--> ')
    run(s)
