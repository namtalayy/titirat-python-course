# Currency Converter

exchange_rate = 35.5

print("Choose conversion direction:")
print("1. THB to USD")
print("2. USD to THB")
choice = int(input("Enter 1 or 2: "))

amount = float(input("Enter the amount to convert: "))

if choice == 1:
    result = amount / exchange_rate
    print(f"calculation formula: {amount:.2f} / {exchange_rate} = {result:.2f}")
    print(f"result: {amount:.2f} THB = {result:.2f} USD")
elif choice == 2:
    result = amount * exchange_rate
    print(f"calculation formula: {amount:.2f} * {exchange_rate} = {result:.2f}")
    print(f"result: {amount:.2f} USD = {result:.2f} THB")
else:
    print("Invalid choice. Please enter 1 or 2.")