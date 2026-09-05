import csv
from src.config import TEMA
from src.tads.lista_enlazada import ListaEnlazada
from src.dominio.pokemon import Pokemon

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def cargar_pokedex(ruta_csv):
    pokedex = ListaEnlazada()
    with open(ruta_csv, encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            tipo2 = fila["tipo2"] if fila["tipo2"] not in ("", "null", "<null>") else None
            pokemon = Pokemon(
                int(fila["id"]),
                fila["nombre"],
                fila["tipo1"],
                tipo2,
                int(fila["hp"]),
                int(fila["ataque"]),
                int(fila["defensa"]),
                int(fila["velocidad"]),
                int(fila["generacion"])
            )
            pokedex.insertar_al_final(pokemon)
    return pokedex


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    pokedex = cargar_pokedex("data/pokedex.csv")

    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()
        if opcion == "0":
            print("Chau.")
        elif opcion == "1":
            for pokemon in pokedex:
                print(pokemon)
        elif opcion in {"2", "3", "4", "5", "6", "7", "8", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
