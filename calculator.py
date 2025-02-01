"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

def calculate_nums():

    while True:

        get_nums = input("Enter your calculations. To exit, type 'q'.")

        token = get_nums.split(' ')

        if token[0] == "q":
            print("You are exiting the calculator.")
            break

        else:
            if token[0] == "+":
                result = add(float(token[1]), float(token[2]))
                print(result)

            elif token[0] == "-":
                result = subtract(float(token[1]), float(token[2]))
                print(result)

            elif token[0] == "*":
                result = multiply(float(token[1]), float(token[2]))
                print(result)

            elif token[0] == "/":
                result = divide(float(token[1]), float(token[2]))
                print(result)

            elif token[0] == "square":
                result = square(float(token[1]))
                print(result)

            elif token[0] == "cube":
                result = cube(float(token[1]))
                print(result)

            elif token[0] == "pow":
                result = power(float(token[1]), float(token[2]))
                print(result)
            
            elif token[0] == "mod":
                result = mod(float(token[1]), float(token[2]))
                print(result)


    return result

calculate_nums()