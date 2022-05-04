# students = ['a','b','c']

# houses = ['h1','h2','h3']

#dictionaries
# students = {
#             'a':'h1',
#             'b':'h2',
#             'c':'h3',
#             'd':'h4'
#             }
students = [
    {'name':'a','house':'h1','class':'1'},
    {'name':'b','house':'h2','class':'2'},
    {'name':'c','house':'h3','class':'3'},
    {'name':'d','house':'h4','class':None},
]

# print(students['a'])
for student in students :
    print(student["name"], student["house"], student["class"],sep = ': ')