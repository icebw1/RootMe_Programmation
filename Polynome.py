import socket
import re


def ConvertToInt(value):
    if value[0] == '-':
        return -int(value[1:].replace(" ", ""))
    elif value[0] == '+':
        return int(value[1:].replace(" ", ""))
    else:
        return int(value)
    
    
def Polynome(derniersElements):
    derniersElements = [value.replace('.', '') for value in derniersElements]
    derniersElements = [value.replace(' ', '') for value in derniersElements]
    convertedValues = [ConvertToInt(value) for value in derniersElements]

    A = int(convertedValues[0]) 
    B = int(convertedValues[1]) 
    C = int(convertedValues[2]) 
    D = int(convertedValues[3]) 

    C = C - D
    Delta = (B**2) - (4*A*C)

    if Delta == 0:
        x = -B/(2*A)
        x = str(round(x, 3))
        solution = "x: " + x
        clientSocket.send((solution+"\n").encode('utf8'))
        donneesRecues = clientSocket.recv(1024).decode('utf8')
        print(f"Delta: {Delta}")
        print(f"Reçu: {donneesRecues}\n")

    elif Delta > 0:
        x1 = (-B-(Delta**0.5))/(2*A)
        x1 = str(round(x1, 3))
        x2 = (-B+(Delta**0.5))/(2*A)
        x2 = str(round(x2, 3))
        solution = "x1: " + x1 + " ; " + "x2: " + x2
        clientSocket.send((solution+"\n").encode('utf8'))
        donneesRecues = clientSocket.recv(1024).decode('utf8')
        print(f"Delta: {Delta}")
        print(f"Reçu: {donneesRecues}\n")

    elif Delta < 0:
        solution = "Not possible"
        clientSocket.send((solution+"\n").encode('utf8'))
        donneesRecues = clientSocket.recv(1024).decode('utf8')
        print(f"Delta: {Delta}")
        print(f"Reçu: {donneesRecues}\n")

    return donneesRecues

# Adresse et port du serveur
host = "challenge01.root-me.org"
port = 52018

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Créer un objet socket
clientSocket.connect((host, port)) 
print("Connecté au serveur")

donneesRecues = clientSocket.recv(1024).decode('utf8') # Recevoir des données
print(f"Reçu: {donneesRecues}\n")
match = re.findall(r'([+-]?\s?\d+\.?\d*)', donneesRecues) 
derniersElements = match[-4:] # 4 dernières valeurs 
donneesRecues = Polynome(derniersElements)

try:
    while 'flag' not in donneesRecues:
        if 'Wrong answer' in donneesRecues:
            clientSocket.close()
            exit()
        elif 'too slow !' in donneesRecues:
            print("Too slow")
            clientSocket.close()
            exit()            
        match = re.findall(r'([+-]?\s?\d+\.?\d*)', donneesRecues) 
        derniersElements = match[-4:]
        donneesRecues = Polynome(derniersElements) 

    if 'flag' in donneesRecues:
        print(donneesRecues + "\n")
        clientSocket.close()
        exit()

except Exception as e:
    print(f"Erreur: {e}")

finally:
    # Fermer la connexion
    clientSocket.close()
    print("Connexion fermée.\n")