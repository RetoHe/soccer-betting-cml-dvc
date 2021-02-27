import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

def favourite_strategy(data):
    for i in range(len(data)):
        if data["B365H"][i] < data["B365A"][i] and data["B365H"][i] < data["B365D"][i] and data["FTR"][i] == "H":
            score_gap += ((data["B365H"][i]*1)-1)
            score_gap_list.append(((data["B365H"][i]*1)-1))
            cum_score_gap_list.append(score_gap)
        elif data["B365A"][i] < data["B365H"][i] and data["B365A"][i] < data["B365D"][i] and data["FTR"][i] == "A":
            score_gap += ((data["B365A"][i]*1)-1)
            score_gap_list.append(((data["B365A"][i]*1)-1))
            cum_score_gap_list.append(score_gap)
        #elif data["B365D"][i] < data["B365H"][i] and data["B365D"][i] < data["B365A"][i] and data["FTR"][i] == "D":
            #score_gap += ((data["B365D"][i]*1)-1)
            #score_gap_list.append(((data["B365D"][i]*1)-1))
            #cum_score_gap_list.append(score_gap)
        elif data["B365A"][i] < data["B365H"][i] and data["B365A"][i] < data["B365D"][i] and data["FTR"][i] != "A":
            score_gap += -1
            score_gap_list.append(-1)
            cum_score_gap_list.append(score_gap)
        elif data["B365H"][i] < data["B365A"][i] and data["B365H"][i] < data["B365D"][i] and data["FTR"][i] != "H":
            score_gap += -1
            score_gap_list.append(-1)
            cum_score_gap_list.append(score_gap)
        #elif data["B365D"][i] < data["B365H"][i] and data["B365D"][i] < data["B365A"][i] and data["FTR"][i] != "D":
            #score_gap += -1
            #score_gap_list.append(-1)
            #cum_score_gap_list.append(score_gap)
        else:
            score_gap_list.append(0)
            cum_score_gap_list.append(score_gap)
    season.append(file)
    scores.append(score_gap)
    results_df[file] = cum_score_gap_list

def outsider_strategy(data):
    for i in range(len(data)):
        if data["B365H"][i] < data["B365A"][i] and data["B365H"][i] < data["B365D"][i] and data["FTR"][i] == "A":
            score_gap += ((data["B365A"][i]*1)-1)
            score_gap_list.append(((data["B365A"][i]*1)-1))
            cum_score_gap_list.append(score_gap)
        elif data["B365A"][i] < data["B365H"][i] and data["B365A"][i] < data["B365D"][i] and data["FTR"][i] == "H":
            score_gap += ((data["B365H"][i]*1)-1)
            score_gap_list.append(((data["B365H"][i]*1)-1))
            cum_score_gap_list.append(score_gap)
        #elif data["B365D"][i] < data["B365H"][i] and data["B365D"][i] < data["B365A"][i] and data["FTR"][i] == "D":
            #score_gap += ((data["B365D"][i]*1)-1)
            #score_gap_list.append(((data["B365D"][i]*1)-1))
            #cum_score_gap_list.append(score_gap)
        elif data["B365A"][i] < data["B365H"][i] and data["B365A"][i] < data["B365D"][i] and data["FTR"][i] != "H":
            score_gap += -1
            score_gap_list.append(-1)
            cum_score_gap_list.append(score_gap)
        elif data["B365H"][i] < data["B365A"][i] and data["B365H"][i] < data["B365D"][i] and data["FTR"][i] != "A":
            score_gap += -1
            score_gap_list.append(-1)
            cum_score_gap_list.append(score_gap)
        #elif data["B365D"][i] < data["B365H"][i] and data["B365D"][i] < data["B365A"][i] and data["FTR"][i] != "D":
            #score_gap += -1
            #score_gap_list.append(-1)
            #cum_score_gap_list.append(score_gap)
        else:
            score_gap_list.append(0)
            cum_score_gap_list.append(score_gap)
    season.append(file)
    scores.append(score_gap)
    results_df[file] = cum_score_gap_list

def strategy_one(data):
    for i in range(len(data)):
        # Calculate Difference Homewin and Awaywin
        gap = data["B365H"][i] - data["B365A"][i]
        # Wenn Differenz größer 5 zwischen Heimsieg und Auswärtssieg, dann Einssatz 5EH auf Heimsieg
        if gap <= -5 and data["FTR"][i] == "H":
            score_gap += ((data["B365H"][i]*5)-5)
            score_gap_list.append(((data["B365H"][i]*5)-5))
            cum_score_gap_list.append(score_gap)
         # Wenn Differenz zwischen 2 und 5 zwischen Heimsieg und Auswärtssieg, dann Einssatz 1EH auf Heimsieg   
        elif gap > -5 and gap <= -2 and data["FTR"][i] == "H":
            score_gap += ((data["B365H"][i]*1)-1)
            score_gap_list.append(((data["B365H"][i]*1)-1))
            cum_score_gap_list.append(score_gap)
        # Wenn Auswärtsteam favorit um mehr als 2, dann 3H auf Auswärtssieg
        elif gap > 2 and data["FTR"][i] == "A":
            score_gap += ((data["B365A"][i]*3)-3)
            score_gap_list.append(((data["B365A"][i]*3)-3))
            cum_score_gap_list.append(score_gap)
         # Wenn Differenz kleiner 1 dann 1EH auf Draw   
        elif gap > -1 and gap <= 1 and data["FTR"][i] == "D":
            score_gap += ((data["B365D"][i]*1)-1)
            score_gap_list.append(((data["B365D"][i]*1)-1))
            cum_score_gap_list.append(score_gap)
        # Evtl. Verluste berechnen    
        elif gap <= -5 and data["FTR"][i] != "H":
            score_gap += -3
            score_gap_list.append(-3)
            cum_score_gap_list.append(score_gap)
        elif gap > -5 and gap <= -2 and data["FTR"][i] != "H":
            score_gap += -1
            score_gap_list.append(-1)
            cum_score_gap_list.append(score_gap)
        elif gap > 2 and data["FTR"][i] != "A":
            score_gap += -3
            score_gap_list.append(-3)
            cum_score_gap_list.append(score_gap)
        elif gap > -1 and gap <= 1 and data["FTR"][i] != "D":
            score_gap += -1
            score_gap_list.append(-1)
            cum_score_gap_list.append(score_gap)
        else:
            score_gap_list.append(0)
            cum_score_gap_list.append(score_gap)
    season.append(file)
    scores.append(score_gap)
    results_df[file] = cum_score_gap_list