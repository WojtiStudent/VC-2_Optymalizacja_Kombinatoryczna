import random


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
    if 0 in check_table:
        return False
    else:
        return True

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


# random_answer = [2,0]
#
# matrix = gnp(n, p)
#
# print("Matrix")
# for e in matrix:
#     print(e)
#
# result = graph_cover_test_graphViz(n,matrix,random_answer)
#

