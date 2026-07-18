class Student:
    """
    A professional class representation of a Student.
    """
    def __init__(self, roll: str, gpa: float):
        """
        Initializes the student with a roll number and GPA upon creation.
        """
        self.roll = roll
        self.gpa = gpa

    def display_info(self) -> None:
        """
        Displays the student's details in a formatted layout.
        """
        print(f"Student Roll : {self.roll}")
        print(f"Student GPA  : {self.gpa:.2f}")


def main():
    """
    Main function to execute the OOP demonstration.
    """
    print("--- Basic Object Instantiation ---")
    # Creating first student instance
    student_korim = Student(roll="12345", gpa=3.5)
    print(f"Roll: {student_korim.roll}, GPA: {student_korim.gpa}")
    print(f"Is 'student_korim' an instance of Student? : {isinstance(student_korim, Student)}\n")

    print("--- Using Class Methods ---")
    # Creating second student instance and using its built-in method
    student_rahim = Student(roll="54321", gpa=3.8)
    student_rahim.display_info()


if __name__ == "__main__":
    main()