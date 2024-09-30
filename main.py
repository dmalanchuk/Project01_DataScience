import pandas as pd

online_retail_dashboard = pd.read_excel('data/Online_Retail.xlsx')
online_retail_dashboard.head(1)

"""
щоб зʼясувати в якій країні відбулось найбільше транзакцій
потрібно проітеруватись по таблиці, та знайти в якій країні найчастіше відбувались
транзакції
"""

country_names = online_retail_dashboard['Country']

country_count = {}

for country in country_names:
    if country in country_count:
        country_count[country] += 1
    else:
        country_count[country] = 1

max_country_count = max(country_count.values())
max_country_name = max(country_names, key=country_count.get)
print(f"max country name: {max_country_name}, and max country count: {max_country_count}")

"""
Порахувати загальний дохід від продажів кожної країни
"""
online_retail_dashboard['totalIncome'] = online_retail_dashboard['Quantity'] * online_retail_dashboard['UnitPrice']
total_income = online_retail_dashboard.groupby('Country')['totalIncome'].sum().reset_index()
print(total_income)

"""
1. Обчислити дохід для кожної транзакції, перемноживши кількість товарів на їхню ціну (Quantity × UnitPrice).  
2. найти товар, який приніс найбільший дохід.
"""

print(online_retail_dashboard['totalIncome'])

max_total_price = max(online_retail_dashboard['totalIncome'])
print(f"The product that brought the most income: {max_total_price}")


"""
1.Порахувати загальну кількість проданих одиниць кожного товару. Це дозволить визначити, які товари є найбільш популярними.  
2.визначити, який товар мав найбільші продажі за кількістю.  
"""

"""
порахувати загальну кількість проданих одиниць кожного товару 

оптимізований код знаходження загальної кількості проданих
одиниць кожного товару. використання transform() в якому передаємо функцію "sum"
та виводим результа, по ітогу нам навіть не протрібно використовувати цикл, та унікальні ключі.
"""
positive_data = online_retail_dashboard[online_retail_dashboard['Quantity'] > 0]

result_table = positive_data.groupby('Description')['Quantity'].sum().reset_index()
result_table.columns = ['Category', 'Total Quantity']
result_table.sort_values('Total Quantity', ascending=True, inplace=True)
print(result_table)

"""
товар який мав найбільше продажів за кількістю
"""

total_quantity = online_retail_dashboard.groupby('Description')['Quantity'].sum().reset_index()
top_product = total_quantity.loc[total_quantity['Quantity'].idxmax()]

print(top_product)
