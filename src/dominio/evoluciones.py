from src.persistencia.texto import cargar_csv


def cargar_evoluciones(ruta_csv):
    filas = cargar_csv(ruta_csv)
    mapa = {}
    for fila in filas:
        origen = int(fila["origen_id"])
        destino = int(fila["destino_id"])
        mapa[origen] = destino
    return mapa


def cadena_evolutiva(id_pokemon, mapa_evoluciones):
    if id_pokemon not in mapa_evoluciones:
        return [id_pokemon]
    siguiente_id = mapa_evoluciones[id_pokemon]
    return [id_pokemon] + cadena_evolutiva(siguiente_id, mapa_evoluciones)