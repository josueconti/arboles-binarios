class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


def insertar(raiz, valor):
    """Inserta un valor en el árbol binario de búsqueda."""
    if raiz is None:
        return Nodo(valor)

    if valor < raiz.valor:
        raiz.izq = insertar(raiz.izq, valor)
    elif valor > raiz.valor:
        raiz.der = insertar(raiz.der, valor)

    return raiz


def buscar(raiz, valor):
    """Busca un valor en el ABB. Devuelve True o False."""
    if raiz is None:
        return False

    if valor == raiz.valor:
        return True
    elif valor < raiz.valor:
        return buscar(raiz.izq, valor)
    else:
        return buscar(raiz.der, valor)


def inorden(raiz):
    """Recorrido inorden: izquierda, raíz, derecha."""
    if raiz is None:
        return

    inorden(raiz.izq)
    print(raiz.valor, end=" ")
    inorden(raiz.der)


def preorden(raiz):
    "implementar recorrido preorden (raíz, izquierda, derecha)."



def postorden(raiz):
    "implementar recorrido postorden (izquierda, derecha, raíz)."



if __name__ == "__main__":
    # Árbol de ejemplo ya construido
    valores = [40, 20, 60, 10, 30, 50, 70]
    raiz = None
    for v in valores:
        raiz = insertar(raiz, v)

    while True:
        print("\n--- Menú Árbol Binario de Búsqueda ---")
        print("1. Mostrar recorrido inorden")
        print("2. Buscar un valor en el árbol")
        print("3. Mostrar recorrido preorden  (cuando lo implementes)")
        print("4. Mostrar recorrido postorden (cuando lo implementes)")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("Recorrido inorden:")
            inorden(raiz)
            print()

        elif opcion == "2":
            try:
                x = int(input("Ingresa el valor a buscar: "))
                if buscar(raiz, x):
                    print(f"El valor {x} SÍ está en el árbol.")
                else:
                    print(f"El valor {x} NO está en el árbol.")
            except ValueError:
                print("Por favor ingresa un número entero.")

        elif opcion == "3":
            print("Recorrido preorden:")
            preorden(raiz)
            print(" esta opción funcionará cuando implementes preorden")

        elif opcion == "4":
            print("Recorrido postorden:")
            postorden(raiz)
            print(" esta opción funcionará cuando implementes postorden")

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")