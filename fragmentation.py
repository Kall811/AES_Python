import pkcs

def main(texte,n=16, padding=True):
    if padding:
        texte=pkcs.padding(texte)
    return [texte[k*n:(k+1)*n] for k in range(len(texte)//n)]