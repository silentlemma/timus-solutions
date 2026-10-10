# 1155. Vaciar de partículas las esquinas de un cubo por pares

[Timus 1155](https://acm.timus.ru/problem.aspx?space=1&num=1155) · dificultad 178 · constructive

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

Ocho cantidades, de `A` a `H`.

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
- una entrada vacía no necesita ninguna operación;
- `IMPOSSIBLE` depende solo de los totales de los dos lados, no de cómo
  se reparten las partículas.

Las respuestas se comprobaron con el comprobador en todas las pruebas y
en 3000 entradas aleatorias; la más larga necesitó 442 operaciones.

## Notas por lenguaje

- Todos los lenguajes recorren las aristas en el mismo orden e imprimen
  las mismas operaciones.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1155_constructive.cpp](1155_constructive.cpp) | G++ 13.2 x64 | constructive | O(total) | AC | 0.015 s | 404 KB |
| [1155_constructive.go](1155_constructive.go) | Go 1.14 x64 | constructive | O(total) | AC | 0.031 s | 1116 KB |
| [1155_constructive.java](1155_constructive.java) | Java 1.8 | constructive | O(total) | AC | 0.156 s | 3884 KB |
| [1155_constructive.py](1155_constructive.py) | Python 3.12 x64 | constructive | O(total) | AC | 0.078 s | 612 KB |
| [1155_constructive.rs](1155_constructive.rs) | Rust 1.75 x64 | constructive | O(total) | AC | 0.015 s | 436 KB |
