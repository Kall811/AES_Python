

def main(texte,cle):
    return [[texte[k][l]^cle[k][l] for l in range(4)] for k in range(4)]