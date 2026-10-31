# 1167. Repartir una fila de caballos negros y blancos en establos con el menor descontento

[Timus 1167](https://acm.timus.ru/problem.aspx?space=1&num=1167) · dificultad 136 · dp

Problema original de Mugurel Ionut Andreica, del Romanian Open Contest de diciembre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N ≤ 500` caballos, negros o blancos, están en fila. Hay que partir la
fila en exactamente `K` tramos consecutivos no vacíos (`1 ≤ K ≤ N`), uno
por establo. Un establo con `i` caballos negros y `j` blancos tiene
descontento `i·j`. Hay que hallar el menor descontento total posible.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `K`, y luego `N` colores: `1` para negro, `0` para blanco.

## Salida

El menor descontento total.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 3
1
1
0
1
0
1
```

Salida:

```
2
```

## Solución

Sea `best[s][i]` el menor descontento de los primeros `i` caballos en `s`
establos. El último establo se lleva los caballos `j..i−1`, así que
`best[s][i] = min sobre j de best[s−1][j] + cost(j, i)`, donde el coste es
negros por blancos, sacado de sumas prefijas de caballos negros. Eso es
`O(K·N²)` en total, unos 20 millones de pasos en los límites: bien para
lenguajes compilados pero lento para Python.

El coste tiene una propiedad útil. Para `a ≤ b ≤ c ≤ d`, sean `x`, `y`,
`z` los trozos `a..b`, `b..c`, `c..d`; entonces
`cost(a, d) + cost(b, c) − cost(a, c) − cost(b, d) = Bx·Wz + Bz·Wx ≥ 0`,
con `B` y `W` las cuentas de negros y blancos. Por esta desigualdad del
cuadrilátero, el mejor último corte nunca se mueve a la izquierda cuando
`i` crece. Así que cada capa se llena con divide y vencerás: se halla el
mejor corte para la `i` del medio, y luego la mitad izquierda solo busca
cortes hasta él y la derecha solo desde él. Cada capa cuesta
`O(N log N)`, todas juntas `O(K·N log N)`.

Detalles a tener en cuenta:

- hay que usar todos los establos, así que `best[s][i]` solo existe para
  `i ≥ s`;
- sin establos solo es posible `best[0][0] = 0`, y todo otro inicio debe
  contar como inalcanzable.

Las respuestas se compararon con la recurrencia simple en `O(K·N²)` en
400 entradas aleatorias de hasta 40 caballos y en todas las pruebas.

## Soluciones optimizadas

La solución optimizada en C++ guarda las sumas prefijas y las dos capas
en arreglos `int` fijos de 501 elementos, suficientes porque `N ≤ 500`,
en lugar de vectores, e intercambia los punteros a las dos capas en
lugar de crear una capa nueva y copiarla de vuelta después de cada
establo: {1167_dp_optimized.cpp}.

La solución optimizada en Go reserva las dos capas una sola vez y las
intercambia después de cada establo en lugar de crear un slice nuevo por
establo. Los valores viejos que quedan en la capa reutilizada no
estorban, porque la capa `s` solo lee las posiciones desde `s − 1`, que
la capa anterior acaba de escribir. Así el recolector de basura no tiene
nada que recoger: {1167_dp_optimized.go}.

La solución optimizada en Java reserva las dos capas una sola vez y las
intercambia después de cada establo en lugar de crear un arreglo nuevo
por establo. Los valores viejos que quedan en la capa reutilizada no
estorban, porque la capa `s` solo lee las posiciones desde `s − 1`, que
la capa anterior acaba de escribir. Así el bucle no reserva memoria:
{1167_dp_optimized.java}.

La solución optimizada en Python reduce el trabajo del intérprete. Si
`K` es al menos el número de tramos monocolor, imprime 0 de
inmediato: cada tramo recibe su propio establo, y los tramos se pueden
seguir partiendo sin coste hasta tener exactamente `K` establos, lo que
es posible porque `K ≤ N`. La primera capa es el coste de un solo
establo y se calcula directamente. La capa `s` solo rellena las
posiciones hasta `N − K + s`, porque cada establo posterior necesita al
menos un caballo. El coste va escrito dentro del bucle más interno, y
los rangos vacíos nunca entran en la pila: {1167_dp_optimized.py}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1167_dp_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +44.90%; base: `1167_dp.cpp`.

- `1167_dp_optimized.go`: reducción de tiempo +0.00%; reducción de
  memoria +65.79%; base: `1167_dp.go`.

- `1167_dp_optimized.java`: reducción de tiempo +12.80%; reducción de
  memoria +67.49%; base: `1167_dp.java`.

- `1167_dp_optimized.py`: reducción de tiempo +59.38%; reducción de
  memoria -25.36%; base: `1167_dp.py`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1167_dp.rs](1167_dp.rs).

- Todos los lenguajes hacen el mismo divide y vencerás; Python usa una
  pila explícita en lugar de recursión.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1167_dp.cpp](1167_dp.cpp) | G++ 13.2 x64 | dp | O(K·N log N) | AC | 0.015 s | 196 KB | 11283090 |
| [1167_dp.go](1167_dp.go) | Go 1.14 x64 | dp | O(K·N log N) | AC | 0.031 s | 3204 KB | 11283095 |
| [1167_dp.java](1167_dp.java) | Java 1.8 | dp | O(K·N log N) | AC | 0.125 s | 1464 KB | 11283098 |
| [1167_dp.py](1167_dp.py) | Python 3.12 x64 | dp | O(K·N log N) | AC | 0.421 s | 552 KB | 11283096 |
| [1167_dp.rs](1167_dp.rs) | Rust 1.75 x64 | dp | O(K·N log N) | AC | 0.031 s | 244 KB | 11283104 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1167_dp_optimized.cpp](1167_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(K·N log N) | AC | 0.015 s | 108 KB | 11304442 |
| [1167_dp_optimized.go](1167_dp_optimized.go) | Go 1.14 x64 | dp | O(K·N log N) | AC | 0.031 s | 1096 KB | 11304443 |
| [1167_dp_optimized.java](1167_dp_optimized.java) | Java 1.8 | dp | O(K·N log N) | AC | 0.109 s | 476 KB | 11304444 |
| [1167_dp_optimized.py](1167_dp_optimized.py) \* | Python 3.12 x64 | dp | O(K·N log N) | AC | 0.171 s | 692 KB | 11304446 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
