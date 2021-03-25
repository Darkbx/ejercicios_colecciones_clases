print("Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro,"
      " en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.")

def superpocision():
    ListaA = ["Mamerto", "Pirulo", "Papolo", "Carlito"]
    ListaB = ["Carlota", "Petronila", "Carlito", "Papo Luca"]
    cont = 0

    for C in ListaA:
        for D in ListaB:
            if C == D:
                cont +=1
    if cont >= 1:
        print(True)
    else:
        print(False)

superpocision()