#19.Looping Structure Using loop structures print even numbers between 1 to 100.
#a) By using For loop, use continue/ break/ pass statement to skip odd numbers.
    #i) Break the loop if the value is 50
    #ii) Use continue for the values 10,20,30,40,50
 #b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
    #i) Break the loop if the value is 90
    #ii) Use continue for the values 60,70,80,90

print ("The even numbers from 1 to 100 using for loop is below:" )
for i in range(1,101):
    if (i%2 ==0):
        print (i)
        print("\n")
print("The numbers from 1 to 100 skipping odd numbers using for loop is below:")
for i in range(1, 101):
    if i==50:
        if (i % 2 != 0):
             continue
             print (i)
             print("\n")

