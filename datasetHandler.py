import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import seaborn as sns

"""
Pandas
"""

def save_post_dataset(data):
    df = pd.DataFrame.from_dict(data)
    if not os.path.exists('./finewood_articles.csv'):
        df.to_csv('finewood_articles.csv', mode='w', index=False, header=True)
    else:
        df.to_csv('finewood_articles.csv', mode='a', index=False, header=False)

# based on the word, we want to get the most popular/frequent question in a category
def get_most_popular_question_category(df, category, word):
    df_copy = df.copy()
    df_copy = df.loc[(df['Category'] == category) & (df['Questions'].str.contains(word.lower()))]
    return df_copy

def most_popular_category_in_order(df):
    df_copy = df.copy()
    return df_copy['Category'].value_counts().nlargest().sort_index()

# most popular article will include most replies in the most popular category
def get_most_popular_article(df):
    df_copy = df.copy()
    most_popular_categories = most_popular_category_in_order(df)
    return df_copy.loc[(df['Category'] == most_popular_categories.index[0]) & (df['Replies'] == df['Replies'].max())]

def get_all_month_articles(df, month):
    df_copy = df.copy()
    return df_copy.loc[df['Month'] == month]

def get_all_year_articles(df, year):
    df_copy = df.copy()
    return df_copy.loc[df['Year'] == year]

# the way you define the most questions in a given period or month in a year is the year and month count
def get_most_replies_in_month_year(df):
    df_copy = df.copy()
    max_articles_year = df_copy['Year'].value_counts().idxmax()
    print(max_articles_year)
    return df_copy.loc[(df['Year'] == max_articles_year) & (df['Replies'] == df['Replies'].max())]

def get_questions_count_each_year(df):
    df_copy = df.copy()
    return df_copy['Year'].value_counts()

"""
Matplotlib
"""

# One graph will be about the number of questions in each year (bar chart and pie)
# Two graph will be about the number of replies in every month for a specific year (bar chart and pie)
# Three graph will be about the number of questions based on the given word (bar chart)
# Four graph will be a plot of all the categories(plot) based on year(x) and the number of replies(y)


def bar_questions_each_year(df):
    df_years = get_questions_count_each_year(df)
    df_years.plot(x=df_years.index, y=df_years.values, kind='bar')
    plt.show()

def pie_questions_each_year(df):
    df_years = get_questions_count_each_year(df)
    df_years.plot(x=df_years.index, y=df_years.values, kind='pie')
    plt.show()

def bar_replies_each_month_year(df, year):
    df_year = get_all_year_articles(df, year)
    df_months = df_year['Month'].value_counts()
    df_months.plot(x=df_months.index, y=df_months.values, kind='bar')
    plt.show()

def pie_replies_each_month_year(df, year):
    df_year = get_all_year_articles(df, year)
    df_months = df_year['Month'].value_counts()
    df_months.plot(x=df_months.index, y=df_months.values, kind='pie')
    plt.show()


def bar_questions_based_on_words(df, category, words):
    questions_count = []
    for word in words:
        df_popular = get_most_popular_question_category(df, category, word)
        questions_count.append(len(df_popular))
    fig = plt.figure(figsize = (10, 5))
 
    # creating the bar plot
    plt.bar(words, questions_count, color ='maroon',
        width = 0.4)
 
    plt.xlabel("Topics")
    plt.ylabel("Count Topics")
    plt.title("Number of times the words showed up")
    plt.show()


def create_colors_plot(df):
    df_copy = df.copy()

    # most_top_categories = most_popular_category_in_order(df)

    categories = np.unique(df_copy['Category'])
    categories = list(filter(lambda x: x != 'Gary Ragowski' or x != 'Hand Tools', categories))
    colors = np.linspace(0, 1, len(categories))
    colordict = dict(zip(categories, colors))
    df_copy["Color"] = df_copy['Category'].apply(lambda x: colordict[x])
    return df_copy

def plot_categories_per_year(df):
    df_copy = create_colors_plot(df)

    fg = sns.FacetGrid(data=df_copy, hue='Category', hue_order=categories, aspect=3.61, height=6.61)
    fg.map(plt.scatter, 'Year', 'Replies').add_legend()
    # sns.scatterplot(data=df_copy,x='Year',y='Replies', c=df_copy['Color'])

    plt.show()