import re
from task1 import ComplexNumber

bracket_regex = re.compile('\([+-i\d]+\)')
operation_regex = re.compile('\)[*+-]\(')
number_regex = re.compile('[-]?\d+')


def parse_equation(string):
    values = re.findall(bracket_regex, string)
    operation = re.findall(operation_regex, string)[0][1]
    number1 = re.findall(number_regex, values[0])
    number2 = re.findall(number_regex, values[1])
    return ComplexNumber(int(number1[0]), int(number1[1])), \
           ComplexNumber(int(number2[0]), int(number2[1])), \
           operation
    pass


if __name__ == '__main__':
    print("Format: (a+bi)*(c+di)")
    print("Supported operations: +/-/*")
    string = input('Equation: ')
    comp1, comp2, operator = parse_equation(string)
    if operator == '+':
        print(f"({comp1})+({comp2})={comp1 + comp2}")
    elif operator == '*':
        print(f"({comp1})*({comp2})={comp1 * comp2}")
    elif operator == '-':
        print(f"({comp1})-({comp2})={comp1 - comp2}")
