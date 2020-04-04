#14.Write a program to create two list A and B such that List A contains Employee Id, List B contains Employee name ( minimum 10 entries in each list ) and perform following operations
#a) Print all names on to screen
#b) Read the index from the user and print the corresponding name from both list.
#c) Print the names from 4th position to 9th position
#d) Print all names from 3rd position till end of the list
#e) Repeat list elements by specified number of times ( N- times, where N is entered by user)
#f) Concatenate two lists and print the output.
#g) Print element of list A and B side by side.( i.e. List-A First element , List-B First element )'''

listEId=[1,2,3,4,5,6,7,8,9,10]
listEName=['Rohit','Dhawan','Kohli','Rahane','Manish','Dhoni','Hardik','Chahal','Bhuvi','Bumrah']
print (listEName)
index=int(input("Enter the index to read from"))
print (listEName[index])
print (listEId[index])
print (listEName[3:-1])
print (listEName[2:])
ntime=int(input("enter the no of times you wish to repeat the list"))
print (listEId*ntime)
print (listEName*ntime)
concatList=listEId+listEName
print (concatList)
for element in range(len(listEId)):
  print ("ListEid element",listEId[element],"listEName elements",listEName[element])