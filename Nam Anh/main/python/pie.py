import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Read given table
df = pd.read_csv("excel\student-scores.csv")

#Scores percentages and lables
score_1 = (len([n for n in df["math_score"] if n < 60])/len(df["math_score"]))*100
score_2 = (len([n for n in df["math_score"] if n in range(60,80)])/len(df["math_score"]))*100
score_3 = (len([n for n in df["math_score"] if n in range(80,100)])/len(df["math_score"]))*100
score_4 = (len([n for n in df["math_score"] if n == 100])/len(df["math_score"]))*100

percentages = [score_1,score_2,score_3,score_4]
pielables = [str(round(score_1,1))+"%",str(round(score_2,1))+"%",str(round(score_3,1))+"%",str(round(score_4,1))+"%"]
legendlables = ["<60", "60-79", "80-99", "100"]

#Plotting
plt.pie(percentages, labels = pielables, startangle=90, colors = ["lightseagreen", "darkslategray", "salmon", "peachpuff"])
plt.legend(loc="lower left", labels = legendlables, title = "Scores")
plt.title("Percentages of students' math scoring")
plt.show() 





    
        
