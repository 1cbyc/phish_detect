import pandas as pd
from sklearn.model_selection import train_test_split

def load_data():
    # now i have to use the phisIIL dataset cause i could not manually sort
    data = pd.read_csv('data/phishIIL.csv')
    # phishing_df = pd.read_csv('data/phishing_urls.csv')
    # legit_df = pd.read_csv('data/legitimate_urls.csv')

    # i want to add a label colum: 1 for phishing and 0 for legit
    phishing_df['label'] = 1
    legit_df['label'] = 0
    # since i 

    # so now i want to concatenate the datasets and shuffle it
    data = pd.concat([phishing_df, legit_df]).sample(franc=1).reset_index(drop=True)
    return data

def split_data(data):
    X = data['url'] # if i run it for the email, i will use 'email' instead of url (depending on the data i use)
    y = data['label']
    return train_test_split(X, y, test_size=0.2, random_state=42)

# the plan now on this script is to load phishing and legit url data. then label the phishing data as 1 and legit as 0. then split the data into training and test sets.

