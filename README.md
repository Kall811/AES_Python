# AES_Python

Implémentation d'AES-128, AES-192 et AES-256 en Python, sans bibliothèque de cryptographie. Ce projet a été réalisée pour comprendre le fonctionnement interne de l'algorithme.

Ce projet permet : 
- Chiffrement et déchiffrement avec des clés de 128, 192 ou 256 bits
- Expansion de clé, SubBytes, ShiftRows, MixColumns, AddRoundKey
- Arithmétique dans le corps GF(2⁸), codée à la main
- Padding PKCS#7
- Résultats conformes aux vecteurs de test officiels FIPS-197 (annexe C)

Chiffrer :
    python main.py -option c -cle key.txt -texte text.txt -sortie chiffre.txt
Déchiffrer :
    python main.py -option d -cle key.txt -texte chiffre.txt -sortie clair.txt

- La clé est un fichier .txt de 16, 24 ou 32 caractères ASCII (pour AES-128, AES-192 ou AES-256).
- Sans -option, le programme chiffre. Sans -sortie, le nom du fichier est généré automatiquement.

Structure de code

- main.py : interface en ligne de commande
- AES_chiffrement.py / AES_dechiffrement.py : les tours d'AES
- expansion_cle.py : génération des clés de tour
- polynome_gf.py : multiplication dans GF(2⁸)
- (les autres fichiers correspondent chacun à une étape d'AES)

Projet pédagogique, à ne pas utiliser pour protéger de vraies données :

- Mode ECB : deux blocs identiques donnent le même chiffré
- Pas d'authentification : le chiffré peut être modifié sans être détecté (en pratique, on utilise AES-GCM)
- Clé lue comme du texte : moins aléatoire qu'une vraie clé binaire
- Padding non vérifié au déchiffrement
- Pas de protection contre les attaques par canaux auxiliaires

A implémenter plus tard :

- Mode CBC ou CTR
- Vérification stricte du padding
