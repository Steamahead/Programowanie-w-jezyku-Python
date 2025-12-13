class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average = sum(self.marks) / len(self.marks)
        return average > 50


student1 = student("Alice", [60, 70, 80, 90])

student2 = student("Bob", [20, 30, 20, 40])

print("Alice - ", student1.is_passed())
print("Bob - ", student2.is_passed())
