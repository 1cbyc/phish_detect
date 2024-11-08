from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np

def extract_text_features(X_train, X_test):
    vectorizer = TfidfVectorizer(max_features=3000, ngram_range=(1, 3), stop_words='english')
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    return X_test_tfidf, X_test_tfidf

def extract_metadata_features(urls):
    # i am looking at possible example of metadata being url, length, special character counts
    lengths = urls.apply(lambda x: len(x))
    special_char_count = urls.apply(lambda x: sum(1 for c in x if not c.isalnum()))

    metadata_features = pd.DataFrame({
        'length': lengths,
        'special_char_count': special_char_count
    })

    return metadata_features.values

def extract_combined_features(X_train, X_test):
    # trying to extract tf-idf features
    X_train_text, X_test_text = extract_text_features(X_train, X_test)

    # will extract metadata features
    X_train_meta = extract_text_features(X_train, X_test)
    X_train_meta = extract_metadata_features(X_test)

    # trying to combine text and metadata features
    X_train