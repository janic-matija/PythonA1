from collections import ChainMap
from collections import Counter
from collections import deque

student = {"name": "Matija", "id_number": 16107, "city": "Nis", "birthYear": 1997}
grades = {"MIKS": 7, "DS": 6, "OOP": 9, "OS": 8}
info = ChainMap(student, grades)
print(info)
print(info["name"])
print(info["OOP"])
print(info["city"])
info["city"] = "KV"
print(info["city"])
print(info["OS"])
grades["OS"] = 7  # info["OS"]=7 dodaje novu vrednost u info/student
print(info["OS"])
print(info)

lista = [1, 3, 3, 5, 7, 3, 9, 11, 7, 13, 22, 5, 13, 1, 3]


def highest_count(niz):
    counter = Counter(niz)
    counter = counter.most_common()
    print(counter[0][0], ":", counter[0][1], "times")


highest_count(lista)


def deque_reverse(niz):
    deque_niz = deque(niz)
    deque_niz.reverse()
    print(deque_niz)


deque_reverse([1, 2, 3, 4, 5, 6, 7, 8, 9])


