dataHexa = "4C6520666C6167206465206365206368616C6C656E6765206573743A203261633337363438316165353436636436383964356239313237356433323465"

# Convertir la chaîne hexadécimale en bytes
dataBytes = bytes.fromhex(dataHexa)

# Décoder les bytes en ASCII
dataASCII = dataBytes.decode('ascii')

print(dataASCII)