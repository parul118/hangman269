word_list = ['Apple','Banana','Mango','Guava','Grapes']
print('Favourite Fruits',word_list)
guess = input("enter a single letter")
if (( len(guess) == 1 ):
  if(isalpha(guess)):
    print( "Good guess!")
  else : 
    print("Oops! That is not a valid input.")
