import base64

chaineADecoder = "aHR0cHM6Ly90ZXh0YmVsdC5jb20vdGV4dA==" # string encodé en base 64
chaine_dechiffree = base64.b64decode(chaineADecoder).decode('utf-8') # string décodé en ut8
print("Chaine chiffrée :", chaineADecoder)
print("Chaine déchiffrée :", chaine_dechiffree)





# # message = base64.b64decode('aHR0cHM6Ly90ZXh0YmVsdC5jb20vdGV4dA=='.encode('ascii')).decode('ascii')
# chaineADecoderASCII = chaineADecoder.encode('ascii')

# etape1 = base64.b64decode(chaineADecoder) # Pareil que : base64.b64decode(chaineADecoder.encode('ascii'))
# etape2 = etape1.decode('ascii')

# try:
#     chaine_dechiffree = base64.b64decode(chaineADecoder).decode('utf-8')
#     print("Chaine chiffrée :", chaineADecoder)
#     print("Chaine déchiffrée :", chaine_dechiffree)
#     # print("Message :", message)

# except:
#     print("Erreur lors du déchiffrage.")