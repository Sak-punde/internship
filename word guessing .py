import random


name=input("what is your name?")
 
print("Wishing you sucess!",name)


words=['water','trees','leaves','rainbow','flower','nature','mountain','river','fruits','root','branch','greenary']

word=random.choice(words)


print("Guess the characters")
guesses = ''
turns = 12

while turns > 0:

   failed = 0
   for char in word:


      if char in guesses:
         print(char, end=" ")

      else :
       print("__")

      failed += 1

   

   if failed == 0:
      print("Achieve Victory !")

      print("The word is",word)
   break



print()

guess=input("Guess the character:")  

guesses += guess

if guess not in word :
   turns -= 1
   print("Incorrect")
    
   print("You have", turns,'more guesses')


if turns == 0:
   print("Experience Loss. The word was:",word)  
      
         
             