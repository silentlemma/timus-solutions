# 1586. Números triprimos

[Timus 1586](https://acm.timus.ru/problem.aspx?space=1&num=1586) · dificultad 144 · dp

Problema original de Denis Musin, de la subregión oriental del NEERC del ACM ICPC 2007–2008, Ekaterimburgo, 27 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un número es triprimo cuando cada tres cifras vecinas forman un primo de
tres cifras. Hay que contar los números triprimos de n cifras
(3 ≤ n ≤ 10000) módulo 10⁹ + 9.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

n.

## Salida

La cuenta módulo 10⁹ + 9.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
```

Salida:

```
204
```

## Solución

Que una cifra pueda seguir depende solo de las dos últimas cifras, así
que los números se cuentan por ellas. Para n = 3 cada primo de tres
cifras cuenta una vez, bajo sus dos últimas cifras. Cada cifra c
siguiente se añade a un número que acaba en ab exactamente cuando abc es
un primo de tres cifras, y el número nuevo acaba en bc. Los 143 primos
de tres cifras dan 143 transiciones por cifra: `O(143·n)`. Los
resultados se contrastaron con comprobar todos los números de hasta seis
cifras.

Detalles a tener en cuenta:

- un primo de tres cifras no puede empezar por 0, así que ninguna
  ventana puede empezar por una cifra cero; contar por los propios
  primos ya lo tiene en cuenta;
- la cuenta crece deprisa y se toma módulo 10⁹ + 9, no 10⁹ + 7.

## Soluciones optimizadas

La solución optimizada en C++ guarda una sola vez, en arreglos fijos, el
par de dígitos de origen y de destino de cada transición por un primo,
en lugar de calcular `p / 10` y `p % 100` de nuevo en cada dígito, y
reutiliza dos arreglos fijos de conteos en lugar de un `vector` nuevo
por dígito. Los conteos son `int` en lugar de `long long`, y cada suma
se reduce con una resta condicional en lugar de `%`: dos restos menores
que 10⁹ + 9 suman menos de 2³¹: {1586_dp_optimized.cpp}.

La solución optimizada en Go guarda una sola vez, en arreglos fijos, el
par de dígitos de origen y de destino de cada transición por un primo, y
reutiliza dos arreglos fijos de conteos en lugar de un slice nuevo por
dígito; cada suma se reduce con una resta condicional en lugar de `%`:
{1586_dp_optimized.go}.

La solución optimizada en Java lee `n` byte a byte con `System.in.read`
en lugar de un `Scanner`, guarda el par de dígitos de origen y de
destino de cada transición en arreglos de `int` en lugar de recorrer una
lista de primos `Integer`, e intercambia dos arreglos de conteos en
lugar de crear uno nuevo por dígito. Los conteos son `int` en lugar de
`long`, y cada suma se reduce con una resta condicional en lugar de `%`:
dos restos menores que 10⁹ + 9 suman menos de 2³¹:
{1586_dp_optimized.java}.

Para `n = 3` la solución optimizada en Python imprime el número de
primos de tres cifras, 143. Para `n ≥ 4` eleva una matriz de
transiciones a una potencia en lugar de recorrer los `n` dígitos. A
partir del cuarto dígito, los dos últimos dígitos terminan cada uno un
primo de tres cifras, así que cada uno es 1, 3, 7 o 9 y quedan solo 16
pares; una matriz de 16 × 16 cuenta los primos que llevan de un par a
otro. Los conteos para cuatro dígitos multiplicados por esa matriz
elevada a `n − 4`, calculada elevando al cuadrado como mucho 14 veces
para `n ≤ 10000`, dan la respuesta, `O(16³ log n)` en total:
{1586_dp_matrix.py}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1586_dp_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +47.06%; base: `1586_dp.cpp`.

- `1586_dp_optimized.go`: reducción de tiempo +0.00%; reducción de
  memoria +83.27%; base: `1586_dp.go`.

- `1586_dp_optimized.java`: reducción de tiempo +36.26%; reducción de
  memoria +93.08%; base: `1586_dp.java`.

- `1586_dp_matrix.py`: reducción de tiempo +76.15%; reducción de memoria
  -44.26%; base: `1586_dp.py`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1586_dp.rs](1586_dp.rs).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1586_dp.cpp](1586_dp.cpp) | G++ 13.2 x64 | dp | O(n) | AC | 0.015 s | 204 KB | 11287946 |
| [1586_dp.go](1586_dp.go) | Go 1.14 x64 | dp | O(n) | AC | 0.031 s | 6456 KB | 11287947 |
| [1586_dp.java](1586_dp.java) | Java 1.8 | dp | O(n) | AC | 0.171 s | 6072 KB | 11287950 |
| [1586_dp.py](1586_dp.py) | Python 3.12 x64 | dp | O(n) | AC | 0.390 s | 488 KB | 11287948 |
| [1586_dp.rs](1586_dp.rs) | Rust 1.75 x64 | dp | O(n) | AC | 0.015 s | 240 KB | 11287953 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1586_dp_optimized.cpp](1586_dp_optimized.cpp) | G++ 13.2 x64 | dp | O(n) | AC | 0.015 s | 108 KB | 11304491 |
| [1586_dp_optimized.go](1586_dp_optimized.go) | Go 1.14 x64 | dp | O(n) | AC | 0.031 s | 1080 KB | 11304492 |
| [1586_dp_optimized.java](1586_dp_optimized.java) | Java 1.8 | dp | O(n) | AC | 0.109 s | 420 KB | 11304525 |
| [1586_dp_matrix.py](1586_dp_matrix.py) \* | Python 3.12 x64 | dp, matrix | O(16³ log n) | AC | 0.093 s | 704 KB | 11304526 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
