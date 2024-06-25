import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv('./student-scores (1).csv', skipinitialspace=True)
sumarize = sum(['chemistry_score']['math_score']['history_score']['physics_score'])
    

week_self_study_hours = df.groupby('gender')['sumarize'].mean()
week_self_study_hours.plot(kind='bar')
plt.title('how extracurricular activities affect your chemistry score')
plt.xlabel('extracurricular activities' )
plt.ylabel('average score')
plt.xticks(rotation=45) 

