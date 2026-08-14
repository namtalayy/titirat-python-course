# Function
# THB <-> USD .. 1 USD = 32 THB
# THB <-> JYP .. 1 JYP = 22 THB

def convert_currency(amount, currency):
    if currency == "USD":
        print(f"{amount:.2f} THB = {amount / 32.0} USD")
    else:
        print(f"{amount:.2f} USD = {amount * 32.0} THB")
    
    if currency == "JYP":
        print(f"{amount:.2f} THB = {amount / 22.0} JYP")
    else:
        print(f"{amount:.2f} JYP = {amount * 22.0} THB")
        
convert_currency(100, "USD")
convert_currency(100, "JYP")
