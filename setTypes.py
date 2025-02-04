#Create
basket = {'apples','Orange','Grapes'}

print(type(basket))

set1 = set(('fruit1','fruit2','fruit3'))

print(type(set1))

#Add an item to existing set

basket.add('apricot')

print(basket)

#check number of items in a set

print(len(basket))

# Remove from set

basket.remove('Grapes')

#Remove all items from Set

basket.clear()

print(basket)

#---------------------------

#Set operation

# Union

S1={'apple','Organes','Grapes','banana'}
S2={'grapefruit','lime','banana'}


print('Union:', S1 | S2)


# Intersection

print('Union:', S1 & S2)


# Difference

print('Union:', S1 - S2)

print('Union:', S2 - S1)


#
print('Union:', S1 ^ S2)
