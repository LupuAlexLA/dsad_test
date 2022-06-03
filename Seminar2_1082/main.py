from matrices import sparse_matrix,diagonal_matrix

try:
    mat1 = sparse_matrix(10, 10, [0, 0, 9], [1, 2, 3], [100, 3.14, 1.71])
    print(mat1)
    print(mat1.n_lin, mat1.n_col)
    mat1.i = [1, 1, 1]
    print(mat1)
    print("Sume pe linii si coloane in mat1:",
          mat1.sum_l(), mat1.sum_c(), sep="\n")
    mat1.add(8, 18, 888)
    print(mat1, mat1.n_lin, mat1.n_col)
    mat2 = sparse_matrix(10, 19, [1, 1, 1, 8], [1, 2, 3, 18],
                         [100, 3.14, 1.71, 888])
    print("mat1==mat2", mat1 == mat2)
    mat2 = diagonal_matrix([234,8,76,-9.9])
    print(mat2)
    mat2.add(1234)
    print(mat2)

except Exception as ex:
    print(ex)
