import csv

with open("NEUROCHIR_P_2024r.csv", "r") as file:
    lignes=file.readlines()
    liste_matrice=[]
    for ligne in lignes:
        liste_colonnes=ligne.split(";")
        liste_matrice.append(liste_colonnes)

# trouver la position de RS
    #print(liste_matrice[0])
    position_RS=liste_matrice[0].index("RS")

# trouver la position de l'ETPSAL
    #print(liste_matrice[0])zzzzzz
    nb=liste_matrice[0].index("ETPSAL")

# creer une liste contenant les RS
    liste_RS = []
    for lines in liste_matrice:
        liste_RS.append(lines[position_RS])
    #print(liste_RS)

    diction={}
    for i in liste_RS:
        listes = []
        for j in liste_matrice:
            if i in j:
                listes.append(j[nb])
            diction[i]=listes
    #print(diction)

# reorganisation
    for clefs in liste_RS:
        for i in range(len(diction[clefs])):
            if diction[clefs][i]=="ETPSAL" or diction[clefs][i]=="":
                diction[clefs][i]="0"
    #print(diction)

    for i in diction:
        valeur=0
        for j in diction[i]:
            valeur+=float(j)
        diction[i]=valeur
    print(diction)


#trouver le ETPSAL le plus eleve
    maximum=0
    for i in diction:
        if diction[i]>maximum:
            maximum=diction[i]
            hopital=i
    print(maximum)
    print(hopital)
