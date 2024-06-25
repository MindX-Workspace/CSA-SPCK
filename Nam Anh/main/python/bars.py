import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Read given table
df = pd.read_csv("excel\student-scores.csv")

#Function that returns rounded average
def avg(x):
    return round(x.sum()/x.shape[0])

#Creating score series
math_1 = df.loc[df["weekly_self_study_hours"]<=20]["math_score"]
math_2 = df.loc[(df["weekly_self_study_hours"]>20) & (df["weekly_self_study_hours"]<=40) ]["math_score"]
math_3 = df.loc[df["weekly_self_study_hours"]>40]["math_score"]

physics_1 = df.loc[df["weekly_self_study_hours"]<=20]["physics_score"]
physics_2 = df.loc[(df["weekly_self_study_hours"]>20) & (df["weekly_self_study_hours"]<=40) ]["physics_score"]
physics_3 = df.loc[df["weekly_self_study_hours"]>40]["physics_score"]

english_1 = df.loc[df["weekly_self_study_hours"]<=20]["english_score"]
english_2 = df.loc[(df["weekly_self_study_hours"]>20) & (df["weekly_self_study_hours"]<=40)]["english_score"]
english_3 = df.loc[df["weekly_self_study_hours"]>40]["english_score"]

history_1 = df.loc[df["weekly_self_study_hours"]<=10]["history_score"]
history_2 = df.loc[(df["weekly_self_study_hours"]>20) & (df["weekly_self_study_hours"]<=40)]["history_score"]
history_3 = df.loc[df["weekly_self_study_hours"]>40]["history_score"]

print(type(math_1))

#Creating dataframes for each scoring category using score series
low_scores = pd.DataFrame({
    "Math" : avg(math_1),
    "Physics" : avg(physics_1),
    "English" : avg(english_1),
    "History" : avg(history_1)
}, index=["count"])

medium_scores = pd.DataFrame({
    "Math" : avg(math_2),
    "Physics" : avg(physics_2),
    "English" : avg(english_2),
    "History" : avg(history_2)
}, index=["count"])

high_scores = pd.DataFrame({
    "Math" : avg(math_3),
    "Physics" : avg(physics_3),
    "English" : avg(english_3),
    "History" : avg(history_3)
}, index=["count"])


#Plotting
categories = ["Math","Physics","English","History"]
plt.figure().set_figheight(10)
plt.bar(np.arange(len(categories))-0.2,low_scores.loc["count"].tolist(),0.2,label="<20 hour score",color="lightseagreen")
plt.bar(np.arange(len(categories)),medium_scores.loc["count"].tolist(),0.2,label="20-40 hour score",color="darkslategray")
plt.bar(np.arange(len(categories))+0.2,high_scores.loc["count"].tolist(),0.2,label="40+ hour score",color="salmon")
plt.xticks(np.arange(len(categories)), categories)
plt.legend(loc='lower right')
plt.xlabel('Core Subjects')
plt.ylabel('Average Scores')
plt.title("Core subjects scoring based on weekly self-study hours")


plt.show()




    
        
