import joblib
# import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from src.data_processing import load_data, split_data
from src.feature_extraction import extract_combined_features
# from src.model_training import train_model
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# will read the csv file here:
# data = pd.read_csv("data/phishing_urls.csv")



def train_model(X_train, y_train):
    model = LogisticRegression(max_iter=1000) # increase max_iter if necessary
    model.fit(X_train, y_train)
    joblib.dump(model, 'src/phish_detection_model.pkl')
    return model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    return {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'f1_score': f1_score(y_test, y_pred)
    }

# what i did here is use logistic regression model (or the decision trees or random forests model) to train and evaluate the mode that i intend to use
