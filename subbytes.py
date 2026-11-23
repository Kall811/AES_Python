import Sbox

def subbytes(texte):
    return [[Sbox.sbox(texte[l][k]) for k in range(4)] for l in range(4)]

def inverse_subbytes(texte):
    return [[Sbox.sbox_inverse(texte[l][k]) for k in range(4)] for l in range(4)]