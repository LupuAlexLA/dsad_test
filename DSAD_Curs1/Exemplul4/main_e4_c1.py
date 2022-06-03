import biblioteca

# Instantiere obiect carte
c = biblioteca.carte("Istoria Romana","Theodor Mommsen",7)
print(c)
print(c.get_autori())

c.numar_volume = 4
print(c.numar_volume)
