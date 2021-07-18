import test_pokryciav2
import zbior_potegowy
import itertools

def full_graph_cover_test(vertexAmount,matrix):
    vertices_list = []
    for e in range(vertexAmount):
        vertices_list.append(e)
    sets = zbior_potegowy.power_set(vertices_list, vertexAmount)

    test_results = []
    best_solutions = []
    shortest_length = vertexAmount

    for set in sets:
        test_result = test_pokryciav2.graph_cover_test(vertexAmount, matrix, set)
        if test_result == True:
            if len(set)<=shortest_length:
                best_solutions.append(set)
                shortest_length=len(set)
        test_results.append(test_result)


    print("Sets and results:")
    print(sets)
    print(test_results)

    return  best_solutions


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
            test_result = test_pokryciav2.graph_cover_test(vertexAmount, matrix, set)
            if test_result == True:
                if len(set) <= shortest_length:
                    best_solutions.append(set)
                    shortest_length = len(set)
            test_results.append(test_result)

    print("Results:")
    #print(zbior_potegowy.power_set(vertices_list,vertexAmount)) #Opcjonalnie do wglądu w podzbiory
    print(test_results)

    return  best_solutions