import matplotlib.pyplot as plt

# List of Days
days = [1, 2, 3, 4, 5]

# No of Study Hours
Studying = [7, 8, 6, 11, 7]

# No of Playing Hours
playing = [8, 5, 7, 8, 13]

# Stackplot with X, Y, colors value
plt.stackplot(days, Studying, playing,
			colors =['r', 'y'])

# Days
plt.xlabel('Days')

# No of hours
plt.ylabel('No of Hours')

# Title of Graph
plt.title('Representation of Study and \
Playing wrt to Days')

# Displaying Graph
plt.show()
