# this script shows the different ways we can manipulate variables

# strings -------------------------------------------------------------------------------------------------------------

username = "player_1"

print("username: " + username)

# change the username to hold a different value
username = "player_2"
print("username: " + username)

# print the first 4 letters of the username
# start at position 0 and print up to position 3
username = username[0:4]
print("username: " + username)

# change to a different data type
# now that it's an integer, it needs to be converted to a string before concatenating with our sentence
username = 12344
print("username: " + str(username))

# tuples --------------------------------------------------------------------------------------------------------------

location = (54.2232, 543.0000)
print(location)

# tuples are IMMUTABLE - they cannot be changed unless you reassign them a completely new value
# location[0] = 5.33 - this is not permissible. The entire tuple must be changed.
location = ("North", "West")  # this is permissible because we gave it an entirely new value
print(location)

# lists ---------------------------------------------------------------------------------------------------------------

serverRoom = ["user142", "player_2", "user9323", "3nnK92"]
print(serverRoom)

# kick out user142
serverRoom = serverRoom[1:]  # reassign the list value excluding the first person
print(serverRoom)

# rename player_2 to something else
# player_2 is now at index 0 after we removed user142
serverRoom[0] = "something_else123"  # player_2 is at position 0 so we change the element at index 0 of the list
print(serverRoom)

# remove the last person in the list
serverRoom.pop()
print(serverRoom)

# add a new person to the end of the list
serverRoom.append("new_user")
print(serverRoom)

# dictionary ----------------------------------------------------------------------------------------------------------

scores = {"user143": 10, "player_2": 8, "user9323": 13, "3nnk92": 7}
print(scores)

# change user9323's score by adding 5 points to it
scores["user9323"] += 5
print(scores)

# delete player_2 from the dictionary
del scores["player_2"]
print(scores)

# add a new player to the dictionary
scores["new_user"] = 0
print(scores)
