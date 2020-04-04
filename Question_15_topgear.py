#15	Create a list of 5 names and check given name exist in the List.
       # a) Use membership operator (IN) to check the presence of an element.
       # b) Perform above task without using membership operator.
       # c) Print the elements of the list in reverse direction.

list1=['Ram','Ravi','Raj','Rakesh','Ravish']
if ('Ravi') in list1: ##Use membership operator (IN) to check the presence of an element.
  print ("Ravi is present in the list")
else:
  print ("Ravi is not present in the list")
  if (i=='Ravi'): ## Perform above task without using membership operator.
    print ("Ravi is present in the list")
    break
else:
    print("Ravi is not present in the list")
list1.reverse() ##Print the elements of the list in reverse direction.
print ("the elements of list1 in reverse direction are",list1)