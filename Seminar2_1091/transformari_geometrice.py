class mat3d():
    def __init__(self):
        self.__t = ([1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1])

    def __str__(self):
        sir = ",".join(str(i) for i in self.__t[0])
        sir += "\n"
        sir += ",".join(str(i) for i in self.__t[1])
        sir += "\n"
        sir += ",".join(str(i) for i in self.__t[2])
        sir += "\n"
        sir += ",".join(str(i) for i in self.__t[3])
        return sir

    def __getTx(self, point):
        return point[0] * self.__t[0][0] + point[1] * self.__t[1][0] + \
               point[2] * self.__t[2][0] + self.__t[3][0]

    def __getTy(self, point):
        return point[0] * self.__t[0][1] + point[1] * self.__t[1][1] + \
               point[2] * self.__t[2][1] + self.__t[3][1]

    def __getTz(self, point):
        return point[0] * self.__t[0][2] + point[1] * self.__t[1][2] + \
               point[2] * self.__t[2][2] + self.__t[3][2]

    def transform(self, point):
        if len(point) != 3:
            raise Exception("Dimensiune invalida pentru punct!")
        p = (
            self.__getTx(point),
            self.__getTy(point),
            self.__getTz(point)
        )
        return p

    def set_element(self, i, j, v):
        if i < 0 or i > 3:
            raise Exception("Pozitie linie invalida!")
        if j < 0 or j > 2:
            raise Exception("Pozitie coloana invalida!")
        self.__t[i][j] = v

    @property
    def t(self):
        return self.__t

    @t.setter
    def t(self, t_):
        if not isinstance(t_, tuple):
            raise Exception("Parametru cu tip invalid!")
        if len(t_) != 4:
            raise Exception("Dimensiune invalida pentru matricea de transformare!")
        for l in t_:
            if len(l) != 4:
                raise Exception("Dimensiune linie invalida!")
        self.__t = t_

    def __eq__(self, other):
        if not isinstance(other, mat3d):
            return False
        return self.__t == other.__t


class mattran3d(mat3d):
    def __init__(self, point):
        if len(point) != 3:
            raise Exception("Definire incorecta!")
        super().__init__()
        super(mattran3d, self).set_element(3, 0, point[0])
        super(mattran3d, self).set_element(3, 1, point[1])
        super(mattran3d, self).set_element(3, 2, point[2])

    def transform(self, point):
        if len(point) != 3:
            raise Exception("Dimensiune incorecta pentru punct!")
        return (self.t[3][0] + point[0], self.t[3][1] + point[1], self.t[3][2] + point[2])
