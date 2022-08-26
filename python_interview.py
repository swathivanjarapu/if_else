# L = ['a','b','c','d']
# print("".join(L))

# D = dict() 
# for x in enumerate(range(2)): 
#     D[x[0]] = x[1] 
#     D[x[1]+7] = x[0] 
# print(D) 

# dict ={}
# print (all(dict))



# sets = {3, 4, 5}
# sets.update([1, 2, 3])
# print(sets)

# print(type(None))

# T1 = (1)
# T2 = (3, 4)
# T1 += 5
# print(T1)
# print(T1 + T2)

# print('{0:.2}'.format(1.0 / 3))

# numbers = (4, 7, 19, 2, 89, 45, 72, 22)
# sorted_numbers = sorted(numbers)
# even = lambda a: a % 2 == 0
# even_numbers = filter(even, sorted_numbers)
# print(type(even_numbers))
# print(even_numbers)


# def what_century(year):
#     b=int(year)
#     a=b//100
#     if b%100==0:
#         return str(a)+str('st')
#     else:
#         return a+1
# c=int(input("enter"))
# print(what_century(c))


# a = "4, 5"
# nums = a.split(',')
# print(nums)

def ordered_count(inp):
    c=0
    a=[]
#     for i in inp:
#         for j in i:
#             c=inp.count(j)
#             b=j,c
#         a.append(b)
#         c=[]
#         for k in a:
#             if k not in c:
#                 c.append(k)
#     return c
# print(ordered_count('abracadabra'))

month=int(input("enter a months"))
if month==1:
	print("jan =31 days")
elif month==2:
    print("feb =30 days")
elif month==3:
    print("march= 31 days")
elif month==4:
     print("april= 30 days")
elif month==5:
    print("may= 31 days")
elif month==6:
    print("june= 30 days")
elif month==7:
     print("july= 31 days")
elif month ==8:
    print("aug= 30 days")
elif month==9:
    print("sep= 31 days")
elif month==10:
    print("oct= 30 days")
elif month==11:
    print("nov= 31 days")
elif month==12:
     print("dec=30 days")
else:
	print("nothing")