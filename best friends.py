#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     19-08-2016
# Copyright:   (c) Admin 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    a=input("Enter the number of people: ")
    b=[]
    for x in range (0,a):
        y=raw_input("Enter their names: ")
        b.append(y)
    c=raw_input("Enter the name of person to find his best friends: ")
    d=b.index(c)
    if d==a-1:
        print "The best friends of ",b[d],"are",b[d-1] ,"and",b[d-2]
    elif d==0:
        print "The best friends of ",b[d],"are",b[d+1] ,"and",b[d+2]
    else:
        print "The best friends of ",b[d],"are",b[d-1] ,"and",b[d+1]







if __name__ == '__main__':
    main()
