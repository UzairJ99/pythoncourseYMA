import math


running = True
score = 0

'''
while(running):
    score += 10
    print(score)
    if (score == 50):
        running = False
'''

while(running):
    if (score == 12):
        score += 1
        continue
    elif (score == 14):
        break
    else:
        print(score)
        score += 1
