 	
# If you write down all the numbers from 1 to 100, then how many times do you write 3 ?
# i=1
# c=0
# s=0
# while i<100:
#     if i%10==3:
#         c+=1
#     i+=1

# print(c)
c1=0
for i in range(0,100):
    if i%10==3:
        c1=c1+1
c2=0
for j in range(0,100):
    if j//10==3:
        c2=c2+1
print(c1,c2)
print(c1+c2)


