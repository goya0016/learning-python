from pickle import FALSE


def main():
 x = int(input('value of x? '))
 if is_even(x):print('even')
 else: print('odd')

def is_even(n):
    # if n%2 == 0: return True
    # else: return False

    # return True if n % 2 == 0 else False
    return n % 2 == 0 
main()
