# (1). Count number of digits
import numbers

from Dictionaries import empty_dict

n = 5873
while n > 0:
    rem = n % 10
    print(rem, end=" ")
    n = n // 10
print()
# (2). Count number of digits
n = 5873
count = 0
while n > 0:
    count = count + 1

    # n = n % 10 no need to do modulo here
    n = n // 10

print("number of digits: ", count)

# (3) check if a number is palindrome or not
n = 121
# print("number of digits: ", len(str(n)))
reserved = n
reversed_num = 0
while n > 0:
    last_digit = n % 10

    reversed_num = reversed_num * 10 + last_digit
    n = n // 10
print(" reversed_num: ", reversed_num)
if reversed_num == reserved:
    print("palindrome numbers")
else:
    print("Not a palindrome number")

# (4) Armstrong Number
# if the number is equal to the sum of its own digits each raised to the power of the number of digits.

number1 = 153
number2 = number1
# number of digits present

counter = 0
while number1 > 0:
    counter = counter + 1
    number1 = number1 // 10
print(counter)

# checking the values , we use (**) for exponential
total = 0
reserve_value = number2
while number2 > 0:
    last = number2 % 10
    total += last ** counter
    number2 = number2 // 10
print("total ", total)

if total == reserve_value:
    print("Is a armstrong number")
else:
    print("Not a armstrong number")

# (5) Given a number , return the number of divisors in a list
given_number = 10
empty_list = []

# for i in range(1, given_number + 1):
for i in range(1, given_number + 1 // 2):
    # if i > given_number / 2 and i != given_number:
    #     continue
    # if i > given_number / 2:
    #     break
    if given_number % i == 0:
        empty_list.append(i)
empty_list.append(given_number)

print(empty_list)
