def main():
    x  = get_int('Value of X? ')
    print (f'Value is {x}')


def get_int(prompt):
    while True:
        try :
            return int(input(prompt))
        except ValueError:
            #pass can be used to catch an error but skip it
            print('Value is not in numbers!!')
    


# print (f'Value is {get_int()}')

main()
