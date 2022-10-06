import sys
import os
n=len(sys.argv)

# for index in range (0,n):
    # print(sys.argv[index])

if sys.argv[1]!='e' and sys.argv[1]!='d':
    print("pogresan prvi parametar ('e' ili 'd')")
    exit()
if int(sys.argv[2])<0 or int(sys.argv[2])>25:
    print("pogresan drugi parametar (izmedju 0 i 25)")
    exit()
if  not os.path.isfile(sys.argv[3]):
    print("pogresan treci parametar (nije fajl)")
    exit()

z=ord('z')
mod=ord('z') - ord('a')  + 1 # mod = 26
a=ord('a')

if sys.argv[1]=='e' or sys.argv[1]=='d':
    shift = int(sys.argv[2])
    letterIndex=-1
    read = open(sys.argv[3], 'r')
    writingFile = 'encoded.txt'
    if sys.argv[1] == 'd':
        writingFile = 'decoded.txt'
    write = open(writingFile, 'w')
    write = open(writingFile, 'a')
    for linija in read:
        for slovo in linija:
            if slovo.isalpha():
                if slovo.isupper():
                    a=ord('A')
                    z=ord('Z')
                if len(sys.argv) == 5:
                    codeWord = sys.argv[4]
                    shift = ord(codeWord[letterIndex%len(codeWord)])-a
                kod = ord(slovo) - a + shift
                if sys.argv[1] == 'd':
                    kod= kod - 2 * shift  # kod - encode - encode
                kod = kod % mod + a
                # kod = (ord(slovo) - a + int(sys.argv[2]) ) % mod + a
                # print(chr( kod ))
                slovo=(chr(kod))
                letterIndex=letterIndex+1
            else:
                letterIndex=0
            write.write(slovo)


