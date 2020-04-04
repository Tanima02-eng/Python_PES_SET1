#13.Write a program to find the biggest of 4 numbers.
    #a) Read 4 numbers from user using Input statement.
    #b) extend the above program to find the biggest of 5 numbers.
#(PS: Use IF and IF & Else, If and ELIf, and Nested IF)

arr=input("Enter the numbers:")
#a,b,c,d=input("Enter the numbers:")
if len(arr) < 5:
    a = arr[0]
    b = arr[1]
    c = arr[2]
    d = arr[3]
    greatest=0
    if (a>b)&(a>c)&(a>d):
        print("the greatest no of the first 4 is",a)
        greatest=a
    elif (b>a)&(b>c)&(b>d):
        print("the greatest no of the first 4 is",b)
        greatest=b
    elif (c>a)&(c>b)&(c>d):
        print("the greatest no of the first 4 is",c)
        greatest=c
    else:
        print("the greatest no of the first 4 is",d)
        greatest=d

    e=int(input("Enter 5th number"))

else:
    print("Invalid entry!!!")

if (e > int(greatest)):
    print(" The biggest of all 5 nos is", e)
else:
    print("Invalid program")