import random;
print("Welcome to the Gasing Game!");

random_number = random.randint(1, 10);
random_number2 = random.random() * 10;
number = int(input("Enter a number between 1 and 10: "));
if number == random_number:
    print("Congratulations! You guessed the number correctly!");
else:
    print(f"Sorry, the correct number was {random_number}. Better luck next time!");
