import socket
import re

# Paramètres de connexion
hote = "challenge01.root-me.org"
port = 52002

# Résolution DNS pour obtenir l'adresse IP
adresseIp = socket.gethostbyname(hote)

# Création du socket et connexion à l'adresse IP et au port
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((adresseIp, port))

# Réception de données
donnees_recues = clientSocket.recv(1024).decode('utf-8')
print("Réponse du serveur:", donnees_recues)

# Utilisez une expression régulière pour extraire le calcul
calcul_match = re.search(r'Calculate the square root of (\d+) and multiply by (\d+)', donnees_recues)

if calcul_match:
    nombre1 = int(calcul_match.group(1))
    nombre2 = int(calcul_match.group(2))

    # Effectuez le calcul
    racineCareeNombre = nombre1 ** 0.5
    resultat = round((racineCareeNombre * nombre2), 2)
    resultatToSend = str(resultat)+"\n"
    clientSocket.send((resultatToSend).encode("utf-8"))

    print("\n####################################################################")
    print("\nRoot of " + str(nombre1) + " multiply by " + str(nombre2) + " = " + str(resultat) + "\n")

else:
    print("Le serveur n'a pas renvoyé de calcul attendu.")

try:
    donnees_recues2 = clientSocket.recv(1024).decode('utf-8')
    print(donnees_recues2)
except:
    print("Pas de nouvelles donnes recues")
    
# Fermeture de la connexion
clientSocket.close()