#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Admin
#
# Created:     17-08-2016
# Copyright:   (c) Admin 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    a=[1,4,3,5,4,3,1,6,5,7,6]
    b=[]
    for x in range (len(a)):
        for y in range (len(a)):
            if a[x]==a[y] and x!=y:
                b.append(a[x])
    print b
    c=set(a)-set(b)
    print c

if __name__ == '__main__':
    main()
