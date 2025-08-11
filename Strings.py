# Length functions
my_string = "hello world"
print(len(my_string))


# which one of the two strings is larger

def get_longer_word(word1: str, word2: str) -> None:
    if len(word1) > len(word2):
        print("word1 is longer than word2")
    elif len(word1) < len(word2):
        print("word2 is longer than word1")
    else:
        print("both the words are of same length")


get_longer_word("hellowWorld", "world")

#  String indexing
my_string = "hello world"
print(my_string[0])
print(my_string[4])
# print(len(my_string[12])) out of range

# ----------string looping-----------
for i in range(len(my_string)):
    print(i, my_string[i])

print("Another way to iterate over the characters")
for char in my_string:
    print(char)

#  -------String Concatenation ---------
str1 = "hello"
str2 = "world"
print(str1 + str2)

# --------Slicing---------
#  Access a portion of a string we can use slicing. Allows us to extract a substring from a string
# by specifying range of index
start, end = 1, 4
print("sliced string ", str1[start:end])


# reversed string
reverse_string = "reverse_this_string"
print(reverse_string[::-1])

# string formatting
name = "Alice"
age = 22
msg = "hello, {}. You are {} years old".format(name, age)
print(msg)
