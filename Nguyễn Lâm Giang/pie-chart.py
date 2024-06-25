import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('coffee.csv')

size_counts = data.groupby('Size')['transaction_qty'].sum()

colors = ['#5356FF','#378CE7','#67C6E3','#F7EEDD']

plt.figure(figsize=(8, 6))
plt.pie(size_counts, labels = size_counts.index, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Mọi người có xu hướng chọn kích thước nào ?')
plt.legend()
plt.show()
