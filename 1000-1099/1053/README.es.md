# 1053. Cortar piezas hasta que quede una

[Timus 1053](https://acm.timus.ru/problem.aspx?space=1&num=1053) · dificultad 343 · number_theory

Problema original de la Academia Estatal de Aviación de Rybinsk.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N` piezas (`1 ≤ N ≤ 1000`) con longitudes enteras de 1 a `2^31 − 1`.
Mientras quede más de una pieza, se toman dos cualesquiera: si son
iguales, se tira una; si no, se corta de la más larga un trozo tan largo
como la más corta y se tira ese trozo. Imprime la longitud de la última
pieza, o `IMPOSSIBLE` si depende de las elecciones.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` longitudes, una por línea.

## Salida

La longitud de la última pieza.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
2
3
4
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
4
12
18
30
42
```

Salida:

```
6
```

## Solución

Los dos pasos conservan el máximo común divisor de todas las longitudes:
`gcd(a, b) = gcd(a − b, b)`, y tirar una de dos piezas iguales no cambia
el conjunto de divisores. El proceso termina con una sola pieza, y el mcd
de un número es el propio número, así que la última pieza es siempre el
mcd de las longitudes iniciales, se elija como se elija. `IMPOSSIBLE`
nunca es la respuesta. `O(N log L)`.

Es la forma por restas del algoritmo de Euclides, aplicada a muchos
números a la vez.

Detalles a tener en cuenta:

- las longitudes llegan a `2^31 − 1`: léelas en enteros de 64 bits o al
  menos en enteros sin signo de 32 bits;
- una sola pieza es la respuesta por sí misma;
- simular los cortes uno a uno es demasiado lento para longitudes como
  `2^31 − 1` y 1.

## Notas por lenguaje

- Todos los lenguajes pliegan las longitudes con el algoritmo de
  Euclides.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1053_number_theory.cpp](1053_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log L) | AC | 0.015 s | 132 KB |
| [1053_number_theory.go](1053_number_theory.go) | Go 1.14 x64 | number_theory | O(N log L) | AC | 0.015 s | 1100 KB |
| [1053_number_theory.java](1053_number_theory.java) | Java 1.8 | number_theory | O(N log L) | AC | 0.093 s | 776 KB |
| [1053_number_theory.py](1053_number_theory.py) | Python 3.12 x64 | number_theory | O(N log L) | AC | 0.078 s | 488 KB |
| [1053_number_theory.rs](1053_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log L) | AC | 0.015 s | 244 KB |
