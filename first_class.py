'''print("hii")'''
'''a=10
b=12
c=a+b
print(c)'''
'''a=100
b=300
c=a-b
print(c)'''
#print(type(35))
'''x=23 #for remainder
y=10
print("remsinder",x%y)'''
#x=5
#print(x**3)
#wap to show the area of circle  where radius is 14cm
'''p=22/7
r=14
area=p*r**2
print(area,"area of circle")'''
'''x=10
y=2
z=3
s=x+y*z/2
print(s)'''
'''x="pyhton "
y=5
print(x*y)'''
# x=5
# x+=5
# # print(x)

# x*=4
# print(x)
#typecasting in python
# typecasting are used to change the datatype in python
# x=int("23")
# y=30
# print(x+y)
# x=100
# y=complex(x)
# print(y)
# number can  be converted into stirng but string cant be convert into number

# sequence datat type: list tuple range
# 1 list
# 2 tuple
# 3 range
# ________________list_______________
# x=["sunday","monday",12,True,None]
# print(x)
# print(type(x))
# x="ankit sah"
# print(len(x)
# #     )
# x=78465
# print(len(str(x)))
# set : set is a collection of non epetative elements and its written in curly bracket

# =========================================
# cnditiional statement
# it is an imp function in python  which is used to print the statement by condition
#         if,elif,else.

# x = 23
# if x>50:
#     print("true")
# else:
#     print("false")
# n=int(input('write a number:'))
# if n>100:
#     print('above')
# else:
#     print("below")
# x=int(input('write a number:'))
# if x%2==0:
#     print("even")
# else:
#     print("odd")

# x=int(input("write a number:"))
# if len(str(x))>3:
#     print("yes")
# else:
#     print('no')


# wap with the help of user input to show the grade of stdents by precentage
# x=int(input("write your precentage:"))
# if x>80 :
#     print('grade A')
# elif x>70:
#     print('grade B')
# elif x>60:
#     print('grade C')
# else:
#     print('garde D')

# ==========================================
#   and 
#  x=int(input("write your precentage:"))
# if x>20 and x<=50:
#     print('yes')
# else:
#     print('no')
#   or
# x=input('write a text')
# if x=='a' or x=='b':
#     print('yes')
# else:
#     print('no')
# x=input('write your text')
# x=x.upper()
# if x=='PYTHON':
#     print('yes')
# else:
#     print('no')
#

#wap to check that  text contains"a" or not?
# x=input('write your text')
# if 'a' in x:
#     print('yes')
# else:
#     print('no')
# x=input('write your text')
# if x in "aeiou":
#     print('vowel')
# else:
#     print('consonent')

# #       count============================
# x='shah'
# x=x.count('h')
# print(x)

# x=python is programming language
# x="python is programming language"
# print(len(x)-x.count(' '))



# x=input('your text:')
# if len(x)>5:
#     print(x.upper())
# else:
#     print(x.lower())
# wap to print last digit of an number
# x=int(input('write a number:'))
# print(x%10)
# ==========string===================
# upper
# lower
# title
# len
# count
# # indexing :-this isused to extract the character from the text
#             1.positive:-it works from starting to end
#             2.negative:-it starts from end
# xtract the last alhabet from text
# x="python"
# print(x[-1])
# x=input('write a text')
# if x[0] in ("pran"):
#     print('yes')
# else:
#     print('no')
# name=input('write a text')
# if name[0]=="a" and name[-1]=="a":
#     print("yes")
# else:
#     print('no')

# x=int(input('enter first number:'))
# y=int(input('enter second number:'))
# z=int(input('enter third number:'))
# if x>y and x>z:
#      print(x)
# elif y>x and y>z:
#      print(y)
# else:
#      print(z)

# to get the position of an element:-
# Find 
# index
# replace:- its replace the old value into new value


#========================================================================
# slicing:-slicing are used to extract the range of charactor from text.
# 1. positive slicing
# 2.negative slicing

# x="programming"
# print(x[4:7])
    
# extract first three alphabet
# x="programming"
# print(x[0:3])

# x="himachal pradesh"
# print(x[2:6])

# x="himachal pradesh"
# print(x[-4:])

# x="himachal pradesh"
# print(x[0:4])

# x="himachal pradesh"
# print(x[1:5])

# x="arunachal"
# print(x[-8:-4])

# x="arunachal"
# print(x[-3:].upper())
    
# x="delhi"
# print(x[-1::-2])

# x="himachal pradesh"
# print(x[0:5:2])

# x="himachal pradesh"
# print(x[-6:-1:2])

# x="himachal pradesh"
# print(x[0:11:3])

# x="himachal pradesh"
# print(x[-14::-1])
# x="himachal pradesh"
# print(x[0].upper(),x[1:-1].lower(),x[-1].upper())
# strip:-its used to remove the extra space from starting and last only
#split:-it divides th text and convert into list
# x="india is my country"
# print(x.split())

# joins :- its convert the list into strings
# x=["delhi","haryana","patna"]
# print(type(" ".join(x)))
# wap to reverse this text
# x="uttar pradesh"
# y=x.split()
# z=y[-1::-1]
# a=" ".join(z)
# print(a)
#
# +++++++++++++++++++++++++++++++++++++++++++++++
# isdigit():its return true when given value contains only number
# isalpha():-its return the true when given value is only text
# isalpha():- it shows true when value contains number or text
# x=input(":enter a pssword")
# if len(x)<6:
#     print("to short")
# elif x.isdigit() or x.isalpha():
#     print("weak password")
# elif x.isalpha() and len(x)>=8:
#     print("strong password")
# else:
#     print("moderate")

# x=input('write a text')
# if x.count("a")>1:
#     print("repeated value")
# else:
#     print("non repeated")

#capitalize:- it converts first alphabet in capital letter and rest in small letter
# x=input("enter a text")
# if x.isupper():
#     print("capital")
# elif x.islower():
#     print("small")
# elif x.istitle():
#     print("title")
# else:
#     print("special characters")


# x="DatA SCIENCE"
# y=x.swapcase()
# print(y)

# ====================================================
# x="sales400"
# y="sales300"
# a=int(x[5:])
# b=int(y[5:])
# print(a+b)
 
# u=input('write yur character:')
# if u.isalnum():
#     print('not special')
# else:
#     print('special character')


# ________________________________________________________________________________________________________________
# x=1
# while x<=10:
#     print(x)
#     x+=1
# else:
#     print("condition false")
#print 10 times hello world______
# x=1
# while x<=10:
#     print("hello worls")
#     x+=1
# else:
#     print("condition false")
# print counting from 10 to 20____
# x=11
# while x<=20:
#       print(x)
#       x+=1
# else:
#      print("condition false")
# print backward from 20 to 1_____________
    
# x=20
# while x>=1:
#      print(x)
#      x-=1
# else:
#      print("condition false")



# x=1
# while x<=20:
#     if x%2==0:
#          print(x)
#     x=x+1

# x=1
# while x<=10:
#     print(x*5)
#     x+=1
# num=int(input("write yiur no.:"))
# x=1
# while x<=10:
#     print(f"{num} X {x} ={x*num}")
#     x+=1

# x = 1
# while x<=50:
#     if x%4==0 and x%5==0:
#         print(x)
#     x+=1

# x=1
# while x<=15:
#     if x>10:
#         print(x,"high")
#     elif x>5:
#         print(x,"medium")
#     else :
#         print(x,"low")
#     x+=1

#print line
#1. vetical line
#2. horizontal line print(x,end=" ")
# x=1
# while x<=20:
#     print(x,end=",")
#     x+=1
# import time
# x=30
# while x>=1:
#     print(x,end="\r")
#     x-=1
#     time.sleep(2)
    
# x=0
# while x<10:
#     x+=1
#     if x==5:
#         break
#     print(x)

# x=0
# while x<10:
#     x+=1
#     if x==5 or x==6:
#         continue
#     print(x)
# c=0
# x=10
# while x<=30:
#     if x%2==0:
#         c=c+1
#     x+=1
# print("total even number",c)


# c=0
# x=1
# while x<=40:
#     if x%4!=0 or x%5!=0:
#         c=c+1
#     x+=1
# print("total even number",c)


# x=1
# while x<=20:
#     print(x,x**3)
#     x+=1


# c=0
# x=1
# while x<=20:
#     if x**2<150:
#         c=c+1
#     x+=1
# print(c)
#wap to sum of first five numbers
# s=0
# x=1
# while x<=5:
#     s+=x
#     x+=1
# print("sum of first 5 numbers",s)

# wap to add all even umber from 1 to 20
# s=0
# x=1
# while x<=20:
#     if x%2==0:
#         s+=x
#     x+=1
# print(s)

# l=0
# s=0
# x=1
# while x<=10:
#     s+=x
#     l+=1
#     x+=1
# avg=s/l
# print("avg of first 10 numbers :",avg)


# wap with the help of user input to show factorial of any number

# num=int(input("write ur number:"))
# x=1
# f=1
# while x<=num:
#     f*=x
#     x+=1
# print("factorial of ur number:", f)


# guess game
# while true:
#     dice=random.randint(1,6)
#     user =int(input("guess a number"))
#     print("machine generated ",dice)
#     if dice==user:
#         print("won")
#         break
#     else:
#         print('computer won')    

# -------------------------------------------------------------------------------------------------------------------------------------
# for loop
# range :- it comes undder sequence data
# for i in range(20,31,1):
#     print(i)

# for i in range(20,9,-1):
#     print(i)

# 1
# for i in range(1,11,1):
#     print('hello word')

# 2
# num=int(input("write no. for table:"))
# for a in range(1,11,1):
#     print(num*a)

# 3
# for a in range(40,29,-1):
#     if a%2==0:
#         print(a)
# 4
# for a in range(10,41,1):
#     if a%3==0 and a%2==0:
#         print(a)

# 5
# c=0
# for a in range(10,26):
#     if a%2==0:
#         c+=1
# print(c)

# 6
# s=0
# for a in range(1,11):
#     s+=a
# print(s)

# 7
# c=0
# for a in range(1947,2025):
#     if a%4==0:
#         c+=1
#         print(a)
# print("count of leap years",c)

# 8.
# x=("sun","mon","tue","wed","thu","fri","sat")
# for i in x:
#     a=x.index(i)
#     print(i,"index no.",a)

# 9.show the index numbers in negative
# x=("sun","mon","tue","wed","thu","fri","sat")
# for i in x:
#     a=x.index(i)
#     print(i,"index no.",a-len(x))

# wap to print the indedx number of each elements without using find and index

# x="delhi"
# # y=range(len(x))
# for a in y:
#     # print(x[a]," : ",a-len(x))
    
# x="ramayana"
# for i in x:
#     if i=="a":
#         continue
#     else:
#         print(i)


#QUS 
#print all the numbera which is repeated morw than 1 times

# x=[2,3,4,5,6,5,9,4,3,2,3,4,6,7,7]
# for i in x:
#     if x.count(i)>1:
#         print(i)

# x="pr1i3n5ce444"
# for a in x:
#     if a.isdigit():
#         print(a)

# x="A2nK4ItS5ah6"
# for a in x:
#     if a.isupper():
#         print(a)

# homework(wap to check if number is prime number or not)
# x=int(input("write a number to check:"))
# c=0
# for a in range(2,x+1):
#     if x%a==0:
#         c+=1
# if c>1:
#     print(x," is not prime number")
# else:
#     print(x," is prime number")


# wap to count all digits in "x"
# x = "p12r4inc797@e^&sh"
# c=0
# for a in x:
#     if a.isdigit():
#         c+=1
# print(c)

# x = "p12r4inc797@e^&sh"
# c=0
# for a in x:
#     if a.isalnum():
#         continue
#     else:
#         c+=1
# print(c)

# wap to sum all numeric data
# x="python12345"
# s=0
# for i in x:
#     if i.isdigit():

        
#         s+=int(i)
# print(s)

# x="python12345"
# text=""
# num=""
# for i in x:
#     if i.isdigit():
#         num+=i
#     else:
#         text+=i

# print(num)
# print(text)

# x=["pyhthon","sql","program","excel","data","pipline"]
# wap to print all text from list whose starts with "p"
# for i in x:
#     if i[0]=="p":
#         print(i)

# wap to print all text whose length is between 4 to 6
# for i in x:
#     if len(i)>4 and len(i)<6:
#         print(i)

# for i in x:
#     if "o" in i:
#         print(i)



# wap to reverse the text with help of loop without slicing
# x="ankit"
# n=-1
# text=""
# for i in x:
#     if i==x[n]:
#         text+=i
#     n-=1
# print(text)

# or

# for i in range(len(x)-1,-1,-1):
#     print(x[i],end="")

# c=0
# num=int(input('wriite a number:'))
# x =range(1,num+10)
# for a in range(num,num+10):
#     if a%x==0:                                        (wrong code)
#         c+=1
# if c<2:
#     print("total prime numbers",c)


# x=[10,20,30,40,50,60,70,80,90]

#extract elements
#1.[70,60]
# print(x[-3:-5:-1])
#10,30,50
# print(x[0:5:2])
#4. 90,80
# print(x[-1:-3:-1])

#nested indexing
# x=[[14,78,59,26,23,[8,7,5,4]]]
#extract values
#78,59
# print(x[0][1:3])
#7,5
# print(x[0][5][1:3])

#4,5,7,8 extract
# print(x[0][5][-1::-1])

# =====================================================================

# c=0
# x=["a","b","c","A","a","c"]
# for i in x:
#     if i.lower()=="a":
#         c+=1
# print(c)
#========================================================================
#how to add elements in list:
#1.insert:-
#2.append:-
#3.extend:-

# {insert}
# x=["a","b","c","A","a","c"]
# x.insert(0,"data")                            
# print(x)


# {extend}
# x=["a","b","c","A","a","c"]
# x.extend([1,2,3,4])                           
# print(x)


# {append}
#wap to add ALL even numbers in list:
# x=[]
# for a in range(1,21):
#     if a%2==0:
#         x.append(a)                             
# print(x)

# how to delete the elements from the list
#pop
#remove
#clear
#del


# #pop:-its delete the last elemnts
# x=["one",'two','three','four','five']
# x.pop()
# print(x)

# remove:-it deletes the elements from list by values
# x.remove("two")
# print(x)

#clear:- it deletes entire elements from the list
# x.clear()
# print(x)

#del:-its a key word in python which is used to delete the value and variable also
# del x[0:2]
# print(x)

# delete 23 from list
# x=[34,23,23,12,34,23,15]

# for a in x:
#     if a==23:
#         x.remove(a)
        
# print(x)

x=["Aman","Ravi",'Alok','Jimmy','Roy','Aryan']
# wap to writen all name which starts with "a"

# y=[]
# for i in x:
#     if i[0]=="A":
#         y.append(i)
# print(y)
# wap to print all common elements
# x=[12,23,45,56,78]
# y=[47,58,12,45,10]
# for i in x:
#     if i in y:
#         print(i)


# x=["sql",45,25j,True,14,"excel","python"]
# wap to print all text data
# for i in x:
#     if type(i)==str:

#         print(i)

# wap to extract all numbers
# for i in x:
#     if type(i) in (int,float,complex):
#         print(i)

# x=[1,1,1,1,2,2,2,3,3,3,4,4,4]
# extract unique numbers from x
# y=[]
# for i in x:
#     if i not in y:
#         y.append(i)
# print(y)

# how to replace the value in list
# x=[12,45,78,89,56]
# x[1]=100
# print(x)


# x=[12,45,78,89,56]
# sort=its arrange the data in asc or desc order in original list
#sorted=it works same as sort but its store in new vaiable
# 1. sort
#for asc order
# x.sort()
# print(x)

#for desc order
# x.sort(reverse=True)
# print(x)
#2. sorted
# x=[12,45,78,89,56]
# y=sorted(x)
# print(y)


# marks=[234,321,342,435,222,360,202,400]

# 1.
# print(marks[0:2])
# 2.
# marks.sort(reverse=True)
# print(marks[0])
3.
# marks.sort()
# print(marks[2])
# 4.
# marks.sort(reverse=True)
# print(marks[0:3])

# ================================================================
# copy():-it copies entire data structure of previous variable.
#===============================================
#sum
#min
#max

# x=[12,45,78,89,56,23]
# m=max(x)
# mn=min(x)


#=====================================================
# x=[[1,2,3,],4,5,6,[7,8,9]]
# #extract in list format
# y=[]
# n=0
# for i in x:
#     if type(i)==list:

#         y.extend(i)
#     else:
#         y.append(i)
        
# print(y)

# 1.
# x=int(input("write length of list"))
# y=[]

# for i in range(x):
#     val=input("enter value to add")
#     y.append(val)
# print(y)

# 2 add missing value
# x=[1,2,4,5]

# for i in range(1,6):
#     if i not in x:
#         x.append(i)
# print(x)
# 4
# x=[20,45,85,60,30]
# z=x.copy()
# x.clear()

# for i in z:
#     if i>75:
#         x.append("high")
#     elif i>40:
#         x.append("medium")
# #     else:
#         x.append("low")
# print(x)

# print most frequent
# x=[8,7,5,7,4,5,8,8]
# f=0
# v=0
# for i in x:
#     c=x.count(i)
#     if c>f:
#         f=c 
#         v=i   
# print(v)

# wap to written elements which is repeated ore than 1 times
# x=["A","A","B","C","C","D"]
# for i in range(len(x)-1):
#     if x[i]==x[i+1]:
#         print(x[i])

# wap to split [1,2,3,4,5,6,7] into chunks or list
# expected output[[1,2,3],[4,5,6],[7]]
# x=[1,2,3,4,5,6,7]
# y=[]
# for i in x:
#     if i in x[0:1]:
#         y.append(x[0:3])
#     elif i in x[1:2]:
#         y.append(x[3:6])
#     elif i in x[2:3]:
#         y.append([x[-1]])

# print(y,": LIST y")

# =========================================================
# x=[12,34,[2,3,4,[8,7,9]]]
# extract these
# 2,3
# print(x[2][0:2])
# [4, [8, 7, 9]]
# print(x[2][2:4])
# 8,9
# print(x[2][3][-1::-2])

# rearrange [8,7,9] as [7,8,9]
# x[2][3].sort()
# print(x)
# =========================================
# x=["apple",'orange','grapes',"lichi","plum","mango"]

# for i in x:
#     if i[0] in "aeiou":
#         print(i)
# =======================

# write max length of text 
# v=""
# f=0
# for i in x:
#     if len(i)>f:
#         f=len(i)
#         v=i
# print(v,f)
# or

x=["apple",'orange','grapes',"lichi","plum","mango"]
# v=""
# c=0
# for i in range(len(x)):
#     if len(x[i])>c:
#         c=len(x[i])
#         v=x[i]
# print(v)

# y=sorted(x,key=len)
# print(y[-1])




# =================list comprehansion==================================================================
# wap to count backward from 10 to 1 store in list with list comprehansion
# x=[i for i in range(10,0,-1)]
# print(x)


# ===================================
# create a list with 10 elements range between 10 to 80
# x=[]
# import random as r
# for a in range(10):
#     k =r.randint(10,80)
#     x.append(k)
# print(x)

# with list comprehansion
# y=[]
# x=[r.randint(10,80) for i in range(10)]
# print(x)
# =====================================
# wap to print all even numbers from list
# # x=[3,8,7,4,6,9,3,4,6,8]
# # x=[i for i in x if i%2==0]
# # print(x)

# # wap to create a list which contains cube of x elements
# # x=[3,8,7,4,6,9,3,4,6,8]
# # y=[i**3 for i in x]
# # print(y)

# ============================tuple===================================
# tuple is a collection of repetatative elements which is used to store the multiple values in single variable.
# this is part of sequence data type.
# 1.tuple is written in round bracket()
# 2. tuple are ordered
# 3.tuple are imutale or un changable
# 4.tuple also allow duplicate values
# 5.tuple are indexed.
# 6. tuple allow multiple type of data


#create blank tuple
# x=()
# y=tuple()

# print(x)
# print(y)
# print(type(x))

# x=(12,23,34,45,56,78,89,90)
# x=list(x)
# repalce first three value into 200
# x[0:3]=[200]
# print(x)

# delete last 2 elements
# x=(12,23,34,45,56,78,89,90)
# x=list(x)
# del x[-1:-3:-1]
# print(x)

# add 256 in last of tuple
# x=list(x)
# x.append(256)
# x = tuple(x)
# print(x)

# fiter all even number store in new tuple----
# x=(12,23,34,45,56,78,89,90)
# y=()
# y=list(y)
# for i in x:
#     if i%2==0:
#         y.append(i)
# y=tuple(y)
# print(y)

# replace 78 into 100
# x=(12,23,34,45,56,78,89,90)
# x=list(x)
# y=x.index(78)

# x[y]=100

# print(x)
# ==============================================
# packing and unpacking in tuple:
# packing:- in this technique we divide the elements of tuple
# in variable.
#           (no. of variable=no. of elements in tuple))

# x=(100,20,300)
# a,b,c=x
# print(a)
# print(c)

# unpacking:- number of variable is less than numbers of values tuple 

# x=(10,20,30,40,50,60,70)
# a,*b,c=x
# print(a)
# print(b)
# print(c)
# # =========================================================================
                    # SET
# 1.set written with in curly bracket.
# 2.set are unordered.
# 3.set is changable.
# 4. set not allow duplicate values.
# 5.set are un-indexed.
# 6.set allow multiple type of data.

# how to ceate blank set
# x=set{}

# x={2,3,5,6,7,8,89,9,}
# print(x)


# x=[1,3,2,3,4,5,3,2,2,3,3,2,1,2,5]
# x=set(x)
# x=list(x)
# print(x)
# ============================================
# how to add elements in set 
# 1.add
# 2.update
# 3.union
# ============================================
#how to delete elements in set{}
x={23,34,56,67,89,21,12}


#1. remove or discard:- it deletes element from set by value or element
# x.remove(89)
# print(x)

# x.discard(21)
# print(x)

# 2. pop  it deletes randon elelment from set.

#3. clear():- it deletes entire elements from from set
# x.clear()
# print(x)

#4. del :- it deletes entire variable of set.
# del x

# =============SYMMETRIC DIFFERENCE==================================
# x={1,2,3,4}
# y={3,4,5,6}
# z=x.symmetric_difference(y)
# print(z)

# x={1,2,3,4}
# y={3,4,5,6}
# x.symmetric_difference_update(y)
# print(x)


# ================intersection==============================
# comon elements
# x={5,6,4,7,1}
# y={1,45,2,9,4}
# a=x.intersection(y)
# print(a)


# x={5,6,4,7,1}
# y={1,45,2,9,4}
# x.intersection_update(y)
# print(x)

# ++++++++++++++++++++++++++++++QUS ON SETS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# x=set()
# for a in range(3):
#     user =int(input("write a number"))
#     x.update({user})
# print(x)


# x={"noise","loud","hike","place","replace",'refine',"logics"}
#1.create a list to store ALL ELEMNETS WHICH CONTAINS "i"
# y=set()
# for a in x:
#     if  "i" in a:
#         y.add(a)
# print(y)

# 2.2. create a set and add all elements aith prefix"pr. " in new set 
# x={"pr. noise","pr.loud....."}

# y=set()
# z="pr."
# for a in x:
    
#         y.add(z+a)
# print(y)

# 3. create a blank set to add the elements with starting and ending of underscore whose name startswith,"r"
# z="_"
# y=set()
# for a in x:
#     if a[0]=="r":
#         y.add(z+a+z)
# print(y)

# wap to create calculator
# o = input("enter a operator :")
# a= int(input('enter a number :'))
# b= int(input('enter b number :'))

# if o=='+':
#     print(a+b)
# elif 0=='-':
#     print(a-b)
# elif o=='*':
#     print(a*b)
# elif 0=='/':
#     print(a/b)
# else :
#     print('wrong operator')

# ==============================or=======================================
# x=eval(input("use calculator :"))
# print(x)


# ===============================DICTIONARY=====================================================
# dictionary is a collection of non repetative elements. 
# its always written with the pair f keys and values
# its also store multiple data type in Dect.
# 1.it doesnt allow duplicate value.
# 2.written in curly bracket
# 3.dict are ordered
# 4dict are mutable and changable.
# 5dict are not idexed.
# 6 its also support multiple type of data

# HOW TO CREATE DUPLICATE DICTIONARY
# dic={}
# dic=dict()

# dc={"brand":"tata",
#     "model":"xyz",
#     "colour":"black"}
# print(dc)

# create dict with name of students
# st={1:"ankit",2:"naman",3:"mayank",4:"nisha"}
# # print(st)

# extract the name of student whose no. is 1
# with formula--------
# x=st.get(2)
# print(x)

# without formula------------------
# dc={"brand":"tata",
#     "model":"xyz",
#     "colour":"black"}
# x=dc["colour"]
# print(x)

# ========================================

# st={
#     "bihar":"patna",
#     "delhi":"new delhi",
#     "assam":"dispur",
#     "up":"lucknow"}
# user=input("write ur state")
# if user not in st:
#     print("not found")
# else:
#     x=st[user.lower()]
#     print(x)


# =============================================
# keys : its return array where show entire keys of dictionary
# values: its return array where show entire values of of dictionary.
# x={1:"ankit",2:"naman",3:"mayank",4:"nisha"}
# key = x.keys()     #extract all keys from dictionary
# print(key)

# val = x.values()   #extract all values from dictionary
# print(val)


# x={"brand":"samsung",
#    "model":["m10","a21","s24","s24 ultra"],
#    "ram":["4gb","6gb","12gb","16gb"],
#    "colour":["black","blue","white"],
#    "storage":["128gb","256gb","512gb","1tb"],
#    "processor":"mediatalk",
#    "price":[56000,70000,85000,125000]}
# # print(x)
# user=input("enter keys:")
# val=x.get(user)
# print(val)

# # find total number of model:
# val=len(x.get("model"))
# print(val)

# how to ADD keys and values in dictionary------------------------
# with formula;--------
# update :- with the help of the formula we can add keys and values in dict and it adds in last of dict.
# x.update({"front camera":"13mp"})
# print(x)

# wihtout formula:--------
# x={1:"oe",
#    2:"two",
#    3:"three",
#    1:"one"}
# # print(x)

# x[6]="six"
# print(x)

# how to replce value from keys
# x={1:"oe",
#    2:"two",
#    3:"three",
#    1:"one"}

# x[1]="hundred"
# print(x)

# 
# how to delete the elements from the dictionary:---------------
# car={"brand":"bmw",
#      "model":"xyz",
#      "color":"red",
#      "price":"1cr",
#      "year":2020}
# print(car)


# pop:-it deletes keys and values by key of dict. 
# car.pop("color")
# print(car)

# popitem:-its delete always last elements from dict.
# car.popitem()
# print(car)

# clear()

# car.clear()

# del 


# x={"brand":"samsung",
#    "model":["m10","a21","s24","s24 ultra"],
#    "ram":["4gb","6gb","12gb","16gb"],
#    "colour":["black","blue","white"],
#    "storage":["128gb","256gb","512gb","1tb"],
#    "processor":"mediatalk",
#    "price":[56000,70000,85000,125000]}

# for i in x:
#     print(i,"==",x[i])
# ==============================
# items:-with the help of this function we can extract 
#         keys and values in tuples of list.

# x={1:"one",2:"two",3:"three"}

# print(x.items())
# =========================================================
# m={"brand":"apple",
#    "model":"16 pro",
#    "Ram":"256gb",
#    "color":"white",
#    "price":100000,
#    "Rank":20}

# # deleta all keys values where keys contains 'o'
# x=[i for i in m if 'o' in i]
# for i in x:
#     del m[i]
# print(m)


# create a dictionary with the help of User
# length=int(input('write dict length:'))
# x={}

# for i in range(length):
#     user=input('write your key:')
#     user2=input('write your values:')
#     x.update({user:user2})
# print(x)


# how to sort the dictionary:---------------------
# sorted:------
# asc-----------
# st={1:'ANKIT',3:"sonu,",2:"aman",4:"raj"}
# s=st.items()
# x=dict(sorted(s))
# print(x)


# desc==
# st={1:'ANKIT',3:"sonu,",2:"aman",4:"raj"}
# s=st.items()
# x=dict(sorted(s,reverse=True))
# print(x)

# sort this dictionary on bases of values
# st={1:'ankit',3:"sonu,",2:"aman",4:"raj"}
# s=st.items()
# x=sorted(s,key=lambda m:m[1])
# x=dict(x)
# print(x)

# reverse keys in values and values into keys of dict--
# st={1:'ANKIT',3:"sonu,",2:"aman",4:"raj"}


# x={j:i for i,j in st.items()}
# print(x)


# ==============nested dictionary==============

# st = {
# 	1:{"Name":"Aman","Age":25,"City":"Noida"},
# 	2:{"Name":"Ankit","Age":30,"City":"Delhi"},
# 	3:{"Name":"Rahul","Age":35,"City":"Haryana"}
# }

# x=st.get(3).get("Name")
# print(x)
		# or
# x=st[3]["Name"]
# print(x)



#			some qus.----
# extract the age of students whose roll no. is 2
# show the all keys of roll number1
# return all values where roll number is 3
# add gender male in roll no.2
# delete city from st where roll no.is 1

#			soluton of above qus.-----
# x=st.get(2)["Age"]
# print(x)

# x=st.get(1).keys()
# print(x)

# x=st.get(3).values()
# print(x)


# st[2].update({"gen":"male"})
# print(st)

# st[1].pop("City")
# print(st)

# =============marksheet of students======================================================
# x={"Prince":{"hnd":56,"math":89,"sc":78,"sst":69,"eng":48},
#    "Sonu":{"hnd":100,"math":95,"sc":98,"sst":93,"eng":99},
#    "Anmol":{"hnd":66,"math":49,"sc":38,"sst":61,"eng":88},
#    "Priya":{"hnd":36,"math":87,"sc":46,"sst":51,"eng":75},
#    "Ankit":{"hnd":35,"math":75,"sc":66,"sst":57,"eng":78},
#    "Mannu":{"hnd":78,"math":85,"sc":46,"sst":81,"eng":91},
#    "Vivek":{"hnd":67,"math":87,"sc":86,"sst":61,"eng":77},
#    "Raj":{"hnd":68,"math":84,"sc":64,"sst":54,"eng":74}}
# # print(x)

# find total marks of students:------------
# user=input("enter the name of stdents:").title()
# st=x.get(user)
# v=st.values()
# s=sum(v)

# print(user,"total marks",s)

# find avg. marks of students:----------
# user=input("enter the name of stdents:").title()
# st=x.get(user)
# v=st.values()
# s=sum(v)

# print(user,"avg. marks",s/500)

# =======================================================/
# x={"Prince":{"hnd":56,"math":89,"sc":78,"sst":69,"eng":48},
#    "Sonu":{"hnd":100,"math":95,"sc":98,"sst":93,"eng":99},
#    "Anmol":{"hnd":66,"math":49,"sc":38,"sst":61,"eng":88},
#    "Priya":{"hnd":36,"math":87,"sc":46,"sst":51,"eng":75},
#    "Ankit":{"hnd":35,"math":75,"sc":66,"sst":57,"eng":78},
#    "Mannu":{"hnd":78,"math":85,"sc":46,"sst":81,"eng":91},
#    "Vivek":{"hnd":67,"math":87,"sc":86,"sst":61,"eng":77},
#    "Raj":{"hnd":68,"math":84,"sc":64,"sst":54,"eng":74}}
# while True:
# 	user=input("enter the name of stdents:").title()
# 	st=x.get(user)
# 	if st==None:
# 		print("enter corect name")
# 	else:
# 		v=st.values()
# 		s=sum(v)
# 		pr=s/5



# 		if pr>=65:
# 			div="first division"
# 		elif pr>=40:
# 			div="second division"

# 		elif pr>=33:
# 			div="third division"
# 		else:
# 			div="fail"
		
# 		print("students","total marks",500)
# 		print("-"*50)
# 		print(user,"-----obtained total marks",s)
# 		print("-"*50)
# 		print(user,"-----precentage",pr)
# 		print("-"*50)
# 		print(user,"-----div",div)
# 		loop=input("i you want to get infrmation of next student press 1 else 2for exit:---")
# 		if loop=="1":
# 			continue
# 		else:
# 			break

# =====================functions=====================================

# WHAT IS FUNCTION?
# FUNCTION IS A BLOCK OF CODE OR BACK OF CODE CA BE RUN AGAIN AGIAN AND AGAIN.

# FUNCTION CREATED BY DEF KEYWORD
# DEF=DEFINE

# THERE ARE TWO TYPE OF FUNCTIONS:-
# 1.IN BUILT 
# 2.USER DEFINED FUNCTIONS

# CREATE A FUNCTION TO GREET GOOD EVENING:
# def greet():
#     print("good evening")

# # calling function 
# greet()


# create a function to print n number of times by User --------

# def mul(n):
#     print("hello world\n"*n)

# mul(5)

# create a function t show the area of circle by radius---------
# def area(r):
#     print(22/7*r**2)

# area(7)

# create a function show square of any number
# def sqr(n):
#     print(n**2)
    
# sqr(5)

# ==============================================================================
# create a function to count-EVEn and print total even number from list
 
# def even(l):
#     
#     x=[x.append(i) for i in l if i%2==0]
    
# l=[1,2,3,4,5,5,5,6,7,8,9,]
# even(l)
 

#  create a function to print an table by passing the argument
# def tabl(num):

#     for i in range(11):
#         print(i*num)
    
# tabl(5)

# create a functoin to show the n highest value
# def large(x,k):
#     x.sort(reverse=True)
#     y=x[k-1]
#     print(y)

# x=[1,2,3,4,5,6,8]
# large(x,3)

# create a function to show thw 2nd position of element

# def positiion(x,v):
#     a=x.find(v)
#     a2=x.find(v,a+1)
#     return a2

# x="ramayan"
# t=positiion(x,"a")
# print(t)

# create a function to show the length of text

# def lennn(x):
#     y=x.replace(" ","")
#     return len(y)

# t="ankit sah"
# l=lennn(t)
# print(l)

# def cap(x):
#    a= x[0:2].upper() 
#    b= x[-2:].upper()
#    c= x[2:-2].lower()
#    val=a+c+b
#    return val

# print(cap("ankit"))


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++/
# ----------------------------by default perameter---------------------

# def percent(x=1000,per=0.1):
#     print("percent :",x*per)

# percent()

# def si(p=1000,r=0.1,t=1):
#     print("simople interest :",(p*r*t))

# si(1000,.1,4)

#============================================================
# arbitatrtry keyword argument
# 1.args and 2.kwrgs can pass a variable number of arguments to a function 
 
# 1.args:
# in python args assign value by index number
# def fun(*x):
#     print(x[0])
#     print(x[1])
#     print(x[2])

# fun(12,3,5,3,4,52,3,5,4)

# 2.kwrgs:
# keyword arbitatry arguments
# in python kwrgs assign value with variable and pint by dictionary keys.

# def fun2(**x):
#     print(x["name"])
#     print(x["city"])

# fun2(name="ankit",Class="10",city="delhi")


# ------------------zip funcction--------------------------
# name=["aman","rahul","ankit","ranjan"]
# salary=[45000,29000,90000,20000]
# x=list(zip(name,salary))
# for i,j in x:
#     if j>50000:
#         print(i)

# ==============================================

# Expected output : {"a":3,"b":3,"d":2,"e":1}
# x=['a','b','a','d','a','b','b','e','d']
# y={}
# for i in x:
#     l=x.count(i)
#     y.update({i:l})

# print(y)

# Write a python program to print the index Number of 
# strings whose text length is even
# x=['pyhton','sql','excel','data','science']

# for i in x:
#     if len(i)%2==0:
#         print(x.index(i),i)

# ============================================================================

# recursion is a programming technique where function calls itself to solve a prolem

# print counting from 1 to 10
# def run(x):
#     if x==11:
#         return
#     print(x)
#     run(x+1)

# run(1)

# print all even number between 1 to 20------
# def run(x):
#     if x==20:
#         return
#     print(x)
#     run(x+2)

# run(2)

# show all the leap year from 1947 to current
# def leap(x):
#     if x==2025:
#         return
#     if x%4==0:
       
        
#        print(x)
#     leap(x+1)

# leap(1947)



# def run(x):
#     if x==21:
#         return
#     if x%3!=0:
#         print(x)
#     run(x+1)

# run(1)

# def add(n):
    
#     if n==0:
#         return 0
#     else:

#         return n+add(n-1)
    
# x=add(5)
# print(x)

# def add(n):
    
#     if n==1 or n==0:
#         return 1
#     else:

#         return n*add(n-1)
    
# x=add(5)
# print(x)

# ==========================LAMBDA=========================================
# lambda function are also called anonymous functions . An anonymous 
# function is function defined without a Name 

# as we know to define a normal function in python we need to use def keyword
# -------qus----------------------
# ex = lambda a:a%2==0
# x=[1,2,27,4,8,9,6]
# f=filter(ex,x)
# print(list(f))
        

# ex = lambda a:len(a)>4

# x=['python','excel','sql','machine']

# f=filter(ex,x)
# print(list(f))    


# ========================file handling=======================================
# open():

# r=read the text File 
# w=write  a text file 
# a=append in text file or add in text file



# import time
# path="C:/Users/DELL/Downloads/python_notes.txt"
# data=open(path,"r")
# for i in data:
#     print(i)
#     time.sleep(1)


# to print only for lines
# import time
# path="C:/Users/DELL/Downloads/python_notes.txt"
# c=0
# data=open(path,"r")
# for i in data:
#     if c==4:
#         break
#     else:
#         print(i)
#         time.sleep(1)
#     c+=1

    
#-----------------------------------------------------
# # read(): 
# in pyhton  read function reads text from  strings 

# path="C:/Users/DELL/Downloads/python_notes.txt"
# x=open(path,"r")
# y=x.read()
# print(y)
# x.close()


# path="C:/Users/DELL/Downloads/python_notes.txt"
# x=open(path,"r")
# y=x.read()
# y=y.split()

# print(str(y[0:4]))
# x.close()

# ------------writing mode-------------------------
#PRINT TABLE OF 10 IN THIS FILE.................

# path="C:/Users/DELL/Downloads/python_notes.txt"
# file=open(path,"w")
# x=10
# for i in range(1,11):
#     file.write(f"{x}X{i}={x*i}\n")
               
# file.close()
# print("done!")

# -----------------append mode-----------------------------------
# path="C:/Users/DELL/Downloads/python_notes.txt"
# file=open(path,"a")
# file.write("\n==========================\n")
# x=15
# for i in range(11):
#     file.write(f"{x}X{i}={x*i}\n")
# file.close()
# print("done!")


# ---------to delete file-------------
# import os
# path="C:/Users/DELL/Downloads/python_notes.txt"
# os.remove(path)
# print("done\n file deleted")

# ================QUESTIONS===========================================
# path="C:/Users/DELL/Downloads/Data_Analysis.txt"
# file=open(path,"r")
# x=file.readlines()
# print(x)
# file.close()

# WAP TO COUNT TOTAL NUMBER OF LINES 
# path="C:/Users/DELL/Downloads/Data_Analysis.txt"
# c=0
# x=open(path,"r")
# for i in x:
#     if "a" in i:
#         c+=1
# print(c)

# path="C:/Users/DELL/Downloads/Data_Analysis.txt"
# c=0
# x=open(path,"r")
# y=x.readlines()
# for i in y:
#     if i.strip():
#          c+=1
# print(c)
# ==============modify this file and delete space extra========================================
# path="C:/Users/DELL/Desktop/Data_Analysis.txt"
# x=open(path,"r")
# y=x.readlines()
# x.close()
# z=[i for i in y if i.strip()]

# file = open(path,"w")
# for i in z:
#     file.write(i)
# print("done!")
# file.close()


# =============find total text===========================
# path="C:/Users/DELL/Desktop/Data_Analysis.txt"

# with open(path,"r") as f:
#      t=0
#      for i in f:
#           i=i.split()
#           ln=len(i)
#           t+=ln
#      print(t)

            #    ==================================
			

# path="C:/Users/DELL/Desktop/Data_Analysis.txt"
# text = 0
# line = 0
# alpha = 0
# with open(path,"r") as f:
# 	for i in f:
# 		line+=1  # count lines or rows
		
# 		y = i.replace(" ","")
# 		alpha +=len(y)
		
# 		x = i.split()
# 		text +=len(x)
# #------------------------------------------------------
# print("Total Rows : ",line)
# print("-"*50)
# print("Total text : ",text)
# print("-"*50)
# print("Total Alphabets : ",alpha)
   

# # ----------------intreview questions-------------------------------------
# def swap(x):
#      a,*b,c=x
#      a,c=c,a
#      return (a,*b,c)

# y=swap([1,2,3,4,5,6,6,7,8,9])
# print(y)
# 2. sort this dictionary By values
# d = {'apple': 2, 'banana': 3, 'cherry': 1}
# d=d.items()
# x=sorted(d,key=lambda a:a[1])
# print(dict(x))

# 3. Flatten This list
# x = [[1, 2], [3, 4], [5]]
# y=list()
# for i in x:
    
#     y.extend(i)
# print(y)


# 4. Remove all non-alphabet characters
# x = "Hello@ world$5^"

# l=""
# for i in x:
#     if i.isalpha():
        
#         l+=i
#     else:
#         x.replace("i","")
# print(l)


# 5. Remove duplicate characters
# x = "Welcome to python"
# l=""
# for i in x:
#     if x.count(i)>1:
#         x.replace("i","")
#     else:
#         l+=i
# print(l)
# ---------------or

# y=""
# for i in x:
#     if i not in y:
#         y+=i

# print(y)



# 6. Create a Funcrtion To Count all Special Charactors from A strings
# x = "Ma2*g2i!c M&^arks"
# c=0
# for i in x:
#     if i.isalpha() or i.isdigit():
#         continue
#     else:
#         c+=1
# print(c)

# 7. Create a Lambda Function To show the Cube of Any Number.
# ex=lambda a:a**3
# x=int(input('write a number for cube :'))
# print(ex(x))


# 8. Create a function to show the Negative index Number of elements from list
# x=["a","b","c","d"]
# for i in x:
#     a=x.index(i)
#     print(a-len(x),i)


# ==============================================================
# exceptional handling
# there are four blocks of exception handling
# 1. try: in this block we willl generate exception or write the code

# 2. except:in this block we will handle the errors or print the statement by user

# 3. else:else block will execute when try block will work....
# 4.finally:finally block will execute with both condition when your code is correct or incorrect.

# -------------------------------------
# x={"a":34,"b":39,"c":98,"d":69}
# try:
#     y=input("enter keys :")
#     a=x[y]
#     print(a)
# except:
#     print("not found")




# try:
#     age=int(input('write your age to check eligibility :'))
#     if age>18:
#         print("eligible")
#     else:
#         print("not eligible")
# except:
#     print("Age should have to be a number")
# else:
#     print('code is working')
# finally:
#     print("python🥱")


n = int(raw_input())
integer_list = map(int, raw_input().split())
t=tuple(integer_list)
print(hash(t))
    


