users = ["player1", "player2", "player3", "player4", "player5"]

print(len(users))

for x in range(0, len(users)):
    print(users[x])

# print("ignore me")
score = 0

'''
this program loops
through a range of 0-10
and adds to the score each time
'''

for x in range(0, 10, 4):
    # looping and adding 50 to the score each time
    # score += 50
    score += 10
    print("the score is " + str(score))

