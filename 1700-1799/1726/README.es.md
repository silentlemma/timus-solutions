# 1726. Visitas

[Timus 1726](https://acm.timus.ru/problem.aspx?space=1&num=1726) · dificultad 120 · sorting

Problema original de Denis Dublennykh, del Concurso Regional de Programación por Equipos de los Urales 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los n miembros de un comité viven en cruces de calles de una ciudad en
cuadrícula y se visitan caminando por las calles por caminos más
cortos. Todos visitan a todos con la misma frecuencia. Hallar la
distancia media recorrida, redondeada hacia abajo.

## Entrada

n (2 ≤ n ≤ 10⁵) en la primera línea y luego n líneas con las
coordenadas x e y (1 ≤ x, y ≤ 10⁶).

## Salida

La distancia media entre las casas de dos miembros, redondeada hacia
abajo.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
10 10
20 20
10 20
```

Salida:

```
13
```

## Solución

Un camino más corto por las calles mide |dx| + |dy|, así que la suma
sobre todos los pares se separa en la suma de |x_i − x_j| y la de
|y_i − y_j|. Se ordenan los x: el i-ésimo (desde 0) es al menos cada
uno de los i anteriores, así que aporta i·x_i menos la suma de ellos,
que lleva un total acumulado. Con y igual. La media sobre los
n(n − 1)/2 pares es esa suma dividida entre el número de pares,
redondeada hacia abajo. `O(n log n)`.

En el ejemplo las distancias son 20, 10 y 10, así que la media es
40/3, que redondeada hacia abajo da 13.

Trampas:

- la suma llega a unos 5·10¹⁵ cuando la mitad de las casas está en una
  esquina lejana y la otra mitad en la opuesta, así que necesita
  64 bits;
- comparar todos los pares cuesta unos 5·10⁹ pasos, demasiados.

Las medias coinciden con una suma sobre todos los pares en 300 mapas
pequeños aleatorios, y con una implementación aceptada independiente en
las pruebas grandes.

## Soluciones optimizadas

La solución optimizada en C++ guarda las coordenadas en arreglos
estáticos `int`, que bastan porque no pasan de 10⁶, en lugar de vectores
de `long long`, y analiza los 2·10⁵ números a mano en bloques de 4 KB
leídos con `fread` en lugar de llamar a `scanf` para cada uno; las sumas
se siguen calculando en `long long`: {1726_sorting_optimized.cpp}.

La solución optimizada en Go analiza los 2·10⁵ números a mano desde un
lector con búfer de 64 KB en lugar de usar `fmt.Fscan`, que es la parte
lenta del programa sencillo: {1726_sorting_optimized.go}.

La solución optimizada en Python lee las líneas en tandas de unos 64 KB
en arreglos de enteros de 32 bits, que bastan porque las coordenadas no
pasan de 10⁶, en lugar de conservar cada token de la entrada como cadena
de bytes y dos listas de enteros de Python. Además calcula cada suma sin
un bucle en Python: en orden, el valor `i`-ésimo de `n` (desde 0) es
mayor o igual que los `i` anteriores y menor o igual que los
`n − 1 − i` siguientes, así que entra en la suma con peso
`2i − (n − 1)`, y `sum(map(mul, …))` sobre los valores ordenados y un
`range` de pesos se ejecuta entero en C:
{1726_sorting_optimized.py}.

La solución optimizada en Rust analiza los números a mano en bloques de
4 KB en lugar de leer toda la entrada en una cadena, y guarda las
coordenadas como `u32`, que basta porque no pasan de 10⁶, en lugar de
`i64`; las sumas se calculan en `u64`: {1726_sorting_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1726_sorting_optimized.cpp`: reducción de tiempo +91.23%; reducción
  de memoria +49.43%; base: `1726_sorting.cpp`.

- `1726_sorting_optimized.go`: reducción de tiempo +70.51%; reducción de
  memoria +37.78%; base: `1726_sorting.go`.

- `1726_sorting_optimized.py`: reducción de tiempo +0.00%; reducción de
  memoria +70.45%; base: `1726_sorting.py`.

- `1726_sorting_optimized.rs`: reducción de tiempo +0.00%; reducción de
  memoria +79.09%; base: `1726_sorting.rs`.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1726_sorting.cpp](1726_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.171 s | 1756 KB | 11304062 |
| [1726_sorting.go](1726_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.156 s | 4404 KB | 11304355 |
| [1726_sorting.java](1726_sorting.java) | Java 1.8 | sorting | O(n log n) | AC | 0.125 s | 2092 KB | 11304357 |
| [1726_sorting.py](1726_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.187 s | 20644 KB | 11304063 |
| [1726_sorting.rs](1726_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.031 s | 4744 KB | 11304064 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1726_sorting_optimized.cpp](1726_sorting_optimized.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.015 s | 888 KB | 11304358 |
| [1726_sorting_optimized.go](1726_sorting_optimized.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.046 s | 2740 KB | 11304362 |
| [1726_sorting_optimized.py](1726_sorting_optimized.py) \* | Python 3.12 x64 | sorting | O(n log n) | AC | 0.187 s | 6100 KB | 11304360 |
| [1726_sorting_optimized.rs](1726_sorting_optimized.rs) \* | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.031 s | 992 KB | 11304361 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
