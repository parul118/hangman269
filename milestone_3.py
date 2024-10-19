
while True:
    guess = input("guess the letter")
    if ( len(guess) == 1 ):
        if(guess.isalpha()):
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

secret_word = "apple"
if guess in secret_word:
    print("Good guess!" + guess + " is in the word.")
else:
    print("Sorry," +  guess + " is not in the word. Try again")
