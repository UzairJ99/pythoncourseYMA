# syntax for a for-loop
for x in range(0, 10):
    # code block is everything that is indented
    print(x)
# end of a for-loop is indicated by the next line not being indented
print("this is outside of the loop")

# x is the iterator; a variable used to keep track of the number of times the code block has looped
# the loop will begin at 0 and count up to (but not including) 10
# notice x's value in the terminal when printed

# let's change the way the loop counts. Let's count by 2s instead
for x in range(0, 10, 2):
    print(x)

# notice the output

# let's count backwards
for x in range(10, 0, -1):
    print(x)

# notice the output and our changed start and end values


