class Student:
    school = "SVU"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


print("Before:", Student.school)
Student.change_school("IIT Madras")
print("After:", Student.school)