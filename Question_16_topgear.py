#16	Python Numbers	Write program to perform following:
    #i) Check whether given number is prime or not.
    #ii) Generate all the prime numbers between 1 to N where N is given number.

num=int(input("Enter the number to check for prime")) #check whether given number is prime or not.
if num==1:
  print ("Number",num,"is not a prime number")
elif num>1:
  for i in range(2,num):
    if num%i==0:
      print ("Number",num," is not a prime number")
      break
  else:
    print ("Number",num,"is a prime number")
upper=int(input("Enter the no till which you need to print the prime numbers")) #Generate all the prime numbers between 1 to N where N is given number.
print ("The prime numbers between the given range is")
for num in range(2,upper+1):
  if num>1:
    for i in range(2,num):
      if(num%i)==0:
        break
    else:
      print (num)
