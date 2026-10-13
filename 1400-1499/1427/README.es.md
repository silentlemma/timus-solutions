# 1427. SMS

[Timus 1427](https://acm.timus.ru/problem.aspx?space=1&num=1427) · dificultad 364 · greedy

Problema original de Dmitry Kovalioff, Nikita Rybak e Ilya Grebnov, de Timus Top Coders: First Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un texto de hasta 100 000 caracteres (letras latinas, espacios, cifras
y los signos . , ; : ! ? - ") se corta en mensajes SMS consecutivos. Un
mensaje de solo letras y espacios puede tener hasta M caracteres;
cualquier otro, solo hasta N (1 ≤ N ≤ M ≤ 10 000). Hay que hallar el
menor número de mensajes.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

N y M, luego el texto en su propia línea.

## Salida

El menor número de mensajes.

## Ejemplos

### Ejemplo 1

Entrada:

```
10 15
On the 11-th of February, 2006 the contest "Timus Top Coders: First Challenge" is held!
```

Salida:

```
8
```

## Solución

Sea run(i) el número de letras y espacios seguidos desde la posición i.
Un mensaje que empieza en i puede terminar en cualquier punto hasta
i + max(N, min(M, run(i))). Este final más lejano nunca retrocede al
crecer i (tanto i + N como el final del tramo de letras solo crecen), y
con un alcance monótono así el voraz que siempre envía el mensaje más
largo posible es óptimo: cualquier otro plan nunca va más adelantado en
ningún paso. Los tramos se cuentan desde el final del texto. `O(L)`.

Detalles a tener en cuenta:

- el texto puede empezar con espacios, así que la segunda línea debe
  leerse entera y no tras saltar blancos (prueba 04);
- las cifras no cuentan como letras (pruebas 03, 06);
- la forma larga solo ayuda cuando el tramo de letras es más largo que
  N (prueba 05).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1427_greedy.cpp](1427_greedy.cpp) | G++ 13.2 x64 | greedy | O(L) | AC | 0.031 s | 924 KB |
| [1427_greedy.go](1427_greedy.go) | Go 1.14 x64 | greedy | O(L) | AC | 0.031 s | 3196 KB |
| [1427_greedy.java](1427_greedy.java) | Java 1.8 | greedy | O(L) | AC | 0.093 s | 1612 KB |
| [1427_greedy.py](1427_greedy.py) | Python 3.12 x64 | greedy | O(L) | AC | 0.093 s | 4392 KB |
| [1427_greedy.rs](1427_greedy.rs) | Rust 1.75 x64 | greedy | O(L) | AC | 0.031 s | 1252 KB |
