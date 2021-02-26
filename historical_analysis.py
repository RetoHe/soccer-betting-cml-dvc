import pandas as pd
import numpy as np
import os

directory = "data/historicaldata"
files = os.listdir(directory)

season = []
scores = []
for file in files:
    data = pd.read_csv(str(directory+"/"+file))
    score_gap_list = []
    score_gap = 0
    for i in range(len(data)):
        #if data["B365H"][i] < data["B365A"][i] and data["B365H"][i] < data["B365D"][i] and data["FTR"][i] == "H":
            #score_gap += ((data["B365H"][i]*1)-1)
            #score_gap_list.append(((data["B365H"][i]*1)-1))
        if data["B365A"][i] < data["B365H"][i] and data["B365A"][i] < data["B365D"][i] and data["FTR"][i] == "A":
            score_gap += ((data["B365A"][i]*1)-1)
            score_gap_list.append(((data["B365A"][i]*1)-1))
        #elif data["B365D"][i] < data["B365H"][i] and data["B365D"][i] < data["B365A"][i] and data["FTR"][i] == "D":
            #score_gap += ((data["B365D"][i]*1)-1)
            #score_gap_list.append(((data["B365D"][i]*1)-1))
        elif data["B365A"][i] < data["B365H"][i] and data["B365A"][i] < data["B365D"][i] and data["FTR"][i] != "A":
            score_gap += -1
            score_gap_list.append(-1)
        #elif data["B365H"][i] < data["B365A"][i] and data["B365H"][i] < data["B365D"][i] and data["FTR"][i] != "H":
            #score_gap += -1
            #score_gap_list.append(-1)
        #elif data["B365D"][i] < data["B365H"][i] and data["B365D"][i] < data["B365A"][i] and data["FTR"][i] != "D":
            #score_gap += -1
            #score_gap_list.append(-1)
        else:
            score_gap_list.append(0)
    season.append(file)
    scores.append(score_gap)

with open("historical_score.txt", "w") as f:
    print("Historical Analysis:", file=f)
    print(season[0], file=f)
    print(scores[0], file=f)
    print(season[1], file=f)
    print(scores[1], file=f)
    print(season[2], file=f)
    print(scores[2], file=f)
    print(season[3], file=f)
    print(scores[3], file=f)
    print(season[4], file=f)
    print(scores[4], file=f)