# 1047. El primer término desconocido de una recurrencia de segundo orden

[Timus 1047](https://acm.timus.ru/problem.aspx?space=1&num=1047) · dificultad 303 · math

Problema original de Dmitry Filimonenkov, del concurso universitario de programación de la Universidad Estatal de los Urales, 25 de marzo de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una sucesión `a0, a1, …, aN+1` (`1 ≤ N ≤ 3000`, `−2000 ≤ ai ≤ 2000`)
cumple `ai = (ai−1 + ai+1) / 2 − ci` para cada `i = 1 … N`. Dados `a0`,
`aN+1` y `c1 … cN`, todos con dos decimales, halla `a1`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`, luego `a0`, luego `aN+1` y luego `c1 … cN`, un número por línea.

## Salida

`a1` con dos decimales.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
50.50
25.50
10.15
```

Salida:

```
27.85
```

### Ejemplo 2

Entrada:

```
2
0.00
9.00
1.00
1.00
```

Salida:

```
1.00
```

## Solución

Se reescribe la relación con las diferencias `d[i] = a[i] − a[i−1]`:

```text
a[i+1] − 2·a[i] + a[i−1] = 2·c[i]   →   d[i+1] = d[i] + 2·c[i]
```

Así que `d[k] = d[1] + 2·(c[1] + … + c[k−1])`, y al sumar todas las
diferencias de `d[1]` a `d[N+1]`, cada `c[i]` aparece `N + 1 − i` veces:

```text
a[N+1] − a[0] = (N + 1)·d[1] + 2 · Σ (N + 1 − i)·c[i]
a[1] = a[0] + d[1] = (N·a[0] + a[N+1] − 2 · Σ (N + 1 − i)·c[i]) / (N + 1)
```

`O(N)`. Para evitar problemas de redondeo, las soluciones trabajan en
centésimas: todas las entradas pasan a ser enteras, el numerador queda por
debajo de unos `10^12`, y la división entre `N + 1` es exacta para una
entrada coherente (por si acaso se redondea a la centésima más cercana).

Detalles a tener en cuenta:

- sumar 3000 términos en coma flotante puede desviarse, y la salida debe
  mostrar exactamente dos decimales; los enteros en centésimas evitan
  ambas cosas;
- una respuesta negativa entre −1 y 0 debe imprimirse como `-0.35`, no
  como `0.35` ni `-0.-35`.

## Notas por lenguaje

- **C++**, **Go**, **Java**, **Rust**: enteros de 64 bits en centésimas.
- **Python**: `Fraction` exactas leídas de las cadenas decimales.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1047_math.cpp](1047_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 156 KB |
| [1047_math.go](1047_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.015 s | 1140 KB |
| [1047_math.java](1047_math.java) | Java 1.8 | math | O(N) | AC | 0.093 s | 1460 KB |
| [1047_math.py](1047_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.109 s | 1068 KB |
| [1047_math.rs](1047_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.031 s | 264 KB |
