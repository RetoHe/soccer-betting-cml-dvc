import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

directory = "data/historicaldata/Deutschland"

overdirectory= "data/historicaldata"
folders = ["Spanien", "Deutschland", "Belgien", "Niederlande", "Italien", "Frankreich", "England"]

season = []
scores = []
gap_steps = [1,3,5,7]
x = 0
for folder in folders:
    files = os.listdir(overdirectory+"/"+folder)
    for file in files:
        data = pd.read_csv(str(overdirectory+"/"+folder+"/"+file))
        results_df = pd.DataFrame()
        x += 1
        for element in gap_steps:
            score_gap_list = []
            score_gap = 0
            cum_score_gap_list = []
            for i in range(len(data)):
                # Calculate Difference Homewin and Awaywin
                gap = data["B365H"][i] - data["B365A"][i]
                # Wenn Differenz größer 5 zwischen Heimsieg und Auswärtssieg, dann Einssatz 5EH auf Heimsieg
                if gap <= - element and data["FTR"][i] == "H":
                    score_gap += ((data["B365H"][i]*1)-1)
                    score_gap_list.append(((data["B365H"][i]*1)-1))
                    cum_score_gap_list.append(score_gap)
                # Wenn Auswärtsteam favorit um mehr als 2, dann 3H auf Auswärtssieg
                elif gap > element and data["FTR"][i] == "A":
                    score_gap += ((data["B365A"][i]*1)-1)
                    score_gap_list.append(((data["B365A"][i]*1)-1))
                    cum_score_gap_list.append(score_gap)
                # Evtl. Verluste berechnen    
                elif gap <= - element and data["FTR"][i] != "H":
                    score_gap += -1
                    score_gap_list.append(-1)
                    cum_score_gap_list.append(score_gap)
                elif gap > element and data["FTR"][i] != "A":
                    score_gap += -1
                    score_gap_list.append(-1)
                    cum_score_gap_list.append(score_gap)
                else:
                    score_gap_list.append(0)
                    cum_score_gap_list.append(score_gap)
            season.append(file)
            scores.append(score_gap)
            results_df["output_{}_{}_GER".format(file, element)] = cum_score_gap_list

        plt.figure()
        sns.lineplot(data=results_df)
        plt.title("output_{}".format(file))
        plt.savefig("output_{}.png".format(x))
        plt.close()

#with open("historical_{}_{}__GER.txt".format(file, element), "w") as f:
    #print("Historical Analysis {}_{}_:".format(file, element), file=f)
    #print(season[0], file=f)
    #print(scores[0], file=f)
    #print(season[1], file=f)
    #print(scores[1], file=f)
    #print(season[2], file=f)
    #print(scores[2], file=f)
    #print(season[3], file=f)
    #print(scores[3], file=f)
    #print(season[4], file=f)
    #print(scores[4], file=f)