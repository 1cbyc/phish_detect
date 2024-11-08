from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.pipeline import OneHotEncoder
from sklearn.impute import SimpleImputer

def preprocess_features(X_train, X_test):
    # i am trying to define which columns are numeric and which are categorical
    numeric_features = X_train.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = X_train.select_dtypes(include=['object']).column