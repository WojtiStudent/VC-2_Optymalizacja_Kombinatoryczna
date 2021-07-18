13.01.2021
# Temat: Problem pokrycia (VC^2) - pokrycie sąsiadów pierwszego i 2-rzędu.

Wojciech Spychalski, Agata Szpotek

## Streszczenie 
Autorzy projektu zaprojektowali i zaimplementowali algorytm pełnego przeglądu podzbiorów wierzchołków grafu, które pokrywają sąsiednie wierzchołki zarówno 1 jak i 2 rzędu. W artykule zawarty jest algorytm sprawdzający pokrycie danego podzbioru, generujący zbiór potęgowy zbioru wierzchołków grafu oraz procedura wykonująca pełen przegląd grafu. Oprócz algorytmów znajduje się tutaj również wizualizacja problemu przy pomocy macierzy oraz oprogramowania generującego grafy GraphViz, a także wykresy związane z średnim czasem wykonania przeglądu oraz średnią wielkością pokrywającego graf podzbioru wierzchołków.


**Słowa kluczowe:** 
  - https://pl.wikipedia.org/wiki/Pokrycie_wierzcho%C5%82kowe
  - https://en.wikipedia.org/wiki/Neighbourhood_(graph_theory)
  - https://en.wikipedia.org/wiki/Second_neighborhood_problem

## Wprowadzenie 

### Definicja
Problem <img src="https://render.githubusercontent.com/render/math?math=VC^{(2)}"> jest uogólnieniem klasycznego problemu pokrycia wierzchołkowego <img src="https://render.githubusercontent.com/render/math?math=VC^{(1)}"> z tą różnicą, że w tym przypadku zasięg pokrycia grafu przez jeden wierzchołek jest rozszerzony z pokrycia sąsiednich wierzchołków (**sąsiadów pierwszego rzędu**) do pokrycia sąsiednich wierzchołków oraz ich sąsiednich wierzchołków (**sąsiadów drugiego rzędu**). W obu przypadkach szukamy rozwiązania w którym wybrane wierzchołki są w stanie pokryć wszystkie wierzchołki znajdujące się w grafie.

### Analiza średniej złożoności 

**Pytanie**: Przy jakich wartościach <img src="https://render.githubusercontent.com/render/math?math=p"> w modelu <img src="https://render.githubusercontent.com/render/math?math=G(n,p)"> oczekiwana liczba wierzchołków należących do rozwiązania równa się 1, 2, 3. 

**Przypadek graniczny:** Jeżeli <img src="https://render.githubusercontent.com/render/math?math=p=1.0"> wówczas w modelu <img src="https://render.githubusercontent.com/render/math?math=G(n,p)"> losowany jest graf pełny <img src="https://render.githubusercontent.com/render/math?math=K_n">. Dla grafu <img src="https://render.githubusercontent.com/render/math?math=K_n"> optymalnym rozwiązaniem problemu <img src="https://render.githubusercontent.com/render/math?math=VC^{(2)}"> jest wybór jednego (dowolnego) z jego wierzchołków. 

**Pozostałe przypadki:** Wykres średniej wielkość zbioru pokrywającego graf dla założonych prawdopodobieństw <img src="https://render.githubusercontent.com/render/math?math=p=0.25,0.50,0.75"> został umieszczony w dziale **Wykresy średniej wielkości dobrego zbioru (takiego, który pokrywa graf)**

#### Wykresy opisujące złożoność

Wykresy te opisują stosunek czasu wykonania (w sekundach) **Pełnego przeglądu grafu** dla <img src="https://render.githubusercontent.com/render/math?math=G_n"> do czasu wykonania (w sekundach) **Pełnego przeglądu grafu** <img src="https://render.githubusercontent.com/render/math?math=G_\frac{n}{2}$ $f(\frac{t(n)}{t(\frac{n}{2})})">, gdzie <img src="https://render.githubusercontent.com/render/math?math=n"> to liczba wierzchołków w grafie, dla każdego z założonych prawdopodobieństw <img src="https://render.githubusercontent.com/render/math?math=p=0.25,0.50,0.75">:

#### Wykres dla p = 0.25

![image](https://user-images.githubusercontent.com/72743103/126076515-07ecbdce-f817-4ffa-8f6a-5265465b3fbe.png)

#### Wykres dla p = 0.50 

![image](https://user-images.githubusercontent.com/72743103/126076490-e1a68b80-1928-4d3d-b65b-85d190f85bcd.png)

#### Wykres dla p = 0.75

![image](https://user-images.githubusercontent.com/72743103/126076496-c144e7f8-a725-479a-9505-818494bc3500.png)

Przebieg tych wykresów wskazuje na ewidentną złożoność czasową **wykładniczą, bądź wyższą**.
### Lasy i drzewa 
Legenda do ilustracji znajduje się w dziale **Ilustracja Problemu**.
#### Ścieżki
Jeden wierzchołek przy ścieżce bez rozgałęzień pokrywa do 5 wierzchołków (licząc razem ze sobą).

*Pokrycie* <img src="https://render.githubusercontent.com/render/math?math=P_5">  *przy pomocy jednego wierzchołka*

![image](https://user-images.githubusercontent.com/72743103/126076866-304dbdc3-888c-497a-9d3f-69da9e6eb720.png)

Do optymalnego pokrycia takiej ścieżki potrzeba <img src="https://render.githubusercontent.com/render/math?math=\lceil n/5 \rceil"> wierzchołków.


*Próba pokrycia* <img src="https://render.githubusercontent.com/render/math?math=P_6">  *przy pomocy jednego wierzchołka* 

![image](https://user-images.githubusercontent.com/72743103/126076952-dfd3d9fc-86a2-4411-ad85-c95501934738.png)

#### Drzewa i Lasy

Jest to rozszerzona wersja ścieżki <img src="https://render.githubusercontent.com/render/math?math=P_n"> - w tym wypadku występują rozgałęzienia. Aby optymalnie pokryć graf każdy wierzchołek nie będący w zbiorze rozwiązań musi być oddalony od wierzchołka pochodzącego z takiego zbioru o maksymalnie 2 krawędzie.

*Próba pokrycia* <img src="https://render.githubusercontent.com/render/math?math=T_{10}"> *przy pomocy jednego wierzchołka* 

![image](https://user-images.githubusercontent.com/72743103/126076982-e4e99cf4-93af-43f8-91a5-04c8286145cb.png)

#### Drzewa binarne

Dla zbalansowanych drzew (wysokość pomiędzy gałęziami różni się maksymalnie o 1) oby optymalnie pokryć graf wystarczy do zbioru rozwiązania dodać wszystkie wierzchołki z co 5 poziomu wysokości( 2 pierwsze poziomy pokrywa 1 aktualny poziom rozwiązujący, następne 2 następny poziom rozwiązujący), najlepiej rozpoczynając o 2 poziomu (korzeń ma poziom 0). Należy również wziąć pod uwagę, że ostatni poziom należący do rozwiązania nie może być oddalony o więcej niż 2 poziomy od ostatniego poziomu wysokości drzewa.


*Pokrycie* <img src="https://render.githubusercontent.com/render/math?math=BT_{31}"> *przy pomocy jednego poziomu wierzchołków* 

![image](https://user-images.githubusercontent.com/72743103/126077056-be41d301-85f7-4265-b29a-054ef5ebd7e4.png)

Dla drzew binarnych niezbalansowanych ze względu na "luki" należy skok między poziomami rozwiązującymi zmienić na 3 oraz zaczynać tylko i wyłącznie od poziomu korzenia.

*Pokrycie niekompletnego* <img src="https://render.githubusercontent.com/render/math?math=BT_{17}"> *przy pomocy dwóch poziomów wierzchołków* 

![image](https://user-images.githubusercontent.com/72743103/126077097-7faed96a-5e94-4551-8974-979c3da0d3cd.png)


### Cykle 

Grafy <img src="https://render.githubusercontent.com/render/math?math=C_n"> (o parzystej i nieparzystej długości) są optymalnie pokryte po przez <img src="https://render.githubusercontent.com/render/math?math=\lceil n/5 \rceil">  wierzchołków. Dowolna para takiego cyklu go pokrywa, pod warunkiem, że między wierzchołkami jest odległość  <img src="https://render.githubusercontent.com/render/math?math=< n "> <img src="https://render.githubusercontent.com/render/math?math=mod"> <img src="https://render.githubusercontent.com/render/math?math=5">;<img src="https://render.githubusercontent.com/render/math?math=5 >"> dla <img src="https://render.githubusercontent.com/render/math?math=n \mod 5 \ne 0">. Dla <img src="https://render.githubusercontent.com/render/math?math=n \mod 5 = 0"> odległość zawsze wynosi 5.  

*Pokrycie* <img src="https://render.githubusercontent.com/render/math?math=C_7"> *przy pomocy dwóch wierzchołków*

![image](https://user-images.githubusercontent.com/72743103/126077800-3e0ec807-8689-40b4-bfcc-0180bf14e1c0.png)

## Wnioski

Problem <img src="https://render.githubusercontent.com/render/math?math=VC^{(k)}">   gdzie <img src="https://render.githubusercontent.com/render/math?math=k \ge 3"> jest dalszym rozwinięciem problemu <img src="https://render.githubusercontent.com/render/math?math=VC^{(2)}">. Algorytmy Weryfikacji Pokrycia Grafu przez rozwiązanie, Zachłanny, Pełenego Przeglądu Grafu oraz Przybliżony dla wyższych problemów <img src="https://render.githubusercontent.com/render/math?math=VC^{(k)}"> mają <img src="https://render.githubusercontent.com/render/math?math=n^{k-2}"> razy większą złożoność (w Algorytmie Weryfikacji pojawia się dodatkowych <img src="https://render.githubusercontent.com/render/math?math=k-2"> pętli). 

Najlepsze rozwiązanie za każdym razem zwróci tylko algorytm Pełnego Przeglądu Grafu. Algorytm zachłanny w przypadku, gdy istnieje kilka wierzchołków, które pokrywają taką samą liczbę niepokrytych wierzchołków mogą wybrać taki wierzchołek, który spowoduje w przyszłości rozdzielenie niepokrytych wierzchołków na osobne podgrafy, a w konsekwencji użycia większej ilości wierzchołków, niż posiadałoby najlepsze rozwiązanie. Rozwiązanie przybliżone ma natomiast niewielką szansę na zwrócenie najlepszego rozwiązania, za to jednak otrzymujemy rozwiązanie dobre w dużo krótszym czasie.


### Literatura

  * https://www.youtube.com/watch?v=ZZxj9hqldng *Vertex cover Problem with example*
  * https://www.youtube.com/watch?v=m_dOtat56vY *Vertex Cover - Georgia Tech - Computability, Complexity, Theory: Algorithms*
  * https://www.youtube.com/watch?v=_8wrCTLwC7E *Vertex Cover Solution - Intro to Theoretical Computer Science*

----
## Ilustracja Problemu 

### Legenda 

**Wierzchołki**

| Oznaczenie | Znaczenie                                                                                           |
|------------|-----------------------------------------------------------------------------------------------------|
| zielony    | Wierzchołek należący do grupy odpowiedzi                                                            |
| czarny     | Zwykły wierzchołek nie należący  zarówno do grupy odpowiedzi jak i  grupy niepokrytych wierzchołków |
| czerwony   | Niepokryty wierzchołek                                                                              |

**Krawędzie**
| Oznaczenie | Znaczenie                                                                |
|------------|--------------------------------------------------------------------------|
| zielony    | Krawędź łącząca  bezpośrednio zielony  wierzchołek z pierwszym  sąsiadem |
| żółty      | Krawędź łącząca pośrednio  zielony wierzchołek z drugim sąsiadem         |
| czarny     | Zwykła krawędź (nie pokrywa grafu)                                       |


### Prawidłowe Pokrycie 

![image](https://user-images.githubusercontent.com/72743103/126077983-cf778c39-c9d7-4de3-95cb-ebfc695c8fbb.png)

**Macierz**
```
[0, 1, 1, 1, 1, 0, 0, 1],
[1, 0, 1, 1, 1, 0, 0, 0],
[1, 1, 0, 0, 1, 1, 1, 1],
[1, 1, 0, 0, 1, 1, 1, 1],
[1, 1, 1, 1, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 0, 0, 0],
[0, 0, 1, 1, 0, 0, 0, 1],
[1, 0, 1, 1, 0, 0, 1, 0]
```

**Wierzchołki należące do zbioru rozwiązania**

```
[2,6]
```

### Niepowodzenie

![image](https://user-images.githubusercontent.com/72743103/126078024-b9bbe47d-7183-418b-8df1-e7eb6e49bdc3.png)

**Macierz**
```
[0, 0, 0, 0, 0, 0, 1, 1],
[0, 0, 0, 0, 1, 0, 1, 0],
[0, 0, 0, 0, 1, 0, 0, 1],
[0, 0, 0, 0, 1, 1, 0, 1],
[0, 1, 1, 1, 0, 0, 1, 1],
[0, 0, 0, 1, 0, 0, 0, 0],
[1, 1, 0, 0, 1, 0, 0, 1],
[1, 0, 1, 1, 1, 0, 1, 0]
```

**Wierzchołki należące do zbioru rozwiązania**

```
[0,1]
```



## Bez Wizualizacji

### Generowanie grafów

**Źródło:** https://pw20we.cs.put.poznan.pl/doku.php?id=ok:modele_grafow_losowych
```
def gnp(n, p):
    "Model G(n,p)"
    a = [[0 for j in range(n)] for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if (random.random() <= p):
                a[i][j] = a[j][i] = 1
    return a
```


### Weryfikacja poprawności rozwiązania

| Dane         | Opis                                                                       |
|--------------|----------------------------------------------------------------------------|
| vertexAmount | liczba wierzchołków w grafie                                               |
| matrix       | macierz sąsiedztwa                                                         |
| answers      | rozwiązanie poddawane weryfikacji                                          |
| check_table  | tablica informująca czy wierzchołek(indeks)  został pokryty(1), czy nie(0) |



```
def graph_cover_test(vertexAmount,matrix,answers):
    check_table=[]
    for i in range(vertexAmount):
        check_table.append(0)
    for answer in answers:
        check_table[answer] = 1
        for i in range(vertexAmount):
            if matrix[answer][i] == 1:
                check_table[i]=1
                for j in range(vertexAmount):
                    if matrix[i][j] == 1:
                        check_table[j]=1
    if 0 in check_table:
        return False
    else:
        return True
```


#### Średnia złożoność:

<img src="https://render.githubusercontent.com/render/math?math=\mathcal{O}(k \cdot n^2)"> 

#### Złożoność pesymistyczna:

<img src="https://render.githubusercontent.com/render/math?math=\mathcal{O}(n^3)">


gdyż w pesymistycznym przypadku <img src="https://render.githubusercontent.com/render/math?math=k"> wynosi <img src="https://render.githubusercontent.com/render/math?math=n">



<img src="https://render.githubusercontent.com/render/math?math=k"> - *liczba wierzchołków w rozwiązaniu*

<img src="https://render.githubusercontent.com/render/math?math=n"> - *liczba wszystkich wierzchołków*



### Algorytm zachłanny

Algorytm:
  - oblicza ile wierzchołków może pokryć każdy z wierzchołków
  - wybiera najlepszy z nich i dodaje do rozwiązania
  - wykonywany jest test pokrycia grafu - w przypadku powodzenia algorytm kończy pracę, w przeciwnym przypadku usuwa krawędzie wybranego wierzchołka i ponownie wykonuje wszystkie kroki algorytmu

#### Zmodyfikowany algorytm testu pokrycia
Do tego algorytmu musimy zmodyfikować algorytm testu pokrycia, tak, aby zwracał oprócz odpowiedzi również liczbę niepokrytych wierzchołków

| Dane              | Opis                                                                       |
|-------------------|----------------------------------------------------------------------------|
| vertexAmount      | liczba wierzchołków w grafie                                               |
| matrix            | macierz sąsiedztwa                                                         |
| answers           | rozwiązanie poddawane weryfikacji                                          |
| check_table       | tablica informująca czy wierzchołek(indeks)  został pokryty(1), czy nie(0) |
| not_covered       | tablica z niepokrytymi wierzchołkami                                       |
| correctly_covered | zmienna boolowska, informująca czy "answers" pokrywa graf                  |

```
def graph_cover_test_greedy(vertexAmount,matrix,answers):
    check_table=[]
    for i in range(vertexAmount):
        check_table.append(0)
    for answer in answers:
        check_table[answer] = 1
        for i in range(vertexAmount):
            if matrix[answer][i] == 1:
                check_table[i]=1
                for j in range(vertexAmount):
                    if j!=answer:
                        if matrix[i][j] == 1:
                            check_table[j]=1
    not_covered = []
    for e in range(vertexAmount):
        if check_table[e] != 1:
            not_covered.append(e)
    if len(not_covered) > 0:
        corectly_covered = False
    else:
        corectly_covered = True

    return corectly_covered,not_covered
```

#### Pomocniczy algorytm zliczający moc pokrycia każdego z wierzchołków

| Dane         | Opis                                                                                                                              |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------|
| matrix       | macierz sąsiedztwa                                                                                                                |
| vertexAmount | liczba wierzchołków w grafie                                                                                                      |
| covered      | tablica informująca czy wierzchołek(indeks)  został pokryty(1), czy nie(0)                                                        |
| vertices     | słownik numerów wierzchołków i ilością wierzchołków, które mogą pokryć                                                            |
| check_table  | tablica informująca czy w danym przejściu pętli wierzchołek(indeks)  został policzony jako możliwy do pokrycia(1), czy też nie(0) |

```
def Connection_counter(matrix,vertexAmount,covered):
    vertices={}
    for vertex in range(vertexAmount):
        vertices[vertex] = 0

    for i in range(vertexAmount):
        check_table = [0 for _ in range(vertexAmount)]
        check_table[i] = 1
        for j in range(vertexAmount):
            if matrix[i][j]==1:
                if check_table[j] == 0:
                    if covered[j] == 0:
                        vertices[i]+=1
                    check_table[j] = 1
                for m in range(vertexAmount):
                    if matrix[j][m] == 1:
                        if check_table[m] == 0:
                            if covered[m] == 0:
                                vertices[i]+=1
                            check_table[m] = 1

    return vertices
```


##### Złożoność:

<img src="https://render.githubusercontent.com/render/math?math=\mathcal{O}(n^3)"> 

<img src="https://render.githubusercontent.com/render/math?math=n"> - *liczba wszystkich wierzchołków*

#### Właściwy algorytm zachłanny

| Dane             | Opis                                                                                                           |
|------------------|----------------------------------------------------------------------------------------------------------------|
| matrix           | macierz sąsiedztwa                                                                                             |
| vertexAmount     | liczba wierzchołków w grafie                                                                                   |
| matrix_copy      | kopia właściwej macierzy, na której są  przeprowadzane działania usuwania połączeń                             |
| covered          | tablica informująca czy wierzchołek(indeks)  został pokryty(1), czy nie(0)                                     |
| vertices         | słownik numerów wierzchołków i ilością wierzchołków, które mogą pokryć                                         |
| solution         | tablica wierzchołków, które pokrywają cały graf                                                                |
| test_result      | zmienna boolowska, informuje czy "solution" pokryło graf  i czy można zakończyć algorytm(True), czy nie(False) |
| ordered_vertices | posortowane wierzchołki - od najwięcej pokrywających wierzchołków do najmniej                                  |
| best_one         | wierzchołek, który w danej sytuacji pokrywa najwięcej niepokrytych wierzchołków                                |
| not_covered      | tablica zawierająca wierzchołki, których "solution" nie pokrywa                                                |

```
import copy

def Greedy_graph_cover_test(matrix,vertexAmount):
    matrix_copy=copy.deepcopy(matrix)

    covered = [0 for _ in range(vertexAmount)]

    vertices = Connection_counter(matrix,vertexAmount,covered)

    solution = []
    test_result = False

    while not test_result:
        ordered_vertices = sorted(vertices, key=vertices.get, reverse=True)
        best_one = ordered_vertices[0]
        while vertices[best_one] == 0 and covered[best_one] == 1:
            vertices.pop(best_one)
            best_one = ordered_vertices[0]
        solution.append(best_one)

        for i in range(vertexAmount):
            if matrix_copy[best_one][i]==1:
                matrix_copy[best_one][i] = 0
                matrix_copy[i][best_one] = 0
                for j in range(vertexAmount):
                    if matrix_copy[i][j] == 1:
                        matrix_copy[i][j] = 0
                        matrix_copy[j][i] = 0

        test_result,not_covered = graph_cover_test_greedy(vertexAmount,matrix,solution)

        covered = [1 for _ in range(vertexAmount)]

        for vertex in not_covered:
            covered[vertex] = 0

        vertices = Connection_counter(matrix_copy, vertexAmount,covered)

    return solution
```

##### Średnia złożoność:

<img src="https://render.githubusercontent.com/render/math?math=\mathcal{O}(n^3)">  → zazwyczaj pętla while wykona się zaledwie parę razy, a najwięcej czasu zabiera **Connection_counter**

#### Złożoność pesymistyczna: 
<img src="https://render.githubusercontent.com/render/math?math=\mathcal{O}(n^4)">  →  pętla while wykona się <img src="https://render.githubusercontent.com/render/math?math=n">  razy, a razem z nią **Connection_counter**

<img src="https://render.githubusercontent.com/render/math?math=n"> - *liczba wszystkich wierzchołków*


### Algorytm przeszukujący wszystkie podzbiory (Brute Force)
Algorytm przeszukuje wszystkie podzbiory grafu, wyświetla podzbiory i wynik testu na pokrycie oraz zwraca wszystkie optymalne rozwiązania

#### Algorytm tworzący zbiór potęgowy grafu(Opcjonalnie)
Algorytm ten można spokojnie zastąpić funkcją **combinations(table_with_elements,number_of_element_to_choose)** z bibilotek **itertools**

| Dane         | Opis                                  |
|--------------|---------------------------------------|
| tab          | lista z wierzchołkami                 |
| vertexAmount | liczba wierzchołków w grafie          |
| results      | lista ze wszystkimi podzbiorami grafu |

```
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
        tmp = []                       #zerujemy tablice wynikowa

    return results
```

##### Złożoność:

<img src="https://render.githubusercontent.com/render/math?math=\mathcal{O}(2^n)">

<img src="https://render.githubusercontent.com/render/math?math=n"> - *liczba wszystkich wierzchołków*

#### Algorytm pełnego przeglądu grafu w celu poszukiwania rozwiązań

| Dane          | Opis                                                                |
|---------------|---------------------------------------------------------------------|
| vertexAmount  | liczba wierzchołków w grafie                                        |
| matrix        | macierz sąsiedztwa                                                  |
| vertices_list | lista z wierzchołkami                                               |
| sets          | lista z wszystkimi podzbiorami grafu                                |
| test_results  | lista z odpowiedziami, czy zbiór  pokrywa graf(True) lub nie(False) |
| test_result   | pojedyncza odpowiedź, czy zbiór  pokrywa graf(True) lub nie(False)  |

```
def full_graph_cover_test(vertexAmount,matrix):
    vertices_list = []
    for e in range(vertexAmount):
        vertices_list.append(e)
    sets = power_set(vertices_list, vertexAmount)

    test_results = []
    best_solutions = []
    shortest_length = vertexAmount

    for set in sets:
        test_result = graph_cover_test(vertexAmount, matrix, set)
        if test_result == True:
            if len(set)<=shortest_length:
                best_solutions.append(set)
                shortest_length=len(set)
        test_results.append(test_result)


    print("Sets and results:")
    print(sets)
    print(test_results)

    return  best_solutions
```

##### Złożoność:

<img src="https://render.githubusercontent.com/render/math?math=(2^n \cdot n^3)"> → każdy podzbiór musi być sprawdzony

<img src="https://render.githubusercontent.com/render/math?math=n"> - *liczba wszystkich wierzchołków*

#### Sposób z użyciem mniejszej ilości pamięci (optymalizacja związana z podzbiorami) - użycie biblioteki itertools

```
import itertools

def full_graph_cover_test2(vertexAmount,matrix):
    vertices_list = []
    for e in range(vertexAmount):
        vertices_list.append(e)

    test_results = []
    best_solutions = []
    shortest_length = vertexAmount

    for i in range(vertexAmount):
        sets = itertools.combinations(vertices_list,i)
        for set in sets:
            test_result = graph_cover_test(vertexAmount, matrix, set)
            if test_result == True:
                if len(set) <= shortest_length:
                    best_solutions.append(set)
                    shortest_length = len(set)
            test_results.append(test_result)

    print("Results:")
    #print(power_set(vertices_list,vertexAmount)) #Opcjonalnie do wglądu w podzbiory
    print(test_results)

    return  best_solutions
```


#### Wykresy czasów wykonania

Wszystkie wykresy zostały wykonane dla próbki danych liczącej **100** różnych grafów dla każdej liczby wierzchołków N.

##### Czas wykonania (w sekundach) pełnego przeglądu grafu o liczbie wierzchołków równej N dla prawdopodobieństwa stworzenia krawędzi p = 0.25:

![image](https://user-images.githubusercontent.com/72743103/126084499-ca5dda15-ff3b-49f7-be15-b06ee81276d6.png)

##### Czas wykonania (w sekundach) pełnego przeglądu grafu o liczbie wierzchołków równej N dla prawdopodobieństwa stworzenia krawędzi p = 0.5:

![image](https://user-images.githubusercontent.com/72743103/126084511-5987941a-3c56-4f1b-a58c-240735d2bb67.png)

##### Czas wykonania (w sekundach) pełnego przeglądu grafu o liczbie wierzchołków równej N dla prawdopodobieństwa stworzenia krawędzi p = 0.75:

![image](https://user-images.githubusercontent.com/72743103/126084527-7c62b32a-675b-48b5-afba-ac665c5e9561.png)

#### Wykresy średniej wielkości dobrego zbioru (takiego, który pokrywa graf)

##### Średnia wielkość dobrego zbioru grafu o liczbie wierzchołków równej N dla prawdopodobieństwa stworzenia krawędzi p = 0.25:

![image](https://user-images.githubusercontent.com/72743103/126084539-3b6a1b64-cf3b-4049-aae6-6f05b5d7fa58.png)

##### Średnia wielkość dobrego zbioru grafu o liczbie wierzchołków równej N dla prawdopodobieństwa stworzenia krawędzi p = 0.5:

![image](https://user-images.githubusercontent.com/72743103/126084558-427fcca0-d24c-45f3-aafa-b2c8c55eb24a.png)

##### Średnia wielkość dobrego zbioru grafu o liczbie wierzchołków równej N dla prawdopodobieństwa stworzenia krawędzi p = 0.75:

![image](https://user-images.githubusercontent.com/72743103/126084563-78a4a210-4a96-49a8-911c-eef46fbae71c.png)

##### Zbiórczy wykres średnich wielkości dobrego zbioru dla wszystkich wyżej wymienionych prawdopodobieństw p:

![image](https://user-images.githubusercontent.com/72743103/126084575-abe602ed-b0ba-4ba9-9a41-772af29c7537.png)

### Algorytm prezentujący rozwiązanie przybliżone
Na podstawie pomiarów średniego zbioru pokrywającego graf przeprowadzonych na **Algorytmie pełnego przeglądu podzbiorów** i regresji przeprowadzonych na uzyskanych wynikach otrzymaliśmy wzór na średnią wielkość pokrywającego podzbioru. Następnie przegląd podzbiorów zaczynamy od podzbiorów o wyliczonej wcześniej wartości. Kończymy po odnalezieniu pierwszego rozwiązania.

**To rozwiązanie zwraca optymalne, choć nie zawsze najlepsze rozwiązanie**

| Dane          | Opis                                                                  |
|---------------|-----------------------------------------------------------------------|
| matrix        | macierz sąsiedztwa                                                    |
| vertexAmount  | liczba wierzchołków w grafie                                          |
| p             | prawdopodobieństwo z jakim tworzono krawędzie w grafie                |
| vertices      | wszystkie wierzchołki podane w jednej liście                          |
| minimalLength | zaokrąglona w górę wyliczona średnia wielkość pokrywającego podzbioru |
| substets      | podzbiory grafu o podanej wielkości                                   |

```
import itertools
import math

def Aproximated_graph_cover_test(matrix, vertexAmount, p):
    vertices = []
    for vertex in range(vertexAmount):
        vertices.append(vertex)
    if p == 0.25:
        minimalLength = math.ceil(0.431698449296429 * vertexAmount + 1.28057012910952)
    elif p == 0.5:
        minimalLength =  math.ceil(0.467252521696703 * vertexAmount + 0.490780704345053)
    elif p == 0.75:
        minimalLength =   math.ceil(0.476384874362637 * vertexAmount + 0.351959433901099)
    else:
        print("Wybrano nieprawidłowe p \n")
        exit(1)
    for amount in range(minimalLength,vertexAmount+1):
        subsets = itertools.combinations(vertices,amount)
        for subset in subsets:
            if (graph_cover_test(vertexAmount,matrix,subset) == True):
                return subset
```

#### Średnia złożoność:

<img src="https://render.githubusercontent.com/render/math?math=\mathcal{O}(n^3)">  → zazwyczaj algorytm przechodzi tylko kilka pętli

#### Złożoność pesymistyczna:


<img src="https://render.githubusercontent.com/render/math?math=\mathcal{O}(m \cdot n^3)"> → <img src="https://render.githubusercontent.com/render/math?math=\mathcal{O}(n^4)">

<img src="https://render.githubusercontent.com/render/math?math=m = 2^n - 2^{\lfloor w \rfloor}"> 

<img src="https://render.githubusercontent.com/render/math?math=w">  - *wyliczona średnia wartość dobrego podzbioru*

<img src="https://render.githubusercontent.com/render/math?math=n"> - *liczba wszystkich wierzchołków*

<img src="https://render.githubusercontent.com/render/math?math=m"> - *maksymalna liczba podzbiorów, które mogą sprawdzone w tym algorytmie*

## Wizualizacja z użyciem GraphViz
Aby móc uruchamiać poniższe algorytmy trzeba do projektu dodać bibliotekę **graphviz**
#### Instalacja GraphViz
  - Pobrać oprogramowanie GraphViz z https://graphviz.org/download/
  - Dodać ścieżkę do folderu "bin" oprogramowania GraphViz do zmiennej środowiskowej *Path*.
  
Przykład:
     *C:\Program Files (x86)\Graphviz2.38\bin*
     
Polecam korzystać z wersji 2.38, dla wersji nowszych/niekompletnych wizualizacja może nie zadziałać.
    
Link do bezpośredniego pobrania (pochodzi ze skryptu używanego przy pobieraniu za pomocą ''winget'' ) : https://graphviz.gitlab.io/_pages/Download/windows/graphviz-2.38.msi 
     
**Uwaga!** Gdyby przy kompilacji kodu nastąpił błąd:

`graphviz.backend.executablenotfound: failed to execute ['circo', '-tpng', '-o', 'graph.gv'], make sure the graphviz executables are on your systems' path`
     
należy do zmiennej środowiskowej *Path* dodać ścieżkę bezpośrednio do pliku "circo.exe" oprogramowania Graphviz.

Przykład:
     *C:\Program Files (x86)\Graphviz2.38\bin\circo.exe*


### Generowanie grafów 

https://pw20we.cs.put.poznan.pl/doku.php?id=ok:modele_grafow_losowych

```
def gnp(n, p):
    "Model G(n,p)"
    a = [[0 for j in range(n)] for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if (random.random() <= p):
                a[i][j] = a[j][i] = 1
    return a
```


### Weryfikacja poprawności rozwiązania

| Dane              | Opis                                                                       |
|-------------------|----------------------------------------------------------------------------|
| vertexAmount      | liczba wierzchołków w grafie                                               |
| matrix            | macierz sąsiedztwa                                                         |
| answers           | rozwiązanie poddawane weryfikacji                                          |
| matrix_to_graphViz | zmodyfikowana macierz sąsiadów, która przyda się przy wizualizacji testu |
| check_table       | tablica informująca czy wierzchołek(indeks) został pokryty(1), czy nie(0) |
| correctly_covered | zmienna boolowska, informująca czy "answers" pokrywa graf                  |

```
from copy import deepcopy

def graph_cover_test_graphViz(vertexAmount,matrix,answers):
    matrix_to_graphViz=deepcopy(matrix)
    check_table=[]
    for i in range(vertexAmount):
        check_table.append(0)
    for answer in answers:
        check_table[answer] = 1
        for i in range(vertexAmount):
            if matrix[answer][i] == 1:
                check_table[i]=1
                matrix_to_graphViz[answer][i]= 2        #2 - krawędź z pierwszym sąsiadem
                matrix_to_graphViz[i][answer]= 2
                for j in range(vertexAmount):
                    if matrix[i][j] == 1:
                        check_table[j]=1
                        if matrix_to_graphViz[i][j]!=2:
                            matrix_to_graphViz[i][j] = 3     # 3 -krawędź z drugim sąsiadem
                            matrix_to_graphViz[j][i] = 3
    not_covered = []
    for e in range(vertexAmount):
        if check_table[e] != 1:
            not_covered.append(e)
    if len(not_covered) > 0:
        print("Wrong covered: " + str(not_covered))
        correctly_covered = False
    else:
        print("Correctly covered.")
        correctly_covered = True
    return correctly_covered,not_covered,matrix_to_graphViz
```

#### Prezentacja testu z użyciem oprogramowania GraphViz

| Dane               | Opis                                                                     |
|--------------------|--------------------------------------------------------------------------|
| vertexAmount       | liczba wierzchołków w grafie                                             |
| matrix_to_graphViz | zmodyfikowana macierz sąsiadów, która przyda się przy wizualizacji testu |
| answers            | rozwiązanie poddawane weryfikacji                                        |
| not_covered        | lista niepokrytych wierzchołków                                          |
| file_number        | numer dopisany do "Graph" w nazwie plików wyjściowych                    |
| display            | graf                                                                     |
| answer             | zmienna boolowska informująca czy wierzchołek był w rozwiązaniu          |
| uncovered          | zmienna boolowska informująca czy wierzchołek nie został przykryty       |


```
import graphviz


def display_cover_test_in_graphViz(vertexAmount,matrix_to_graphViz,answers,not_covered,filenumber):
    display = graphviz.Graph(engine='circo',filename="Graph"+str(filenumber)) #inicjalizacja i nadanie nazwy plikom
    for vertex in range(vertexAmount):
        answer = False
        uncovered = False

        if vertex in not_covered:
            uncovered = True
        if vertex in answers:
            answer = True
        if uncovered:
            display.node(str(vertex), str(vertex), color='red')    #dodanie wierzchołka niepokrytego do grafu
        elif answer:
            display.node(str(vertex), str(vertex), color='green')     #dodanie wierzchołka z rozwiązania do grafu
        else:
            display.node(str(vertex), str(vertex))    #dodanie innych wierzchołków do grafu

    for i in range(vertexAmount - 1):
        for j in range(i, vertexAmount):
            if matrix_to_graphViz[i][j] == 1:
                display.edge(str(i), str(j), constraint='false')     #dodanie zwykłej krawędzi do grafu
            elif matrix_to_graphViz[i][j] == 2:
                display.edge(str(i), str(j), constraint='false', color='green')     #dodanie krawędzi połączenia z pierwszym sąsiadem wierzchołka z rozwiązania do grafu
            elif matrix_to_graphViz[i][j] == 3:
                display.edge(str(i), str(j), constraint='false', color='yellow')     #dodanie krawędzi połączenia z drugim sąsiadem wierzchołka z rozwiązania do grafu
    # print(display.source)             # kod w GraphViz
    display.render( format='png')              # generuje plik z kodem do Graphviz i plik png z wizualizacją testu
    #display.render(view='true', format='png')   # to co wyżej + otwiera plik png do podgladu
```



### Algorytm zachłanny

#### Pomocniczy algorytm zliczający moc pokrycia każdego z wierzchołków

| Dane         | Opis                                                                                                                              |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------|
| matrix       | macierz sąsiedztwa                                                                                                                |
| vertexAmount | liczba wierzchołków w grafie                                                                                                      |
| covered      | tablica informująca czy wierzchołek(indeks)  został pokryty(1), czy nie(0)                                                        |
| vertices     | słownik numerów wierzchołków i ilością wierzchołków, które mogą pokryć                                                            |
| check_table  | tablica informująca czy w danym przejściu pętli wierzchołek(indeks)  został policzony jako możliwy do pokrycia(1), czy też nie(0) |

```
def Connection_counter(matrix,vertexAmount,covered):
    vertices={}
    for vertex in range(vertexAmount):
        vertices[vertex] = 0

    for i in range(vertexAmount):
        check_table = [0 for _ in range(vertexAmount)]
        check_table[i] = 1
        for j in range(vertexAmount):
            if matrix[i][j]==1:
                if check_table[j] == 0:
                    if covered[j] == 0:
                        vertices[i]+=1
                    check_table[j] = 1
                for m in range(vertexAmount):
                    if matrix[j][m] == 1:
                        if check_table[m] == 0:
                            if covered[m] == 0:
                                vertices[i]+=1
                            check_table[m] = 1

    return vertices
```


#### Właściwy algorytm zachłanny

| Dane             | Opis                                                                                                           |
|------------------|----------------------------------------------------------------------------------------------------------------|
| matrix           | macierz sąsiedztwa                                                                                             |
| vertexAmount     | liczba wierzchołków w grafie                                                                                   |
| matrix_copy      | kopia właściwej macierzy, na której są  przeprowadzane działania usuwania połączeń                             |
| covered          | tablica informująca czy wierzchołek(indeks)  został pokryty(1), czy nie(0)                                     |
| vertices         | słownik numerów wierzchołków i ilością wierzchołków, które mogą pokryć                                         |
| solution         | tablica wierzchołków, które pokrywają cały graf                                                                |
| test_result      | zmienna boolowska, informuje czy "solution" pokryło graf  i czy można zakończyć algorytm(True), czy nie(False) |
| ordered_vertices | posortowane wierzchołki - od najwięcej pokrywających wierzchołków do najmniej                                  |
| best_one         | wierzchołek, który w danej sytuacji pokrywa najwięcej niepokrytych wierzchołków                                |
| not_covered      | tablica zawierająca wierzchołki, których "solution" nie pokrywa                                                |
| matrix_to_graphViz | zmodyfikowana macierz, użyteczna w wizualizacji rozwiązania |

```
import copy


def Greedy_graph_cover_test(matrix,vertexAmount):
    matrix_copy=copy.deepcopy(matrix)

    covered = [0 for _ in range(vertexAmount)]

    vertices = Connection_counter(matrix,vertexAmount,covered)

    solution = []
    test_result = False

    while not test_result:
        ordered_vertices = sorted(vertices, key=vertices.get, reverse=True)
        best_one = ordered_vertices[0]
        while vertices[best_one] == 0 and covered[best_one] == 1:
            vertices.pop(best_one)
            best_one = ordered_vertices[0]
        solution.append(best_one)

        for i in range(vertexAmount):
            if matrix_copy[best_one][i]==1:
                matrix_copy[best_one][i] = 0
                matrix_copy[i][best_one] = 0
                for j in range(vertexAmount):
                    if matrix_copy[i][j] == 1:
                        matrix_copy[i][j] = 0
                        matrix_copy[j][i] = 0

        test_result,not_covered,matrix_to_graphViz = graph_cover_test_graphViz(vertexAmount,matrix,solution)

        covered = [1 for _ in range(vertexAmount)]

        for vertex in not_covered:
            covered[vertex] = 0

        vertices = Connection_counter(matrix_copy, vertexAmount,covered)



    display_cover_test_in_graphViz(vertexAmount, matrix_to_graphViz, solution, not_covered, 1)
    return solution
```



### Algorytm przeszukujący wszystkie podzbiory (Brute Force)
#### Algorytm tworzący zbiór potęgowy grafu

| Dane         | Opis                                  |
|--------------|---------------------------------------|
| tab          | lista z wierzchołkami                 |
| vertexAmount | liczba wierzchołków w grafie          |
| results      | lista ze wszystkimi podzbiorami grafu |


```
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
        tmp = []                       #zerujemy tablice wynikowa

    return results
```


#### Algorytm pełnego przeglądu grafu w celu poszukiwania rozwiązań

| Dane          | Opis                                                                |
|---------------|---------------------------------------------------------------------|
| vertexAmount  | liczba wierzchołków w grafie                                        |
| matrix        | macierz sąsiedztwa                                                  |
| vertices_list | lista z wierzchołkami                                               |
| sets          | lista z wszystkimi podzbiorami grafu                                |
| test_results  | lista z odpowiedziami, czy zbiór  pokrywa graf(True) lub nie(False) |
| test_result   | pojedyncza odpowiedź, czy zbiór  pokrywa graf(True) lub nie(False)  |
| for_graphViz_to_display | lista zmodyfikowanych macierzy, użytecznych w wizualizacji rozwiązań |
| matrix_to_graphViz | zmodyfikowana macierz, użyteczna w wizualizacji rozwiązania |
| not_covered_list | lista z listami niepokrytych wierzchołków |
| not_covered | lista niepokrytych wierzchołków |

```
def full_graph_cover_test(vertexAmount,matrix):
    vertices_list = []
    for e in range(vertexAmount):
        vertices_list.append(e)
    sets = power_set(vertices_list, vertexAmount)

    test_results = []
    for_graphViz_to_display = []
    not_covered_list = []

    best_solutions = []
    shortest_length = vertexAmount

    for e in sets:
        test_result, not_covered, matrix_to_graphViz = graph_cover_test_graphViz(vertexAmount, matrix, e)
        if test_result == True:
            print("xd")
            if len(e) <= shortest_length:
                best_solutions.append(e)
                for_graphViz_to_display.append(matrix_to_graphViz)
                not_covered_list.append(not_covered)
                shortest_length = len(e)
        test_results.append(test_result)


    print("Sets and results:")
    print(sets)
    print(test_results)

    for e in range(len(best_solutions)):
        display_cover_test_in_graphViz(vertexAmount, for_graphViz_to_display[e], best_solutions[e], not_covered_list[e], e)

    return  best_solutions
```

#### Sposób z użyciem mniejszej ilości pamięci (optymalizacja związana z podzbiorami)

```
import itertools

def full_graph_cover_test2(vertexAmount,matrix):
    vertices_list = []
    for e in range(vertexAmount):
        vertices_list.append(e)


    test_results = []
    for_graphViz_to_display = []
    not_covered_list = []

    best_solutions = []
    shortest_length = vertexAmount

    for i in range(vertexAmount):
        sets = itertools.combinations(vertices_list,i)
        for e in sets:
            test_result, not_covered, matrix_to_graphViz = graph_cover_test_graphViz(vertexAmount, matrix, e)
            if test_result == True:
                if len(e) <= shortest_length:
                    best_solutions.append(e)
                    for_graphViz_to_display.append(matrix_to_graphViz)
                    not_covered_list.append(not_covered)
                    shortest_length = len(e)
            test_results.append(test_result)


    print("Results:")
    # print(power_set(vertices_list,vertexAmount)) #Opcjonalnie do wglądu w podzbiory
    print(test_results)

    for e in range(len(best_solutions)):
        display_cover_test_in_graphViz(vertexAmount, for_graphViz_to_display[e], best_solutions[e], not_covered_list[e], e)

    return best_solutions
```

### Algorytm prezentujący rozwiązanie przybliżone 

| Dane          | Opis                                                                  |
|---------------|-----------------------------------------------------------------------|
| matrix        | macierz sąsiedztwa                                                    |
| vertexAmount  | liczba wierzchołków w grafie                                          |
| p             | prawdopodobieństwo z jakim tworzono krawędzie w grafie                |
| vertices      | wszystkie wierzchołki podane w jednej liście                          |
| minimalLength | zaokrąglona w górę wyliczona średnia wielkość pokrywającego podzbioru |
| substets      | podzbiory grafu o podanej wielkości                                   |
| not_covered | lista niepokrytych wierzchołków |
| matrix_to_graphViz | zmodyfikowana macierz, użyteczna w wizualizacji rozwiązania |
| test_result | zmienna boolowska, czy dany zbiór pokrywa graf(True) lub nie(False) |

```
import itertools
import math

def Aproximated_graph_cover_test(matrix, vertexAmount, p):
    vertices = []
    for vertex in range(vertexAmount):
        vertices.append(vertex)
    if p == 0.25:
        minimal_length = math.ceil(0.431698449296429 * vertexAmount + 1.28057012910952)
    elif p == 0.5:
        minimal_length =  math.ceil(0.467252521696703 * vertexAmount + 0.490780704345053)
    elif p == 0.75:
        minimal_length =   math.ceil(0.476384874362637 * vertexAmount + 0.351959433901099)
    else:
        print("Wybrano nieprawidłowe p \n")
        exit(1)
    for amount in range(minimal_length,vertexAmount+1):
        subsets = itertools.combinations(vertices,amount)
        for subset in subsets:
            test_result,not_covered,matrix_to_graphViz = graph_cover_test(vertexAmount,matrix,subset)
            if ( test_result == True):
                display_cover_test_in_graphViz(vertexAmount, matrix_to_graphViz, subset, not_covered, 2)
                return subset
```

