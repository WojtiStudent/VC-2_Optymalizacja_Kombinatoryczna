import test_pokryciav2
import wyczerpujacy_przeglad_grafu
import zachlanne

n=6
p=0.5
matrix = test_pokryciav2.gnp(n,p)
print("Matrix")
for e in matrix:
    print(e)

sol = zachlanne.Greedy_graph_cover_test(matrix,n)
print(sol)
#wyczerpujacy_przeglad_grafu.full_graph_cover_test2(n,matrix)

