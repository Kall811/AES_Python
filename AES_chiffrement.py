import conversion_bytes_matrice
import add_round_key
import subbytes
import mix_columns
import shiftrows
import transposition


def main(texte,C_etendue):
    T=conversion_bytes_matrice.conversion_texte_matrice(texte)
    T=transposition.transposition(T)
    R=len(C_etendue)-1

    S=add_round_key.main(T,C_etendue[0])

    for k in range(1,R):
        S=subbytes.subbytes(S)
        S=shiftrows.shiftrows(S)
        S=mix_columns.mixcolumns(S)
        S=add_round_key.main(S,C_etendue[k])
    
    S=subbytes.subbytes(S)
    S=shiftrows.shiftrows(S)
    S=add_round_key.main(S,C_etendue[R])
    S=transposition.transposition(S)

    sortie=conversion_bytes_matrice.conversion_matrice_texte(S)

    return sortie
