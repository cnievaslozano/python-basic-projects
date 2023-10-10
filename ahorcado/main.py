import random
import string

from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual
from unidecode import unidecode


def obtener_palabra_valida(lista_palabras):
    # Seleccionar al azar palabra
    palabra = random.choice(lista_palabras)

    return palabra.upper()


def ahoracado():
    print("""
    ==============================================================
                        AHORCADO GAME!!!
    ==============================================================
    """)

    palabra = obtener_palabra_valida(palabras)

    # convertimos la palabra en un conjunto
    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)
    # Agregar la letra "Ñ" al conjunto
    abecedario.add("Ñ")

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        # Mostrar el estado actual de la bapalbra
        palabra_lista = []

        for letra in palabra:
            if letra in letras_adivinadas:
                palabra_lista.append(letra)
            else:
                palabra_lista.append('-')

        # Mosatrar estado ahorcado
        print(vidas_diccionario_visual[vidas])
        #Mostgrar las letras
        print(f"Palabra: {''.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()

        # Si la letrra escogida por el usuario esta en el abecedario y no esta en el conjunto
        # de letras que ya se han ingresado, se añade la letra al conjunto de letreas ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)

            # esta en la palabra?
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print("")
            else:
                print("Perdiste 1 vida")
                print(f"Tu letra {letra_usuario} no esta en la palbra ")
                vidas -= 1
        #la letra escogida ya fue ingresada
        elif letra_usuario in letras_adivinadas:
            print("ya escogiste esa letra, porfavor escoge una letra nueva")
        else:
            print("esta letra no es válida")


    # FIN JUEGO
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Ahorcado!!! La palbra era: {palabra} ")

    else:
        print(f"Perfecto!!  Ganaste, adivinaste la palbra {palabra}")

ahoracado()
