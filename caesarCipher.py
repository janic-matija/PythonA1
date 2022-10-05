import sys
import os
n=len(sys.argv)

# for index in range (0,n):
    # print(sys.argv[index])

if sys.argv[1]!='e' and sys.argv[1]!='d':
    print("char")
    exit()
if int(sys.argv[2])<0 or int(sys.argv[2])>25:
    print("int")
    exit()
if  not os.path.isfile(sys.argv[3]):
    print("file")
    exit()

z=ord('z')
a=ord('a')
if sys.argv[1]=='e':
    f = open(sys.argv[3], 'r')
    for linija in f:
        for slovo in linija:
            if slovo.isalpha():
                kod=(ord(slovo)-a+int(sys.argv[2]))
                if kod > z:
                    kod=kod-2
                print(chr( kod%(z-a)+a ))