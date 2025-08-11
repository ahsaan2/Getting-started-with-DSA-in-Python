from variables import message

account_balance = 200
if account_balance >= 200:
    print("your account has balance")
print(account_balance)  # not in the if statement


def find_amount(balance: int) -> None:
    if balance <= 100:
        print("insufficient balance", "->", balance)
    # print(balance)


find_amount(100)

#  if statement scope-> unlike functions, if statements do not create a new scope
# tha variables defined inside an if statement are accessible outside the if
# statement  (different from java)

if True:
    message = 'If statement is true'
print(message)


#  within functions if statements have the same scope as that of the functions.

def is_balance_low(balance: int) -> None:
    if balance <= 100:
        msg = "low balance present"
        print(msg)


is_balance_low(100)


# now here the msg variable will not be accessible although, it is in if statement,
# it has the same scope here as that if the function
# print(msg)

# -----if else----
def get_min(a: int) -> None:
    bal = 100
    if bal <= 0:
        print("Insufficient balance")
    else:
        print("your current balance is", bal)


get_min(100)


#  elif statements  (execute multiple if-else conditions
def check_range(num: int) -> None:
    current_balance = 400
    if current_balance > num and current_balance == num:
        print("Available balance is ", current_balance)
    elif current_balance < num:
        print("Please maintain the account balance!")
    else:
        print("Please choose the correct option")


check_range(10000)


#  ---------Logical conditions
#  and
def variable_balance(num):
    balance = 100000
    if balance <= num:
        print("insufficient balance")
    elif balance > num and balance > 1000:
        print("you have maintained the account balance")


variable_balance(5000)


mssg = ""
if mssg:
    print("this is an empty string")
else:
    print("this is not an empty string")



