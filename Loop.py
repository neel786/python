count = 0
print('Starting')

while count < 10:
    print(count, ' ', end='')
    count +=1
    #count = count + 1
print()
print('Done')


#=============================

#For loop example

for i in range(0,10):
    print(i, ' ', end=' ')
print()
print('Done')


for i in range(0,10,2):
    print(i, ' ', end=' ')
print()
print('Done')

#===========================


num= int(input('Enter the number to break'))

for i in range(0,10):
    if i == num:
        break
    print(i, ' ', end=' ')
print()
print('Done')


#============================

for i in range(0,10):
    print(i, ' ', end='')
    if i % 2 == 1:
        continue
    print('hey its an even number')
print('Done')
   
#=============================

num= int(input('Enter the number to break'))

for i in range(0,10):
    if i == num:
        break
    print(i, ' ', end=' ')
    
else:
    print()
    print('All condition ran successfully')
