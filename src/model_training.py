import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def train_model(X_train, y_train):
    model = LogisticRegression(max_iter=1000) # increase max_iter if necessary
    model