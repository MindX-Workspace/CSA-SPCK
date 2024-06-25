import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv('./student-scores (1).csv', skipinitialspace=True)




#average chemistry test score with self study hour
week_self_study_hours = df.groupby('weekly_self_study_hours')['chemistry_score'].mean()
week_self_study_hours.plot(kind='line')
plt.title('average chemistry test score with self study hour')
plt.xlabel(' self study hour')
plt.ylabel('average score')
plt.xticks(rotation=45) 
plt.tight_layout() 




#percentage of student have a part time job
true_count = df['part_time_job'].value_counts()[True]
false_count = df['part_time_job'].value_counts()[False]
labels = 'Have a part time job', "didn't have a part time job"
sizes = [true_count, false_count]
colors = ['purple','brown']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  
plt.title('percentage of student have a part time job')
plt.show()




#average chemistry test score with extracurricular activities
week_self_study_hours = df.groupby('extracurricular_activities')['chemistry_score'].mean()
week_self_study_hours.plot(kind='bar')
plt.title('how extracurricular activities affect your chemistry score')
plt.xlabel('extracurricular activities' )
plt.ylabel('average score')
plt.xticks(rotation=45) 




#percentage of student have a activities outside school (club,group studies , etc..)
true_count = df['extracurricular_activities'].value_counts()[True]
false_count = df['extracurricular_activities'].value_counts()[False]
labels = 'have activities outside school', "didn't have activities outside school"
sizes = [true_count, false_count]
colors = ['yellow','pink']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  
plt.title('percentage of student have a activities outside school (club,group studies , etc..)')
plt.show()




#average math score with absense day
week_of_absense_day = df.groupby('absence_days')['math_score'].mean()
week_of_absense_day.plot(kind='line')
plt.title('average math score with absense day')
plt.xlabel(' absense day')
plt.ylabel('average math score')
plt.xticks(rotation=45) 
plt.tight_layout() 




#average math score with how many absence days
absence_days_to_math_score = df.groupby('absence_days')['math_score'].mean()
absence_days_to_math_score.plot(kind='bar')
plt.title('average math score with how many absence days')
plt.xlabel('absence days' )
plt.ylabel('average score')
plt.xticks(rotation=45) 

plt.show()