def calculate_electricity_cost(units):
    if units < 0:
        print("กรุณากรอกจำนวนหน่วยไฟฟ้าใหม่")
        return
        
    if units <= 50:
        cost = units * 2.50
    elif units <= 100:
        cost = (50 * 2.50) + ((units - 50) * 3.00)
    elif units <= 200:
        cost = (50 * 2.50) + (50 * 3.00) + ((units - 100) * 3.50)
    elif units >= 200:
        cost = (50 * 2.50) + (50 * 3.00) + (100 * 3.50) + ((units - 200) * 4.00)
        
    print("\nรายละเอียดค่าไฟฟ้า")
    
    if units <= 50:
        print(f"1-{units:.0f} หน่วย : {units * 2.50:.2f} บาท")
        
    elif units <= 100:
        print("1-50 หน่วย : 125.00 บาท")
        print(f"51-{units:.0f} หน่วย : {(units - 50) * 3:.2f} บาท")
    
    elif units <= 200:
        print("1-50 หน่วย : 125.00 บาท")
        print("51-100 หน่วย : 150.00 บาท")
        print(f"101-{units:.0f} หน่วย : {(units - 100) * 3.5:.2f} บาท")
        
    else:
        print("1-50 หน่วย : 125.00 บาท")
        print("51-100 หน่วย : 150.00 บาท")
        print("101-200 หน่วย : 350.00 บาท")
        print(f"201-{units:.0f} หน่วย : {(units - 200) * 4:.2f} บาท")
        
    print("ค่าบริการ : 25.00 บาท")
    print(f"รวมค่าไฟฟ้าทั้งสิ้น : {cost + 25:.2f} บาท")

while True:
    print("=====โปรแกรมคำนวณค่าไฟฟ้า=====")
    print("1.คำนวณค่าไฟฟ้า")
    print("2.ออกจากโปรแกรม")
    
    choice = input("เลือกเมนู: ")
    
    if choice == "1":
        units = float(input("\nกรอกจำนวนหน่วยไฟฟ้า: "))
        calculate_electricity_cost(units)
     
    elif choice == "2":
        print("ออกจากโปรแกรม")
        break
    
    else:
        print("เลือกเมนูไม่ถูกต้อง")