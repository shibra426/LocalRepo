from art import*
print(text2art("Guess"))
import random
hidden_list=[" porche","bugatti ","mercedes"]
Hidden_word=random.choice(hidden_list)
user=list()
word=True
print("----------------------------------")
print("\t\tGuess the hidden word?????")
i=5
while i>=0:
    ans=input("\nEnter alphabet = ").lower()
    word=True
    if  ans in Hidden_word:
       user.append(ans)
       for letter in Hidden_word:
          if letter in user:
            print("\t",letter,end="")   
          else:
            print("\t_",end="")
            word=False
       if word:
         print("\n\t\t----- > YOU WON <-----\n")
         break
    else:
      print("attempts left = !",i)  
      i-=1 
if not  word:
  print("\tgame over")
  
print("The hidden word was = ",Hidden_word) 
print("-----------------------------------")