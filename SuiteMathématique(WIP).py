import re
import requests

"""
Somme des termes d'une suite arithmétique Un avec un 1er terme U0 et une diff d est donnée par :
Sn=(n/2)*(2*U0+(n-1)*d)

exemple :
Un+1 = [15+Un]+[n*d]
Un+1 = [15+Un]+[n*14]
U0 = 793

On veut trouver U818985 :
U818985 = 15+(818985/2)*(2*U0+(818985-1)*d)
"""

# "<html><body><link rel='stylesheet' property='stylesheet' id='s' type='text/css' href='/template/s.css' 
# media='all' /><iframe id='iframe' src='https://www.root-me.org/?page=externe_header'>
# </iframe>U<sub>n+1</sub> = [ 39 + U<sub>n</sub> ] + [ n * 41 ]<br />\nU<sub>0</sub> = 629\n<br />
# You must find U<sub>717446</sub><br /><br /> 

# Fonction pour extraire la valeur de U<sub>n</sub> à partir du code source HTML
def SommeSuiteArithmetique(html_content):
    try:
        # U0
        matchU0 = re.search(r'U<sub>0</sub>\s*=\s*(-?\d+)', html_content)
        if matchU0:
            U0 = matchU0.group(1)
            U0 = eval(U0) # Évaluer l'expression pour obtenir la valeur de U<sub>0</sub>\s*=\s*(-?\d+)

        # Un+1
        matchUnp1 = re.findall(r'\d+', html_content) 
        if matchUnp1:
            constante1 = matchUnp1[1]
            constante1 = eval(constante1) 
            d = matchUnp1[2]
            d = eval(d) 

        # U à trouver
        matchUrep = re.findall(r'U<sub>(\d+)<\/sub>', html_content) 
        if matchUrep:
            Urep = matchUrep[1]
            Urep = eval(Urep) 
            
        Solution = constante1+(Urep/2)*(2*U0+(Urep-1)*d)

        return Solution
    
    except ValueError:
        print("Impossible de trouver la valeur de U<sub>n</sub> dans le code source.")


# URL du challenge
url = "http://challenge01.root-me.org/programmation/ch1/"

# Récupération du contenu HTML
response = requests.get(url)
html_content = response.text

# Extraction de la solution
result = SommeSuiteArithmetique(html_content)
# result = str(result)

# URL de l'endpoint HTTP GET
url_endpoint = "http://challenge01.root-me.org/programmation/ch1/ep1_v.php"

# Ajout du résultat dans l'URL comme spécifié dans l'énoncé
url_with_result = f"{url_endpoint}?result={result}"

# Envoi de la requête GET
response_challenge = requests.get(url_with_result)

# Affichage de la réponse du serveur
print(response_challenge.text)