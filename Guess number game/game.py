import random

number=random.randint(1,5)


print("Enter a number between 1 to 5:")

givenNumber=int(input())

if(givenNumber==number):
    print("Successfully match number and you win")
else: print("Try again for last attempt")
givenNumber=int(input())


if(givenNumber==number):
    print("Successfully match number in 2nd attempt and you win")
else: print("Sorry you lose")

# Basic and very simple game for freshers and this is the first step. Next time we will make it advance and complex
# 20/04/2025
