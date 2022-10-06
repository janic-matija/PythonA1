from collections import ChainMap
from collections import Counter

student={"name":"Matija","id_number":16107,"city":"Nis", "birthYear":1997}
grades={"MIKS":7,"DS":6,"OOP":9, "OS":8}
info = ChainMap(student, grades)
print(info)
print(info["name"])
print(info["OOP"])
print(info["city"])
info["city"] = "KV"
print(info["city"])
print(info["OS"])
grades["OS"] = 7# info["OS"]=7 dodaje novu vrednost u info/student
print(info["OS"])
print(info)

lista=[1, 3, 3, 5, 7, 3, 9, 11, 7, 13, 22, 5, 13, 1, 3]
def highestCount(lista):
    counter = Counter(lista)
    counter = counter.most_common()
    print(counter[0][0], ":", counter[0][1], "times")
highestCount(lista)
