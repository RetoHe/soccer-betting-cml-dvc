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