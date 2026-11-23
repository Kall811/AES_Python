import conversion_bytes_matrice
import add_round_key
import subbytes
import mix_columns
import shiftrows
import copy
import transposition


def main(texte,C_etendue_arg):
    T=conversion_bytes_matrice.conversion_texte_matrice(texte)
    T=transposition.transposition(T)
    C_etendue=copy.deepcopy(C_etendue_arg)
    C_etendue.reverse()
    R=len(C_etendue)-1

    S=add_round_key.main(T,C_etendue[0])

    for k in range(1,R):
        S=shiftrows.inverse_shiftrows(S)
        S=subbytes.inverse_subbytes(S)
        S=add_round_key.main(S,C_etendue[k])
        S=mix_columns.mixcolumns_inv(S)
    
    S=shiftrows.inverse_shiftrows(S)
    S=subbytes.inverse_subbytes(S)
    S=add_round_key.main(S,C_etendue[R])
    S=transposition.transposition(S)

    sortie=conversion_bytes_matrice.conversion_matrice_texte(S)

    return sortie
