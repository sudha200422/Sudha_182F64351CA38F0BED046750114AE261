class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, CGPA: {self.cgpa}"

def sort_students_ascending(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa)
    return sorted_students

# Example usage:
students = [
    Student("devi", "A123", 3.5),
    Student("keerthana  ", "B456", 3.8),
    Student("priya", "C789", 3.2),
    Student("maha", "D234", 3.9),
    

]

sorted_students_ascending = sort_students_ascending(students)

print("Sorted Students by CGPA (Ascending Order):")
for student in sorted_students_ascending:
    print(student)
