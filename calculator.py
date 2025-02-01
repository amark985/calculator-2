"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

def calculate_nums():

    while True:

        get_nums = input("Enter your calculations. To exit, type 'q'.")

        tokens = get_nums.split('')

        if token[0] == "q":
            break

        else:
            if token[0] == "add":
                add(float(token[1]), token[2])

            elif token[0] == "subtract":
                subtract(float(token[1]), token[2])

            elif token[0] == "multiply":
                multiply(float(token[1]), token[2])

            elif token[0] == "divide":
                divide(float(token[1]), token[2])

            elif token[0] == "square":
                square(float(token[1]))

            elif token[0] == "cube":
                cube(float(token[1]))

            elif token[0] == "power":
                power(float(token[1]), token[2])
            
            elif token[0] == "mod":
                mod(float(token[1]), token[2])

calculate_nums()