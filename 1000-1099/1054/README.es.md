# 1054. El número de paso de una posición de la Torre de Hanói

[Timus 1054](https://acm.timus.ru/problem.aspx?space=1&num=1054) · dificultad 643 · math

Problema original de la Academia Estatal de Aviación de Rybinsk.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N` discos (`1 ≤ N ≤ 31`, el disco 1 es el más pequeño) empiezan en la
varilla 1 y se llevan a la varilla 2 con la recursión óptima clásica

```text
Hanoi(n, from, to, via):
    si n > 0:
        Hanoi(n − 1, from, via, to)
        mover el disco n de `from` a `to`
        Hanoi(n − 1, via, to, from)
```

llamada como `Hanoi(N, 1, 2, 3)`. Una posición da la varilla de cada
disco. Halla tras cuántos movimientos aparece la posición dada, o `-1` si
no aparece nunca.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego las varillas `D1 … DN` de los discos `1 … N`, una por línea.

## Salida

El número de movimientos, o `-1`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
3
3
1
```

Salida:

```
3
```

### Ejemplo 2

Entrada:

```
1
3
```

Salida:

```
-1
```

## Solución

Se sigue la recursión desde el disco más grande hacia abajo. Mientras los
discos `1 … k` se llevan de `a` a `b` pasando por `c`, el disco `k` se
mueve exactamente una vez, tras los primeros `2^(k−1) − 1` movimientos
(que llevan los discos `1 … k − 1` a `c`). Así:

- el disco `k` sigue en `a`: estamos en la primera mitad; se sigue con los
  discos `1 … k − 1` que van de `a` a `c` pasando por `b`;
- el disco `k` está en `b`: la primera mitad y el movimiento del disco
  `k` ya se hicieron, son `2^(k−1)` movimientos; se sigue con los discos
  `1 … k − 1` que van de `c` a `b` pasando por `a`;
- el disco `k` está en `c`: esto nunca ocurre, la respuesta es `-1`.

La suma de `2^(k−1)` de todos los discos que están en su varilla de
destino da el número de paso. `O(N)`.

Detalles a tener en cuenta:

- las varillas intercambian sus papeles en cada nivel; que el disco más
  pequeño vaya primero a la varilla 2 o a la 3 depende de la paridad de
  `N`;
- la posición final de 31 discos se alcanza tras `2^31 − 1` movimientos,
  así que hacen falta enteros de 64 bits (o de 32 sin signo);
- un solo disco en la varilla «equivocada» hace inalcanzable toda la
  posición.

## Notas por lenguaje

- Todos los lenguajes recorren los discos con el mismo bucle y tres
  variables para los papeles de las varillas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1054_math.cpp](1054_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.031 s | 196 KB |
| [1054_math.go](1054_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.015 s | 1084 KB |
| [1054_math.java](1054_math.java) | Java 1.8 | math | O(N) | AC | 0.125 s | 1620 KB |
| [1054_math.py](1054_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.093 s | 396 KB |
| [1054_math.rs](1054_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 216 KB |
