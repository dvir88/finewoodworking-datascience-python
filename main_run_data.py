import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from forumApiRequests import get_html_data
import os
import datasetHandler

if __name__ == '__main__':
    df = pd.read_csv('./finewood_articles.csv')
    # print(df)
    df_most_popular_questions = datasetHandler.get_most_popular_question_category(df, 'General Discussion', 'need')
    # print(df_most_popular_questions)

    df_most_popular_category = datasetHandler.most_popular_category_in_order(df)
    # print(df_most_popular_category)

    df_most_popular_article = datasetHandler.get_most_popular_article(df)
    # print(df_most_popular_article)

    df_month_articles = datasetHandler.get_all_month_articles(df, 7)
    # print(df_month_articles)

    df_year_articles = datasetHandler.get_all_year_articles(df, 2021)
    # print(df_year_articles)

    df_most_replies_in_month_year = datasetHandler.get_most_replies_in_month_year(df)
    # print(df_most_replies_in_month_year)

    # print(df.groupby('Year').count())
    # print(df['Year'].value_counts().index)
    # print(df['Year'].value_counts().values)

    # datasetHandler.bar_questions_each_year(df)

    # datasetHandler.pie_questions_each_year(df)

    # datasetHandler.bar_replies_each_month_year(df, 2020)

    # datasetHandler.pie_replies_each_month_year(df, 2020)

    # datasetHandler.bar_questions_based_on_words(df, 'General Discussion', ['twisting', 'racking', 'evaluation', 'Antique', 'need'])

    datasetHandler.plot_categories_per_year(df)