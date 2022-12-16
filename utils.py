from bs4 import BeautifulSoup

import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import wikipedia


def scrape_page(url: str):
    '''
    This function does the web scrape of the given wikipedia url. Returning the data in the wikipedia's paragraphs.
    Input: url:str.
    Output : data in the page's paragraphs : str.
    '''

    response = requests.get(url)

    wiki_page = BeautifulSoup(response.content, "html.parser")

    data_wiki = ""
    for paragraph in wiki_page.select('p'):
        element_parag = paragraph.getText()
        data_wiki += element_parag

    return data_wiki


def show_data_element(url: str):
    '''
    This function calls for the scrape_page function to have its data and then returns a list of all the words in the data.
    Input: url : str
    Output : list of elements in the data : list

    '''
    data_wiki = scrape_page(url)
    list_element_data = data_wiki.split()
    return list_element_data


def word_cloud_plot(url: str):
    '''
    This function calls for show_data_element function to have its list of data elements, 
        turns the list into one string
        and then using this string to generate a Word Cloud type plot.

    Input: url:str
    Output: Word Cloud plot : png file
    '''
    list_element_data = show_data_element(url)
    print(list_element_data)
    element_data_string = " ".join(list_element_data)
    print(element_data_string)

    word_cloud = WordCloud(
        collocations=False, background_color='white').generate(element_data_string)
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
