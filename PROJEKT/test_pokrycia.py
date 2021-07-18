import random
import graphviz
from copy import deepcopy


n = 7
p = 0.4


def gnp(n, p):
    "Model G(n,p)"
    a = [[0 for j in range(n)] for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if (random.random() <= p):
                a[i][j] = a[j][i] = 1
    return a

def graph_cover_test(vertexAmount,matrix,answers):
    check_table=[]
    for i in range(vertexAmount):
        check_table.append(0)
    for answer in answers:
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
        print("Wrong covered: " + str(not_covered))
    else:
        print("Correctly covered.")
    return not_covered


random_answer = [2,0]

matrix = gnp(n, p)

print("Matrix")
for e in matrix:
    print(e)

not_covered = graph_cover_test(n,matrix,random_answer)


# dot -c
dot = graphviz.Graph(engine= 'circo')
for e in range(n):
    dot.node(str(e), str(e))

for i in range(n-1):
    for j in range(i,n):
        if matrix[i][j]==1:
            dot.edge(str(i),str(j),constraint = 'false')

#print(dot.source)
dot.render(view= 'true',format='png')


# 1. Strona Graphviz i pobranie dla Windowsa
# 2. terminal odpalamy jako admin i wklepujemy "dot -c"

# 3. A instalacja paczki do pythona to po prostu w pycharmie xd











