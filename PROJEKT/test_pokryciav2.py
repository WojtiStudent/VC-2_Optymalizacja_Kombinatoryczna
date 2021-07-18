import random
import graphviz
from copy import deepcopy


# n = 7
# p = 0.4


def gnp(n, p):
    "Model G(n,p)"
    a = [[0 for j in range(n)] for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if (random.random() <= p):
                a[i][j] = a[j][i] = 1
    return a

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
        corectly_covered = False
    else:
        print("Correctly covered.")
        corectly_covered = True
    return corectly_covered,not_covered,matrix_to_graphViz


def display_cover_test_in_graphViz(vertexAmount, matrix_to_graphViz, answers, not_covered, filenumber):
    display = graphviz.Graph(engine='circo', filename="Graph" + str(filenumber))  # inicjalizacja i nadanie nazwy plikom
    for vertex in range(vertexAmount):
        answer = False
        uncovered = False

        if vertex in not_covered:
            uncovered = True
        if vertex in answers:
            answer = True
        if uncovered:
            display.node(str(vertex), str(vertex), color='red')  # dodanie wierzchołka niepokrytego do grafu
            print('l'+str(vertex)+" [ label = \""+str(vertex)+"\", color = red ];" )
        elif answer:
            display.node(str(vertex), str(vertex), color='green')  # dodanie wierzchołka z rozwiązania do grafu
            print('l' + str(vertex) + " [ label = \"" + str(vertex) + "\", color = green ];")
        else:
            display.node(str(vertex), str(vertex))  # dodanie innych wierzchołków do grafu
            print('l' + str(vertex) + " [ label = \"" + str(vertex) + "\"];")

    for i in range(vertexAmount - 1):
        for j in range(i, vertexAmount):
            if matrix_to_graphViz[i][j] == 1:
                display.edge(str(i), str(j), constraint='false')  # dodanie zwykłej krawędzi do grafu
                print("l"+str(i)+" -> l"+str(j)+";")
            elif matrix_to_graphViz[i][j] == 2:
                display.edge(str(i), str(j), constraint='false',
                             color='green')  # dodanie krawędzi połączenia z pierwszym sąsiadem wierzchołka z rozwiązania do grafu
                print("l" + str(i) + " -> l" + str(j) + " [color = green];")
            elif matrix_to_graphViz[i][j] == 3:
                display.edge(str(i), str(j), constraint='false',
                             color='yellow')  # dodanie krawędzi połączenia z drugim sąsiadem wierzchołka z rozwiązania do grafu
                print("l" + str(i) + " -> l" + str(j) + " [color = yellow];")
    #print(display.source)             # kod w GraphViz
    #display.render(format='png')  # generuje plik z kodem do Graphviz i plik png z wizualizacją testu
    #display.render(view='true', format='png')   # to co wyżej + otwiera plik png do podgladu
    display.render(view='true', format='svg')




#
# random_answer = [2,0]
#
# matrix = gnp(n, p)
#
# print("Matrix")
# for e in matrix:
#     print(e)
#
# not_covered,matrix_to_graphViz = graph_cover_test_graphViz(n,matrix,random_answer)
#
# print("GraphViz_matrix")
# for e in matrix_to_graphViz:
#     print(e)
#
# display_cover_test_in_graphViz(n,matrix_to_graphViz,random_answer,not_covered)

