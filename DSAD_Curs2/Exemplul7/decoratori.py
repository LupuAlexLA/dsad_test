def decorator_medie(functie):
    def functie_wrapper(x):
        rez = functie(x)
        return rez, rez / len(x)

    return functie_wrapper
