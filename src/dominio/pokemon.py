from src.tads.lista_enlazada import ListaEnlazada
from src.persistencia.texto import cargar_csv


class Pokemon:
    def __init__(self, id_pokemon, nombre, tipo1, tipo2, hp, ataque, defensa, velocidad, generacion):
        self.id = id_pokemon
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.generacion = generacion

    def __str__(self):
        return f"#{self.id} {self.nombre} ({self.tipo1}) - HP:{self.hp} ATK:{self.ataque}"


def cargar_pokedex(ruta_csv):
    pokedex = ListaEnlazada()
    filas = cargar_csv(ruta_csv)
    for fila in filas:
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