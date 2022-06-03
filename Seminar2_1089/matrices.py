class sparse_matrix():

    def __init__(self, n_lin, n_col):
        self.__n_lin = n_lin
        self.__n_col = n_col
        self.__x = []

    def __str__(self):
        sir = str(self.__n_lin) + "," + str(self.__n_col) + ",["
        for p in self.__x:
            sir += "(" + str(p[0]) + "," + str(p[1]) + "," + str(p[2]) + ")"
        sir += "]"
        return sir

    @property
    def n_lin(self):
        return self.__n_lin

    @n_lin.setter
    def n_lin(self, n_lin_):
        self.__n_lin = n_lin_

    @property
    def n_col(self):
        return self.__n_col

    @n_col.setter
    def n_col(self, n_col_):
        self.__n_col = n_col_

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x_):
        for p in x_:
            if p[0] >= self.__n_lin or p[1] >= self.__n_col:
                raise Exception("Indice linie sau coloana invalid!")
        self.__x = x_

    def add(self, p):
        if p[0] >= self.__n_lin or p[1] >= self.__n_col:
            raise Exception("Indice linie sau coloana invalid!")
        self.__x.append(p)

    def sum_l(self):
        s = [0] * self.__n_lin
        for element in self.__x:
            s[element[0]] += element[2]
        return s

    def sum_c(self):
        s = [0] * self.__n_col
        for element in self.__x:
            s[element[1]] += element[2]
        return s

    def __eq__(self, other):
        if not isinstance(other, sparse_matrix):
            return False
        assert isinstance(other, sparse_matrix)
        if self.__n_lin != other.__n_lin or self.__n_col != other.__n_col:
            return False
        return True


class diagonal_matrix(sparse_matrix):
    def __init__(self, v):
        n = len(v)
        super(diagonal_matrix, self).__init__(n, n)
        for i in range(n):
            super().add([i, i, v[i]])

    def add(self,val):
        n = self.n_lin
        self.n_lin = self.n_lin + 1
        self.n_col = self.n_col + 1
        super(diagonal_matrix, self).add([n,n,val])
