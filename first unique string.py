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
    s=raw_input()
    a=list(s)
    b=[]
    c=[]
    for x in range (len(a)):
        for y in range (len(a)):
            if a[x]==a[y] and x!=y:
                b.append(a[x])
    c=set(a)-set(b)
    c=list(c)
    d=[]
    for x in a:
        if x in c:
            d.append(x)
    print d[0]

if __name__ == '__main__':
    main()
