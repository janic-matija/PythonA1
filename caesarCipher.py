import sys
import os

n = len(sys.argv)
# niz=['caesarCipher.py','e',1,'encodeme.txt','python']
# sys.argv=niz
if sys.argv[1] != 'e' and sys.argv[1] != 'd':
    print("pogresan prvi parametar ('e' ili 'd')")
    exit()
if int(sys.argv[2]) < 0 or int(sys.argv[2]) > 25:
    print("pogresan drugi parametar (izmedju 0 i 25)")
    exit()
if not os.path.isfile("TXT/" + sys.argv[3]):
    print("pogresan treci parametar (nije fajl)")
    exit()

if sys.argv[1] == 'e' or sys.argv[1] == 'd':
    filePath = "TXT/"
    shift = int(sys.argv[2])
    letterIndex = 0
    readingFile = filePath + str(sys.argv[3])
    read = open(readingFile, 'r')
    writingFile = filePath
    if sys.argv[1] == 'd':
        writingFile += "decoded.txt"
    else:
        writingFile += "encoded.txt"
    write = open(writingFile, 'w')
    for linija in read:
        for slovo in linija:
            z = ord('z')
            a = ord('a')
            mod = z - a + 1  # mod = 26
            if slovo.isalpha():
                if slovo.isupper():
                    a = ord('A')
                    z = ord('Z')
                if len(sys.argv) == 5:
                    codeWord = sys.argv[4]
                    if slovo.isupper():
                        codeWord = codeWord.upper()
                    shift = ord(codeWord[letterIndex % len(codeWord)]) - a
                kod = ord(slovo) - a + shift
                if sys.argv[1] == 'd':
                    kod = kod - 2 * shift  # kod - encode - encode
                kod = kod % mod + a
                slovo = (chr(kod))
                letterIndex = letterIndex + 1
            else:
                letterIndex = 0
            write.write(slovo)
