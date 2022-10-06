import sys
import os
n=len(sys.argv)
# niz=['caesarCipher.py','e',1,'encodeme.txt','python']
# sys.argv=niz
if sys.argv[1]!='e' and sys.argv[1]!='d':
    print("pogresan prvi parametar ('e' ili 'd')")
    exit()
if int(sys.argv[2])<0 or int(sys.argv[2])>25:
    print("pogresan drugi parametar (izmedju 0 i 25)")
    exit()
if  not os.path.isfile("TXT/"+sys.argv[3]):
    print("pogresan treci parametar (nije fajl)")
    exit()

z=ord('z')
mod=ord('z') - ord('a')  + 1 # mod = 26
a=ord('a')

if sys.argv[1]=='e' or sys.argv[1]=='d':
    filePath="TXT/"
    shift = int(sys.argv[2])
    letterIndex=-1
    readingFile=filePath+str(sys.argv[3])
    read = open(readingFile, 'r')
    writingFile=filePath
    if sys.argv[1] == 'd':
        writingFile += "decoded.txt"
    else:
        writingFile += "encoded.txt"
    write = open(writingFile, 'w')
    write = open(writingFile, 'a')
    for linija in read:
        for slovo in linija:
            if slovo.isalpha():
                letterIndex = letterIndex + 1
                if slovo.isupper():
                    a=ord('A')
                    z=ord('Z')
                if len(sys.argv) == 5:
                    codeWord = sys.argv[4]
                    shift = ord(codeWord[letterIndex%len(codeWord)])
                kod = ord(slovo) - a + shift
                if sys.argv[1] == 'd':
                    kod= kod - 2 * shift  # kod - encode - encode
                kod = kod % mod + a
                # kod = (ord(slovo) - a + int(sys.argv[2]) ) % mod + a
                # print(chr( kod ))
                slovo=(chr(kod))
            else:
                letterIndex=0
            write.write(slovo)


