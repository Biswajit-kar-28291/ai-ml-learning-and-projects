class Student:
    school = "SVU"

    def __init__(self, name):
        self.name = name


s1 = Student("Biswajit")
s2 = Student("Rahul")

print(s1.name, "studies at", s1.school)
print(s2.name, "studies at", s2.school)