#6.Write a program to read string and print each character separately.
#a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.
#b) Repeat the string 100 times using repeat operator *
#c) Read string 2 and concatenate with other string using + operator.

str1=input("Enter the string")
for character in str1:
  print (character)
str2=str1[1:-1]
str3=str1[2:-2]
print ("sliced string: ", str2)
print ("sliced string2: ", str3)
str1=input("Enter the string")
print ("str1*100 times=",str1*100)#Repeat the string 100 times using repeat operator *
str1=input("Enter the string")
str3=str1+" hello India"
print ("str3 =",str3)#) Read string 2 and concatenate with other string using + operator.
