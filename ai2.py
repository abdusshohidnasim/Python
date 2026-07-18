def check_vowel_or_consonant(char):
    """
    Checks if a given single character is a vowel or consonant.
    """
    # Check if input is exactly one letter
    if not char.isalpha() or len(char) != 1:
        return "Invalid input. Please enter a single letter."
    
    # Using a set for faster lookup and .lower() for case-insensitivity
    vowels = {'a', 'e', 'i', 'o', 'u'}
    if char.lower() in vowels:
        return "Vowel"
    return "Consonant"

def calculate_grade(score):
    """
    Calculates the student's grade based on numerical score.
    """
    if 80 <= score <= 100:
        return "Grade A"
    elif 60 <= score < 80:
        return "Grade B"
    elif 40 <= score < 60:
        return "Grade C"
    elif 0 <= score < 40:
        return "Fail"
    else:
        return "Invalid input! Score must be between 0 and 100."

def main():
    """
    Main function to execute the evaluations.
    """
    print("--- Character Evaluator ---")
    sample_char = "a"
    print(f"Character '{sample_char}' is a : {check_vowel_or_consonant(sample_char)}\n")

    print("--- Grade Calculator ---")
    try:
        # Taking user input safely
        user_input = input("Enter a number to check grade (0-100): ")
        result = int(user_input)
        grade = calculate_grade(result)
        print(f"Result: {grade}")
    except ValueError:
        print("Invalid input! Please enter a valid integer number.")

if __name__ == "__main__":
    main()