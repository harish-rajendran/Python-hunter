#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     18-08-2016
# Copyright:   (c) Admin 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    dicta = {"a":1,"b":2,"c":3,"d":4,"e":1,"f":3}
    dictb = {"a":1,"c":3,"e":1,"f":3}
    a=[]
    count=0
    for item in dictb.keys():
        if item in dicta.keys():
            del dicta[item]
    a=list(dicta)
    print a[0]
if __name__ == '__main__':
    main()
