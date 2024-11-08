from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.pipeline import OneHotEncoder
from sklearn.impute import SimpleImputer

def preprocess_features(X_train)