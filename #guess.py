
from random import randrange

number = randrange(1,101)

print "Guess the mystery number - it's between 1 and 100!"
guess = input("Type in your first guess: ")
while guess != number:
    if guess > number:
        print "Too high! Guess lower!"
    else:
        print "Too low! Guess higher!"
    guess = input("Type in your guess:")

print "Well done. You are right!"
print "The number was", number




-----------------------------------
Traceback (most recent call last):
  File "C:/Program Files/IBM/SPSS/Statistics/25/week 12 exercise", line 1, in <module>
    number=randrange(1,101)
NameError: name 'randrange' is not defined
>>> ================================ RESTART ================================
>>> 
Guess the mystery number - it's between 1 and 100!
Type in your first guess: 5
Too low! Guess higher!
Type in your guess:55
Too high! Guess lower!
Type in your guess:25
Too low! Guess higher!
Type in your guess:35
Too low! Guess higher!
Type in your guess:45
Too high! Guess lower!
Type in your guess:40
Too low! Guess higher!
Type in your guess:39
Too low! Guess higher!
Type in your guess:40
Too low! Guess higher!
Type in your guess:100
Too high! Guess lower!
Type in your guess:1
Too low! Guess higher!
Type in your guess:1
Too low! Guess higher!
Type in your guess:3
Too low! Guess higher!
Type in your guess:42
Too low! Guess higher!
Type in your guess:43
Too low! Guess higher!
Type in your guess:44
Well done. You are right!
The number was 44
>>> 


