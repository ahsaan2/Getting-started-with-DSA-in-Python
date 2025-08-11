# ------------------While loop---------

i = 0
while i < 5:
    print("I am in a while loop")
    i += 1

# --------for loop ----------

#  starting i at the index 0
for i in range(10):
    print(i)

# starting i at some index or run the loop in a range
print("We are in range, where the increment will be 1")
for i in range(20, 25):
    print(i)

#  increment i by some value
print("Even numbers")
for i in range(0, 10, 2):
    print(i)

#  reverse order
print("reverse numbers")
for i in range(20, 9, -1):
    print(i)

    #  reversing the numbers using reversed
print("reverse the values using function")
for i in reversed(range(10, 21)):  # 21 is explicit
    print(i)

#  ------Nested loops------------

for i in range(1, 5):
    for j in range(1, 5):
        print("value of i is ", i, "value of j is ", j)



