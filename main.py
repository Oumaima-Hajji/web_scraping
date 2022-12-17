from utils import *

if __name__ == "__main__":
    urls = all_wiki_links(wiki_word="united states")

    for url in urls:
        print(f"getting WordCloud plot for link : {url}")
        word_cloud_plot(url)
