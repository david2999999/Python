def main():
    print("Guess a number between 1 and 100.")
    randomNumber = 35
    found = False

    while not found:
        userGuess = int(input("Your guess: "))
        if userGuess == randomNumber:
            print("You got it!")
            found = True
        elif userGuess > randomNumber:
            print("Guess Lower")
        else:
            print("Guess Higher")

if __name__ == "__main__":
    main()