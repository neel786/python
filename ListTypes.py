#Create List

List1 = ['Item1',45]


#Accessing List
List1[0]

List1[1]

#Add item to a list

List1.append('Item2')

print(List1)

#Insert at a particular position

List1.insert(1,'Item3')

#concatination
List1 = ['Item1','Item2','Item3']

List2 = ['Item4','Item5','Item6']

List3= List1+List2

print(List3)

# Remove

List3.remove('Item6')

print(List3)

#Pop

List3.pop(1)

print(List3)

del List3[0:2]


print(List3)
