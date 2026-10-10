# 1167. Repartir una fila de caballos negros y blancos en establos con el menor descontento

[Timus 1167](https://acm.timus.ru/problem.aspx?space=1&num=1167) · dificultad 136 · dp

Problema original de Mugurel Ionut Andreica, del Romanian Open Contest de diciembre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N ≤ 500` caballos, negros o blancos, están en fila. Hay que partir la
fila en exactamente `K` tramos consecutivos no vacíos, uno por establo. Un
establo con `i` caballos negros y `j` blancos tiene descontento `i·j`. Hay
que hallar el menor descontento total posible.

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

Las respuestas se compararon con la recurrencia simple en `O(K·N²)` en 400
entradas aleatorias de hasta 40 caballos y en todas las pruebas.

## Notas por lenguaje

- Todos los lenguajes hacen el mismo divide y vencerás; Python usa una
  pila explícita en lugar de recursión.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1167_dp.cpp](1167_dp.cpp) | G++ 13.2 x64 | dp | O(K·N log N) | AC | 0.015 s | 196 KB |
| [1167_dp.go](1167_dp.go) | Go 1.14 x64 | dp | O(K·N log N) | AC | 0.031 s | 3204 KB |
| [1167_dp.java](1167_dp.java) | Java 1.8 | dp | O(K·N log N) | AC | 0.125 s | 1464 KB |
| [1167_dp.py](1167_dp.py) | Python 3.12 x64 | dp | O(K·N log N) | AC | 0.421 s | 552 KB |
| [1167_dp.rs](1167_dp.rs) | Rust 1.75 x64 | dp | O(K·N log N) | AC | 0.031 s | 244 KB |
