import argparse
import fragmentation
import AES_chiffrement 
import AES_dechiffrement 
import expansion_cle
import conversion_bytes_matrice
import pkcs

def format_texte(nom):
    n=len(nom)
    if n>=5:
        queue=nom[n-4:n]
        if queue==".txt":
            return True
    return False
    
def lecture_fichier(fichier):
    with open(fichier,"r",encoding="utf-8") as f:
        contenu=f.read()
    
    return contenu

def lecture_fichier_binaire(fichier):
    with open(fichier,"rb") as f:
        contenu=f.read()
    
    return contenu

def ecriture_fichier_binaire(fichier,texte):
    with open(fichier,"wb") as f:
        f.write(texte)

def ecriture_fichier(fichier,texte):
    with open(fichier,"w",encoding="utf-8") as f:
        f.write(texte)

if __name__=='__main__':
    
    parser = argparse.ArgumentParser()

    parser.add_argument("-option",help="Choisir entre chiffrement et dechiffrement",type=str)
    parser.add_argument("-cle",help="Clé servant au chiffrement et au déchiffrement",type=str,required=True)
    parser.add_argument("-texte",help="Texte modifié par AES",required=True)
    parser.add_argument("-sortie",help="Nom du fichier contenant le résultat de l'opération")

    args = parser.parse_args()

    print("Verification des arguments...")

    if args.option==None:
        #On chiffre si ce n'est pas précisé
        args.option="chiffrement"

    if args.sortie==None:
        args.sortie = "sortie_AES_"+args.option+".txt"

    if not (format_texte(args.texte) and format_texte(args.cle) and format_texte(args.sortie)):
        exit("Mauvais format des fichiers txt sont attendus pour les arguments cle, sortie et texte")

    if args.option not in ["chiffrement","dechiffrement","c","d"]:
        exit("L'argument option doit prendre les valeurs suivantes : chiffrement (ou c), dechiffrement (ou d)")

    print("Verification réussi.")

    option=args.option

    print("Lecture du fichier clé...")


    cle=bytes(lecture_fichier(args.cle),"utf-8")
    print("Lecture du fichier clé réussi")

    sortie_fichier=args.sortie

    if len(cle) not in [16,24,32]:
        exit("Clé de mauvaise taille (taille attendue : 128, 192 ou 256 bits)")

    print("Lancement d'AES")

    #Utilisation d'AES

    print("Expansion de la clé..")

    C=conversion_bytes_matrice.conversion_texte_matrice(cle)
    C_etendue = expansion_cle.main(C)

    print("Expansion de clé réussie")

    resultat=bytes([])

    if option=="c" or option=="chiffrement":
        print("Lancement du chiffrement")

        print("Lecture du texte à chiffrer...")
        texte=lecture_fichier(args.texte)
        print("Lecture du texte à chiffrer réussie")
        texte=bytes(texte,"utf-8")
        fragments=fragmentation.main(texte)
        for fragment in fragments:
            resultat+=AES_chiffrement.main(fragment,C_etendue)

        print("Ecriture du texte chiffré...")
        ecriture_fichier_binaire(sortie_fichier,resultat)
        print("Ecriture du texte chiffré réussie")


    else:
        print("Lancement du dechiffrement")

        print("Lecture du fichier à dechiffrer...")
        texte=lecture_fichier_binaire(args.texte)
        print("Lecture du fichier à déchiffrer réussie")
        fragments=fragmentation.main(texte,padding=False)
        for fragment in fragments:
            resultat+=AES_dechiffrement.main(fragment,C_etendue)
        resultat=pkcs.unpadding(resultat)
        resultat=bytes.decode(resultat,"utf-8")

        print("Ecriture du texte dechiffré...")
        ecriture_fichier(sortie_fichier,resultat)
        print("Ecriture du texte dechiffré réussie")
