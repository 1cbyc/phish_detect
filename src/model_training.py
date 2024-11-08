import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

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

# what i did here is use logistic regression model (or the decision trees or random forests model)
