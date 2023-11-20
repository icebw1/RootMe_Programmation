import socket
import re
import base64

# Paramètres de connexion
hote = "challenge01.root-me.org"
port = 52023

# Résolution DNS pour obtenir l'adresse IP
adresseIp = socket.gethostbyname(hote)

# Création du socket et connexion à l'adresse IP et au port
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((adresseIp, port))

# Réception de données
donnees_recues = clientSocket.recv(1024).decode('utf-8')
print("Réponse du serveur:", donnees_recues)

# Chaîne de texte contenant la chaîne chiffrée
chaine_chiffree_match = re.search(r"'([^']+)'", donnees_recues)

try:
    chaine_chiffree = chaine_chiffree_match.group(1)
    chaine_dechiffree = base64.b64decode(chaine_chiffree).decode('utf-8')
    print("Chaine chiffrée :", chaine_chiffree)
    print("Chaine déchiffrée :", chaine_dechiffree)
    clientSocket.send((chaine_dechiffree+"\n").encode("utf-8"))

except:
    print("Aucune chaîne chiffrée trouvée dans la réponse du serveur.")

try:
    donnees_recues2 = clientSocket.recv(1024).decode('utf-8')
    print(donnees_recues2)
except:
    print("Pas de nouvelles donnes recues")
    
# Fermeture de la connexion
clientSocket.close()



"""
- AES (Advanced Encryption Standard) : 
L'AES est un algorithme de chiffrement symétrique couramment utilisé pour protéger les données. Il est largement utilisé pour le chiffrement des données sensibles.

- RSA (Rivest–Shamir–Adleman) : 
L'algorithme RSA est un algorithme de chiffrement asymétrique qui est souvent utilisé pour établir des connexions sécurisées et pour la cryptographie à clé publique.

- MD5 (Message Digest Algorithm 5) : 
MD5 est un algorithme de hachage qui génère une empreinte numérique d'une longueur fixe à partir de données d'entrée. Il est souvent utilisé pour vérifier l'intégrité 
des données.

- SHA (Secure Hash Algorithm) : 
Les différentes variantes de l'algorithme SHA (comme SHA-256, SHA-512, etc.) sont couramment utilisées pour générer des hachages sécurisés de données.

- DES (Data Encryption Standard) : 
Bien que désormais considéré comme obsolète en raison de sa faible sécurité, le DES est un algorithme de chiffrement symétrique largement utilisé par le passé.

- HMAC (Hash-based Message Authentication Code) : 
HMAC est une technique de vérification de l'intégrité et d'authentification basée sur des fonctions de hachage cryptographiques.

- Base32 et Base16 : 
Ces méthodes de codage sont similaires à Base64, mais utilisent un alphabet plus petit pour représenter les données. Base32 est souvent utilisé dans les codes QR, 
par exemple.

- XOR (Bitwise XOR) : 
XOR (ou exclusif) est une opération de chiffrement simple qui peut être utilisée pour masquer ou chiffrer des données.

- Vigenère Cipher : 
Le chiffre de Vigenère est un chiffrement par substitution polyalphabétique historique.

- ROT13 (Rotation by 13 places) : 
ROT13 est une forme de chiffrement de substitution par décalage couramment utilisée pour obscurcir du texte.

"""