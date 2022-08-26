# a="soso"
# a+="  sharm"
# print(a)

# x = 2  # 0b1001
# y = 4
#   # 0b1010

# print(x and y)
# print(bin(x & y))


# x=4
# y=6
# print(x ^ y)
# print(x ^ y)

# a=11%4-3//2//5//4+21
# print(a)

# print(len([0]))
# from itertools import count


# string="arfardarb"

# a=[]
# for i in range(0, len(string)):  
#     c = 1;  
#     for j in range(i+1, len(string)):  
#         if string[i] == string[j] :  
#             c = c + 1;  
#             string = string[:j] +'0'+ string[j+1:];
#     if(c >= 1 and string[i] != '0'): 
#                 a.extend([string[i],c])
# print(a)
# s="arfardarb"
# d={}
# a=[]

# c=0
# for i in s:
#     # d[i]=i
#     f={}
#     for j in i:
#         c=s.count(j)
#         d[j]=c
       
       

# print([d])


# def fun(n):
#     s=0
#     while n>0:
#         m=n%10
#         s+=m
#         n//=10
#     if s>=10 or s<10:
#         while s:
#             a=s%10
#             s//=10
#     elif s%2==0:
#         return "even"
#     else:
#         return "odd"

# n=int(input("enter  "))
# v=fun(n)
# print(v)


def fun(n):
    s=0
    while n>0 or s>=10:
        if n==0:
            n=s
            s=0
        s+=n%10
        n//=10
    if s%2==0:
        return "even"
    else:
        return "odd"
n=int(input("enter  "))
a=fun(n)
print(a)



