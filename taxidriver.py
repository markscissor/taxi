import pandas as pd
import random

firstName = pd.read_csv("firstname.csv")
lastName = pd.read_csv("lastname.csv")
roofColor = pd.read_csv("roof.csv")

num = int(input('How many names do you want to generate? '))
print('\nDrivers:\n')
for _ in range(num):
    first = random.choice(firstName.firstname)
    last = random.choice(lastName.lastname)
    print(first, last)

print('\nColors:\n')
for _ in range(num):
    roof = random.choice(roofColor.roof)
    print(roof)

print('')

# with open('firstname.csv', 'r') as file:
#     data = file.read()
#     # print(data)
    
#     with open('firstout1.csv', 'w') as ofile:
#         prev = ''
#         for row in data:
#             print(prev, row)
#             if (row.islower()):
#                 ofile.write(row)
#             elif (row.isupper() and prev.islower()):
#                 ofile.write( '\n' + row)
#                 print('newline')
            
#             prev = row
            

