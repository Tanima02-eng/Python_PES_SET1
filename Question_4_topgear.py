#4 Write a program to find the number is Prime or not.

num=int(input("Enter the number to check for prime"))
if num==1:
  print ("Number",num,"is not a prime number")
elif num>1:
  for i in range(2,num):
    if num%i==0:
      print ("Number",num," is not a prime number")
      break
  else:
    print ("Number",num,"is a prime number")