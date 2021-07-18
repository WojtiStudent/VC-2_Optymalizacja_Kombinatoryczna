import copy
#1. Tworzymy tablice wynikowa, z jednym zbiorem pustym
#2. Przechodzimy po elementach tablicy wejsciowej
#3. Dla kazdego zbioru z tablicy wynikowej tworzymy kopie
#4. Nastepnie dodajemy do niej element z tablicy wejsciowej
#4. Nowo powstale zbior dodajemy do puli zbiorow w tablicy wynikowej
#5. Kroki te powtarzamy, az nie skoncza nam sie elementy tablicy wejsciowej

def power_set(tab,vertexAmount):
    results = [[]]                           #przygotowanie tablicy na wyniki
    tmp = []                                #tablica tworzaca kolejne zbior
    # dla kazdego elementu zbioru wejsciowego
    # przechodzimy elementy tablicy z wynikami
    for i in range(vertexAmount):
        for el in results:
            tmp.append(copy.deepcopy(el))   # do tablicy tymczasowej dodajemy kopie zbioru z tablicy wynikowej
            #print(tmp)
            tmp[-1].append(tab[i])     #do ostatnio dodanego zbioru dodajemy nowy element
        for el2 in tmp:
            results.append(el2)         #dodajemy elementy z tablicy tymczasowej do tablicy z wynikami
        print(results)
        tmp = []                       #zerujemy tablice wynikowa

    return results


