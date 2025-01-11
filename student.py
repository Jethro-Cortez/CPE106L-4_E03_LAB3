# student.py

class Student:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        """Check if two students have the same name."""
        if isinstance(other, Student):
            return self.name == other.name
        return NotImplemented

    def __lt__(self, other):
        """Check if this student's name is less than the other student's name."""
        if isinstance(other, Student):
            return self.name < other.name
        return NotImplemented

    def __ge__(self, other):
        """Check if this student's name is greater than or equal to the other student's name."""
        if isinstance(other, Student):
            return self.name >= other.name
        return NotImplemented

def main():
    name1 = input("Enter the name of the first student: ")
    name2 = input("Enter the name of the second student: ")
    name3 = input("Enter the name of the third student: ")

    student1 = Student(name1)
    student2 = Student(name2)
    student3 = Student(name3)

    # Test equality
    print(f"Is {student1.name} equal to {student2.name}? {student1 == student2}")
    print(f"Is {student1.name} equal to {student3.name}? {student1 == student3}")

    # Test less than
    print(f"Is {student1.name} less than {student2.name}? {student1 < student2}")
    print(f"Is {student2.name} less than {student1.name}? {student2 < student1}")

    # Test greater than or equal to
    print(f"Is {student1.name} greater than or equal to {student2.name}? {student1 >= student2}")
    print(f"Is {student2.name} greater than or equal to {student1.name}? {student2 >= student1}")
    print(f"Is {student1.name} greater than or equal to {student3.name}? {student1 >= student3}")

if __name__ == "__main__":
    main()