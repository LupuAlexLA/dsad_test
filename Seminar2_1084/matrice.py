class sparse_matrix():
    def __init__(self, n_lin, n_col, i, j, x):
        if max(i) >= n_lin:
            raise Exception("Index linie invalid!")
        if max(j) >= n_col:
            raise Exception("Index coloana invalid!")
        n = len(i)
        if len(j) != n or len(x) != n:
            raise Exception("Numar diferit de elemente in structura!")
        self.__i = i
        self.__j = j
        self.__x = x
        self.n_lin = n_lin
        self.n_col = n_col

    def __str__(self):
        sir = "["
        for k in range(len(self.__x)):
            sir += ("(" + str(self.__i[k]) + "," + str(self.__j[k]) + "," + str(self.__x[k]) + ")")
        return sir

    @property
    def i(self):
        return self.__i

    @i.setter
    def i(self, i):
        self.__i = i

    @property
    def j(self):
        return self.__j

    @j.setter
    def j(self, j):
        self.__j = j

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    #     Calcul sume pe linii/coloane
    def l_sum(self):
        s = [0] * self.n_lin
        for k in range(len(self.__x)):
            s[self.__i[k]] += self.__x[k]
        return s

    def c_sum(self):
        s = [0] * self.n_col
        for k in range(len(self.__x)):
            s[self.__j[k]] += self.__x[k]
        return s

    #     Adaugare de element
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
        return self.n_lin == other.n_lin and \
               self.n_col == other.n_col and \
               self.__i == other.__i and \
               self.__j == other.__j and \
               self.__x == other.__x


class diagonal_matrix(sparse_matrix):
    def __init__(self, x):
        n = len(x)
        i = list(v for v in range(n))
        j = list(v for v in range(n))
        super().__init__(n, n, i, j, x)

    def add(self, val):
        n = len(self.x)
        super().add(n,n,val)


