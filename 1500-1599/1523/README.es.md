# 1523. K-inversiones

[Timus 1523](https://acm.timus.ru/problem.aspx?space=1&num=1523) · dificultad 296 · fenwick

Problema original de Dmitry Gozman, del Dmitry Gozman Contest 1 en el campus de invierno de Petrozavodsk, enero de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una permutación a1, …, an de 1 … n (1 ≤ n ≤ 20000), hay que contar
sus k-inversiones (2 ≤ k ≤ 10): sucesiones de índices
i1 < i2 < … < ik con ai1 > ai2 > … > aik. Se escribe la cuenta módulo
10⁹.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n y k, y luego la permutación.

## Salida

El número de k-inversiones módulo 10⁹.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 2
3 1 2
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
5 3
5 4 3 2 1
```

Salida:

```
10
```

## Solución

Sea ends[i] el número de cadenas decrecientes de longitud L que acaban
en la posición i; para L = 1 vale 1 en todas partes. Una cadena de
longitud L + 1 que acaba en i es una cadena de longitud L que acaba en
una posición anterior p con ap > ai, seguida de i. Así, cada nivel es
una pasada de izquierda a derecha con un árbol de Fenwick sobre los
valores: se consulta la suma de los valores mayores que ai y luego se
suma ends[i] en ai. Contando los valores desde arriba, «mayor» se
convierte en un prefijo. k − 1 pasadas dan `O(n·k·log n)`.

Detalles a tener en cuenta:

- k puede superar la longitud de la cadena decreciente más larga, o
  incluso n, y entonces la respuesta es 0 (pruebas 04, 05, gen3);
- las cuentas crecen como C(20000, 10), así que hay que reducirlas
  módulo 10⁹ al sumarlas (gen2, gen5).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1523_fenwick.cpp](1523_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(n * k * log n) | AC | 0.031 s | 596 KB |
| [1523_fenwick.go](1523_fenwick.go) | Go 1.14 x64 | fenwick | O(n * k * log n) | AC | 0.031 s | 4576 KB |
| [1523_fenwick.java](1523_fenwick.java) | Java 1.8 | fenwick | O(n * k * log n) | AC | 0.125 s | 3512 KB |
| [1523_fenwick.py](1523_fenwick.py) | Python 3.12 x64 | fenwick | O(n * k * log n) | AC | 0.562 s | 5172 KB |
| [1523_fenwick.rs](1523_fenwick.rs) | Rust 1.75 x64 | fenwick | O(n * k * log n) | AC | 0.031 s | 1292 KB |
