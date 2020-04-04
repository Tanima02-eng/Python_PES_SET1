#5.(b) Find the biggest of three numbers, where three numbers are passed as command line arguments.

import sys
def main2(argv):
        if len(argv) < 3:
            print("Invalid entry!!!!")
        else:
            a= argv[1]
            b= argv[2]
            c= argv[3]
            print ('Params=', a, b, c)
#if _name_ == __main__:

#a,b,c,d=input("Enter the numbers:")

        if (a>b)&(a>c):
            print("the greatest no is",a)
            greatest=a
        elif (b>a)&(b>c):
            print("the greatest no  is",b)
            greatest=b
        else:
            print("the greatest no  is",c)

if __name__ == '__main__':
    main2(sys.argv)
