# 1250. Islas dentro del mar sagrado

[Timus 1250](https://acm.timus.ru/problem.aspx?space=1&num=1250) · dificultad 724 · graphs

Problema original de Stanislav Skorb (preparado por Ivan Dashkevich), del Concurso Abierto por Equipos de la Universidad Estatal de los Urales, 15 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un mapa de W × H (W, H ≤ 500) muestra mar `.` y tierra `#`. Las casillas
de mar forman un mismo mar si se tocan por un lado o una esquina; las de
tierra forman una misma isla si se tocan solo por un lado. El mar que
contiene la casilla (X, Y), contada desde la esquina superior izquierda,
es sagrado, y toda la tierra dentro de él también lo es, incluidas las
islas de los mares que hay dentro de sus islas, y así sucesivamente. Hay
que contar las islas sagradas que no tocan el borde del mapa.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

W, H, X e Y separados por uno o más espacios, y luego H líneas de W
caracteres.

## Salida

El número de esas islas.

## Ejemplos

### Ejemplo 1

Entrada:

```
9 7 1 1
........#
.#######.
.#.....#.
.#.#.#.#.
.#.....#.
.#######.
#........
```

Salida:

```
3
```

### Ejemplo 2

Entrada:

```
9 7 3 3
........#
.#######.
.#.....#.
.#.#.#.#.
.#.....#.
.#######.
#........
```

Salida:

```
2
```

## Solución

Se rodea el mapa con un anillo de casillas exteriores. Un mar unido por
esquinas no se puede atravesar con un camino que solo pasa por lados:
donde parece estrecho, dos de sus casillas se tocan por una esquina y
cierran el hueco. Así que la tierra dentro del mar sagrado es justo la
que no alcanza una inundación por lados desde el anillo exterior que
evita el mar sagrado.

El programa halla el mar sagrado con una inundación en las ocho
direcciones desde (X, Y), inunda desde el anillo exterior todas las
casillas que no están en él y cuenta las islas entre las casillas no
alcanzadas, con una inundación por lados por isla. Una isla que toca el
borde siempre se alcanza desde el anillo, así que nunca cuenta. Cada
inundación usa una pila explícita para evitar una recursión profunda en
mapas grandes. `O(W·H)`.

Detalles a tener en cuenta:

- las islas anidadas en lagos de islas sagradas también cuentan: en el
  primer ejemplo, el anillo y las dos islas de dentro (la prueba 06 tiene
  un lago);
- la tierra que solo se toca por una esquina forma islas distintas
  (prueba 08);
- la primera línea puede llevar varios espacios entre los números, así
  que el mapa se lee como los siguientes W·H caracteres `.` y `#`, haya lo
  que haya entre ellos.

Los recuentos se compararon con una segunda solución que construye el
árbol de mares e islas, en 1500 mapas pequeños aleatorios.

## Notas por lenguaje

- Python inunda con arreglos de bytes de casillas «aún libres», que la
  inundación va borrando.

## Soluciones optimizadas

Las inundaciones comparten un byte de estado por casilla. Un borde protector impide salir del mapa, por lo que cada vecina se obtiene con un desplazamiento fijo sin comprobar los límites de fila y columna en cada paso.

Go 1.14 x64, envío 11318425. Tiempo 0,046 → 0,031 s, memoria 6644 → 4280 KB.

Rust 1.75 x64, envío 11318428. Tiempo 0,046 → 0,015 s, memoria 4948 → 1684 KB.

Python 3.12 x64, envío 11318431. Tiempo 0,468 → 0,328 s, memoria 14592 → 6444 KB.

Java 1.8, envío 11318433. Tiempo 0,093 → 0,125 s, memoria 3184 → 1620 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321900 · Go 1.14 x64 №11322182 · Java 1.8 №11322183 · Python 3.12 x64 №11322184 · Rust 1.75 x64 №11322185.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1250_graphs.cpp](1250_graphs.cpp) | G++ 13.2 x64 | graphs | O(W·H) | AC | 0.015 s | 2408 KB | 11321900 |
| [1250_graphs.go](1250_graphs.go) | Go 1.14 x64 | graphs | O(W·H) | AC | 0.046 s | 6644 KB | 11322182 |
| [1250_graphs.java](1250_graphs.java) | Java 1.8 | graphs | O(W·H) | AC | 0.093 s | 3184 KB | 11322183 |
| [1250_graphs.py](1250_graphs.py) | Python 3.12 x64 | graphs | O(W·H) | AC | 0.468 s | 14592 KB | 11322184 |
| [1250_graphs.rs](1250_graphs.rs) | Rust 1.75 x64 | graphs | O(W·H) | AC | 0.046 s | 4948 KB | 11322185 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1250_graphs_optimized.go](1250_graphs_optimized.go) \* | Go 1.14 x64 | graphs | O(W·H) | AC | 0.031 s | 4280 KB | 11318425 |
| [1250_graphs_optimized.rs](1250_graphs_optimized.rs) \* | Rust 1.75 x64 | graphs | O(W·H) | AC | 0.015 s | 1684 KB | 11318428 |
| [1250_graphs_optimized.py](1250_graphs_optimized.py) | Python 3.12 x64 | graphs | O(W·H) | AC | 0.328 s | 6444 KB | 11318431 |
| [1250_graphs_optimized.java](1250_graphs_optimized.java) \* | Java 1.8 | graphs | O(W·H) | AC | 0.125 s | 1620 KB | 11318433 |

\* Las versiones marcadas aún pueden mejorar su clasificación.
