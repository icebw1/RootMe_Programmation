import socket
import re
import base64
import zlib

# Paramètres de connexion
hote = "challenge01.root-me.org"
port = 52022

# Résolution DNS pour obtenir l'adresse IP
adresseIp = socket.gethostbyname(hote)

# Création du socket et connexion à l'adresse IP et au port
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((adresseIp, port))

# Réception de données
donnees_recues = clientSocket.recv(1024).decode('utf-8')
print(donnees_recues + "\n")

# Chaîne de texte contenant la chaîne chiffrée
chaineChiffree_match = re.search(r"'([^']+)'", donnees_recues)

data = chaineChiffree_match.group(1)
chaineBytes = data.encode('utf-8') # Encoder la chaîne en bytes (UTF-8 est un encodage couramment utilisé)
chaineDechiffree = base64.b64decode(chaineBytes) # Dechiffrer la chaine
donneesDecompressee = zlib.decompress(chaineDechiffree) # Decompresser la chaîne
solutionString = str(donneesDecompressee)
solution_match = re.search(r"'([^']+)'", solutionString)
solutionData = solution_match.group(1)

try:
    clientSocket.send((solutionData+"\n").encode("utf-8"))
    donnees_recues = clientSocket.recv(1024).decode('utf-8')

    while '[+] Good job ! Here is your flag' not in donnees_recues:
        if donnees_recues == '[!] Wrong answer! You lost ^-^\n':
            print(donnees_recues)
        chaineChiffree_match = re.search(r"'([^']+)'", donnees_recues)
        data = chaineChiffree_match.group(1)
        chaineBytes = data.encode('utf-8') # Encoder la chaîne en bytes (UTF-8 est un encodage couramment utilisé)
        chaineDechiffree = base64.b64decode(chaineBytes) # Dechiffrer la chaine
        donneesDecompressee = zlib.decompress(chaineDechiffree) # Decompresser la chaîne
        solutionString = str(donneesDecompressee)
        solution_match = re.search(r"'([^']+)'", solutionString)
        solutionData = solution_match.group(1)

        clientSocket.send((solutionData+"\n").encode("utf-8"))
        donnees_recues = clientSocket.recv(1024).decode('utf-8')
    
    if '[+] Good job ! Here is your flag' in donnees_recues:
        print(donnees_recues + "\n")

    clientSocket.close()


except:
    print("Except\n")
    clientSocket.close()