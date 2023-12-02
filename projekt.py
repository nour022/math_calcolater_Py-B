from art import logo
# Exponents         2 ** 2

""" the Addition function """


def addition(a, b):
    return a+b


""" the Subtraction function """


def subtraction(a, b):
    return a+b


""" the Division function """


def division(a, b):
    return a/b


""" the Multiplication function """


def multiplication(a, b):
    return a*b


""" the Exponents function """


def exponents(a, b):
    return a**b


opertor = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
    "**": exponents
}
continues = True
test = "a"
print(logo)
while continues:
    if test == "a":
        num1 = int(input("What's the first number?: "))
        oper = input("+\n-\n*\n/\n**\nPick on operation: ")
        num2 = int(input("What's the next number?: "))
        function = opertor[oper]
        cerent_result = function(num1, num2)
        print(f"{num1} {oper} {num2} = {cerent_result}")
    ask = input(
        "Type 'y' to continue calculating with , or type 'n' to start a new calculation: ")
    test = ask
    if test == "y":
        oper = input("+\n-\n*\n/\n**\nPick on operation: ")
        num2 = int(input("What's the next number?: "))
        function = opertor[oper]
        secand_result = function(cerent_result, num2)
        cerent_result = secand_result
        print(f"{cerent_result} {oper} {num2} = {secand_result}")
    else:
        print("GoodBye")
        continues = False
