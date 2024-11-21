'''
2018 - Task 4 [20]
You have been asked to create a guessing game program.
The program should:
- Allow player 1 to input a whole number between 
1 and 50 inclusive, for player 2 to guess. 

There must be validation present to check that the 
number entered is between 1 and 50 inclusive.

-	Allow player 2 to have 5 guesses to correctly guess 
the number input by player 1. 
You do not need to validate the input for player 2.

-	Output “You guessed the correct number.” 
When player 2 inputs the same number as player 1. 
The game must end if the correct number is guessed.

-	Output “You did not guess the correct number.” 
When player 2 does not input the same number as player 1.

-	Output “Game over!” when player 2 has five incorrect guesses.
'''

'''
10.	Write your program and test that it works.
[10]
'''
# Write and test your code here
chance = 0
while True:
    p1 = int(input("Player One Input Number "))
    if p1 >= 1 and p1 <= 50:
        print ("Number Accepted")
        break
    else:
        print ("Number Not Accepted (Must be Between 1-50)")
gw = (False)
while True:
    gd = input("easy,medium or hard")
    if gd == ("easy"):
        chance = 8
        print ("Easy chosen, 8 chances given")
        break
    elif gd == ("medium"):
        chance = 6
        print ("Medium chosen, 6 chances given")
        break
    elif gd == ("hard"):
        chance = 4
        print ("Hard chosen, 4 chances given")
        break
    else:
        print ("Sorry, what?")

for i in range (chance):
    p2 = int(input("Player 2 Guess The Number "))
    if p2 == p1:
        print (" That Is The Correct Number")
        gw = (True)
        break
    else:
        print ("Wrong Number, Try Again")
        if p2 > p1:
            print ("Go Lower.")
        else:
            print ("Go Higher.")
if gw == (False):
    print ("Game Over!")
else:
    print ("You Won!")


##### END QUESTION
'''
11.	When your program is complete, test it for the following:
a.	Test 1 - Player 1 inputs the number 55
b.	Test 2 - Player 1 inputs the number 0
c.	Test 3 - Player 1 inputs the number 10 and player 2 guesses 
    the numbers 15 and 10
d.	Test 4 - Player 1 inputs the number 20 and player 2 guesses 
    the numbers 30, 35, 22, 15, 49
[4]
'''
# Test Your Code ABOVE



##### END QUESTION
'''
12.	
Extend your program to identify if player 2's 
guess is lower or higher than the number input by player 1. 
A suitable message must then be output.

Save your program.
[2]
'''
# Copy your code from above. Write and test your code here




##### END QUESTION
'''
13.	

Extend your program to allow player 2 to choose an 
easy, medium or hard game. 

An easy game allows eight guesses, a medium game allows 
six guesses and a hard game allows four guesses.

If player 2 inputs a correct guess, the program must output the 
number of guesses made.

You are not required to validate the input for player 2.

Save your program.
[4]
'''
# Copy your code from above. Write and test your code here



##### END QUESTION