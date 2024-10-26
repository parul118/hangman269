import random


class Hangman:
    
    def __init__(self,word_list,num_lives=5):

        
        
        self.word = random.choice(word_list)
        
        self.word_guessed = ['_' for _ in self.word]
        
        self.num_letters = len(set(self.word))
        
        
        self.num_lives = num_lives
        
        self.list_of_guesses = []
        
        

        print("The mystery word has" + str(self.num_letters) + "characters")

        print(self.word_guessed)
         

    def check_guess (self, guess):
        guess = guess.lower()
        if guess in self.word:
            print("Good guess!" + guess + " is in the word.")
            for i in range(len(self.word)):                                                                                                                                                                         
                if (self.word[i] == guess):
                    self.word_guessed[i] = guess
                    
            self.num_letters-1
        else:
            self.num_lives = self.num_lives - 1
            
            print("Sorry," +  guess + " is not in the word. Try again")
            print("You have " + str(self.num_lives) + "  lives left.")

        
    def ask_for_input(self):
        
        while self.num_lives > 0:
        
            guess = input("guess the letter")
            if ( len(guess) != 1 ):
                print("Invalid letter. Please, enter a single alphabetical character.")
               
            elif ( guess in self.list_of_guesses):
                print("You already tried that letter!")
            else:
                self.check_guess( guess )
                self.list_of_guesses.append(guess)
                break
                

    @staticmethod
    def play_game(word_list):
        
    
        game = Hangman(word_list)
        while game.num_lives > 0 and game.num_letters > 0:
            game.ask_for_input()
            print(" ".join(game.word_guessed))
            if game.num_letters == 0:
                print("Congratulations! You won the game!")
                break
            elif game.num_lives == 0:
                print("You lost! The word was:", game.word)
                
            
word_list = ['python', 'java', 'kotlin', 'javaScript']
game = Hangman.play_game(word_list)
