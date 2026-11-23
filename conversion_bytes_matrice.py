
def conversion_texte_matrice(b):
    N=len(b)//4
    return [[b[4*k+l] for l in range(4)] for k in range(N)]

def conversion_matrice_texte(M,option="c"):
    x=sum(M,[])
    b=bytes(x)
    return b
    




