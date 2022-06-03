from shapes import shape, rectangle

try:
    fig_a = shape([2, 5, 3, 2.5, 1], [1, 1, 4, 7, 4], "A")
    print(fig_a)
    print("Coordonate x pentru", fig_a.denumire,
          ":", fig_a.x)
    fig_a.y = [1, 2, 3, 6, 9]
    print("Perimetrul pentru figura",
          fig_a.denumire, "este",
          fig_a.perimetru())
    fig_b = shape([23, 5, 7], [56, 59, 67], "B")
    print(fig_a == fig_b)
    fig_c = rectangle(2, 1, 3, 2, "C")
    print(fig_c, "Perimetru:",
          fig_c.perimetru(), sep="\n")
    fig_d = rectangle(1, 1, 4, 1)
    print(fig_d)
    print(fig_d == fig_c)
except Exception as ex:
    print(ex)
