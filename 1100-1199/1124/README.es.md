# 1124. Devolver piezas de colores a sus cajas con el menor número de movimientos de mano

[Timus 1124](https://acm.timus.ru/problem.aspx?space=1&num=1124) · dificultad 299 · dsu

Problema original de Stanislav Vasiliev, del sexto concurso universitario de programación de la Universidad Estatal de los Urales, 21 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `M` colores (`2 ≤ M ≤ 500`), `N` piezas de cada uno (`2 ≤ N ≤ 50`) y
`M` cajas, la caja `i` destinada al color `i`; ahora cada caja tiene `N`
piezas de colores cualesquiera. Un movimiento de mano lleva una pieza de
la caja donde está la mano a otra caja (la mano acaba allí) o mueve la
mano vacía a otra caja. La mano puede empezar gratis en cualquier caja.
Halla el menor número de movimientos que deja cada pieza en su caja.

Límite de tiempo: 0,25 segundos. Límite de memoria: 64 MB.

## Entrada

`M N` y luego `M` líneas de `N` colores: las piezas de cada caja.

## Salida

El menor número de movimientos de mano.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3
1 3 1
2 3 3
1 2 2
4 4 4
```

Salida:

```
6
```

## Solución

Se traza una arista dirigida de la caja `b` a la caja `c` por cada pieza
de color `c` que esté en la caja `b ≠ c`. Cada pieza mal colocada necesita
al menos un movimiento que la lleve, y cada movimiento así arregla como
mucho una pieza. Cada caja tiene `N` piezas y debe acabar con `N`, así que
cada caja tiene tantas aristas de entrada como de salida, y cada grupo
conexo de cajas tiene un circuito euleriano: la mano puede seguirlo,
llevando una pieza por cada arista y terminando cada traslado donde
empieza el siguiente. Entre dos grupos la mano necesita un movimiento en
vacío. Así que con `E` piezas mal colocadas en `G` grupos la respuesta es
`E + G − 1`, y 0 si no hay ninguna mal colocada. Una unión de conjuntos
disjuntos sobre las cajas halla los grupos. `O(M·N)`.

Detalles a tener en cuenta:

- las cajas ya correctas no forman grupo y no hace falta visitarlas;
- la primera colocación de la mano es gratis, de ahí el `− 1`;
- sin piezas mal colocadas la respuesta es 0, no `−1`.

La fórmula se comprobó con una búsqueda en anchura sobre el estado
completo (el contenido de cada caja y la posición de la mano) en 150
mosaicos diminutos; las pruebas hechas a mano salen de esa búsqueda y las
grandes se comprobaron con la fórmula calculada aparte.

## Notas por lenguaje

- Todos los lenguajes usan la misma unión de conjuntos disjuntos con
  compresión de caminos a la mitad.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1124_dsu.cpp](1124_dsu.cpp) | G++ 13.2 x64 | dsu | O(M·N) | AC | 0.015 s | 208 KB |
| [1124_dsu.go](1124_dsu.go) | Go 1.14 x64 | dsu | O(M·N) | AC | 0.046 s | 1520 KB |
| [1124_dsu.java](1124_dsu.java) | Java 1.8 | dsu | O(M·N) | AC | 0.125 s | 480 KB |
| [1124_dsu.py](1124_dsu.py) | Python 3.12 x64 | dsu | O(M·N) | AC | 0.078 s | 1860 KB |
| [1124_dsu.rs](1124_dsu.rs) | Rust 1.75 x64 | dsu | O(M·N) | AC | 0.015 s | 652 KB |
