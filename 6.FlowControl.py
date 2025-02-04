# ==

3==3

3==4

# !=

3!=3
3!=4

3<4
3<2

#>

3>2
2>3

#<=

3<=3
3<=2

#>=

3>=3
3>=4

#===============================================
#and operator example
(3<2) and (3<1)


(3<4) and (3<5)

(3<4) and (3<2)


#True + True = True
#True + False = False
#False + False = False

#============================================


(3<4) or (3<2)

#or scenario  you should remember

#True + False = True
#True + True = True
#False + False = False


#=======================

not (3<2)

#============================

# If example

num = int(input('Enter a number:'))

if num < 0:
    print(num, 'is negative')
elif num > 0:
    print(num, 'is positive')
else:
    print('I dont know')
    
    
#========================
#nested if
    
snowing = True
temp = -1
if temp < 0:
    print('It is freezing')
    if snowing:
        print('Put on boots')
    print('Time for Hot Chocolate')
print('Bye')

#=========================

age=15
status = ( 'teenager 'if age > 12 and age<20 else 'not teenager')

print(status)
