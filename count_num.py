# num1=int(input("enter the number:"))
# num2=int(input("entr the number:"))
# i=1
# while i<num1 and i<num2:
#     if num1%i==0 and num2%i==0:
#         hcf=i
#     i+=1
# print("the hcf of",num1,"and",num2,"=",hcf)


a=int(input("enter thr number:"))
b=int(input("enter the number:"))
i=1
while i<=a*b:
    if i%a==0 and i%b==0:
        print("lcm of",a,"and",b,"=",i)
        break
    i+=1