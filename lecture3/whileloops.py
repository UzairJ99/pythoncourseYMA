# syntax for while loops
'''
while(True):
    # code block
    print("hi")
'''

# we wouldn't want to run this because it will result in an infinite loop.
# instead we'll replace True with a dynamic condition (one that can change so the loop can stop eventually)
# Since the condition is currently set to True, it's static - never changes - and will cause the loop to repeat forever

# let's make a finite loop
counter = 0  # this counter will determine how many times we've looped

while (counter < 10):
    print("hi")
    counter += 1  # increase the value of counter by 1 each time the code loops

# this will print hi 10 times because it will loop until counter has reached the value 9 (notice counter < 10)

# let's use a boolean data type as our condition

keepGoing = True

while (keepGoing):
    print("loop")
    keepGoing = False  # keepGoing is set to false, so the next iteration the condition is not met

# we only see 1 occurrence of "loop" because once the first iteration is complete, the condition is no longer met

# let's combine the two styles to make one complex loop

on = True  # this variable will hold whether the game is still on or not
score = 0  # this variable keeps track of the player's score

while(on):
    if (score == 10):  # conditionals are a decision making model - more on this in lecture
        on = False  # turn off the game
    else:
        print("score: " + str(score))
        score += 1  # increase the score
print("game over.")

# the game will increase the player's score until it reaches 10 and then it will end

# let's look at the break command.  What if we wanted to terminate the loop based on another condition rather than
# the original condition.

score = 0

while(score < 10):
    if (score == 5):
        break
    else:
        print(score)
        score += 1


