# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema:Pokedex
- Por qué lo eligieron (5–8 líneas): El tema Pokédex generó un interés particular. Dentro de lo visto en clases,
- despertó curiosidad cómo se podría desarrollar algo así, y además hay un interés personal por la saga de Pokémon. 
- Es un tema de naturaleza compleja, como la interacción entre tipos, qué habilidades puede aprender cada Pokémon y sus IVs, 
- lo cual lo vuelve un desafío interesante para aplicar lo que estamos aprendiendo.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

Un ítem del catálogo es un objeto de la clase Pokemon, con los atributos: id, nombre, tipo1, tipo2, hp, ataque, defensa, velocidad y generacion.
Los tipos usados dentro de Pokemon (int, str, None) son inmutables: no se puede modificar el valor en sí, solo reemplazarlo. 
El objeto Pokemon en sí es mutable:sus atributos se pueden reasignar después de creado.
Para tipo2 usamos None en vez de un string vacío ("") cuando el Pokémon no tiene segundo tipo, ya que None representa la ausencia real de un dato.
El catálogo completo se guarda en una ListaEnlazada propia, construida con nodos enlazados por punteros. 
La colección principal (equipo), la pila (historial) y la cola todavía no están implementadas — se suman en entregas siguientes, reutilizando la misma ListaEnlazada como base.

```text
Pokemon (dominio)
  - id: int
  - nombre: str
  - tipo1: str
  - tipo2: str | None
  - hp, ataque, defensa, velocidad, generacion: int

ListaEnlazada (TAD)
  - Nodo (dato, siguiente)
  - cabeza -> Nodo -> Nodo -> ... -> None
```

## 3. Recursión (E2)

- Función:
- Caso base:
- Caso recursivo:
- Traza de un ejemplo real del dataset:

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
