import test_pokryciav2
import wyczerpujacy_przeglad_grafu
import zachlanne

n=7
p=0.25
#matrix = test_pokryciav2.gnp(n,p)

# jeden = 1
# dwa = 2
#
# matrix = []
# for i in range(n):
#     line = [0 for _ in range(n)]
#     matrix.append(line)
#
# for i in range(n):
#     for j in range(n):
#         if j == jeden:
#             matrix[i][j] = 1
#             matrix[j][i] = 1
#         elif j == dwa:
#             matrix[i][j] = 1
#             matrix[j][i] = 1
#     jeden+=2
#     dwa+=2

matrix = [[0,1,0,0,0,0,1],
          [1,0,1,0,0,0,0],
          [0,1,0,1,0,0,0],
          [0,0,1,0,1,0,0],
          [0,0,0,1,0,1,0],
          [0,0,0,0,1,0,1],
          [1,0,0,0,0,1,0]]


print("Matrix")
for e in matrix:
    print(e)

solution = [0,2]

corectly_covered,not_covered,matrix_to_graphViz = test_pokryciav2.graph_cover_test_graphViz(n,matrix,solution)

test_pokryciav2.display_cover_test_in_graphViz(n, matrix_to_graphViz, solution, not_covered, 1)

#solution = zachlanne.Greedy_graph_cover_test(matrix,n)
print(solution)

#test_pokryciav2.display_cover_test_in_graphViz(n, matrix_to_GraphViz, solution, not_covered, 1)

# wyczerpujacy_przeglad_grafu.full_graph_cover_test(n,matrix)

