# # ----------------intreview questions-------------------------------------
# def swap(x):
#      a,*b,c=x
#      a,c=c,a
#      return (a,*b,c)
# # 
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
x = "Welcome to python"
l=""
for i in x:
   if i not in l:
      l+=i
print(l)



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

# 9.  Create a Function to Count unique Alphabet from text
# x = "Python is awesome"
# c=0
# for i in x:
#     if x.count(i)<2:
#         c+=1
# print(c)                     #9 output


# 10. Print all prime numbers between 10 and 50
# c=0
# for i in range(10,51):
   




# # 11. Print 12th of Table With Recursion
def table(x=1):
    user=int(input("table no. u want to print :"))
    if x==11:
        return
    else:
        
        print(f"{user}X{x}={user*x}\n")
    table(x+1)

table()

# 12. Create a Function who will Generate a Random Number from 1 to 6
#		and print "good" if number is Even else print "odd"
# import random
# num=random.randint(1,6)

# print(num)
# if num%2==0:
#     print("good")
# else:
#     print("bad")


# 13.  Find the key with the maximum value
# d = {'a': 5, 'b': 10, 'c': 3}
# d=d.items()
# x=sorted(d,key=lambda m:m[1],reverse=True)


# i,j=x[0]
# print(i)        #key of maximum value



# 14. Create a Dictionary from two List and show All text in capital letter.
# skill = ["python","sql","Excel","Tableau"]
# part = ["Programming","Database","Microsoft","Salesforce"]
# dc=dict(zip(skill,part))
# print(dc)

# 15. Update a dictionary value conditionally
#      Add 10 in Each Value in Dictionary

#x = {"Joe":45,"Ross":63,"Alice":71}





# import ankit

# x=[2,3,4,4,2,4,6]
# l=ankit.even(x)
# print(l)
