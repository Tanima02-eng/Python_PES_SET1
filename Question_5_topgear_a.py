#5.Write a program to receive 5 command line arguments and print each argument separately.
#Example: >> python test.py arg1 arg2 arg3 arg4 arg5
#a) From the above statement your program should receive arguments and print them each of them.*/
import sys
def main2(argv):
        if len(argv) < 6:
            print("Invalid entry!!!!")
        else:
            param_1= argv[1]
            param_2= argv[2]
            param_3= argv[3]
            param_4= argv[4]
            param_5= argv[5]
            print ('Params=', param_1, param_2, param_3,param_4,param_5)
#if _name_ == __main__:
if __name__ == '__main__':
         main2(sys.argv)

