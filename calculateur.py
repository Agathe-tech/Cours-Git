def calculer_prix(base, taxe):
    return round(base * taxe * 0.9, 2)

print("prix final :",calculer_prix(100, 1.7))

def calculer_distance(x1, y1, x2, y2):
    return((x2-x1)**2 +(y2-y1)**2)**0.5
distance = calculer_distance(1, 2, 4, 6)
print("distance :",distance)