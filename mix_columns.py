import polynome_gf

def main(texte,M):
    sortie=[[0 for _ in range(4)] for _ in range(4)]
    for k in range(4):
        for l in range(4):
            for i in range(4):
                sortie[l][k] ^= polynome_gf.produit_gf(M[l][i],texte[i][k])
    return sortie

def mixcolumns(texte):
    M=[[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
    return main(texte,M)

def mixcolumns_inv(texte):
    M_inv=[[0x0E,0x0B,0x0D,0x09],[0x09,0x0E,0x0B,0x0D],[0x0D,0X09,0X0E,0x0B],[0x0B,0x0D,0x09,0x0E]]
    return main(texte,M_inv)
