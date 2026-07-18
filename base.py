def print_message_multiple_times(message, times):
    """
    Prints a given message a specified number of times.
    """
    for i in range(times):
        print(f"[{i + 1}] {message}")

def main():
    """
    Main function to execute the script.
    """
    target_message = "how bae create"
    repeat_count = 3
    
    print("--- Output System ---")
    print_message_multiple_times(target_message, repeat_count)

if __name__ == "__main__":
    main()