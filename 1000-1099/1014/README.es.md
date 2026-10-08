# 1014. El menor número con un producto de dígitos dado

[Timus 1014](https://acm.timus.ru/problem.aspx?space=1&num=1014) · dificultad 94 · greedy

Problema original del Ural State University Internal Contest '99 #2.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dado `N` (`0 ≤ N ≤ 10^9`), encuentra el menor entero positivo `Q` cuyos
dígitos decimales multiplicados den exactamente `N`, o indica que no existe.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El entero `N`.

## Salida

`Q`, o `-1` si no existe tal número.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
36
```

Salida:

```
49
```

### Ejemplo 2

Entrada:

```
0
```

Salida:

```
10
```

## Solución

Primero, dos casos especiales:

- `N = 0`: un número tiene producto de dígitos 0 exactamente cuando contiene
  un cero, y el menor de esos números positivos es `10`;
- `N = 1`: la respuesta es `1` (no un número vacío).

En otro caso ningún dígito es 0 o 1 (un 1 solo alarga el número), así que
`Q` está formado por dígitos 2–9. Un número más corto es menor, y entre los
de igual longitud el menor es el que tiene los dígitos en orden creciente.
Así que hay que escribir `N` como producto del menor número de dígitos.

**Voraz:** se divide `N` entre 9 mientras se pueda, luego entre 8, 7, ..., 2,
y se van guardando los dígitos. Si queda algo distinto de 1, `N` tiene un
factor primo mayor que 7 y la respuesta es `-1`. Se imprimen los dígitos
guardados en orden creciente.

Por qué primero los dígitos grandes: las potencias de 3 se empaquetan mejor
en nueves (dos treses en un dígito), las de 2 en ochos, y un 3 y un 2
sobrantes forman un 6 en vez de dos dígitos; dividir entre 9, 8, ..., 2 en
ese orden produce justo ese empaquetado. `O(log N)` pasos.

Detalles a tener en cuenta:

- `N = 0` y `N = 1`;
- la respuesta puede tener 12 dígitos (`10^9 = 2^9 · 5^9` da
  `555555555888`): no la guardes en un entero de 32 bits; imprime los
  dígitos como cadena.

## Notas por lenguaje

El mismo voraz en todos los lenguajes; los dígitos se juntan en una cadena.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1014_greedy.cpp](1014_greedy.cpp) | G++ 13.2 x64 | greedy | O(log N) | AC | 0.015 s | 192 KB |
| [1014_greedy.go](1014_greedy.go) | Go 1.14 x64 | greedy | O(log N) | AC | 0.031 s | 1096 KB |
| [1014_greedy.java](1014_greedy.java) | Java 1.8 | greedy | O(log N) | AC | 0.125 s | 1604 KB |
| [1014_greedy.py](1014_greedy.py) | Python 3.12 x64 | greedy | O(log N) | AC | 0.093 s | 444 KB |
| [1014_greedy.rs](1014_greedy.rs) | Rust 1.75 x64 | greedy | O(log N) | AC | 0.046 s | 232 KB |
