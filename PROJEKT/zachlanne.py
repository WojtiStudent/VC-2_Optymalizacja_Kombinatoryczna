import test_pokryciav2
import itertools
import copy


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

        test_result,not_covered,matrix_to_graphViz = test_pokryciav2.graph_cover_test_graphViz(vertexAmount,matrix,solution)

        covered = [1 for _ in range(vertexAmount)]

        for vertex in not_covered:
            covered[vertex] = 0

        vertices = Connection_counter(matrix_copy, vertexAmount,covered)



    test_pokryciav2.display_cover_test_in_graphViz(vertexAmount, matrix_to_graphViz, solution, not_covered, 1)
    return solution