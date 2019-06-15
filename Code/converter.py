# Função de arredondamento
def converterUmZero(resultado):
    for i in range(resultado.size):
        if(resultado[i] >= 0.5):
            resultado[i] = 1
        else:
            resultado[i] = 0
    return resultado

# Converte os valores de Y em valores numéricos
def converterY(vetor):
    for i in range(vetor.size):
        if(vetor[i] == 'e'):
            vetor[i] = 0
        elif(vetor[i] == 'p'):
            vetor[i] = 1
    vetor = list(map(float, vetor))
    return vetor

# Converte os valores de X em valores numéricos
# Valores desbalanceados com a variável 11
def converterX(vetor):
    for i in range(vetor.shape[0]):
        # 1. cap-shape: bell=b, conical=c, convex=x, flat=f, knobbed=k, sunken=s
        if(vetor[i][0] == 'b'):
            vetor[i][0] = 0
        elif(vetor[i][0] == 'c'):
            vetor[i][0] = 1
        elif(vetor[i][0] == 'x'):
            vetor[i][0] = 2
        elif(vetor[i][0] == 'f'):
            vetor[i][0] = 3
        elif(vetor[i][0] == 'k'):
            vetor[i][0] = 4
        elif(vetor[i][0] == 's'):
            vetor[i][0] = 5

        # 2. cap-surface: fibrous=f, grooves=g, scaly=y, smooth=s
        if(vetor[i][1] == 'f'):
            vetor[i][1] = 0
        elif(vetor[i][1] == 'g'):
            vetor[i][1] = 1
        elif(vetor[i][1] == 'y'):
            vetor[i][1] = 2
        elif(vetor[i][1] == 's'):
            vetor[i][1] = 3

        # 3. cap-color: brown=n, buff=b, cinnamon=c, gray=g, green=r, pink=p, purple=u, red=e, white=w, yellow=y
        if(vetor[i][2] == 'n'):
            vetor[i][2] = 0
        elif(vetor[i][2] == 'b'):
            vetor[i][2] = 1
        elif(vetor[i][2] == 'c'):
            vetor[i][2] = 2
        elif(vetor[i][2] == 'g'):
            vetor[i][2] = 3
        elif(vetor[i][2] == 'r'):
            vetor[i][2] = 4
        elif(vetor[i][2] == 'p'):
            vetor[i][2] = 5
        elif(vetor[i][2] == 'u'):
            vetor[i][2] = 6
        elif(vetor[i][2] == 'e'):
            vetor[i][2] = 7
        elif(vetor[i][2] == 'w'):
            vetor[i][2] = 8
        elif(vetor[i][2] == 'y'):
            vetor[i][2] = 9

        # 4. bruises?: bruises=t, no=f
        if(vetor[i][3] == 'f'):
            vetor[i][3] = 0
        elif(vetor[i][3] == 't'):
            vetor[i][3] = 1

        # 5. odor: almond=a, anise=l, creosote=c, fishy=y, foul=f, musty=m, none=n, pungent=p, spicy=s
        if(vetor[i][4] == 'a'):
            vetor[i][4] = 0
        elif(vetor[i][4] == 'l'):
            vetor[i][4] = 1
        elif(vetor[i][4] == 'c'):
            vetor[i][4] = 2
        elif(vetor[i][4] == 'y'):
            vetor[i][4] = 3
        elif(vetor[i][4] == 'f'):
            vetor[i][4] = 4
        elif(vetor[i][4] == 'm'):
            vetor[i][4] = 5
        elif(vetor[i][4] == 'n'):
            vetor[i][4] = 6
        elif(vetor[i][4] == 'p'):
            vetor[i][4] = 7
        elif(vetor[i][4] == 's'):
            vetor[i][4] = 8

        # 6. gill-attachment: attached=a, descending=d, free=f, notched=n
        if(vetor[i][5] == 'a'):
            vetor[i][5] = 0
        elif(vetor[i][5] == 'd'):
            vetor[i][5] = 1
        elif(vetor[i][5] == 'f'):
            vetor[i][5] = 2
        elif(vetor[i][5] == 'n'):
            vetor[i][5] = 3

        # 7. gill-spacing: close=c, crowded=w, distant=d
        if(vetor[i][6] == 'c'):
            vetor[i][6] = 0
        elif(vetor[i][6] == 'w'):
            vetor[i][6] = 1
        elif(vetor[i][6] == 'd'):
            vetor[i][6] = 2

        # 8. gill-size: broad=b, narrow=n
        if(vetor[i][7] == 'b'):
            vetor[i][7] = 0
        elif(vetor[i][7] == 'n'):
            vetor[i][7] = 1

        # 9. gill-color: black=k, brown=n, buff=b, chocolate=h, gray=g, green=r,
        # orange=o, pink=p, purple=u, red=e, white=w, yellow=y
        if(vetor[i][8] == 'k'):
            vetor[i][8] = 0
        elif(vetor[i][8] == 'n'):
            vetor[i][8] = 1
        elif(vetor[i][8] == 'b'):
            vetor[i][8] = 2
        elif(vetor[i][8] == 'h'):
            vetor[i][8] = 3
        elif(vetor[i][8] == 'g'):
            vetor[i][8] = 4
        elif(vetor[i][8] == 'r'):
            vetor[i][8] = 5
        elif(vetor[i][8] == 'o'):
            vetor[i][8] = 6
        elif(vetor[i][8] == 'p'):
            vetor[i][8] = 7
        elif(vetor[i][8] == 'u'):
            vetor[i][8] = 8
        elif(vetor[i][8] == 'e'):
            vetor[i][8] = 9
        elif(vetor[i][8] == 'w'):
            vetor[i][8] = 10
        elif(vetor[i][8] == 'y'):
            vetor[i][8] = 11

        # 10. stalk-shape: enlarging=e, tapering=t
        if(vetor[i][9] == 'e'):
            vetor[i][9] = 0
        elif(vetor[i][9] == 't'):
            vetor[i][9] = 1

        # 11. stalk-root: bulbous=b, club=c, cup=u, equal=e, rhizomorphs=z, rooted=r, missing=?
        if(vetor[i][10] == '?'):
            vetor[i][10] = 0
        elif(vetor[i][10] == 'b'):
            vetor[i][10] = 1
        elif(vetor[i][10] == 'c'):
            vetor[i][10] = 2
        elif(vetor[i][10] == 'u'):
            vetor[i][10] = 3
        elif(vetor[i][10] == 'e'):
            vetor[i][10] = 4
        elif(vetor[i][10] == 'z'):
            vetor[i][10] = 5
        elif(vetor[i][10] == 'r'):
            vetor[i][10] = 6

        # 12. stalk-surface-above-ring: fibrous=f, scaly=y, silky=k, smooth=s
        if(vetor[i][11] == 'f'):
            vetor[i][11] = 0
        elif(vetor[i][11] == 'y'):
            vetor[i][11] = 1
        elif(vetor[i][11] == 'k'):
            vetor[i][11] = 2
        elif(vetor[i][11] == 's'):
            vetor[i][11] = 3

        # 13. stalk-surface-below-ring: fibrous=f, scaly=y, silky=k, smooth=s
        if(vetor[i][12] == 'f'):
            vetor[i][12] = 0
        elif(vetor[i][12] == 'y'):
            vetor[i][12] = 1
        elif(vetor[i][12] == 'k'):
            vetor[i][12] = 2
        elif(vetor[i][12] == 's'):
            vetor[i][12] = 3

        # 14. stalk-color-above-ring: brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y
        if(vetor[i][13] == 'n'):
            vetor[i][13] = 0
        elif(vetor[i][13] == 'b'):
            vetor[i][13] = 1
        elif(vetor[i][13] == 'c'):
            vetor[i][13] = 2
        elif(vetor[i][13] == 'g'):
            vetor[i][13] = 3
        elif(vetor[i][13] == 'o'):
            vetor[i][13] = 4
        elif(vetor[i][13] == 'p'):
            vetor[i][13] = 5
        elif(vetor[i][13] == 'e'):
            vetor[i][13] = 6
        elif(vetor[i][13] == 'w'):
            vetor[i][13] = 7
        elif(vetor[i][13] == 'y'):
            vetor[i][13] = 8

        # 15. stalk-color-below-ring: brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y
        if(vetor[i][14] == 'n'):
            vetor[i][14] = 0
        elif(vetor[i][14] == 'b'):
            vetor[i][14] = 1
        elif(vetor[i][14] == 'c'):
            vetor[i][14] = 2
        elif(vetor[i][14] == 'g'):
            vetor[i][14] = 3
        elif(vetor[i][14] == 'o'):
            vetor[i][14] = 4
        elif(vetor[i][14] == 'p'):
            vetor[i][14] = 5
        elif(vetor[i][14] == 'e'):
            vetor[i][14] = 6
        elif(vetor[i][14] == 'w'):
            vetor[i][14] = 7
        elif(vetor[i][14] == 'y'):
            vetor[i][14] = 8

        # 16. veil-type: partial=p, universal=u
        if(vetor[i][15] == 'p'):
            vetor[i][15] = 0
        elif(vetor[i][15] == 'u'):
            vetor[i][15] = 1

        # 17. veil-color: brown=n, orange=o, white=w, yellow=y
        if(vetor[i][16] == 'n'):
            vetor[i][16] = 0
        elif(vetor[i][16] == 'o'):
            vetor[i][16] = 1
        elif(vetor[i][16] == 'w'):
            vetor[i][16] = 2
        elif(vetor[i][16] == 'y'):
            vetor[i][16] = 3

        # 18. ring-number: none=n, one=o, two=t
        if(vetor[i][17] == 'n'):
            vetor[i][17] = 0
        elif(vetor[i][17] == 'o'):
            vetor[i][17] = 1
        elif(vetor[i][17] == 't'):
            vetor[i][17] = 2

        # 19. ring-type: cobwebby=c, evanescent=e, flaring=f, large=l, none=n, pendant=p, sheathing=s, zone=z
        if(vetor[i][18] == 'c'):
            vetor[i][18] = 0
        elif(vetor[i][18] == 'e'):
            vetor[i][18] = 1
        elif(vetor[i][18] == 'f'):
            vetor[i][18] = 2
        elif(vetor[i][18] == 'l'):
            vetor[i][18] = 3
        elif(vetor[i][18] == 'n'):
            vetor[i][18] = 4
        elif(vetor[i][18] == 'p'):
            vetor[i][18] = 5
        elif(vetor[i][18] == 's'):
            vetor[i][18] = 6
        elif(vetor[i][18] == 'z'):
            vetor[i][18] = 7

        # 20. spore-print-color: black=k, brown=n, buff=b, chocolate=h, green=r, orange=o, purple=u, white=w, yellow=y
        if(vetor[i][19] == 'k'):
            vetor[i][19] = 0
        elif(vetor[i][19] == 'n'):
            vetor[i][19] = 1
        elif(vetor[i][19] == 'b'):
            vetor[i][19] = 2
        elif(vetor[i][19] == 'h'):
            vetor[i][19] = 3
        elif(vetor[i][19] == 'r'):
            vetor[i][19] = 4
        elif(vetor[i][19] == 'o'):
            vetor[i][19] = 5
        elif(vetor[i][19] == 'u'):
            vetor[i][19] = 6
        elif(vetor[i][19] == 'w'):
            vetor[i][19] = 7
        elif(vetor[i][19] == 'y'):
            vetor[i][19] = 8

        # 21. population: abundant=a, clustered=c, numerous=n, scattered=s, several=v, solitary=y
        if(vetor[i][20] == 'a'):
            vetor[i][20] = 0
        elif(vetor[i][20] == 'c'):
            vetor[i][20] = 1
        elif(vetor[i][20] == 'n'):
            vetor[i][20] = 2
        elif(vetor[i][20] == 's'):
            vetor[i][20] = 3
        elif(vetor[i][20] == 'v'):
            vetor[i][20] = 4
        elif(vetor[i][20] == 'y'):
            vetor[i][20] = 5

        # 22. habitat: grasses=g, leaves=l, meadows=m, paths=p, urban=u, waste=w, woods=d
        if(vetor[i][21] == 'g'):
            vetor[i][21] = 0
        elif(vetor[i][21] == 'l'):
            vetor[i][21] = 1
        elif(vetor[i][21] == 'm'):
            vetor[i][21] = 2
        elif(vetor[i][21] == 'p'):
            vetor[i][21] = 3
        elif(vetor[i][21] == 'u'):
            vetor[i][21] = 4
        elif(vetor[i][21] == 'w'):
            vetor[i][21] = 5
        elif(vetor[i][21] == 'd'):
            vetor[i][21] = 6

    return vetor

# Valores desbalanceados sem a variável 11
def converterX2(vetor):
    for i in range(vetor.shape[0]):
        # 1. cap-shape: bell=b, conical=c, convex=x, flat=f, knobbed=k, sunken=s
        if(vetor[i][0] == 'b'):
            vetor[i][0] = 0
        elif(vetor[i][0] == 'c'):
            vetor[i][0] = 1
        elif(vetor[i][0] == 'x'):
            vetor[i][0] = 2
        elif(vetor[i][0] == 'f'):
            vetor[i][0] = 3
        elif(vetor[i][0] == 'k'):
            vetor[i][0] = 4
        elif(vetor[i][0] == 's'):
            vetor[i][0] = 5

    # 2. cap-surface: fibrous=f, grooves=g, scaly=y, smooth=s
        if(vetor[i][1] == 'f'):
            vetor[i][1] = 0
        elif(vetor[i][1] == 'g'):
            vetor[i][1] = 1
        elif(vetor[i][1] == 'y'):
            vetor[i][1] = 2
        elif(vetor[i][1] == 's'):
            vetor[i][1] = 3

    # 3. cap-color: brown=n, buff=b, cinnamon=c, gray=g, green=r, pink=p, purple=u, red=e, white=w, yellow=y
        if(vetor[i][2] == 'n'):
            vetor[i][2] = 0
        elif(vetor[i][2] == 'b'):
            vetor[i][2] = 1
        elif(vetor[i][2] == 'c'):
            vetor[i][2] = 2
        elif(vetor[i][2] == 'g'):
            vetor[i][2] = 3
        elif(vetor[i][2] == 'r'):
            vetor[i][2] = 4
        elif(vetor[i][2] == 'p'):
            vetor[i][2] = 5
        elif(vetor[i][2] == 'u'):
            vetor[i][2] = 6
        elif(vetor[i][2] == 'e'):
            vetor[i][2] = 7
        elif(vetor[i][2] == 'w'):
            vetor[i][2] = 8
        elif(vetor[i][2] == 'y'):
            vetor[i][2] = 9

    # 4. bruises?: bruises=t, no=f
        if(vetor[i][3] == 'f'):
            vetor[i][3] = 0
        elif(vetor[i][3] == 't'):
            vetor[i][3] = 1

    # 5. odor: almond=a, anise=l, creosote=c, fishy=y, foul=f, musty=m, none=n, pungent=p, spicy=s
        if(vetor[i][4] == 'a'):
            vetor[i][4] = 0
        elif(vetor[i][4] == 'l'):
            vetor[i][4] = 1
        elif(vetor[i][4] == 'c'):
            vetor[i][4] = 2
        elif(vetor[i][4] == 'y'):
            vetor[i][4] = 3
        elif(vetor[i][4] == 'f'):
            vetor[i][4] = 4
        elif(vetor[i][4] == 'm'):
            vetor[i][4] = 5
        elif(vetor[i][4] == 'n'):
            vetor[i][4] = 6
        elif(vetor[i][4] == 'p'):
            vetor[i][4] = 7
        elif(vetor[i][4] == 's'):
            vetor[i][4] = 8

    # 6. gill-attachment: attached=a, descending=d, free=f, notched=n
        if(vetor[i][5] == 'a'):
            vetor[i][5] = 0
        elif(vetor[i][5] == 'd'):
            vetor[i][5] = 1
        elif(vetor[i][5] == 'f'):
            vetor[i][5] = 2
        elif(vetor[i][5] == 'n'):
            vetor[i][5] = 3

    # 7. gill-spacing: close=c, crowded=w, distant=d
        if(vetor[i][6] == 'c'):
            vetor[i][6] = 0
        elif(vetor[i][6] == 'w'):
            vetor[i][6] = 1
        elif(vetor[i][6] == 'd'):
            vetor[i][6] = 2

    # 8. gill-size: broad=b, narrow=n
        if(vetor[i][7] == 'b'):
            vetor[i][7] = 0
        elif(vetor[i][7] == 'n'):
            vetor[i][7] = 1

    # 9. gill-color: black=k, brown=n, buff=b, chocolate=h, gray=g, green=r,
    # orange=o, pink=p, purple=u, red=e, white=w, yellow=y
        if(vetor[i][8] == 'k'):
            vetor[i][8] = 0
        elif(vetor[i][8] == 'n'):
            vetor[i][8] = 1
        elif(vetor[i][8] == 'b'):
            vetor[i][8] = 2
        elif(vetor[i][8] == 'h'):
            vetor[i][8] = 3
        elif(vetor[i][8] == 'g'):
            vetor[i][8] = 4
        elif(vetor[i][8] == 'r'):
            vetor[i][8] = 5
        elif(vetor[i][8] == 'o'):
            vetor[i][8] = 6
        elif(vetor[i][8] == 'p'):
            vetor[i][8] = 7
        elif(vetor[i][8] == 'u'):
            vetor[i][8] = 8
        elif(vetor[i][8] == 'e'):
            vetor[i][8] = 9
        elif(vetor[i][8] == 'w'):
            vetor[i][8] = 10
        elif(vetor[i][8] == 'y'):
            vetor[i][8] = 11

    # 10. stalk-shape: enlarging=e, tapering=t
        if(vetor[i][9] == 'e'):
            vetor[i][9] = 0
        elif(vetor[i][9] == 't'):
            vetor[i][9] = 1

    # 12. stalk-surface-above-ring: fibrous=f, scaly=y, silky=k, smooth=s
        if(vetor[i][10] == 'f'):
            vetor[i][10] = 0
        elif(vetor[i][10] == 'y'):
            vetor[i][10] = 1
        elif(vetor[i][10] == 'k'):
            vetor[i][10] = 2
        elif(vetor[i][10] == 's'):
            vetor[i][10] = 3

    # 13. stalk-surface-below-ring: fibrous=f, scaly=y, silky=k, smooth=s
        if(vetor[i][11] == 'f'):
            vetor[i][11] = 0
        elif(vetor[i][11] == 'y'):
            vetor[i][11] = 1
        elif(vetor[i][11] == 'k'):
            vetor[i][11] = 2
        elif(vetor[i][11] == 's'):
            vetor[i][11] = 3

    # 14. stalk-color-above-ring: brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y
        if(vetor[i][12] == 'n'):
            vetor[i][12] = 0
        elif(vetor[i][12] == 'b'):
            vetor[i][12] = 1
        elif(vetor[i][12] == 'c'):
            vetor[i][12] = 2
        elif(vetor[i][12] == 'g'):
            vetor[i][12] = 3
        elif(vetor[i][12] == 'o'):
            vetor[i][12] = 4
        elif(vetor[i][12] == 'p'):
            vetor[i][12] = 5
        elif(vetor[i][12] == 'e'):
            vetor[i][12] = 6
        elif(vetor[i][12] == 'w'):
            vetor[i][12] = 7
        elif(vetor[i][12] == 'y'):
            vetor[i][12] = 8

    # 15. stalk-color-below-ring: brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y
        if(vetor[i][13] == 'n'):
            vetor[i][13] = 0
        elif(vetor[i][13] == 'b'):
            vetor[i][13] = 1
        elif(vetor[i][13] == 'c'):
            vetor[i][13] = 2
        elif(vetor[i][13] == 'g'):
            vetor[i][13] = 3
        elif(vetor[i][13] == 'o'):
            vetor[i][13] = 4
        elif(vetor[i][13] == 'p'):
            vetor[i][13] = 5
        elif(vetor[i][13] == 'e'):
            vetor[i][13] = 6
        elif(vetor[i][13] == 'w'):
            vetor[i][13] = 7
        elif(vetor[i][13] == 'y'):
            vetor[i][13] = 8

    # 16. veil-type: partial=p, universal=u
        if(vetor[i][14] == 'p'):
            vetor[i][14] = 0
        elif(vetor[i][14] == 'u'):
            vetor[i][14] = 1

    # 17. veil-color: brown=n, orange=o, white=w, yellow=y
        if(vetor[i][15] == 'n'):
            vetor[i][15] = 0
        elif(vetor[i][15] == 'o'):
            vetor[i][15] = 1
        elif(vetor[i][15] == 'w'):
            vetor[i][15] = 2
        elif(vetor[i][15] == 'y'):
            vetor[i][15] = 3

    # 18. ring-number: none=n, one=o, two=t
        if(vetor[i][16] == 'n'):
            vetor[i][16] = 0
        elif(vetor[i][16] == 'o'):
            vetor[i][16] = 1
        elif(vetor[i][16] == 't'):
            vetor[i][16] = 2

    # 19. ring-type: cobwebby=c, evanescent=e, flaring=f, large=l, none=n, pendant=p, sheathing=s, zone=z
        if(vetor[i][17] == 'c'):
            vetor[i][17] = 0
        elif(vetor[i][17] == 'e'):
            vetor[i][17] = 1
        elif(vetor[i][17] == 'f'):
            vetor[i][17] = 2
        elif(vetor[i][17] == 'l'):
            vetor[i][17] = 3
        elif(vetor[i][17] == 'n'):
            vetor[i][17] = 4
        elif(vetor[i][17] == 'p'):
            vetor[i][17] = 5
        elif(vetor[i][17] == 's'):
            vetor[i][17] = 6
        elif(vetor[i][17] == 'z'):
            vetor[i][17] = 7

    # 20. spore-print-color: black=k, brown=n, buff=b, chocolate=h, green=r, orange=o, purple=u, white=w, yellow=y
        if(vetor[i][18] == 'k'):
            vetor[i][18] = 0
        elif(vetor[i][18] == 'n'):
            vetor[i][18] = 1
        elif(vetor[i][18] == 'b'):
            vetor[i][18] = 2
        elif(vetor[i][18] == 'h'):
            vetor[i][18] = 3
        elif(vetor[i][18] == 'r'):
            vetor[i][18] = 4
        elif(vetor[i][18] == 'o'):
            vetor[i][18] = 5
        elif(vetor[i][18] == 'u'):
            vetor[i][18] = 6
        elif(vetor[i][18] == 'w'):
            vetor[i][18] = 7
        elif(vetor[i][18] == 'y'):
            vetor[i][18] = 8

    # 21. population: abundant=a, clustered=c, numerous=n, scattered=s, several=v, solitary=y
        if(vetor[i][19] == 'a'):
            vetor[i][19] = 0
        elif(vetor[i][19] == 'c'):
            vetor[i][19] = 1
        elif(vetor[i][19] == 'n'):
            vetor[i][19] = 2
        elif(vetor[i][19] == 's'):
            vetor[i][19] = 3
        elif(vetor[i][19] == 'v'):
            vetor[i][19] = 4
        elif(vetor[i][19] == 'y'):
            vetor[i][19] = 5

    # 22. habitat: grasses=g, leaves=l, meadows=m, paths=p, urban=u, waste=w, woods=d
        if(vetor[i][20] == 'g'):
            vetor[i][20] = 0
        elif(vetor[i][20] == 'l'):
            vetor[i][20] = 1
        elif(vetor[i][20] == 'm'):
            vetor[i][20] = 2
        elif(vetor[i][20] == 'p'):
            vetor[i][20] = 3
        elif(vetor[i][20] == 'u'):
            vetor[i][20] = 4
        elif(vetor[i][20] == 'w'):
            vetor[i][20] = 5
        elif(vetor[i][20] == 'd'):
            vetor[i][20] = 6

    return vetor

# Valores balanceados
def converterX3(vetor):
    for i in range(len(vetor)):
        # 1. cap-shape: bell=b, conical=c, convex=x, flat=f, knobbed=k, sunken=s
        if(vetor[i][0] == 'b'):
            vetor[i][0] = 0
        elif(vetor[i][0] == 'c'):
            vetor[i][0] = 1 / 5
        elif(vetor[i][0] == 'x'):
            vetor[i][0] = 2 / 5
        elif(vetor[i][0] == 'f'):
            vetor[i][0] = 3 / 5
        elif(vetor[i][0] == 'k'):
            vetor[i][0] = 4 / 5
        elif(vetor[i][0] == 's'):
            vetor[i][0] = 5 / 5

        # 2. cap-surface: fibrous=f, grooves=g, scaly=y, smooth=s
        if(vetor[i][1] == 'f'):
            vetor[i][1] = 0
        elif(vetor[i][1] == 'g'):
            vetor[i][1] = 1 / 3
        elif(vetor[i][1] == 'y'):
            vetor[i][1] = 2 / 3
        elif(vetor[i][1] == 's'):
            vetor[i][1] = 3 / 3

        # 3. cap-color: brown=n, buff=b, cinnamon=c, gray=g, green=r, pink=p, purple=u, red=e, white=w, yellow=y
        if(vetor[i][2] == 'n'):
            vetor[i][2] = 0
        elif(vetor[i][2] == 'b'):
            vetor[i][2] = 1 / 9
        elif(vetor[i][2] == 'c'):
            vetor[i][2] = 2 / 9
        elif(vetor[i][2] == 'g'):
            vetor[i][2] = 3 / 9
        elif(vetor[i][2] == 'r'):
            vetor[i][2] = 4 / 9
        elif(vetor[i][2] == 'p'):
            vetor[i][2] = 5 / 9
        elif(vetor[i][2] == 'u'):
            vetor[i][2] = 6 / 9
        elif(vetor[i][2] == 'e'):
            vetor[i][2] = 7 / 9
        elif(vetor[i][2] == 'w'):
            vetor[i][2] = 8 / 9
        elif(vetor[i][2] == 'y'):
            vetor[i][2] = 9 / 9

        # 4. bruises?: bruises=t, no=f
        if(vetor[i][3] == 'f'):
            vetor[i][3] = 0
        elif(vetor[i][3] == 't'):
            vetor[i][3] = 1

        # 5. odor: almond=a, anise=l, creosote=c, fishy=y, foul=f, musty=m, none=n, pungent=p, spicy=s
        if(vetor[i][4] == 'a'):
            vetor[i][4] = 0
        elif(vetor[i][4] == 'l'):
            vetor[i][4] = 1 / 8
        elif(vetor[i][4] == 'c'):
            vetor[i][4] = 2 / 8
        elif(vetor[i][4] == 'y'):
            vetor[i][4] = 3 / 8
        elif(vetor[i][4] == 'f'):
            vetor[i][4] = 4 / 8
        elif(vetor[i][4] == 'm'):
            vetor[i][4] = 5 / 8
        elif(vetor[i][4] == 'n'):
            vetor[i][4] = 6 / 8
        elif(vetor[i][4] == 'p'):
            vetor[i][4] = 7 / 8
        elif(vetor[i][4] == 's'):
            vetor[i][4] = 8 / 8

        # 6. gill-attachment: attached=a, descending=d, free=f, notched=n
        if(vetor[i][5] == 'a'):
            vetor[i][5] = 0
        elif(vetor[i][5] == 'd'):
            vetor[i][5] = 1 / 3
        elif(vetor[i][5] == 'f'):
            vetor[i][5] = 2 / 3
        elif(vetor[i][5] == 'n'):
            vetor[i][5] = 3 / 3

        # 7. gill-spacing: close=c, crowded=w, distant=d
        if(vetor[i][6] == 'c'):
            vetor[i][6] = 0
        elif(vetor[i][6] == 'w'):
            vetor[i][6] = 1 / 2
        elif(vetor[i][6] == 'd'):
            vetor[i][6] = 2 / 2

        # 8. gill-size: broad=b, narrow=n
        if(vetor[i][7] == 'b'):
            vetor[i][7] = 0
        elif(vetor[i][7] == 'n'):
            vetor[i][7] = 1

        # 9. gill-color: black=k, brown=n, buff=b, chocolate=h, gray=g, green=r,
        # orange=o, pink=p, purple=u, red=e, white=w, yellow=y
        if(vetor[i][8] == 'k'):
            vetor[i][8] = 0
        elif(vetor[i][8] == 'n'):
            vetor[i][8] = 1 / 11
        elif(vetor[i][8] == 'b'):
            vetor[i][8] = 2 / 11
        elif(vetor[i][8] == 'h'):
            vetor[i][8] = 3 / 11
        elif(vetor[i][8] == 'g'):
            vetor[i][8] = 4 / 11
        elif(vetor[i][8] == 'r'):
            vetor[i][8] = 5 / 11
        elif(vetor[i][8] == 'o'):
            vetor[i][8] = 6 / 11
        elif(vetor[i][8] == 'p'):
            vetor[i][8] = 7 / 11
        elif(vetor[i][8] == 'u'):
            vetor[i][8] = 8 / 11
        elif(vetor[i][8] == 'e'):
            vetor[i][8] = 9 / 11
        elif(vetor[i][8] == 'w'):
            vetor[i][8] = 10 / 11
        elif(vetor[i][8] == 'y'):
            vetor[i][8] = 11 / 11

        # 10. stalk-shape: enlarging=e, tapering=t
        if(vetor[i][9] == 'e'):
            vetor[i][9] = 0
        elif(vetor[i][9] == 't'):
            vetor[i][9] = 1

        # 11. stalk-root: bulbous=b, club=c, cup=u, equal=e, rhizomorphs=z, rooted=r, missing=?
        if(vetor[i][10] == '?'):
            vetor[i][10] = 0
        elif(vetor[i][10] == 'b'):
            vetor[i][10] = 1 / 6
        elif(vetor[i][10] == 'c'):
            vetor[i][10] = 2 / 6
        elif(vetor[i][10] == 'u'):
            vetor[i][10] = 3 / 6
        elif(vetor[i][10] == 'e'):
            vetor[i][10] = 4 / 6
        elif(vetor[i][10] == 'z'):
            vetor[i][10] = 5 / 6
        elif(vetor[i][10] == 'r'):
            vetor[i][10] = 6 / 6

        # 12. stalk-surface-above-ring: fibrous=f, scaly=y, silky=k, smooth=s
        if(vetor[i][11] == 'f'):
            vetor[i][11] = 0
        elif(vetor[i][11] == 'y'):
            vetor[i][11] = 1 / 3
        elif(vetor[i][11] == 'k'):
            vetor[i][11] = 2 / 3
        elif(vetor[i][11] == 's'):
            vetor[i][11] = 3 / 3

        # 13. stalk-surface-below-ring: fibrous=f, scaly=y, silky=k, smooth=s
        if(vetor[i][12] == 'f'):
            vetor[i][12] = 0
        elif(vetor[i][12] == 'y'):
            vetor[i][12] = 1 / 3
        elif(vetor[i][12] == 'k'):
            vetor[i][12] = 2 / 3
        elif(vetor[i][12] == 's'):
            vetor[i][12] = 3 / 3

        # 14. stalk-color-above-ring: brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y
        if(vetor[i][13] == 'n'):
            vetor[i][13] = 0
        elif(vetor[i][13] == 'b'):
            vetor[i][13] = 1 / 8
        elif(vetor[i][13] == 'c'):
            vetor[i][13] = 2 / 8
        elif(vetor[i][13] == 'g'):
            vetor[i][13] = 3 / 8
        elif(vetor[i][13] == 'o'):
            vetor[i][13] = 4 / 8
        elif(vetor[i][13] == 'p'):
            vetor[i][13] = 5 / 8
        elif(vetor[i][13] == 'e'):
            vetor[i][13] = 6 / 8
        elif(vetor[i][13] == 'w'):
            vetor[i][13] = 7 / 8
        elif(vetor[i][13] == 'y'):
            vetor[i][13] = 8 / 8

        # 15. stalk-color-below-ring: brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y
        if(vetor[i][14] == 'n'):
            vetor[i][14] = 0
        elif(vetor[i][14] == 'b'):
            vetor[i][14] = 1 / 8
        elif(vetor[i][14] == 'c'):
            vetor[i][14] = 2 / 8
        elif(vetor[i][14] == 'g'):
            vetor[i][14] = 3 / 8
        elif(vetor[i][14] == 'o'):
            vetor[i][14] = 4 / 8
        elif(vetor[i][14] == 'p'):
            vetor[i][14] = 5 / 8
        elif(vetor[i][14] == 'e'):
            vetor[i][14] = 6 / 8
        elif(vetor[i][14] == 'w'):
            vetor[i][14] = 7 / 8
        elif(vetor[i][14] == 'y'):
            vetor[i][14] = 8 / 8

        # 16. veil-type: partial=p, universal=u
        if(vetor[i][15] == 'p'):
            vetor[i][15] = 0
        elif(vetor[i][15] == 'u'):
            vetor[i][15] = 1

        # 17. veil-color: brown=n, orange=o, white=w, yellow=y
        if(vetor[i][16] == 'n'):
            vetor[i][16] = 0
        elif(vetor[i][16] == 'o'):
            vetor[i][16] = 1 / 3
        elif(vetor[i][16] == 'w'):
            vetor[i][16] = 2 / 3
        elif(vetor[i][16] == 'y'):
            vetor[i][16] = 3 / 3

        # 18. ring-number: none=n, one=o, two=t
        if(vetor[i][17] == 'n'):
            vetor[i][17] = 0
        elif(vetor[i][17] == 'o'):
            vetor[i][17] = 1 / 2
        elif(vetor[i][17] == 't'):
            vetor[i][17] = 2 / 2

        # 19. ring-type: cobwebby=c, evanescent=e, flaring=f, large=l, none=n, pendant=p, sheathing=s, zone=z
        if(vetor[i][18] == 'c'):
            vetor[i][18] = 0 / 7
        elif(vetor[i][18] == 'e'):
            vetor[i][18] = 1 / 7
        elif(vetor[i][18] == 'f'):
            vetor[i][18] = 2 / 7
        elif(vetor[i][18] == 'l'):
            vetor[i][18] = 3 / 7
        elif(vetor[i][18] == 'n'):
            vetor[i][18] = 4 / 7
        elif(vetor[i][18] == 'p'):
            vetor[i][18] = 5 / 7
        elif(vetor[i][18] == 's'):
            vetor[i][18] = 6 / 7
        elif(vetor[i][18] == 'z'):
            vetor[i][18] = 7 / 7

        # 20. spore-print-color: black=k, brown=n, buff=b, chocolate=h, green=r, orange=o, purple=u, white=w, yellow=y
        if(vetor[i][19] == 'k'):
            vetor[i][19] = 0
        elif(vetor[i][19] == 'n'):
            vetor[i][19] = 1 / 8
        elif(vetor[i][19] == 'b'):
            vetor[i][19] = 2 / 8
        elif(vetor[i][19] == 'h'):
            vetor[i][19] = 3 / 8
        elif(vetor[i][19] == 'r'):
            vetor[i][19] = 4 / 8
        elif(vetor[i][19] == 'o'):
            vetor[i][19] = 5 / 8
        elif(vetor[i][19] == 'u'):
            vetor[i][19] = 6 / 8
        elif(vetor[i][19] == 'w'):
            vetor[i][19] = 7 / 8
        elif(vetor[i][19] == 'y'):
            vetor[i][19] = 8 / 8

        # 21. population: abundant=a, clustered=c, numerous=n, scattered=s, several=v, solitary=y
        if(vetor[i][20] == 'a'):
            vetor[i][20] = 0
        elif(vetor[i][20] == 'c'):
            vetor[i][20] = 1 / 5
        elif(vetor[i][20] == 'n'):
            vetor[i][20] = 2 / 5
        elif(vetor[i][20] == 's'):
            vetor[i][20] = 3 / 5
        elif(vetor[i][20] == 'v'):
            vetor[i][20] = 4 / 5
        elif(vetor[i][20] == 'y'):
            vetor[i][20] = 5 / 5

        # 22. habitat: grasses=g, leaves=l, meadows=m, paths=p, urban=u, waste=w, woods=d
        if(vetor[i][21] == 'g'):
            vetor[i][21] = 0
        elif(vetor[i][21] == 'l'):
            vetor[i][21] = 1 / 6
        elif(vetor[i][21] == 'm'):
            vetor[i][21] = 2 / 6
        elif(vetor[i][21] == 'p'):
            vetor[i][21] = 3 / 6
        elif(vetor[i][21] == 'u'):
            vetor[i][21] = 4 / 6
        elif(vetor[i][21] == 'w'):
            vetor[i][21] = 5 / 6
        elif(vetor[i][21] == 'd'):
            vetor[i][21] = 6 / 6

    return vetor

# Valores balanceados sem a variável 11
def converterX4(vetor):
    for i in range(len(vetor)):
        # 1. cap-shape: bell=b, conical=c, convex=x, flat=f, knobbed=k, sunken=s
        if(vetor[i][0] == 'b'):
            vetor[i][0] = 0
        elif(vetor[i][0] == 'c'):
            vetor[i][0] = 1 / 5
        elif(vetor[i][0] == 'x'):
            vetor[i][0] = 2 / 5
        elif(vetor[i][0] == 'f'):
            vetor[i][0] = 3 / 5
        elif(vetor[i][0] == 'k'):
            vetor[i][0] = 4 / 5
        elif(vetor[i][0] == 's'):
            vetor[i][0] = 5 / 5

        # 2. cap-surface: fibrous=f, grooves=g, scaly=y, smooth=s
        if(vetor[i][1] == 'f'):
            vetor[i][1] = 0
        elif(vetor[i][1] == 'g'):
            vetor[i][1] = 1 / 3
        elif(vetor[i][1] == 'y'):
            vetor[i][1] = 2 / 3
        elif(vetor[i][1] == 's'):
            vetor[i][1] = 3 / 3

        # 3. cap-color: brown=n, buff=b, cinnamon=c, gray=g, green=r, pink=p, purple=u, red=e, white=w, yellow=y
        if(vetor[i][2] == 'n'):
            vetor[i][2] = 0
        elif(vetor[i][2] == 'b'):
            vetor[i][2] = 1 / 9
        elif(vetor[i][2] == 'c'):
            vetor[i][2] = 2 / 9
        elif(vetor[i][2] == 'g'):
            vetor[i][2] = 3 / 9
        elif(vetor[i][2] == 'r'):
            vetor[i][2] = 4 / 9
        elif(vetor[i][2] == 'p'):
            vetor[i][2] = 5 / 9
        elif(vetor[i][2] == 'u'):
            vetor[i][2] = 6 / 9
        elif(vetor[i][2] == 'e'):
            vetor[i][2] = 7 / 9
        elif(vetor[i][2] == 'w'):
            vetor[i][2] = 8 / 9
        elif(vetor[i][2] == 'y'):
            vetor[i][2] = 9 / 9

        # 4. bruises?: bruises=t, no=f
        if(vetor[i][3] == 'f'):
            vetor[i][3] = 0
        elif(vetor[i][3] == 't'):
            vetor[i][3] = 1

        # 5. odor: almond=a, anise=l, creosote=c, fishy=y, foul=f, musty=m, none=n, pungent=p, spicy=s
        if(vetor[i][4] == 'a'):
            vetor[i][4] = 0
        elif(vetor[i][4] == 'l'):
            vetor[i][4] = 1 / 8
        elif(vetor[i][4] == 'c'):
            vetor[i][4] = 2 / 8
        elif(vetor[i][4] == 'y'):
            vetor[i][4] = 3 / 8
        elif(vetor[i][4] == 'f'):
            vetor[i][4] = 4 / 8
        elif(vetor[i][4] == 'm'):
            vetor[i][4] = 5 / 8
        elif(vetor[i][4] == 'n'):
            vetor[i][4] = 6 / 8
        elif(vetor[i][4] == 'p'):
            vetor[i][4] = 7 / 8
        elif(vetor[i][4] == 's'):
            vetor[i][4] = 8 / 8

        # 6. gill-attachment: attached=a, descending=d, free=f, notched=n
        if(vetor[i][5] == 'a'):
            vetor[i][5] = 0
        elif(vetor[i][5] == 'd'):
            vetor[i][5] = 1 / 3
        elif(vetor[i][5] == 'f'):
            vetor[i][5] = 2 / 3
        elif(vetor[i][5] == 'n'):
            vetor[i][5] = 3 / 3

        # 7. gill-spacing: close=c, crowded=w, distant=d
        if(vetor[i][6] == 'c'):
            vetor[i][6] = 0
        elif(vetor[i][6] == 'w'):
            vetor[i][6] = 1 / 2
        elif(vetor[i][6] == 'd'):
            vetor[i][6] = 2 / 2

        # 8. gill-size: broad=b, narrow=n
        if(vetor[i][7] == 'b'):
            vetor[i][7] = 0
        elif(vetor[i][7] == 'n'):
            vetor[i][7] = 1

        # 9. gill-color: black=k, brown=n, buff=b, chocolate=h, gray=g, green=r,
        # orange=o, pink=p, purple=u, red=e, white=w, yellow=y
        if(vetor[i][8] == 'k'):
            vetor[i][8] = 0
        elif(vetor[i][8] == 'n'):
            vetor[i][8] = 1 / 11
        elif(vetor[i][8] == 'b'):
            vetor[i][8] = 2 / 11
        elif(vetor[i][8] == 'h'):
            vetor[i][8] = 3 / 11
        elif(vetor[i][8] == 'g'):
            vetor[i][8] = 4 / 11
        elif(vetor[i][8] == 'r'):
            vetor[i][8] = 5 / 11
        elif(vetor[i][8] == 'o'):
            vetor[i][8] = 6 / 11
        elif(vetor[i][8] == 'p'):
            vetor[i][8] = 7 / 11
        elif(vetor[i][8] == 'u'):
            vetor[i][8] = 8 / 11
        elif(vetor[i][8] == 'e'):
            vetor[i][8] = 9 / 11
        elif(vetor[i][8] == 'w'):
            vetor[i][8] = 10 / 11
        elif(vetor[i][8] == 'y'):
            vetor[i][8] = 11 / 11

        # 10. stalk-shape: enlarging=e, tapering=t
        if(vetor[i][9] == 'e'):
            vetor[i][9] = 0
        elif(vetor[i][9] == 't'):
            vetor[i][9] = 1

        # 12. stalk-surface-above-ring: fibrous=f, scaly=y, silky=k, smooth=s
        if(vetor[i][10] == 'f'):
            vetor[i][10] = 0
        elif(vetor[i][10] == 'y'):
            vetor[i][10] = 1 / 3
        elif(vetor[i][10] == 'k'):
            vetor[i][10] = 2 / 3
        elif(vetor[i][10] == 's'):
            vetor[i][10] = 3 / 3

        # 13. stalk-surface-below-ring: fibrous=f, scaly=y, silky=k, smooth=s
        if(vetor[i][11] == 'f'):
            vetor[i][11] = 0
        elif(vetor[i][11] == 'y'):
            vetor[i][11] = 1 / 3
        elif(vetor[i][11] == 'k'):
            vetor[i][11] = 2 / 3
        elif(vetor[i][11] == 's'):
            vetor[i][11] = 3 / 3

        # 14. stalk-color-above-ring: brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y
        if(vetor[i][12] == 'n'):
            vetor[i][12] = 0
        elif(vetor[i][12] == 'b'):
            vetor[i][12] = 1 / 8
        elif(vetor[i][12] == 'c'):
            vetor[i][12] = 2 / 8
        elif(vetor[i][12] == 'g'):
            vetor[i][12] = 3 / 8
        elif(vetor[i][12] == 'o'):
            vetor[i][12] = 4 / 8
        elif(vetor[i][12] == 'p'):
            vetor[i][12] = 5 / 8
        elif(vetor[i][12] == 'e'):
            vetor[i][12] = 6 / 8
        elif(vetor[i][12] == 'w'):
            vetor[i][12] = 7 / 8
        elif(vetor[i][12] == 'y'):
            vetor[i][12] = 8 / 8

        # 15. stalk-color-below-ring: brown=n, buff=b, cinnamon=c, gray=g, orange=o, pink=p, red=e, white=w, yellow=y
        if(vetor[i][13] == 'n'):
            vetor[i][13] = 0
        elif(vetor[i][13] == 'b'):
            vetor[i][13] = 1 / 8
        elif(vetor[i][13] == 'c'):
            vetor[i][13] = 2 / 8
        elif(vetor[i][13] == 'g'):
            vetor[i][13] = 3 / 8
        elif(vetor[i][13] == 'o'):
            vetor[i][13] = 4 / 8
        elif(vetor[i][13] == 'p'):
            vetor[i][13] = 5 / 8
        elif(vetor[i][13] == 'e'):
            vetor[i][13] = 6 / 8
        elif(vetor[i][13] == 'w'):
            vetor[i][13] = 7 / 8
        elif(vetor[i][13] == 'y'):
            vetor[i][13] = 8 / 8

        # 16. veil-type: partial=p, universal=u
        if(vetor[i][14] == 'p'):
            vetor[i][14] = 0
        elif(vetor[i][14] == 'u'):
            vetor[i][14] = 1

        # 17. veil-color: brown=n, orange=o, white=w, yellow=y
        if(vetor[i][15] == 'n'):
            vetor[i][15] = 0
        elif(vetor[i][15] == 'o'):
            vetor[i][15] = 1 / 3
        elif(vetor[i][15] == 'w'):
            vetor[i][15] = 2 / 3
        elif(vetor[i][15] == 'y'):
            vetor[i][15] = 3 / 3

        # 18. ring-number: none=n, one=o, two=t
        if(vetor[i][16] == 'n'):
            vetor[i][16] = 0
        elif(vetor[i][16] == 'o'):
            vetor[i][16] = 1 / 2
        elif(vetor[i][16] == 't'):
            vetor[i][16] = 2 / 2

        # 19. ring-type: cobwebby=c, evanescent=e, flaring=f, large=l, none=n, pendant=p, sheathing=s, zone=z
        if(vetor[i][17] == 'c'):
            vetor[i][17] = 0 / 7
        elif(vetor[i][17] == 'e'):
            vetor[i][17] = 1 / 7
        elif(vetor[i][17] == 'f'):
            vetor[i][17] = 2 / 7
        elif(vetor[i][17] == 'l'):
            vetor[i][17] = 3 / 7
        elif(vetor[i][17] == 'n'):
            vetor[i][17] = 4 / 7
        elif(vetor[i][17] == 'p'):
            vetor[i][17] = 5 / 7
        elif(vetor[i][17] == 's'):
            vetor[i][17] = 6 / 7
        elif(vetor[i][17] == 'z'):
            vetor[i][17] = 7 / 7

        # 20. spore-print-color: black=k, brown=n, buff=b, chocolate=h, green=r, orange=o, purple=u, white=w, yellow=y
        if(vetor[i][18] == 'k'):
            vetor[i][18] = 0
        elif(vetor[i][18] == 'n'):
            vetor[i][18] = 1 / 8
        elif(vetor[i][18] == 'b'):
            vetor[i][18] = 2 / 8
        elif(vetor[i][18] == 'h'):
            vetor[i][18] = 3 / 8
        elif(vetor[i][18] == 'r'):
            vetor[i][18] = 4 / 8
        elif(vetor[i][18] == 'o'):
            vetor[i][18] = 5 / 8
        elif(vetor[i][18] == 'u'):
            vetor[i][18] = 6 / 8
        elif(vetor[i][18] == 'w'):
            vetor[i][18] = 7 / 8
        elif(vetor[i][18] == 'y'):
            vetor[i][18] = 8 / 8

        # 21. population: abundant=a, clustered=c, numerous=n, scattered=s, several=v, solitary=y
        if(vetor[i][19] == 'a'):
            vetor[i][19] = 0
        elif(vetor[i][19] == 'c'):
            vetor[i][19] = 1 / 5
        elif(vetor[i][19] == 'n'):
            vetor[i][19] = 2 / 5
        elif(vetor[i][19] == 's'):
            vetor[i][19] = 3 / 5
        elif(vetor[i][19] == 'v'):
            vetor[i][19] = 4 / 5
        elif(vetor[i][19] == 'y'):
            vetor[i][19] = 5 / 5

        # 22. habitat: grasses=g, leaves=l, meadows=m, paths=p, urban=u, waste=w, woods=d
        if(vetor[i][20] == 'g'):
            vetor[i][20] = 0
        elif(vetor[i][20] == 'l'):
            vetor[i][20] = 1 / 6
        elif(vetor[i][20] == 'm'):
            vetor[i][20] = 2 / 6
        elif(vetor[i][20] == 'p'):
            vetor[i][20] = 3 / 6
        elif(vetor[i][20] == 'u'):
            vetor[i][20] = 4 / 6
        elif(vetor[i][20] == 'w'):
            vetor[i][20] = 5 / 6
        elif(vetor[i][20] == 'd'):
            vetor[i][20] = 6 / 6

    return vetor
