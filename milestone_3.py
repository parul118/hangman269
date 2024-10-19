
def check_guess (guess):
    guess = guess.lower()
    secret_word = "apple"
    if guess in secret_word:
        print("Good guess!" + guess + " is in the word.")
    else:
        print("Sorry," +  guess + " is not in the word. Try again")

def ask_for_input():
    while True:
        
        guess = input("guess the letter")
        if ( len(guess) == 1 ):
                if(guess.isalpha()):
                    check_guess(guess)
                    break
                else:
                    print("Invalid letter. Please, enter a single alphabetical character.")
                

ask_for_input()

