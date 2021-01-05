import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, RobustScaler, LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import FeatureUnion

# import data
data = pd.read_csv("data/soccerdata_cleaned.csv")

# encode Output Variable
data["FTR"] = data["FTR"].replace("H", 1)
data["FTR"] = data["FTR"].replace("D", 2)
data["FTR"] = data["FTR"].replace("A", 3)

# Train Test Split
# Train Test Split
input_features = [
    'HomeShoot', 'AwayShoot', 'HomeCorner',
    'AwayCorner', 'HomeFouls', 'AwayFouls', 'HomeYellow', 'AwayYellow',
    'HomeRed', 'AwayRed', 'HomeWin', 'AwayWin', 'HomeDraw', 'AwayDraw',
    'HomeLoss', 'AwayLoss',
]

output_features = [
    "FTR" 
]

X_train, X_test, y_train, y_test = train_test_split(
    data[input_features],
    data[output_features],
    random_state = 42
)

# Logistic Regression Model
from sklearn.linear_model import LogisticRegression

logistic_model = LogisticRegression()
logistic_model.fit(X_train, y_train)
logistic_prediction = logistic_model.predict(X_test)
test_score = round(logistic_model.score(X_test, y_test),2)
with open("testscore.txt", "w") as f:
    print(test_score, file=f)