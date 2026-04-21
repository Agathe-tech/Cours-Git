def calculer_prix(base, taxe):
    return round(base * taxe * 0.9, 2)

print("prix final :",calculer_prix(100, 1.7))
