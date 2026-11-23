import Sbox

import fragmentation

def rotword(ligne):
    return [ligne[1],ligne[2],ligne[3],ligne[0]]

def subword(ligne):
    return [Sbox.sbox(element) for element in ligne]

def xor_ligne(a,b):
    return [a[k]^b[k] for k in range(4)]

Rcon = ( 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a )

def rcon(k):
    return [Rcon[k],0,0,0]


def transposition(cle):
    n=len(cle)
    return [[cle[k][l] for k in range(n)] for l in range(n)]

def main(cle_base):
    N=len(cle_base)
    cle=cle_base
    if N==4:
        R=11
    elif N==6:
        R=13
    else:
        R=15
    cle_etendue=[[]]*4*R

    for i in range(4*R):
        if i<N:
            cle_etendue[i]=cle[i]
        else:
            if i%N==0:
                cle_etendue[i]=xor_ligne(xor_ligne(cle_etendue[i-N],subword(rotword(cle_etendue[i-1]))),rcon(i//N))
            else:
                if N>6 and i%N==4:
                    cle_etendue[i]=xor_ligne(cle_etendue[i-N],subword(cle_etendue[i-1]))
                else:
                    cle_etendue[i]=xor_ligne(cle_etendue[i-N],cle_etendue[i-1])
    
    sortie=[[]]*R
    for k in range(R):
        a=4*k
        sortie[k]=transposition([cle_etendue[a],cle_etendue[a+1],cle_etendue[a+2],cle_etendue[a+3]])

    return sortie