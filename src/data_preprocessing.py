import pandas as pd
from sklearn.model_selection import train_test_split

def load_data():
    phishing_df = pd.read_csv('data/phishing_urls.csv')
    legit_df = pd.read_csv