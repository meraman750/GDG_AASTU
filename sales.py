sales_list = []
with open("sales.txt", "r") as file:
    for line in file:
        try:
            sales_list.append(int(line))
        except ValueError:
            continue

sum = 0

for sale in sales_list:
    sum += sale
print(sum)
