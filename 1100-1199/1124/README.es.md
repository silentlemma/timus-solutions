# 1124. Devolver piezas de colores a sus cajas con el menor número de movimientos de mano

[Timus 1124](https://acm.timus.ru/problem.aspx?space=1&num=1124) · dificultad 297 · dsu

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
disjuntos sobre las cajas halla los grupos. `O(M·N·log M)`.

Detalles a tener en cuenta:

- las cajas ya correctas no forman grupo y no hace falta visitarlas;
- la primera colocación de la mano es gratis, de ahí el `− 1`;
- sin piezas mal colocadas la respuesta es 0, no `−1`.

La fórmula se comprobó con una búsqueda en anchura sobre el estado
completo (el contenido de cada caja y la posición de la mano) en 150
mosaicos diminutos; las pruebas grandes se comprobaron con la fórmula
calculada aparte.

## Soluciones optimizadas

Go y Rust combinan pertenencia, tamaño y activación de componentes en un vector de 16 bits. Cero indica un nodo sin activar, un valor negativo representa una raíz y el tamaño de su componente, y uno positivo señala al padre. La unión por tamaño con reducción de caminos mantiene el número de componentes activos mientras se leen las bolas mal colocadas.

El envío aceptado en Rust 1.75 x64 tarda 0.046 s frente a 0.015 s de la base y usa 196 KB frente a 652 KB.

Las implementaciones base aceptadas [1124_dsu.cpp](1124_dsu.cpp), [1124_dsu.java](1124_dsu.java), [1124_dsu.py](1124_dsu.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes usan la misma unión de conjuntos disjuntos con
  compresión de caminos a la mitad.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1124_dsu.cpp](1124_dsu.cpp) | G++ 13.2 x64 | dsu | O(M·N·log M) | AC | 0.015 s | 208 KB | 11279302 |
| [1124_dsu.go](1124_dsu.go) | Go 1.14 x64 | dsu | O(M·N·log M) | AC | 0.046 s | 1520 KB | 11279303 |
| [1124_dsu.java](1124_dsu.java) \* | Java 1.8 | dsu | O(M·N·log M) | AC | 0.125 s | 480 KB | 11279306 |
| [1124_dsu.py](1124_dsu.py) \* | Python 3.12 x64 | dsu | O(M·N·log M) | AC | 0.078 s | 1860 KB | 11279305 |
| [1124_dsu.rs](1124_dsu.rs) | Rust 1.75 x64 | dsu | O(M·N·log M) | AC | 0.015 s | 652 KB | 11279308 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1124_dsu_optimized.go](1124_dsu_optimized.go) \* | Go 1.14 x64 | dsu | O(M·N·α(M)) | AC | 0.031 s | 972 KB | 11311105 |
| [1124_dsu_optimized.rs](1124_dsu_optimized.rs) \* | Rust 1.75 x64 | dsu | O(M·N·α(M)) | AC | 0.046 s | 196 KB | 11310569 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
