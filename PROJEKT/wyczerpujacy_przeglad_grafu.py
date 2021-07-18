import test_pokryciav2
import zbior_potegowy
import itertools

def full_graph_cover_test(vertexAmount,matrix):
    vertices_list = []
    for e in range(vertexAmount):
        vertices_list.append(e)
    sets = zbior_potegowy.power_set(vertices_list, vertexAmount)

    test_results = []
    for_graphViz_to_display = []
    not_covered_list = []

    best_solutions = []
    shortest_length = vertexAmount

    for e in sets:
        test_result, not_covered, matrix_to_graphViz = test_pokryciav2.graph_cover_test_graphViz(vertexAmount, matrix, e)
        if test_result == True:
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
        test_pokryciav2.display_cover_test_in_graphViz(vertexAmount, for_graphViz_to_display[e], best_solutions[e], not_covered_list[e], e)

    return best_solutions

    # for e in range(pow(2, vertexAmount)):
    #     test_pokryciav2.display_cover_test_in_graphViz(vertexAmount, for_graphViz_to_display[e], sets[e], not_covered_list[e], e)

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
            test_result, not_covered, matrix_to_graphViz = test_pokryciav2.graph_cover_test_graphViz(vertexAmount, matrix, e)
            if test_result == True:
                if len(e) <= shortest_length:
                    best_solutions.append(e)
                    for_graphViz_to_display.append(matrix_to_graphViz)
                    not_covered_list.append(not_covered)
                    shortest_length = len(e)
            test_results.append(test_result)


    print("Results:")
    # print(zbior_potegowy.power_set(vertices_list,vertexAmount)) #Opcjonalnie do wglądu w podzbiory
    print(test_results)

    for e in range(len(best_solutions)):
        test_pokryciav2.display_cover_test_in_graphViz(vertexAmount, for_graphViz_to_display[e], best_solutions[e], not_covered_list[e], e)

    return best_solutions