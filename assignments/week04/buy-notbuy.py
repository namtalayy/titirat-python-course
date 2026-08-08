list_price = []
list_spend = []
total_spend = 0

#รับคาราสินค้า 6 ชิ้น
print("Enter prices of 6 items:")
for i in range(6):
    price = int(input(f"Item {i+1}: "))
    list_price.append(price)

#รับงบประมาณรวม
print("\n")
total_budget = int(input("Enter total budget: "))

#ตรวจสอบราคาสินค้า
print("\n")
for i in range(6):
    if total_spend + list_price[i] <= total_budget:
        print(f"Item {i+1} = {list_price[i]} -> buy")
        total_spend += list_price[i]
        list_spend.append(list_price[i])
    else:
        print(f"Item {i+1} = {list_price[i]} -> cannot buy")
        
    print(f"Current total = {total_spend}")
    print("\n")

#สรุปยอดทั้งหมด  
print(f"Bought items: {list_spend}")
print(f"Total spent: {total_spend}")
print(f"Remaining budget: {total_budget - total_spend}")