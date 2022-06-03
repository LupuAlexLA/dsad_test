from matrices import sparse_matrix,diagonal_matrix

try:
    mat1 = sparse_matrix(10, 10)
    print(mat1)
    print("Numar de linii pentru mat1:", mat1.n_lin)
    mat1.x = [[1, 1, 20]]
    mat1.add([0, 0, 200])
    mat1.add([0, 9, 1000])
    print(mat1)
    print("Sumele pe linii si coloane in mat1:")
    print(mat1.sum_l(), mat1.sum_c(), sep="\n")
    mat2 = sparse_matrix(10, 10)
    mat2.add([3, 4, 100])
    print("Test egalitate intre mat1 si mat2:", mat1 == mat2)
    mat3 = diagonal_matrix([10,20,30])
    print(mat3)
    mat3.add(999)
    print(mat3)
except Exception as ex:
    print(ex)
