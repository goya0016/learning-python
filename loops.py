# i=0
# while i <3  :
#     print ("loops")
#     i += 1


# # i=3
# # while i !=0 :
# #     print ("loops")
# #     i = i-1


# for i in range(3):
#     print('loops')

# while True:
#     n= int(input('what is n? '))
#     if n>0: 
#         break

# for _ in range (n):
#     print (n)

def main ():
    number = get_number()
    loop(number)

def get_number():
    while True:
        n= int(input('what is n? ')) 
        if n>0 :
            break
    return n
    
def loop(n):
    for _ in range(n):
        print ('loop')

main()