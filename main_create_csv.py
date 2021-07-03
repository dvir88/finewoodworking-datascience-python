import pandas as pd
import numpy as np
from forumApiRequests import get_html_data
import os
from datasetHandler import save_post_dataset

if __name__ == '__main__':
    if os.path.exists('./finewood_articles.csv'):
        os.remove('./finewood_articles.csv')
    run = True
    page = 1
    while (run):
        status = get_html_data(page)
        if status is None:
            run = False
        page += 1