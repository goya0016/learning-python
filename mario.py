def main():
    # print_coloum(int(input('How many blocks? ')))
    # print_row(int(input('How many blocks? ')))
    print_square(int(input('How many blocks? ')))

def print_square(size):
    #for each row in square
    for i in range(size):
        #for each brick in row
        # for j in range(size):
            #print brick
            print('#'*size)

        # print()

def print_row(width):
    print('?'*width)


def print_coloum(height):
    for _ in range(height):
        print('#')

main()