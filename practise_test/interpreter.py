def main():
    expression = input('Expression: ')
    exp= expression.split(' ')
    x = float(exp[0])
    y=exp[1]
    z= float(exp[2])
    if y == "/":
        print(x/z)
    elif y == "*":
        print(x*z)
    elif y == "+":
        print(x+z)
    else : print(x-z)
main()