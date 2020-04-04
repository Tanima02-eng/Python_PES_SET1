#12.Read 10 numbers from user and find the average of all.
#a) Use comparison operator to check how many numbers are less than average and print them
#b) Check how many numbers are more than average.
#c)  How many are equal to average.


total_sum = 0
for n in range(1,11):
    numbers = float(input('Enter number : '))
    total_sum += numbers
avg = total_sum/10
print('Average of ', 10, ' numbers is :', avg)