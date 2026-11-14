# 1085. La parada de tranvía más barata para que se reúna un grupo de amigos

[Timus 1085](https://acm.timus.ru/problem.aspx?space=1&num=1085) · dificultad 629 · bfs, graphs

Problema original de Alexander Somov, de la Tercera Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 4 de marzo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ciudad tiene `N` paradas y `M` líneas de tranvía (`1 ≤ N, M ≤ 100`),
cada una una lista de 2 a 100 paradas. Un billete cuesta 4 y sirve para
un viaje por una línea; cada cambio de línea necesita un billete nuevo.
Cada uno de los `K` amigos (`1 ≤ K ≤ 100`) parte de alguna parada con
como mucho 1000 de dinero, y algunos tienen un abono con el que todos los
viajes son gratis. Halla la parada donde pueden reunirse todos, pagando
cada uno su viaje, con el menor coste total (la de menor número en caso
de empate), e imprímela con el coste, o `0` si no existe.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y `M`; `M` líneas con la longitud de una línea y sus paradas; `K`;
`K` líneas con el dinero de un amigo, su parada de partida y 1 si tiene
abono o 0.

## Salida

La parada y el coste total, o `0`.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3
2 1 2
2 2 3
2 3 4
3
27 1 0
15 4 0
45 4 0
```

Salida:

```
4 12
```

## Solución

Sin abono, un trayecto cuesta 4 por el número de viajes, y un viaje
cubre cualquier tramo de una línea, así que lo que importa es el menor
número de viajes
desde la partida hasta cada parada. Una búsqueda en anchura lo halla:
desde una parada se abre una vez cada línea que pasa por ella y aún no se
ha usado, y todas sus paradas no alcanzadas reciben un viaje más. Cada
línea se abre como mucho una vez, así que una búsqueda cuesta
`O(N + ΣL)`.

Se lanza la búsqueda desde la parada de cada amigo. Para cada parada `t`,
un amigo sin abono paga `4 · viajes`, que no debe superar su dinero; un
amigo con abono no paga nada, pero `t` debe ser alcanzable igualmente. Se
suman los costes de los amigos, se marcan las paradas a las que alguien
no puede llegar o no puede pagar, y se toma la más barata de las
restantes con el menor número. `O(K · (N + ΣL))`.

Detalles a tener en cuenta:

- el abono hace gratis el viaje, pero no vuelve alcanzable una parada
  inalcanzable;
- la propia parada de un amigo no cuesta nada aunque no pase ninguna línea
  por ella;
- un amigo sin abono puede tener menos dinero que un billete, y entonces
  solo es posible su propia parada.

Las respuestas se comprobaron con Floyd–Warshall en el grafo de paradas
donde dos paradas de una misma línea están a un viaje de distancia.

## Notas por lenguaje

- Los cinco lenguajes guardan para cada parada la lista de líneas que
  pasan por ella y marcan las líneas ya abiertas en cada búsqueda.

## Soluciones optimizadas

Java representa con máscaras de bits las paradas alcanzables en un viaje y hace una sola búsqueda en anchura por parada de origen (U en la tabla). Cada grupo usa el presupuesto más ajustado de los viajeros sin abono. El envío 11317236 tardó 0,125 s y usó 432 KB frente a 0,109 s y 1020 KB en la base.

Python construye las máscaras de paradas al leer las rutas y comprueba primero los presupuestos más ajustados. El envío 11318373 tardó 0,078 s y usó 760 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321815 · Go 1.14 x64 №11321818 · Rust 1.75 x64 №11321820 · Java 1.8 №11322058 · Python 3.12 x64 №11322059.

Rust agrupa a los pasajeros por parada de origen y representa cada nivel de la búsqueda en anchura con una máscara de 128 bits. Rust 1.75 x64, envío 11322390. Tiempo 0,031 → 0,015 s, memoria 232 → 216 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1085_bfs.cpp](1085_bfs.cpp) | G++ 13.2 x64 | bfs | O(K · (N + ΣL)) | AC | 0.015 s | 204 KB | 11321815 |
| [1085_bfs.go](1085_bfs.go) | Go 1.14 x64 | bfs | O(K · (N + ΣL)) | AC | 0.031 s | 1376 KB | 11321818 |
| [1085_bfs.java](1085_bfs.java) | Java 1.8 | bfs | O(K · (N + ΣL)) | AC | 0.109 s | 1020 KB | 11322058 |
| [1085_bfs.py](1085_bfs.py) | Python 3.12 x64 | bfs | O(K · (N + ΣL)) | AC | 0.078 s | 780 KB | 11322059 |
| [1085_bfs.rs](1085_bfs.rs) | Rust 1.75 x64 | bfs | O(K · (N + ΣL)) | AC | 0.031 s | 232 KB | 11321820 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1085_bfs_optimized.java](1085_bfs_optimized.java) \* | Java 1.8 | bfs | O(ΣL + U N) | AC | 0.125 s | 432 KB | 11317236 |
| [1085_bfs_optimized.py](1085_bfs_optimized.py) \* | Python 3.12 x64 | bfs | O(ΣL + U N) | AC | 0.078 s | 760 KB | 11318373 |
| [1085_bfs_optimized.rs](1085_bfs_optimized.rs) | Rust 1.75 x64 | bfs | O(ΣL + U N) | AC | 0.015 s | 216 KB | 11322390 |

\* Java aún no alcanza el objetivo en la clasificación guardada. Python aún no alcanza el objetivo en la clasificación guardada.
