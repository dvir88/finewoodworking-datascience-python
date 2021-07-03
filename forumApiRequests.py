from crawlService import fetch_html_soup_data
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime
import dateutil.parser
from datasetHandler import save_post_dataset

def get_html_data(page=1):
    url = 'https://www.finewoodworking.com/discussion-forum?paged={}'.format(page)

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_driver_path = os.getcwd() + '/bin/chromedriver_91'
    print(chrome_driver_path)
    chrome_driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver_path)#, options=chrome_options)
    chrome_driver.get(url)

    data = chrome_driver.page_source

    community_columns, articles, pagination = fetch_html_soup_data(data)

    print('articles: {}'.format(articles))
    print('community columns: {}'.format(community_columns))

    d = {
        'Questions': [],
        'Category': [],
        'Replies': [],
        'Day': [],
        'Month': [],
        'Year': []
    }

    for article in articles:
        for column_index, column in enumerate(article.find_all('li')):
            if column_index == 0:
                print('Question column: ', column.h2.a.text)
                d['Questions'].append(column.h2.a.text)
            elif column_index == 1:
                print('Category column: ', column.a.text)
                d['Category'].append(column.a.text)
            elif column_index == 2:
                print('Replies column: ', column.text.strip().split()[0])
                d['Replies'].append(column.text.strip().split()[0])
            elif column_index == 3:
                print('Last Updated column: ', column.time.text.strip())
                article_date = dateutil.parser.parse(column.time.text.strip())
                d['Day'].append(article_date.day)
                d['Month'].append(article_date.month)
                d['Year'].append(article_date.year)

    chrome_driver.quit()

    save_post_dataset(d)

    # check if there is next
    pagination_spans = pagination.find_all('span')

    print('has next? ', pagination_spans[2].a.get('href'))

    return pagination_spans[2].a.get('href')
