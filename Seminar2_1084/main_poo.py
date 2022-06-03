from matrice import sparse_matrix, diagonal_matrix

try:
    a = sparse_matrix(10, 10, [0, 4, 5], [1, 4, 4], [100, 999, 897])
    print(a)
    print("Indecsi linie pentru a:")
    print(a.i)
    print("Sume pe linii si coloane in matricea a:")
    print(a.l_sum(), a.c_sum(), sep="\n")
    a.add(10, 10, 3.14)
    print(a, a.n_lin, a.n_col)
    b = diagonal_matrix([100, 300, 1500, 10])
    print("Matricea b:", b, sep="\n")
    b.add(1550)
    print("Matricea b:", b, sep="\n")

except Exception as ex:
    print(ex)
