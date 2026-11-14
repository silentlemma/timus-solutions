# 2182. Botellas que se multiplican según los unos del número de su caja

[Timus 2182](https://acm.timus.ru/problem.aspx?space=1&num=2182) · dificultad 663 · dp, combinatorics

Problema original de Artyom Kutuzov, del Concurso por Equipos de Programación de los Urales 2024.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las botellas numeradas 1 … 2ⁿ − 1 van a las cajas con los mismos
números. Meter una botella en la caja k crea una botella nueva con número
popcount(k), la cantidad de unos de k en binario, salvo que sea el propio
k; la nueva botella va a su caja y hace lo mismo. Para q cajas, imprimir
cuántas botellas acaban en ellas. Los límites son 1 segundo y 256 MB.

## Entrada

n, 1 ≤ n ≤ 60, q, 1 ≤ q ≤ 10⁵, y luego los números de caja,
1 ≤ aᵢ ≤ 2ⁿ − 1.

## Salida

El número de botellas de cada caja pedida.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
2
8 4
```

Salida:

```
1 6
```

## Solución

Cada botella que cae en la caja j envía una botella a la caja popcount(j)
cuando esta es distinta de j. Así que, con c(k) la cuenta final de la
caja k,

c(k) = 1 + Σ c(j) sobre las cajas j ≠ k con popcount(j) = k.

Ninguna caja por encima de 60 recibe nada, porque un número menor que
2⁶⁰ tiene a lo sumo 60 unos, así que esas cajas tienen una botella. Para
k ≤ 60 las cajas j con popcount(j) = k son C(n, k) números; todas menos
las pocas que son a lo sumo 60 tienen una botella cada una, así que c(k)
es C(n, k) más 1 más las botellas extra de las cajas pequeñas k < j ≤ 60 con
popcount(j) = k, menos una por j = k cuando k = 1. Como popcount(j) < j
para j > 1, rellenar c desde 60 hasta 1 solo usa valores ya calculados.
La mayor cuenta, unos 2⁶⁰, cabe en 64 bits, y cada consulta es una
búsqueda en la tabla.

En el ejemplo la caja 4 recibe su propia botella y una de cada una de las
C(5, 4) = 5 cajas 15, 23, 27, 29 y 30.

## Soluciones optimizadas

Se calculan los coeficientes binomiales sucesivamente sin construir el triángulo de Pascal. Cada caja pequeña envía sus botellas adicionales a una única caja menor, cuyo índice es la cantidad de bits activos. Se guarda el texto de los recuentos para responder al leer cada consulta.

**Envíos de las versiones optimizadas en Timus**

`2182_dp_combinatorics_optimized.cpp` (G++ 13.2 x64) №11320975 · `2182_dp_combinatorics_optimized.java` (Java 1.8) №11317427 · `2182_dp_combinatorics_optimized.py` (Python 3.12 x64) №11317438.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321973 · Go 1.14 x64 №11321784 · Java 1.8 №11321975 · Python 3.12 x64 №11321977 · Rust 1.75 x64 №11321980.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2182_dp_combinatorics.cpp](2182_dp_combinatorics.cpp) | G++ 13.2 x64 | dp, combinatorics | O(60^2 + q) | AC | 0.125 s | 668 KB | 11321973 |
| [2182_dp_combinatorics.go](2182_dp_combinatorics.go) | Go 1.14 x64 | dp, combinatorics | O(60^2 + q) | AC | 0.031 s | 4308 KB | 11321784 |
| [2182_dp_combinatorics.java](2182_dp_combinatorics.java) | Java 1.8 | dp, combinatorics | O(60^2 + q) | AC | 0.14 s | 24916 KB | 11321975 |
| [2182_dp_combinatorics.py](2182_dp_combinatorics.py) | Python 3.12 x64 | dp, combinatorics | O(60^2 + q) | AC | 0.109 s | 12936 KB | 11321977 |
| [2182_dp_combinatorics.rs](2182_dp_combinatorics.rs) | Rust 1.75 x64 | dp, combinatorics | O(60^2 + q) | AC | 0.046 s | 6904 KB | 11321980 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [2182_dp_combinatorics_optimized.java](2182_dp_combinatorics_optimized.java) | Java 1.8 | dp, combinatorics | O(n + q) | AC | 0.14 s | 500 KB | 11317427 |
| [2182_dp_combinatorics_optimized.py](2182_dp_combinatorics_optimized.py) | Python 3.12 x64 | dp, combinatorics | O(n + q) | AC | 0.109 s | 1876 KB | 11317438 |
| [2182_dp_combinatorics_optimized.cpp](2182_dp_combinatorics_optimized.cpp) | G++ 13.2 x64 | dp, combinatorics | O(n + q) | AC | 0.031 s | 160 KB | 11320975 |
| [2182_dp_combinatorics_optimized.go](2182_dp_combinatorics_optimized.go) | Go 1.14 x64 | dp, combinatorics | O(n + q) | AC | 0.046 s | 924 KB | 11322385 |
| [2182_dp_combinatorics_optimized.rs](2182_dp_combinatorics_optimized.rs) | Rust 1.75 x64 | dp, combinatorics | O(n + q) | AC | 0.031 s | 212 KB | 11322386 |
