def main():
    get_input = input('What is answer to the Great Question of Life, the Universe and Everything? ')

    if get_input == '42':
        print('Yes')
    elif get_input.lower() == 'forty-two':
        print('Yes')
    elif get_input.lower()== 'forty two':
        print('Yes')
    else: print('No')

main()