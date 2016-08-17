#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     17-08-2016
# Copyright:   (c) Admin 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    l=[18,45,2,32,87,9,75,41]
    length=len(l)
    count=0
    for i in range(0,length):
        if l[i]==i:
            print "the number and index are same at: ",i
            count+=1
    if count==0:
        print "the index and number are not same in the list "



if __name__ == '__main__':
    main()
