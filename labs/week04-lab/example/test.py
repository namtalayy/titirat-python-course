# รับชื่อจริง (หรือข้อความ) จากผู้ใช้
# นับจำนวนสระทั้งหมดในข้อความนั้นว่ามีกี่ตัว (a, e, i, o, u)

# ตัวอย่างหน้าจอ
# What is your name? : Boonchoo
# Yor text have 4 vowels.

count = 0
name = input("What is your name : ")
letter = list(name)
print(letter)

for letter in name:
    if letter == 'a'or letter == 'A':
        count = count + 1
    elif letter == 'e'or letter == 'E':
            count = count + 1
    elif letter == 'i'or letter == 'I':
            count = count + 1
    elif letter == 'o'or letter == 'O':
            count = count + 1
    elif letter == 'u'or letter == 'U':
            count = count + 1
            
print("Your text in voweles", count)


