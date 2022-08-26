a= [1,2,3,0,0,0]
# b=[2,5,6]
# c=[]
# i=0
# while i<3:
#     c.append(a[i])
#     i+=1
# e=c+b
# e.sort()
# print(e)
# j=0
# f=[]
# while j<len(e)-1:
#     if e[j]<=e[j+1]:
#         f.append(e[j])
#     j+=1
# print(f)





# c.remove(0)


# c=[1,2,3] 
# d=[2,5,6]
# e=c+d
# print(sorted(e))

# m=int(input("enter num "))
# a= [1,2,3,0,0,0]
# b=[2,5,6,8,4,2]
# c=[]
# for i in range(m):
#     c.append(a[i])
# n=int(input("enter num "))
# for j in range(n):
#     c.append(b[j])
# print(sorted(c))
# d=[]
# for k in c:
#     if k<=k+1:
#         d.append(k)
# print(d)


# i=0
# b=[]
# while i<m:
#     b.append(a[i])
#     i+=1
# print(b)
# n=int(input("enter num  "))
# j=0
# while j<n:
#     b.append(c[j])
#     j+=1
# print(b)


#  def sumDigits(n):
#   if n == 0:
#     return 0
#   else:
#      return n % 10 + sumDigits((n // 10))
# print(sumDigits(345))
# print(sumDigits(45))

from random import shuffle
a=['Python', 'list', 'exercises', 'practice', 'solution']
shuffle(a)
" ".join(a)

print(a)