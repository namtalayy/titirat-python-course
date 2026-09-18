try:
    num1 = float(input("ตัวเลขที่ 1: "))
    num2 = float(input("ตัวเลขที่ 2: "))
    operator = input("เครื่องหมาย (+, -, *, /): ")
    
    if operator not in ["+", "-", "*", "/"]:
        raise ValueError("เครื่องหมายต้องเป็น +, -, *, / เท่านั้น")
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
        
    print(f"{num1} {operator} {num2} = {result}")   
       
except ValueError: #กรณีผู้ใช้ไม่พิมพ์ตัวเลข
    print("กรุณากรอกตัวเลขหรือเครื่องหมายให้ถูกต้อง")
    
except ZeroDivisionError: #กรณีผู้ใช้ตัวหารเป็น 0
    print("ไม่สามารถหารด้วยศูนย์ได้")
    
else: #จะทำที่นี่ต่อเมื่อไม่มี exception 
    print("คำนวณข้อมูลเรียบร้อยแล้ว")
    
finally: #ทำเสมอไม่ว่าจะมีหรือไม่มี exception เกิดขึ้นก็ตาม
    print("จบการทำงาน")