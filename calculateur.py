def calculer_prix(base, taxe):
    return round(base * taxe, 2)

print("prix final :",calculer_prix(100, 1.7))
