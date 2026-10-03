from src.config import TEMA
from src.dominio.pokemon import cargar_pokedex
from src.dominio.evoluciones import cargar_evoluciones, cadena_evolutiva
from src.dominio.equipo import Equipo
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def buscar_por_nombre(pokedex, nombre):
    for p in pokedex:
        if p.nombre.lower() == nombre.lower():
            return p
    return None


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


def menu_equipo(equipo, pokedex):
    print()
    print("--- Equipo ---")
    print("1. Agregar Pokémon al equipo")
    print("2. Listar equipo")
    print("0. Volver")
    opcion = input("> ").strip()
    if opcion == "1":
        nombre = input("Nombre del Pokémon: ").strip()
        encontrado = buscar_por_nombre(pokedex, nombre)
        if encontrado is None:
            print("No se encontró ese Pokémon en la Pokédex.")
            return
        try:
            equipo.agregar(encontrado)
            print(f"{encontrado.nombre} agregado al equipo.")
        except ColeccionLlenaError as e:
            print(f"Error: {e}")
    elif opcion == "2":
        equipo.listar()


def menu_historial(historial):
    print()
    print("--- Historial (Pila) ---")
    print("1. Agregar visita")
    print("2. Deshacer (desapilar)")
    print("3. Ver última visita (ver_tope)")
    print("0. Volver")
    opcion = input("> ").strip()
    if opcion == "1":
        nombre = input("Nombre del Pokémon visitado: ").strip()
        historial.apilar(nombre)
        print(f"{nombre} agregado al historial.")
    elif opcion == "2":
        try:
            deshecho = historial.desapilar()
            print(f"Deshecho: {deshecho}")
        except PilaVaciaError as e:
            print(f"Error: {e}")
    elif opcion == "3":
        try:
            print(f"Última visita: {historial.ver_tope()}")
        except PilaVaciaError as e:
            print(f"Error: {e}")


def menu_cola(turnos):
    print()
    print("--- Cola de turnos ---")
    print("1. Encolar Pokémon")
    print("2. Atender siguiente (desencolar)")
    print("3. Ver próximo (ver_frente)")
    print("0. Volver")
    opcion = input("> ").strip()
    if opcion == "1":
        nombre = input("Nombre del Pokémon: ").strip()
        turnos.encolar(nombre)
        print(f"{nombre} encolado.")
    elif opcion == "2":
        try:
            atendido = turnos.desencolar()
            print(f"Turno atendido: {atendido}")
        except ColaVaciaError as e:
            print(f"Error: {e}")
    elif opcion == "3":
        try:
            print(f"Próximo: {turnos.ver_frente()}")
        except ColaVaciaError as e:
            print(f"Error: {e}")


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    pokedex = cargar_pokedex("data/pokedex.csv")
    mapa_evoluciones = cargar_evoluciones("data/evoluciones.csv")
    equipo = Equipo()
    historial = Pila()
    turnos = Cola()

    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()
        if opcion == "0":
            print("Chau.")
        elif opcion == "1":
            for pokemon in pokedex:
                print(pokemon)
        elif opcion == "5":
            id_texto = input("ID del Pokémon: ").strip()
            if id_texto.isdigit():
                cadena = cadena_evolutiva(int(id_texto), mapa_evoluciones)
                print(" -> ".join(str(i) for i in cadena))
            else:
                print("Ingresá un número válido.")
        elif opcion == "6":
            menu_equipo(equipo, pokedex)
        elif opcion == "7":
            menu_historial(historial)
        elif opcion == "8":
            menu_cola(turnos)
        elif opcion in {"2", "3", "4", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()