def shellSort(lista):
    # gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    gaps = [5, 3, 1]
    for gap in gaps:
        if gap < len(lista):
            for index in range(0, gap):
                prvi=index
                drugi=index+gap
                while drugi <len(lista):
                    while lista[drugi] >= lista[prvi] and prvi-gap>0:
                        prvi = prvi - gap
                    if lista[drugi] <= lista[prvi]:
                        swap=lista[prvi]
                        lista[prvi]=lista[drugi]
                        lista[drugi]=swap
                    drugi=drugi+gap
                    prvi=drugi-gap
        print(lista)

def histogram(rec):
    recnik={}
    recnik['a'] = 1
    for index in range(ord('a'), ord('z')+1):
        recnik[chr(index)] = rec.count(chr(index).upper())+rec.count(chr(index))
    return recnik

