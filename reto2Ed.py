palabrafrase = input("escribe una palabra o una frase:")

buentexto = ''.join(c.lower() for c in palabrafrase if c.isalnum())
if buentexto == buentexto[::-1]:
    print("es un palindromo")
else:
    print("no es un palindromo")
