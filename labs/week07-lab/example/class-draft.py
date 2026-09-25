"""
2 types of programming
1) structured programming --> การเขียนโปรแกรมเชิงโครงสร้าง ex. c, js, python
2) object-oriented programming (OOP) --> การเขียนโปรแกรมเชิงวัตถุ ex. java, c#, python 

"""
# วิธีในการแก้ปัญหา เป็นแค่แนวทาง template แม่แบบ
class ClassName: # struct
    """Class docstring"""
    
    # ข้อมูลที่ต้องใช้ในการแก้ปัญหา ระบุไว้ใน Constructor method หน้าตาเป็นแบบนี้เสมอ
    def __init__(self, parameters):
        # Constructor method
        self.attribute = value
    
    # การกระทำ --> method
    def method_name(self):
        # Instance method
        return something
    
    def method_name2(self):
        pass

# การสร้างวัตถุจาก class --> เอา class มาใช้
myObj = ClassName(parameters)

# ใช้งานวัตถุจาก class
print(myObj.attribute)
resultFromMethod = myObj.method_name()
myObj.method_name2()

myObj2 = ClassName(parameters)
print(myObj2.attribute)
print(myObj2.method_name())
myObj2.method_name2()