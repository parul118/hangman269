
import random




class Hangman:
    
    def __init__(self,word_list,num_lives=5):

        
        
        self.word = random.choice(word_list)
        
        self.word_guessed = ['_' for _ in self.word]
        
        self.num_letters = len(set(self.word))
        
        
        self.num_lives = num_lives
        
        self.list_of_guesses = []
        
        

        print("The mistery word has" + str(self.num_letters) + "characters")

        print(self.word_guessed)
         

    def check_guess (self,word , guess , word_guessed , num_letters):
        guess = guess.lower()
        if guess in word:
            print("Good guess!" + guess + " is in the word.")
            for i in range(len(word)):                                                                                                                                                                         
                if (word[i] == guess):
                    word_guessed[i] = guess
                    
            return num_letters - 1
        else:
            self.num_lives = self.num_lives - 1
            
            print("Sorry," +  guess + " is not in the word. Try again")
            print("You have " + str(self.num_lives) + " left.")

        
    def ask_for_input(self):
        
        while True:
        
            guess = input("guess the letter")
            if ( len(guess) != 1 ):
                print("Invalid letter. Please, enter a single alphabetical character.")
               
            elif ( guess in self.list_of_guesses):
                print("You already tried that letter!")
            else:
                self.check_guess(self.word ,guess ,self.word_guessed,self.num_letters)
                self.list_of_guesses.append(guess)
                
word_list = ['python', 'java', 'swift', 'hangman']
game = Hangman(word_list)
game.ask_for_input() 
