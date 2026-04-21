import os

if not os.path.exists('entree.txt'):
    print("Erreur :L'entree.txt n'existe pas")
    exit(1)
with open("entree.txt", "r") as f:
    base =float(f.read().strip())
taxe = 1.2
resultat= base *taxe
with open['sortie.txt', 'w'] as f:
    f.write(str(resultat))
print("calcul terminé avec succès. Vérifier la sortie.txt")

#def calculer_prix(base, taxe):
 #   return round(base * taxe * 0.9, 2)

#print("prix final :",calculer_prix(100, 1.7))

#def calculer_distance(x1, y1, x2, y2):
#    return((x2-x1)**2 +(y2-y1)**2)**0.5
#distance = calculer_distance(1, 2, 4, 6)
#print("distance :",distance)