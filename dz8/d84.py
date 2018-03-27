import os

directory=input('enter directory:')

d=os.listdir(directory)

print(d)


#####

import os

directory=input('enter directory:')

for i in os.listdir(directory):
    print(i)