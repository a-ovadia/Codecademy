hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for num in prices:
    total_price += num

average_price = total_price / len(prices)

print("Average Haircut Price: <" + str(average_price) + ">")

new_prices = [num - 5 for num in prices]
print(new_prices)


total_revenue = 0

i = range(len(hairstyles))

for num in i:
    total_revenue +=last_week[num]

print("Total Revenue: <" + str(total_revenue) + ">")

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue:", average_daily_revenue)

cuts_under_30 = [hairstyles[num] for num in range(len(new_prices) - 1) if new_prices[num] < 30]
print(cuts_under_30)