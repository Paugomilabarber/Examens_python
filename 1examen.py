import random

# 1
def llegir_llista_enters():
    l = []
    while True:
        entrada = input("Introdueix un número (o '.' per acabar): ")
        if entrada == '.':
            break
        try:
            l.append(int(entrada))
        except ValueError:
            print("Si us plau, introdueix un número enter vàlid.")
    return l

# 2
def senar_llista():
    llista = llegir_llista_enters()
    return [num for num in llista if num % 2 != 0]

# 3
def parell_llista():
    llista = llegir_llista_enters()
    return [num for num in llista if num % 2 == 0]

def sumar_parells_llista():
    llista = parell_llista()
    return sum(llista)

#4 
def llegir_llista_paraules():
    llista = []
    while True:
        entrada = input("Introdueix una paraula (o '.' per acabar): ")
        if entrada == '.':
            break
        llista.append(entrada)
    return llista

# 5
def crear_paraula_llista(llista):
    return ''.join(paraula[0] for paraula in llista)

# 6
def crear_llista_num_aleatoris():
    return [random.randint(0, 100) for _ in range(5)]

# 7
def comparar_llistes(llista1, llista2):
    resultat = []
    for i in range(len(llista2)):
        if llista2[i] not in llista1:
            resultat.append(0)
        elif llista2[i] == llista1[i]:
            resultat.append(2)
        else:
            resultat.append(1)
    return resultat

# 8
def majors_edat(edat1, edat2):
    if edat1 >= 18 and edat2 >= 18:
        resultat = "Totes dues persones són majors d'edat."
    elif edat1 < 18 and edat2 < 18:
        resultat = "Totes dues persones són menors d'edat."
    elif edat1 >= 18 and edat2 < 18:
        resultat = "La persona de {} anys és major d'edat i la persona de {} és menor d'edat.".format(edat1,edat2)
    elif edat1 < 18 and edat2 >= 18:
        resultat = "La persona de {} anys és major d'edat i la persona de {} és menor d'edat.".format(edat2,edat1,)
    return resultat

# 9. Funció per cercar un número dins una llista
def cercar_numero_llista(llista, numero):
    if numero in llista:
        return llista.index(numero)
    return -1

# 10. Menú per seleccionar una opció i cridar les funcions anteriors
def menu():
    print("Selecciona una opció:")
    print("1. Llegir llista d'enters")
    print("2. Senars de la llista")
    print("3. Sumar parells de la llista")
    print("4. Cercar número en la llista")
    print("5. Llegir llista de paraules")
    print("6. Crear paraula de la llista")
    print("7. Crear llista de números aleatoris")
    print("8. Comparar llistes")
    print("9. Majors d'edat")
    print("0. Sortir")
    return int(input("Escull una opció: "))

# Programa principal utilitzant `match case`
def programa_principal():
    while True:
        opcio = menu()
        match opcio:
            case 1:
                llista_enters = llegir_llista_enters()
                print("Llista llegida: {}".format(llista_enters))
            case 2:
                llista_senars = senar_llista()
                print("Senars de la llista: {}".format(llista_senars))
            case 3:
                suma_parells = sumar_parells_llista()
                print("Suma de parells de la llista: {}".format(suma_parells))
            case 4:
                llista_enters = llegir_llista_enters()
                numero = int(input("Introdueix un número per cercar: "))
                posicio = cercar_numero_llista(llista_enters, numero)
                print("Posició del número {}: {}".format(numero, posicio))
            case 5:
                llista_paraules = llegir_llista_paraules()
                print("Llista llegida: {}".format(llista_paraules))
            case 6:
                llista_paraules = llegir_llista_paraules()
                paraula = crear_paraula_llista(llista_paraules)
                print("Paraula creada: {}".format(paraula))
            case 7:
                llista_aleatoris = crear_llista_num_aleatoris()
                print("Llista de números aleatoris: {}".format(llista_aleatoris))
            case 8:
                llista1 = crear_llista_num_aleatoris()
                llista2 = crear_llista_num_aleatoris()
                comparacio = comparar_llistes(llista1, llista2)
                print("Comparació de les llistes:\nLlista 1: {}\nLlista 2: {}\nResultat: {}".format(llista1, llista2, comparacio))
            case 9:
                edat1 = int(input("Introdueix la primera edat: "))
                edat2 = int(input("Introdueix la segona edat: "))
                resultat = majors_edat(edat1, edat2)
                print("Resultat: {}".format(resultat))
            case 0:
                print("Sortint...")
                break
            case _:
                print("Opció no vàlida. Si us plau, torna a intentar-ho.")

# Executar el programa principal
programa_principal()