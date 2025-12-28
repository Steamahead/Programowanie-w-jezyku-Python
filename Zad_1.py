class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        srednia = sum(self.marks) / len(self.marks)
        return srednia > 50


student_1 = Student("John", [40, 70, 90, 10, 50])
student_2 = Student("Tom", [20, 40, 50, 60, 10])


print(f"Czy {student_1.name} zdał egzamin: {student_1.is_passed()}")
print(f"Czy {student_2.name} zdał egzamin: {student_2.is_passed()}")
