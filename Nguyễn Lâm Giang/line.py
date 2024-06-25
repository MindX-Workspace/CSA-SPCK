import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('coffee.csv')

data['transaction_date'] = pd.to_datetime(data['transaction_date'], format='%d-%m-%Y', errors='coerce')

monthly_revenue = data.groupby(data['transaction_date'].dt.month)['Total_Bill'].sum()

months = []
for i in range(1, 7):
    months.append('Tháng ' + str(i))

plt.figure(figsize=(10, 6))
plt.plot(months, monthly_revenue, marker='o', color='skyblue', linewidth=2, markersize=8)
plt.title('Thay đổi về doanh thu theo tháng')
plt.grid(axis = 'y',linestyle='--')
plt.show()
