

import pandas as pd
import matplotlib.pyplot as plt

# 1

data = {'Volume (mL)': [21, 26, 31, 36, 41, 46, 51, 56],
        'Pression (hPa)': [1860, 1525, 1300, 1115, 1002, 870, 789, 726]} # mis data moi meme
df = pd.DataFrame(data)

fig1, ax = plt.subplots()

ax.set_xlim(20,60)
ax.set_ylim(600,1950)

ax.set_ylabel('Pression (hPa)')
ax.set_xlabel('Volume (mL)')

fig1.suptitle('La pression en fonction du volume', fontsize=16) # mettre en anglais les titres

df.plot(x='Volume (mL)', y='Pression (hPa)', ax=ax)

plt.show()

# 2

data = {'Gaz': ["Dioxygène", "Diazote", "Autres gaz"],
        'Pourcentage': [21, 78, 1]}
df = pd.DataFrame(data)

fig, ax = plt.subplots()

ax.set_title("Composition chimique de l'air")

ax.pie(df['Pourcentage'], labels=df['Gaz'], autopct='%1.1f%%')

plt.show()

# 3

data = {'Éléments chimiques': ["Fer", "Oxygène", "Silicium", "Magnésium", "Soufre", "Nickel", "Calcium", "Aluminium", "Autres"],
        'Pourcentage': [32.1, 30.1, 15.1, 13.9, 2.9, 1.8, 1.5, 1.4, 1.2]}
df = pd.DataFrame(data)

fig, ax = plt.subplots()

ax.set_ylim(0,100)
ax.set_ylabel('en %')
ax.set_title("Composition chimique de la Terre")

ax.bar(df['Éléments chimiques'], df['Pourcentage'], color=['#6890F0', '#a9f971', '#fcf39b', '#1b9e77', '#fdaa48', '#A890F0', '#ff89aa', '#7fe7f1', '#1f0092'])

ax.legend(title="Éléments chimiques")

plt.show()