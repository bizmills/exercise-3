"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import arithmetic  

def main():
    # Your code goes here
    user_input = raw_input('> ')

    calculator_input = user_input.split(" ")
    first_num = int(calculator_input[1])
    second_num = int(calculator_input[2])

    if calculator_input[0] == "+":
        result = arithmetic.add(first_num, second_num)
        print result

    else:
        return 0

#    pass


if __name__ == '__main__':
    main()