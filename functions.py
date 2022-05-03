#def is used to define functions
#(to="world") is used to assign a default value to the to variable
def main():
    name = input("Your name? ")
    #pass name variable as argument in the hello function
    hello(name)


def hello(to="world"):
    #recieve value of name variable as a variable "to"
    print('hello,',to)


main()



# print(name)