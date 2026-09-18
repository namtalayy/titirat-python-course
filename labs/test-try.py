"""
#ZeroDivisionException
try:
    numertor = float(input("กรอกตัวตั้ง: "))
    denominator = float(input("กรอกตัวหาร: "))
    
    result = numertor / denominator
    print(f"ผลลัพธ์ = {result}")

except ValueError:
    print("กรุณากรอกตัวเลขให้ถูกต้อง")
    
except ZeroDivisionError: 
    print("ไม่สามารถหารด้วยศูนย์ได้")
"""
#FileNotFoundException, PermissionException
try:
    filename = input("ชื่อไฟล์: ")
    
    with open(filename, "r", encoding="uf-8") as file:
        content = file.read()
        
    print("เนื้อหาในไฟล์")
    print(content)

except FileNotFoundError: #ไม่มีไฟล์นี้อยู่จริง
    print(f"ไม่พบไฟล์ชื่อ {filename}")
    
except PermissionError: #สิทธิ์เข้าถึงไฟล์
    print("ไม่มีสิทธิ์เข้าถึงไฟล์นี้")