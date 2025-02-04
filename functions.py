#Syntax of User Defined Function

def <functionsname>([parameter1,parameter2..]):
    statement 1...
    statement 2...
    statement 3...

#Call a function
<functionname>(arg1,arg2)
list2=['apple','orange','banana']
def printList(flist):
  for idx,fruit in enumerate(flist):
    print('Item',idx+1,"We are having :", fruit)
printList(list2)
#output
Item 1 We are having : apple
Item 2 We are having : orange
Item 3 We are having : banana

numlist=[1,2,3,4,5,6]
def squareNum(numberList):
  squareList=[]

  for number in numberList:
    x=number**2
    squareList.append(x)
  return squareList
squaredList=squareNum(numlist)
print(squaredList)


