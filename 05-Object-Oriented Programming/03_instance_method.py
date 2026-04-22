class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)


s1 = Student("Biswajit")
s1.greet()