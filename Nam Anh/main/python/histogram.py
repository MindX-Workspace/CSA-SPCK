import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Read given table
df = pd.read_csv("excel\student-scores.csv")

#Function that returns number of failed scores
def gend_scores(subject,gender):
    return len(df.loc[(df[subject]<=60) & (df["gender"]==gender)]["id"])

#Dataframe for plotting
newdf = pd.DataFrame({
    "Subjects":[ "English", "Geography", "History",],
    "Male":[
        (gend_scores("english_score","male") / (gend_scores("english_score","male")+gend_scores("english_score","female")))*100,
        (gend_scores("geography_score","male") / (gend_scores("geography_score","male")+gend_scores("geography_score","female")))*100,
        (gend_scores("history_score","male") / (gend_scores("history_score","male")+gend_scores("history_score","female")))*100
        ],
        

    "Female":[
        (gend_scores("english_score","female") / (gend_scores("english_score","male")+gend_scores("english_score","female")))*100,
        (gend_scores("geography_score","female") / (gend_scores("geography_score","male")+gend_scores("geography_score","female")))*100,
        (gend_scores("history_score","female") / (gend_scores("history_score","male")+gend_scores("history_score","female")))*100
        ]
})

#Plotting
newdf.plot( 
    x = "Subjects", 
    kind = 'barh', 
    stacked = True, 
    title = 'Ratio of males and females who have a non-passing score in social studies', 
    mark_right = True,
    color = ["lightseagreen", "salmon",]
)

plt.show()




    
        
