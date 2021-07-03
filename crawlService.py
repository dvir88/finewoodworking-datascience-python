from bs4 import BeautifulSoup

def fetch_html_soup_data(data):
    soup = BeautifulSoup(data, 'html.parser')

    community_columns = soup.find('ul', { "class": "community__columns--labels" })
    articles = soup.find_all('article', { "class": "community__post" })
    pagination = soup.find('div', { "class": "ajax-pagination" })

    # print('these are the articles: {}'.format(div_articles))
    return (community_columns, articles, pagination)