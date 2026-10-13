# 1483. Futbolín

[Timus 1483](https://acm.timus.ru/problem.aspx?space=1&num=1483) · dificultad 384 · math

Problema original de Sergey Pupyrev, del Campeonato de la Universidad Estatal de los Urales, 7 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N equipos (1 ≤ N ≤ 1000) juegan una liga a una vuelta: cada pareja se
enfrenta una vez, una victoria da 3 puntos, un empate 1 y una derrota 0.
Los equipos con los mismos puntos comparten puesto. Un equipo quedó
primero y otro último. Hay que hallar el menor número de puntos que
pudo tener el primero y el mayor que pudo tener el último.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N.

## Salida

Los dos números.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
1 1
```

## Solución

Cada partido reparte al menos 2 puntos (un empate) y como mucho 3 (una
victoria). Así que entre todos suman al menos N(N − 1) puntos y el
líder tiene al menos la media N − 1; si todos los partidos acaban en
empate, cada equipo tiene exactamente N − 1.

Entre todos suman como mucho 3·N(N − 1)/2 puntos, así que el último
tiene como mucho ⌊3(N − 1)/2⌋. Con N impar cada equipo puede ganar
justo la mitad de sus N − 1 partidos, y todos tienen 3(N − 1)/2. Con N
par, los equipos empatan por parejas, un empate cada uno, y el resto de
partidos se reparte para que cada equipo gane la mitad de sus otros
N − 2: todos tienen 3(N − 2)/2 + 1 = ⌊3(N − 1)/2⌋. `O(1)`.

Detalles a tener en cuenta:

- con un solo equipo no hay partidos: 0 y 0 (prueba 02);
- con N par la cota necesita un empate por equipo, porque sin empates
  los puntos son múltiplos de 3 (prueba 04);
- las dos respuestas se optimizan por separado, no en la misma liga
  (prueba 03).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1483_math.cpp](1483_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.001 s | 128 KB |
| [1483_math.go](1483_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1084 KB |
| [1483_math.java](1483_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1588 KB |
| [1483_math.py](1483_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 320 KB |
| [1483_math.rs](1483_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 232 KB |
