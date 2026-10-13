# 1492. El padre de Vasia 2

[Timus 1492](https://acm.timus.ru/problem.aspx?space=1&num=1492) · dificultad 1995 · math

Problema original de Fedor Fominykh, del Decimotercer Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 14 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una función lineal a trozos viene dada por N vértices (2 ≤ N ≤ 30000,
coordenadas enteras de hasta 15000 en valor absoluto) con x creciente,
x_1 = −x_N y sin tres vértices consecutivos alineados. ¿Puede escribirse
como suma de una función lineal a trozos par y otra impar? Se escribe
«Yes» y los vértices de la parte par y luego los de la impar, con al
menos cuatro decimales, o «No».

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego N líneas x y.

## Salida

«Yes» y las dos listas de vértices, o «No».

## Ejemplos

### Ejemplo 1

Entrada:

```
2
-1 0
1 0
```

Salida:

```
Yes
-1.0000 0.0000
1.0000 0.0000
-1.0000 0.0000
1.0000 0.0000
```

## Solución

Toda función en [−a, a] se descompone de una sola manera:
E(x) = (f(x) + f(−x))/2 es par, O(x) = (f(x) − f(−x))/2 es impar y su
suma es f. Así que la respuesta siempre es «Yes», y las dos partes están
determinadas.

Ambas partes son lineales entre los puntos de f y sus reflejos, así que
esos x, ordenados y sin repetir, son los vértices candidatos; los
valores salen de f por interpolación. Un candidato solo se queda donde
la parte se dobla de verdad, porque no puede haber tres vértices
consecutivos alineados. La pendiente de E entre dos candidatos es
(a/b − c/d)/2, donde a/b es la pendiente de f ahí y c/d la de f en el
trozo reflejado; O usa un signo más. Comparar dos de esas fracciones
multiplicando en cruz es exacto, y todos los factores quedan por debajo
de 2·10⁹, así que bastan 64 bits. `O(N log N)`.

Detalles a tener en cuenta:

- «No» nunca es la respuesta (todas las pruebas);
- un punto reflejado a menudo no es un pliegue de una de las partes, y
  conservarlo deja tres vértices alineados (pruebas 05, 07, gen3, gen4);
- una entrada par o impar deja la otra parte como un cero recto con solo
  dos vértices (pruebas 01, 02, 03, 05, 07);
- los pliegues deben hallarse con pendientes exactas, no comparando
  valores interpolados en coma flotante (gen5, prueba 07).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1492_math.cpp](1492_math.cpp) | G++ 13.2 x64 | math | O(N log N) | AC | 0.187 s | 1700 KB |
| [1492_math.go](1492_math.go) | Go 1.14 x64 | math | O(N log N) | AC | 0.125 s | 5884 KB |
| [1492_math.java](1492_math.java) | Java 1.8 | math | O(N log N) | AC | 0.546 s | 17680 KB |
| [1492_math.py](1492_math.py) | Python 3.12 x64 | math | O(N log N) | AC | 0.468 s | 23408 KB |
| [1492_math.rs](1492_math.rs) | Rust 1.75 x64 | math | O(N log N) | AC | 0.062 s | 4672 KB |
