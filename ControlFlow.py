# control flow statements
# pass -> acts as a placeholder and does nothing. We cannot have empty loops, we  use
# pass to avoid errors. It can also be used in conditional statements and functions.

for i in range(1, 5):
    pass  # this code won't throw an error here

for i in range(1, 8):
    if i == 3:
        continue
    if i == 6:
        break
    # if i == 5:
    #     pass
    print("value of i is ", i)
