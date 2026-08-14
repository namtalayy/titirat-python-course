# Function
# THB <-> USD .. 1 USD = 32 THB
# THB <-> JPY .. 1 JYP = 22 THB

def convert_currency(amount, currency):
    if currency == "USD":
        print(f"{amount:.2f} THB = {amount / 32.0} USD")
    else:
        print(f"{amount:.2f} USD = {amount * 32.0} THB")
    
    if currency == "JPY":
        print(f"{amount:.2f} THB = {amount / 22.0} JPY")
    else:
        print(f"{amount:.2f} JPY = {amount * 22.0} THB")
        
convert_currency(100, "USD")
convert_currency(100, "JPY")
