# 1155. Vaciar de partículas las esquinas de un cubo por pares

[Timus 1155](https://acm.timus.ru/problem.aspx?space=1&num=1155) · dificultad 171 · constructive

Problema original del campeonato de programación por equipos de los Urales, Perm, abril de 2001, ronda en inglés.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Ocho cámaras, de `A` a `H`, están en las esquinas de un cubo (`A B C D`
alrededor de una cara, `E F G H` encima en el mismo orden), cada una con
0 a 100 partículas. Una operación crea o destruye dos partículas en dos
cámaras vecinas, una en cada una. Imprime como mucho 1000 operaciones
que vacíen todas las cámaras, o `IMPOSSIBLE`.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

Una línea con ocho enteros de 0 a 100, de `A` a `H` en orden.

## Salida

Una operación por línea: las dos cámaras y `+` o `-`; o `IMPOSSIBLE`.

## Evaluación

Se acepta cualquier secuencia válida. El comprobador repite las
operaciones: cada una debe unir cámaras vecinas, ninguna cámara puede
bajar de cero, puede haber como mucho 1000, y al final todas las cámaras
deben quedar vacías. `IMPOSSIBLE` debe imprimirse justo cuando los dos
lados de abajo difieren.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 0 1 0 3 1 0 0
```

Salida:

```
EF-
AE-
BA+
CB-
AE-
```

### Ejemplo 2

Entrada:

```
0 1 0 1 2 3 2 2
```

Salida:

```
IMPOSSIBLE
```

## Solución

Se colorean las esquinas como un tablero de ajedrez: `A C F H` en un lado
y `B D E G` en el otro. Cada arista une los dos lados, así que cada
operación cambia los totales de ambos lados en la misma cantidad y su
diferencia nunca cambia. Si la diferencia no es cero, la respuesta es
`IMPOSSIBLE`.

Si no, primero se recorren una vez las doce aristas y en cada una se
destruyen tantos pares como permiten sus dos extremos. Las cantidades
solo bajan, así que después cada arista tiene un extremo vacío. Una
esquina que aún tiene partículas tiene vacías sus tres vecinas, y su
esquina opuesta, la única del otro lado que no es vecina suya, guarda
todas las partículas de ese lado. Como los totales son iguales, lo que
queda son `k` partículas en cada una de dos esquinas opuestas `u` y `w`.
Están a tres aristas, `u x y w`, y el trío «crear en `x y`, destruir en
`u x`, destruir en `y w`» quita una de cada una. La primera pasada usa
como mucho 400 operaciones y el resto como mucho `3·100`, así que nunca se
llega al límite de 1000.

Detalles a tener en cuenta:

- un par solo se puede destruir si ambas cámaras tienen una partícula,
  así que en cada trío la creación va primero;
- si todas las cantidades son cero, no hace falta ninguna operación (prueba 03);
- las ocho cantidades deben estar en una sola línea; repartirlas entre líneas
  incumple el formato de entrada, y Python solo lee la primera línea;
- `IMPOSSIBLE` depende solo de los totales de los dos lados, no de cómo
  se reparten las partículas.

Las respuestas se comprobaron con el comprobador en las 13 pruebas fijas y
generadas. El oráculo independiente y la repetición de las operaciones
validaron 3000 entradas aleatorias pequeñas y 374 casos límite, con un
máximo de 500 operaciones.

## Soluciones optimizadas

La solución optimizada en C++ imprime las mismas operaciones, pero
guarda las cantidades y los tres vecinos de cada vértice en pequeños
arreglos fijos indexados por la letra del vértice en lugar de
`std::map`, lee con `scanf` en lugar de `iostream` e imprime cada
operación con `printf` en el acto en lugar de juntar toda la salida en
una cadena: {1155_constructive_optimized.cpp}.

La solución optimizada en Java imprime las mismas operaciones, pero
guarda las cantidades y los tres vecinos de cada vértice en arreglos
fijos indexados por la letra del vértice en lugar de mapas de caracteres
empaquetados y listas creadas con lambdas, y lee los ocho números byte a
byte en bloques de 4 KB en lugar de con `Scanner`:
{1155_constructive_optimized.java}.

La solución optimizada en Rust imprime las mismas operaciones, pero
guarda las cantidades y los tres vecinos de cada vértice en arreglos
fijos indexados por la letra del vértice en lugar de tablas hash, y
escribe cada operación directamente en un `BufWriter` en lugar de juntar
toda la salida en una cadena: {1155_constructive_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1155_constructive_optimized.cpp`: reducción de tiempo -106.67%;
  reducción de memoria +75.25%; base: `1155_constructive.cpp`.

- `1155_constructive_optimized.java`: reducción de tiempo +40.38%;
  reducción de memoria +88.26%; base: `1155_constructive.java`.

- `1155_constructive_optimized.rs`: reducción de tiempo +0.00%;
  reducción de memoria +50.46%; base: `1155_constructive.rs`.

## Notas por lenguaje

- Todos los lenguajes recorren las aristas en el mismo orden e imprimen
  las mismas operaciones.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1155_constructive.cpp](1155_constructive.cpp) | G++ 13.2 x64 | constructive | O(total) | AC | 0.015 s | 404 KB | 11281010 |
| [1155_constructive.go](1155_constructive.go) | Go 1.14 x64 | constructive | O(total) | AC | 0.031 s | 1116 KB | 11281106 |
| [1155_constructive.java](1155_constructive.java) | Java 1.8 | constructive | O(total) | AC | 0.156 s | 3884 KB | 11281181 |
| [1155_constructive.py](1155_constructive.py) | Python 3.12 x64 | constructive | O(total) | AC | 0.078 s | 612 KB | 11281128 |
| [1155_constructive.rs](1155_constructive.rs) | Rust 1.75 x64 | constructive | O(total) | AC | 0.015 s | 436 KB | 11281207 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1155_constructive_optimized.cpp](1155_constructive_optimized.cpp) \* | G++ 13.2 x64 | constructive | O(total) | AC | 0.031 s | 100 KB | 11307258 |
| [1155_constructive_optimized.java](1155_constructive_optimized.java) \* | Java 1.8 | constructive | O(total) | AC | 0.093 s | 456 KB | 11307261 |
| [1155_constructive_optimized.rs](1155_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(total) | AC | 0.015 s | 216 KB | 11307262 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
