player1Score = 10
player2Score = 10
player3Score = 10

'''
if (player1Score == 5):
    print("Player1 has won")
else:
    print("Player1 has lost")
'''


if (player1Score > player2Score and player1Score > player3Score):
    print("Player1 has won")
elif (player2Score > player1Score and player2Score > player3Score):
    print("Player2 has won")
elif (player3Score > player1Score and player3Score > player2Score):
    print("Player3 has won")
elif (player3Score == player2Score and player2Score == player1Score):
    print("the game was a tie")

