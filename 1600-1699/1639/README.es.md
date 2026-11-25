# 1639. Chocolate 2

[Timus 1639](https://acm.timus.ru/problem.aspx?space=1&num=1639) · dificultad 32 · games

Problema original de Alexander Pronchenkov (preparado por Ivan Burmistrov), del USU Junior Contest, octubre de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos jugadores parten por turnos una tableta de chocolate de m × n: cada
movimiento toma cualquier trozo y lo parte en dos por las ranuras. Pierde
quien no puede mover porque solo quedan trozos de 1 × 1. ¿Debe Karlsson
mover primero o segundo para ganar con seguridad?

## Entrada

Dos enteros m y n (1 ≤ m, n ≤ 50).

## Salida

`[:=[first]` si gana quien mueve primero, y `[second]=:]` en otro caso.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 4
```

Salida:

```
[:=[first]
```

### Ejemplo 2

Entrada:

```
1 3
```

Salida:

```
[second]=:]
```

## Actualización de envíos aceptados

Archivos actualizados: [1639_parsing_implementation_optimized.rs](1639_parsing_implementation_optimized.rs). Las tablas de soluciones muestran los nuevos Accepted correspondientes exactamente al código fuente de estos archivos. Las mediciones y posiciones comparativas anteriores pertenecen a versiones previas y se conservan como datos históricos. La auditoría en caché confirma implementaciones que cumplen los criterios en todos los lenguajes disponibles. Se conservan las versiones didácticas por su claridad; si un mismo archivo cubre también la versión rápida, debe cumplir el criterio de rendimiento.

## Solución

Cada movimiento convierte un trozo en dos, así que aumenta el número de
trozos exactamente en uno. El juego empieza con un trozo y termina con
m · n, de modo que siempre dura m · n − 1 movimientos, hagan lo que
hagan los jugadores. El primer jugador hace el último movimiento, y
gana, exactamente cuando m · n − 1 es impar, es decir, cuando m · n es
par. `O(1)`.

Detalles a tener en cuenta:

- la estrategia no importa, así que no hay nada que buscar;
- una tableta de 1 × 1 no admite ningún movimiento, y el primer jugador
  pierde enseguida (prueba 03).

## Soluciones optimizadas

La solución optimizada en Java analiza los dos números a mano con
`System.in.read` en lugar de usar `Scanner`: 372 KB en lugar de 1608 KB,
con el mismo tiempo. Comprueba directamente la paridad de `m · n`, que
es la contraria de la paridad del número de jugadas `m · n − 1`.

Leer las dos dimensiones como bytes y comprobar directamente la paridad del número de piezas. El envío aceptado 11301875 tardó 0.078 s y usó 404 KB. La versión sencilla tardó 0.078 s y usó 412 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1639_games_optimized.go`. Se conservan el algoritmo y sus casos límite. Se sustituye fmt por conversión de números y palabras y un búfer de salida reutilizable. La entrada completa se guarda en bytes: se intercambia ese espacio por un menor coste de la E/S general.

Accepted #11328578 (Go 1.14 x64): **0.031 s / 908 KB**. Comparación archivada: `1639_games.go` (Go 1.14 x64) — 0.031 s / 1132 KB (#11288462).

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1639_parsing_implementation_optimized.rs`. Los dos enteros se leen directamente con un búfer nativo acotado y la respuesta fija de paridad se escribe en bytes, sin almacenar toda la entrada.

Accepted #11329177 (Rust 1.75 x64): **0.031 s / 52 KB**. Comparación archivada: `1639_games.rs` (Rust 1.75 x64) — 0.046 s / 236 KB (#11303478).

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1639_games.cpp](1639_games.cpp) | G++ 13.2 x64 | games | O(1) | AC | 0.015 s | 120 KB | 11288461 |
| [1639_games.go](1639_games.go) | Go 1.14 x64 | games | O(1) | AC | 0.031 s | 1132 KB | 11288462 |
| [1639_games.java](1639_games.java) | Java 1.8 | games | O(1) | AC | 0.125 s | 1608 KB | 11288464 |
| [1639_games.py](1639_games.py) | Python 3.12 x64 | games | O(1) | AC | 0.078 s | 412 KB | 11288463 |
| [1639_games.rs](1639_games.rs) | Rust 1.75 x64 | games | O(1) | AC | 0.046 s | 236 KB | 11303478 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1639_games_optimized.java](1639_games_optimized.java) | Java 1.8 | games | O(1) | AC | 0.109 s | 372 KB | 11303628 |
| [1639_games_optimized.py](1639_games_optimized.py) | Python 3.12 x64 | games | O(1) | AC | 0.078 s | 404 KB | 11301875 |
| [1639_games_optimized.go](1639_games_optimized.go) | Go 1.14 x64 | games | O(1) | AC | 0.031 s | 908 KB | 11328578 |
| [1639_parsing_implementation_optimized.rs](1639_parsing_implementation_optimized.rs) | Rust 1.75 x64 | parsing, implementation | O(1) | AC | 0.031 s | 48 KB | 11330235 |
