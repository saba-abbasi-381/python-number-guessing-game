import random

def guess_game():
    secret_num = random.randint(1,100)
    print("secret num",secret_num)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I have selected a num between 1 to 100.")

    while True:
        try:
            guess_num = int(input("enter num from 1 to 100: ")) 

            attempts += 1
            
            if guess_num < 1 or guess_num > 100:
                print("Please enter a number between 1 to 100")
            elif guess_num > secret_num:
                print("too high")
            elif guess_num < secret_num:
                print("too low")
            else:
                print(f"Congratulations! you guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! please enter a valid number.")

while True:
    guess_game()
    
    again = input("Do you want to play again? (Yes/No): ").lower()

    if again != 'yes':
        print("Thanks for playing!")
        break