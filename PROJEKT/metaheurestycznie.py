import test_pokryciav2.py
import itertools
import math


def Metaheuristic_graph_cover_test(matrix, vertexAmount, p):
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
            test_result,not_covered,matrix_to_graphViz = test_pokryciav2.graph_cover_test(vertexAmount,matrix,subset)
            if ( test_result == True):
                test_pokryciav2.display_cover_test_in_graphViz(vertexAmount, matrix_to_graphViz, subset, not_covered, 2)
                return subset