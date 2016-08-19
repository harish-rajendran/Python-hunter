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
    a=input("enter the length of list: ")
    b=[]
    for x in range (a):
        y=input("Enter the number: ")
        b.append(y)
    d=[]
    for x in range (len(b)):
        for y in range (len(b)):
            if b[x]==b[y] and x!=y:
                d.append(b[x])
    print d[0]



if __name__ == '__main__':
    main()
