import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('coffee.csv')

category_transaction_totals = data.groupby('product_category')['transaction_qty'].sum()

bars = plt.bar(category_transaction_totals.index, category_transaction_totals, color='skyblue')

for bar in bars:
    xpos = bar.get_x() + bar.get_width() / 2
    ypos = bar.get_height()
    plt.text(xpos, ypos, ypos, ha = 'center', va = 'bottom')


plt.title('Mặt hàng nào đang trở nên phổ biến nhất ?')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()