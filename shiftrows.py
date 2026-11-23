
def shiftrows(texte):
    sortie=[[0 for k in range(4)] for l in range(4)]
    for k in range(4):
        for l in range(4-k):
            sortie[k][l]=texte[k][k+l]
        for l in range(4-k,4):
            sortie[k][l]=texte[k][l-4+k]
    return sortie

def inverse_shiftrows(texte):
    sortie=[[0 for k in range(4)] for l in range(4)]
    for k in range(4):
        for l in range(4-k):
            sortie[k][l+k]=texte[k][l]
        for l in range(4-k,4):
            sortie[k][l-4+k]=texte[k][l]
    return sortie