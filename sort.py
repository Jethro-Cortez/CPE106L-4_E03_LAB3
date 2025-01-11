import random

class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.name < other.name
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.name >= other.name
        return NotImplemented

    def __str__(self):
        return f"Student(name={self.name})"

def main():
    # Create a list of Student objects with different names
    students = [
        Student("Jethro"),
        Student("Maurice"),
        Student("Franz"),
        Student("Carl"),
        Student("Razec")
    ]

    # Shuffle the list of students
    random.shuffle(students)
    print("Shuffled students:")
    for student in students:
        print(student)

    # Sort the list of students
    students.sort()
    print("\nSorted students:")
    for student in students:
        print(student)

if __name__ == "__main__":
    main()