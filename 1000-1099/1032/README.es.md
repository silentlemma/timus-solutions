# 1032. Elegir números cuya suma sea múltiplo de N

[Timus 1032](https://acm.timus.ru/problem.aspx?space=1&num=1032) · dificultad 301 · prefix_sums, math

Problema original del III Campeonato Universitario por Equipos de Programación de los Urales, 1999.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados `N` enteros positivos (`1 ≤ N ≤ 10 000`, cada uno como mucho 15 000,
con repeticiones posibles), elige uno o más cuya suma sea divisible entre
`N`. Si no hay tal elección, imprime 0.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego los `N` números, uno por línea.

## Salida

La cantidad de números elegidos y luego esos números, uno por línea, en
cualquier orden; o 0.

## Evaluación

Se acepta cualquier elección válida. El verificador comprueba que cada
número se usa como mucho tantas veces como aparece, que se elige al menos
uno y que la suma es múltiplo de `N`.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
3
8
6
1
```

Salida:

```
1
8
```

### Ejemplo 2

Entrada:

```
1
15000
```

Salida:

```
1
15000
```

## Solución

**Siempre existe una elección**, e incluso puede ser un bloque de números
consecutivos. Mira las `N + 1` sumas prefijas `S_0 = 0, S_1, ..., S_N`
módulo `N`. Toman como mucho `N` valores distintos, así que por el
**principio del palomar** dos coinciden, `S_i ≡ S_j (mod N)` con `i < j`;
entonces `a_{i+1} + ... + a_j = S_j - S_i` es múltiplo de `N`.

Se recorren los números manteniendo la suma prefija módulo `N` y la primera
posición en que apareció cada resto (el resto 0 en la posición 0). El primer
resto repetido da el bloque. `O(N)`.

Así que la respuesta 0 nunca hace falta.

Detalles a tener en cuenta:

- el resto 0 debe darse por «visto» en la posición 0, para encontrar un
  prefijo que ya sea múltiplo de `N`;
- en la salida van los valores, no sus posiciones;
- `N = 1`: cualquier número sirve.

## Notas por lenguaje

La misma pasada en todos los lenguajes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1032_prefix_sums.cpp](1032_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N) | AC | 0.015 s | 232 KB |
| [1032_prefix_sums.go](1032_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N) | AC | 0.031 s | 1368 KB |
| [1032_prefix_sums.java](1032_prefix_sums.java) | Java 1.8 | prefix_sums | O(N) | AC | 0.156 s | 944 KB |
| [1032_prefix_sums.py](1032_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N) | AC | 0.093 s | 2608 KB |
| [1032_prefix_sums.rs](1032_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.046 s | 464 KB |
