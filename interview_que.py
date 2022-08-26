# def adding_two_num(i1, i2):
#    while i2 != 0:
#        data = i1 & i2
#        i1 = i1 ^ i2
#        i2 = data << 1
#    return i1
# print("Adding without using plus operator")
# print(adding_two_num(6,1))

# map function
# def addition(n):
#     return n + n
# numbers = (10, 20, 30,40)
# result = map(addition, numbers)
# print("Using map() function\n")
# print(list(result))

# def extendList(val, list=[]):
#     list.append(val)
#     return list
# list1 = extendList(10)
# list2 = extendList("CopyAssignment",[])
# list3 = extendList('a')

# print("Output:\n")
# print(list1,list2,list3)


# list = [ [ ] ] * 6
# print(list) 
# list[0].append(99)
# print(list)
# list[1].append(98)
# print(list)
# list.append(97)
# print(list)

# filename=input("Enter file name: ")
# for line in reversed(list(open(filename))):
#     print(line.rstrip())

# import sys
# print(sys.version)

# from math import factorial, sqrt
# print(sqrt(6))
# print(factorial(4))

# print("f","g",sep="")
# print('09','12','2016', sep='-')
 
# #another example
# print('pratik','geeksforgeeks', sep='@')


# print('G','F', sep='', end='')
# print('G')
# #\n provides new line after printing the year
# print('09','12','2016', sep='-', end='')
 
# print('prtk','agarwal', sep='', end='@')
# print('geeksforgeeks')

# a="aaaabbbcccabcdeff"
# i=0
# while i<len(a)-1:
#     if a[i]!=a[i+1]:
#         print(a[i],end="")
       
#     i+=1
# print(a[-1])
# a="rohini   "
# b="swathi"
# a+=b
# print(a)
# op rohini swathi
  

# s='arfardarb'
# # i=0
# a=[]
# b=[]

# while i<len(s):
#     j=0
#     c=0
#     while j<len(s):
#         if s[i]==s[j] and i<j:
#             c+=1
        
#         j+=1
#     i+=1


#    a.append(s[i])
#    i+=1
# j=0

# while j<len(a):
#     c=a.count(a[i])
#     j+=1
#     print([a[j],c])
# s='arfardarb'
# for i in range(0,len(s)):
#     c=0
#     for j in range(i+1,len(s)):
#         if s[i]==s[j] and i<j:
#             c+=1
#             print([s[i],c],end ="")
# a=[]
# import collections
# from unittest import result
# results = collections.Counter(s)
# print(results)

# for char in s:
#   c = s.count(char)
#   if c >1  :
#     print(char,c)


# def century(year):
#     # Finish this :)
#     b=year//100
#     if year%100==0:
#         return b
#     else:
#         return b+1

# print(len([0,0]))
# i=1
# while i<=100:
#     if i%2==0:
#         print(-i,end=" ")
       
#     else:
#         print(i,end=" ")
#     i+=1 

# l=[2,8,9,2,6,7,4]
# i=0
# c=[]
# while i<len(l)-1:
#     if l[i]<l[i+1]:
#         c.append(l[i])
#     i+=1
# print(c)



# l=[1,2,3,4,3,5]
# i=0
# c=[]
# while i<len(l):
#     l[i], l[i+1] = l[i+1], l[i]
#     c.extend([l[i],l[i+1]])
#     i+=2
# print(c)


# a=[['a',5],['b',4],['c',6]]

# s=[]
# d={}
# for i in a:
#     for j in i:
#        s.append(j)
# for k in s:
#     d[k]=k
   
    
# print(d)
       
# s=[]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         s.append(a[i][j])
#         j+=1
#     i+=1
# print(sorted(s))


# from math import sqrt
# def nearest_sq(n):
#     return  round(sqrt(n)) ** 2

# print(nearest_sq(45))


# def nearest_sq(n):
#     return round(n**0.5)**2
# print(nearest_sq(45))

def build_string(*args):
    a='I like '
    for i in args:
        a+=i+','
    return a+"!"+'Return the correct String'
print(build_string('Cheese','Milk','Chocolate'))

        
       


