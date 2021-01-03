import pandas as pd
import numpy as np

# Import Data
data = pd.read_csv("data/soccerdata.csv")
# Choose necessary colums
data = data[["HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR", "HTHG", "HTAG", "HTR","HS","AS","HST","AST","HF","AF","HC","AC","HY","AY","HR","AR","B365H","B365D","B365A"]]
# Export cleaned Dataframe to csv
data.to_csv(r'data/soccerdata_cleaned.csv', index = False)
