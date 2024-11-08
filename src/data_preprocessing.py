import pandas as pd
from sklearn.model_selection import train_test_split

def load_data():
    phishing_df = pd.read_csv('data/phishing_urls.csv')
    legit_df = pd.read_csv('data/legitimate_urls.csv')

    # i want to add a label colum: 1 for phishing and 0 for legit
    phishing_df['label'] = 1
    legit_df['label'] = 0

    # so now i want to concatenate the datasets and shuffle it
    data = pd.concat([phishing_df, legit_df])