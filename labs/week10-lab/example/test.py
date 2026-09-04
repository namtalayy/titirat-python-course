# 1. รับค่า text จากผู้ใช้
# 2. รับค่าอักษระที่ต้องการค้นหาจากผู้ใช้
# 3. แสดงผลจำนวนอักษระในข้อความ text 

# ตัวอย่างหน้าจอ
# Insert your text: Boonchoo Jitnupong
# Character to find = o
# 5 leter 'o' found in 'Boochoo Jitnupong'
"""
print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Insert your text:")
char = input("Character to find =")
for letter in text: 
    if letter == char: 
        count += 1
print(f"{count} letters '{char}' found in '{text}'")
"""
"""
print("\n=== MEMBERSHIP TEST ===")
print("'a' in 'program':", 'a' in 'program')  # True
print("'at' not in 'battle':", 'at' not in 'battle')  # False
"""
"""
print("\nRaw string example:")
print("Normal: This is \\x61 \\ngood example")
print(r"Raw: This is \x61 \ngood example")
"""
"""
print("\n=== STRING METHODS ===")
text = "welcome to the world of python"
# Search methods
print(f"Find 'world': {text.find('world')}")
print(f"Count 'o': {text.count('o')}")
print(f"Starts with 'welcome': {text.startswith('welcome')}")
print(f"Ends with 'python': {text.endswith('python')}")
print(f"Replace 'python' with 'java': {text.replace('python', 'java')}") # เปลี่ยนค่า python เป็น java
words = text.split() # แบ่งข้อมูลให้เป็นก้อนย่อยๆ # ['welcome', 'to', 'the', 'world', 'of', 'java']
print(f"Split into words: {words}")
print(f"Join with '-': {'-'.join(words)}") # welcome-to-the-world-of-python
"""
"""
# เขียนโปรแกรมตรวจสอบความแข็งแรงของ password
# นิยามของ storng password คือ ยาวมากว่า 8 ตัว, มีอักษระ @ 1 ตัว, มีตัวเลข, มีตัวอักษร

# ตัวอย่างหน้าจอ
# Insert your password: Boonchoo
# Your password is not storng!

# ตัวอย่างหน้าจอ
# Insert your password: Test@123
# Your password is storng!

password = input("Insert your password:")
lenght = len(password)
words = password.split('@')

if len(words) > 1 and password.count('@') == 1:
    left = words[0].isalnum()
    right = words[1].isalnum()
else: 
    left = False;
    right = False;

if lenght >= 8 and len(words) == 2 and left == True and right == True:
    print("Your password is storng!")
else:
    print("Your password is not storng!")
"""
print("\n=== ORD() AND CHR() FUNCTIONS ===")
ch = 'R'
print(f"ord('{ch}') = {ord(ch)}")
print(f"chr(82) = {chr(82)}")

# ASCII table example
print("\nASCII values for A-Z:")
for i in range(65, 71):  # A-F
    print(f"chr({i}) = {chr(i)}")
    
        

