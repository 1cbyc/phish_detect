from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

def extract_text_features(X_train, X_test):
    vectorizer = TfidfVectorizer(max_features=3000, ngram_range=(1, 3), st)