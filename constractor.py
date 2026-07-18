class Student:
    """
    A professional representation of a Student entity.
    """
    
    def __init__(self, name: str, age: int):
        """
        Initializes the student with a name and age upon creation.
        """
        self.name = name
        self.age = age

    def display_info(self) -> None:
        """
        Displays the student's details in a clean format.
        """
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


def main():
    """
    Main function to execute the Student class demonstration.
    """
    print("--- Student Profile ---")
    # Creating a student instance with explicit keyword arguments
    student1 = Student(name="Naiem", age=22)
    student1.display_info()


if __name__ == "__main__":
    main()