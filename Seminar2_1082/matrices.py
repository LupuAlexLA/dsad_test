class sparse_matrix():
    def __init__(self, n_lin, n_col, i, j, v):
        if max(i) >= n_lin:
            raise Exception("Indice linie invalid!")
        if max(j) >= n_col:
            raise Exception("Indice coloana invalid!")
        n = len(v)
        if len(i) != n or len(j) != n:
            raise Exception("Dimensiuni invalide")
        self.n_lin = n_lin
        self.n_col = n_col
        self.__i = i
        self.__j = j
        self.__x = v

    def __str__(self):
        sir = "["
        for k in range(len(self.__x)):
            sir += ("(" +
                    str(self.__i[k]) + "," +
                    str(self.__j[k]) + "," +
                    str(self.__x[k]) + ")")
        sir += "]"
        return sir

    @property
    def i(self):
        return self.__i

    @i.setter
    def i(self, i_):
        self.__i = i_

    @property
    def j(self):
        return self.__j

    @j.setter
    def j(self, j_):
        self.__j = j_

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x_):
        self.__x = x_

    # Calcul sume pe linii/coloane
    def sum_l(self):
        s = [0] * self.n_lin
        for k in range(len(self.__x)):
            s[self.__i[k]] += self.__x[k]
        return s

    def sum_c(self):
        s = [0] * self.n_col
        for k in range(len(self.__x)):
            s[self.__j[k]] += self.__x[k]
        return s

    def add(self, ki, kj, val):
        if ki >= self.n_lin:
            self.n_lin = ki + 1
        if kj >= self.n_col:
            self.n_col = kj + 1
        assert isinstance(self.__i, list)
        self.__i.append(ki)
        self.__j.append(kj)
        self.__x.append(val)

    def __eq__(self, other):
        assert isinstance(other, sparse_matrix)
        if self.n_lin != other.n_lin or self.n_col != other.n_col:
            return False
        if self.__i != other.__i:
            return False
        if self.__j != other.__j:
            return False
        if self.__x != other.__x:
            return False
        return True


class diagonal_matrix(sparse_matrix):
    def __init__(self, v):
        n = len(v)
        i_ = [k for k in range(n)]
        j_ = [k for k in range(n)]
        super().__init__(n, n, i_, j_, v)

    def add(self, val):
        n = len(self.x)
        super(diagonal_matrix, self).add(n, n, val)

    def __eq__(self, other):
        return self.x == other.x
