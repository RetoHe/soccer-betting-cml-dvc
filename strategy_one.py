import pandas as pd
import numpy as np

data = pd.read_csv("data/soccerdata_cleaned.csv")

score_gap_list = []
score_gap = 0
for i in range(len(data)):
    gap = data["B365A"][i] - data["B365H"][i]
    if gap >= 5 and data["FTR"][i] == "H":
        score_gap += ((data["B365H"][i]*5)-5)
        score_gap_list.append(((data["B365H"][i]*5)-5))
    elif gap <= 5 and gap >= 3 and data["FTR"][i] == "H":
        score_gap += ((data["B365H"][i]*3)-3)
        score_gap_list.append(((data["B365H"][i]*3)-3))
    elif gap <= -5 and data["FTR"][i] == "A":
        score_gap += ((data["B365A"][i]*5)-5)
        score_gap_list.append(((data["B365A"][i]*5)-5))
    elif gap >= -5 and gap <= -3 and data["FTR"][i] == "A":
        score_gap += ((data["B365A"][i]*3)-3)
        score_gap_list.append(((data["B365A"][i]*3)-3))
    else:
        score_gap_list.append(0)

with open("score.txt", "w") as f:
    print("Score Strategy Gap", file=f)
    print(score_gap, file=f)