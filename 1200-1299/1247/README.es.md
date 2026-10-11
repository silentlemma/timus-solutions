# 1247. Ningún tramo pesa más que su longitud más N

[Timus 1247](https://acm.timus.ru/problem.aspx?space=1&num=1247) · dificultad 241 · dp

Problema original de Alexander Mironenko, del Concurso Individual de la Universidad Estatal de los Urales, 1 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una secuencia A_1 … A_S de enteros de 0 a 100 suma S + N
(S, N ≤ 30 000). Hay que decidir si todo tramo cumple
`A_i + … + A_j ≤ (j − i + 1) + N`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

S y N, y luego los S números.

## Salida

`YES` o `NO`.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3
2
3
0
2
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
4 5
1
0
5
3
```

Salida:

```
NO
```

## Solución

Restando 1 a cada elemento, la condición pasa a ser «ningún tramo de
`B_i = A_i − 1` suma más de N». Así que solo importa la mayor suma de un
tramo, y el algoritmo de Kadane la halla en una pasada: la mejor suma de
un tramo que acaba en i es `max(anterior, 0) + B_i`, y la respuesta es la
mayor de ellas comparada con N. `O(S)`.

La secuencia entera suma exactamente N en B, así que la respuesta es NO
justo cuando quitar un prefijo o un sufijo de suma negativa deja un tramo
más pesado.

Detalles a tener en cuenta:

- un cero al principio ya hace demasiado pesado el resto (prueba 04);
- un tramo de un solo elemento también cuenta.

## Notas por lenguaje

- Todos los lenguajes hacen el mismo recorrido de una pasada.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1247_dp.cpp](1247_dp.cpp) | G++ 13.2 x64 | dp | O(S) | AC | 0.031 s | 124 KB |
| [1247_dp.go](1247_dp.go) | Go 1.14 x64 | dp | O(S) | AC | 0.031 s | 1348 KB |
| [1247_dp.java](1247_dp.java) | Java 1.8 | dp | O(S) | AC | 0.109 s | 528 KB |
| [1247_dp.py](1247_dp.py) | Python 3.12 x64 | dp | O(S) | AC | 0.093 s | 1312 KB |
| [1247_dp.rs](1247_dp.rs) | Rust 1.75 x64 | dp | O(S) | AC | 0.062 s | 840 KB |
