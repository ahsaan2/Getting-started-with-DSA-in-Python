def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

# 1 2 6 5 4 3 7 8 9 10
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num[::-1])


from multiprocessing.connection import answer_challenge

name1 = "madam"
left = 0
right = len(name1) - 1
while left < right:
    if name1[left] != name1[right]:
        print("Not a palindrome")
        break
    left = left + 1
    right = right - 1
    if left == right:
        print("Palindrome")


# print("valid palindrome")


def palindrome(name2, start, end) -> bool:
    if start >= end:
        return True
    if name2[start] != name2[end]:
        return False
    return palindrome(name2, start + 1, end - 1)


name2 = "madam"

start = 0
end = len(name2) - 1

print(palindrome(name2, start, end))


# Find the fibonacci number
class Solution:
    def fib(self, n: int) -> int:
        return fibo(n)


def fibo(num: int) -> int:
    if num == 0 or num == 1:
        return num
    else:
        return fibo(num - 1) + fibo(num - 2)

# create an object of the solution class
s = Solution()
# call the fub method
print(s.fib(10))


from multiprocessing.connection import answer_challenge

name1 = "madam"
left = 0
right = len(name1) - 1
while left < right:
    if name1[left] != name1[right]:
        print("Not a palindrome")
        break
    left = left + 1
    right = right - 1
    if left == right:
        print("Palindrome")


# print("valid palindrome")


def palindrome(name2, start, end) -> bool:
    if start >= end:
        return True
    if name2[start] != name2[end]:
        return False
    return palindrome(name2, start + 1, end - 1)


name2 = "madam"

start = 0
end = len(name2) - 1

print(palindrome(name2, start, end))


# Find the fibonacci number
class Solution:
    def fib(self, n: int) -> int:
        return fibo(n)


def fibo(num: int) -> int:
    if num == 0 or num == 1:
        return num
    else:
        return fibo(num - 1) + fibo(num - 2)

# create an object of the solution class
s = Solution()
# call the fub method
print(s.fib(10))