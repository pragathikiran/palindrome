def is_palindrome_number(number):
    return number == number[::-1]

def start_game():
    print("enter a number to check if it is a palindrome")
    while True:
        number = input("enter a number")

        if number.lower() == "exit":
            print("thanks for playing")
            break

        if not number.isdigit():
            print("enter numbers only")
            continue

        if is_palindrome_number(number):
            print("you are right")

        else:
            print("oops it is not a palindrome number")

start_game()
