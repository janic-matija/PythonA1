import time
numbers = [62,83,18,53,7,17,95,86,47,69,25,28]
numbers2 = [62,83,18,53,7,17,95,86,47,69,25,28]

def shellSort(lista):
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    # gaps = [5, 3, 1]
    for gap in gaps:
        if gap < len(lista):
            for index in range(0, gap):
                prvi=index
                drugi=index+gap
                while drugi <len(lista):
                    element = lista[drugi]
                    while prvi>=0 and element <= lista[prvi]:
                        lista[drugi]=lista[prvi]
                        prvi = prvi - gap
                        drugi = drugi-gap
                    lista[prvi+gap]=element
                    drugi=drugi+gap
                    prvi=drugi-gap

start = time.time()
shellSort(numbers)
end = time.time()
print(str(end-start))

start = time.time()
numbers2.sort()
end = time.time()
print(str(end-start))

def histogram(rec):
    recnik={}
    recnik['a'] = 1
    for index in range(ord('a'), ord('z')+1):
        recnik[chr(index)] = rec.count(chr(index).upper())+rec.count(chr(index))
    return recnik

