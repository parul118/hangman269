
while True:
    guess = input("guess the letter")
    if ( len(guess) == 1 ):
        if(guess.isalpha()):
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
