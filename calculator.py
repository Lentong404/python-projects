def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def subtract(n1, n2):
    return n1 - n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}



def mathematics():
    reuse_number = True

    first_number = float(input("What is the first number? "))

    while reuse_number:
        operator = input("What is the operation you want to use? +, -, *, /")
        second_number = float(input("What is the second number? "))
        for o in operations:
            answer = operations[operator](first_number, second_number)

        print(f"{first_number} {operator} {second_number} is equal to {answer}")
        reuse_number = input("Do you wish to continue with the answer? Y or N ").lower()
        if reuse_number == "y":
            first_number = answer
        elif reuse_number == "n":
            reuse_number = False

            mathematics()
        else:
            print("This is an unexpected statement. The program will now cease.")
            return


mathematics()