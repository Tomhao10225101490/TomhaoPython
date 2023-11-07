def fib( n):
    a, b = 0,1
    while b < n :
        print(b,end = ' ')
        a, b = b, a+b

def add(x, y):
    """
    The function "add" takes two parameters, x and y, and returns their sum.
    
    :param x: The first parameter, x, is a variable that represents the first number to be added
    :param y: The parameter "y" is a variable that represents the second number to be added
    :return: the sum of the two input values, x and y.
    """
    return int(x) + int(y)
# The line `x = input("please input your x:")` is prompting the user to input a value for `x` and storing that value in the variable `x`. The `input()` function is used to take user input from the console. In this case, the prompt message is "please input your x:".
x = input("please input your x:")
y = input("please input your y:")
res = add(x,y)
print("the result of the funtion is ",res)
