list_score = []

#รับค่านักเรียนจำนวน 5 คน
for i in range(5):
    score = int(input(f"Enter score of student {i+1}: "))
    list_score.append(score)
    
#คะแนน ผ่าน/ไม่ผ่าน
print("\n")
for i in range(5):
    if list_score[i] >= 50:
        print(f"Student {i+1}: {list_score[i]} -> ผ่าน")
    else:
        print(f"Student {i+1}: {list_score[i]} -> ไม่ผ่าน")