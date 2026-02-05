import numpy as np
import pandas as pd 
#Loading data
df  = pd.read_csv('index_1.csv')
#Convert money column to float
money = df['money'].astype('float').values
print("\n----PRINT FIRST 5 COLUMN------\n")
print(df.head())

#BASIC SALES STATISTIC

print("\n-----BASIC SALES STATISTIC------\n")

total_sales = np.sum(money)
avg_sales = np.mean(money)
max_sales = np.max(money)
min_sales = np.min(money)

print("Total Money earn: " , total_sales , 'UAH')
print("Avgeage sales: " , round(avg_sales , 2))
print("Max sales: " , max_sales)
print("Min sales: " , min_sales)

#BEST SELLING COFFEE

print("\n----BEST SEELING COFFEE-----\n")

coffee_type = df['coffee_name'].values
unique_coffee = np.unique(coffee_type)

totals = np.array([np.sum(money[coffee_type == coffee]) for coffee in unique_coffee])
best_idx = np.argmax(totals)

print("Best-selling coffee:",
        unique_coffee[best_idx],
        "with ", 
        totals[best_idx],
        "UAH")

# PAYMENT METHOD ANALYSIS

print("\n-------PAYMENT METHOD ANALYSIS------\n")

payment = df['cash_type'].values
unique_payments = np.unique(payment)

for p in unique_payments:
    totalp = np.sum(money[payment == p])
    count = np.sum(payment == p) 
    print(f"{p}: Total Money = {totalp} UAH, Transactions = {count}")

best_payment = np.argmax(totalp)
print("\n")
print("Prefered payment method: " , unique_payments[best_payment])

# HOURLY SALES ANALYSIS

print("\n---- HOURLY SALES -----\n")

df['datetime'] = pd.to_datetime(df['datetime'])
hours = df['datetime'].dt.hour.values
unique_hours = np.unique(hours)
hourly_totals = []

for h in unique_hours:
    mask = hours == h
    total = np.sum(money[mask])
    hourly_totals.append(total)
    print(f"Hour {h}:00 → Total Sales: {total} UAH")

hourly_totals = np.array(hourly_totals)
busiest_idx = np.argmax(hourly_totals)
print("Busiest hour:", 
      unique_hours[busiest_idx], 
      "with",
      hourly_totals[busiest_idx], "UAH")

#COFFEE POPULARITY BY HOUR

print("\n----COFFEE POPULARITY BY HOUR------\n")
# Ensure datetime column is datetime type
df['datetime'] = pd.to_datetime(df['datetime'])

# Money and coffee type arrays
money = df['money'].astype(float).values
coffee = df['coffee_name'].values
hours = df['datetime'].dt.hour.values

# Unique hours and coffee types
unique_hours = np.unique(hours)
unique_coffee = np.unique(coffee)

print("-----Total sales per coffee type per hour----\n")

for h in unique_hours:
    print(f"Hour {h}:00")
    for c in unique_coffee:
        mask = (hours == h) & (coffee == c)   # Filter for this hour and coffee
        total = np.sum(money[mask])
        if total > 0:
            print(f"   {c}: {total} UAH")
    print()

print("----Most popular coffee per hour-----\n")
for h in unique_hours:
    totals = {c: np.sum(money[(hours == h) & (coffee == c)]) for c in unique_coffee}
    popular = max(totals, key=totals.get)
    print(f"Hour {h}:00 → Most popular: {popular} ({totals[popular]} UAH)")
