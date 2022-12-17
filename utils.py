from bs4 import BeautifulSoup

import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import wikipedia


stopwords_list = requests.get(
    "https://gist.githubusercontent.com/rg089/35e00abf8941d72d419224cfd5b5925d/raw/12d899b70156fd0041fa9778d657330b024b959c/stopwords.txt"
).content
eng_stopwords = set(stopwords_list.decode().splitlines())


def scrape_page(url: str):
    """
    This function does the web scrape of the given wikipedia url. Returning the data in the wikipedia's paragraphs.
    Input: url:str.
    Output : the text data in the page's paragraphs : str.
    """

    response = requests.get(url)

    wiki_page = BeautifulSoup(response.content, "html.parser")

    data_wiki = ""
    for paragraph in wiki_page.select("p"):
        element_parag = paragraph.getText()
        data_wiki += element_parag

    return data_wiki


def show_data_element(url: str):
    """
    This function calls for the scrape_page function to have its data and then returns a list of all the words in the data.
    Input: url : str
    Output : list of elements in the data : list
    """
    data_wiki = scrape_page(url)
    list_element_data = data_wiki.split()
    return list_element_data


def all_wiki_links(wiki_word: str):

    list_wiki = wikipedia.search(f"{wiki_word}")

    list_urls = []
    try:
        for wiki in list_wiki:
            wiki_page = wikipedia.page(
                f"{wiki}", auto_suggest=False, redirect=True, preload=False
            )

            wiki_url = wiki_page.url

            list_urls.append(str(wiki_url))

        return list_urls
    except wikipedia.DisambiguationError :
        print(
            """ERROR : There is disambiguation in the chosen term.
        Please be more specific.
        For example, instead of "strawberry",
        put "strawberry fruit". """
        )


def get_word_url(url: str):
    """
    Returns the last word after '/' in a url
    Input: url:str
    Outout : The words after the last '/' in a url
    """
    word = url.split("/")
    return word[-1]


def word_cloud_plot(url: str):
    """
    This function calls for show_data_element function to have its list of data elements,
        turns the list into one string
        and then using this string to generate a Word Cloud type plot.
    Input: url:str
    Output: WordCloud plot : png file
    """
    list_element_data = show_data_element(url)
    element_data_string = " ".join(list_element_data)
    word_cloud = WordCloud(
        width=3000,
        height=2000,
        random_state=1,
        background_color="navy",
        colormap="rainbow",
        collocations=False,
        stopwords=eng_stopwords,
    ).generate(element_data_string)
    plt.imshow(word_cloud, interpolation="bilinear")
    word_url = get_word_url(url)
    plt.title(f"Wiki Article: {word_url}")
    plt.axis("off")
    plt.show()
