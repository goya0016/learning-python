# get input from user
name = input("Your name? ").strip().title()

# remove whitespace from string
# name = name.strip()

# # captialize first letter
# name = name.capitalize()

# # captialize whole
# name = name.title()

# # combine
# name = name.strip().title()



# print
#  f is inseted with {} to make it use parameteres and insert value directly
#  
print("hello,", "\"name\"")
print(f"hello, {name}")
print("hello,",name)
print("hello, "+name)
