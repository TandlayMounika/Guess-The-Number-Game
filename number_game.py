#Guess the Number Game
import random
n = random.randrange(1,50)
chances=10
guess = int(input("Guess a number between 1 to 50: "))
while chances>0:
	if n==guess:
	    print("--------------------------")
	    print("Hurray!! You won the game")
	    print("--------------------------")
	    break
	elif guess<n:
		print("The Number is Too low")
	elif guess>n:
	    print("The Number is Too high!")
	chances-=1
	if chances==0:
	    print("--------------------------")
	    print(f"The Number is:{n}")
	    print("Better Luck Next Time")
	    print("--------------------------")
	    break
	print(f"You Have {chances} chances left!!")
	guess=int(input("Enter the number again: "))