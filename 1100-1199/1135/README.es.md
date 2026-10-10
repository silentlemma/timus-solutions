# 1135. Contar los giros de reclutas cara a cara hasta que la fila se estabiliza

[Timus 1135](https://acm.timus.ru/problem.aspx?space=1&num=1135) · dificultad 160 · math

Problema original del cuarto de final de la región central de Rusia, Rybinsk, 17–18 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N ≤ 30000` reclutas están en fila, cada uno mirando a la izquierda (`<`)
o a la derecha (`>`). Cada segundo, todas las parejas de vecinos que se
miran (`><`) se dan la vuelta a la vez. Cuenta los giros de parejas hasta
que nada cambia, o imprime `NO` si el proceso no termina nunca.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego exactamente `N` caracteres `<` y `>` repartidos en líneas de
hasta 255 caracteres.

## Salida

El número de giros de parejas.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
>><<><
```

Salida:

```
7
```

## Solución

Una pareja que gira, `><`, se convierte en `<>`: en cuanto a las
direcciones, es un intercambio de dos vecinos. Cada intercambio elimina
exactamente un par de reclutas (no necesariamente vecinos) con un `>`
antes de un `<`, y no crea ninguno. La fila es estable justo cuando no
queda ningún `><`, es decir, cuando todos los `<` están antes de todos los
`>`, y entonces no hay ningún par así. Por tanto el proceso siempre
termina, `NO` nunca se imprime, y el número de giros es el número de
pares con `>` antes de `<`. Una pasada los cuenta: se lleva el número de
`>` vistos hasta el momento y se suma en cada `<`. `O(N)`.

Detalles a tener en cuenta:

- la fila está repartida en varias líneas, quizá con alguna vacía, así
  que se leen caracteres hasta reunir `N`;
- la respuesta llega a `15000² = 2,25·10⁸`, que aún cabe en 32 bits, pero
  los contadores de 64 bits no cuestan nada;
- el orden de los giros dentro de un segundo no afecta a la cuenta.

Las respuestas se compararon con una simulación segundo a segundo en 200
filas aleatorias de hasta 300 reclutas.

## Notas por lenguaje

- Todos los lenguajes saltan los saltos de línea y llevan la misma cuenta
  acumulada.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1135_math.cpp](1135_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 132 KB |
| [1135_math.go](1135_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 1100 KB |
| [1135_math.java](1135_math.java) | Java 1.8 | math | O(N) | AC | 0.125 s | 532 KB |
| [1135_math.py](1135_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.078 s | 420 KB |
| [1135_math.rs](1135_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.031 s | 248 KB |
