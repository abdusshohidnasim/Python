def check_exam_status(mark: int) -> str:
    """
    Checks if a student has passed or failed based on their mark.
    Assuming 33 or above is a passing mark.
    """
    if mark >= 33:
        return "Pass"
    return "Fail"

def get_max_value(val1: int, val2: int) -> int:
    """
    Returns the maximum of two values using a ternary operator.
    """
    # Correct usage of Python's ternary conditional operator
    return val1 if val1 > val2 else val2

def main():
    """
    Main execution block to test the functions.
    """
    print("--- Exam Status Checker ---")
    student_mark = 20
    status = check_exam_status(student_mark)
    print(f"Student Mark: {student_mark} -> Status: {status}\n")

    print("--- Maximum Value Finder ---")
    num1 = 40
    num2 = 55
    max_num = get_max_value(num1, num2)
    print(f"The maximum between {num1} and {num2} is: {max_num}\n")

    print("--- Basic Logic Evaluation ---")
    # Evaluating a simple mathematical truth (from your 5 < 6 logic)
    is_less = 5 < 6
    print(f"Is 5 less than 6? : {is_less}")

if __name__ == "__main__":
    main()
    