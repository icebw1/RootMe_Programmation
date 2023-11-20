import socket
import re

def dechiffrer_rot13(chaine):
    resultat = ''
    for caractere in chaine:
        if 'a' <= caractere <= 'z':
            decalage = ord(caractere) - ord('a')
            decalage = (decalage + 13) % 26
            resultat += chr(ord('a') + decalage)
        elif 'A' <= caractere <= 'Z':
            decalage = ord(caractere) - ord('A')
            decalage = (decalage + 13) % 26
            resultat += chr(ord('A') + decalage)
        else:
            resultat += caractere
    return resultat

# Paramètres de connexion
hote = "challenge01.root-me.org"
port = 52021

# Résolution DNS pour obtenir l'adresse IP
adresseIp = socket.gethostbyname(hote)

# Création du socket et connexion à l'adresse IP et au port
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((adresseIp, port))

# Réception de données
donnees_recues = clientSocket.recv(1024).decode('utf-8')
print("Réponse du serveur:", donnees_recues)

# Utilisation d'une expression régulière pour extraire la chaîne chiffrée
chaine_chiffree_match = re.search(r"'([^']+)'", donnees_recues)

if chaine_chiffree_match:
    chaine_chiffree = chaine_chiffree_match.group(1)
    chaine_dechiffree = dechiffrer_rot13(chaine_chiffree)
    print("Chaine chiffrée :", chaine_chiffree)
    print("Chaine déchiffrée :", chaine_dechiffree)
    clientSocket.send((str(chaine_dechiffree)+"\n").encode("utf-8"))
else:
    print("Aucune chaîne chiffrée trouvée dans la réponse du serveur.")

try:
    donnees_recues2 = clientSocket.recv(1024).decode('utf-8')
    print(donnees_recues2)
except:
    print("Pas de nouvelles donnes recues")
    
# Fermeture de la connexion
clientSocket.close()