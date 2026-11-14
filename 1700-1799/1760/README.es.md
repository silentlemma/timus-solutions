# 1760. Trabajo infernal

[Timus 1760](https://acm.timus.ru/problem.aspx?space=1&num=1760) · dificultad 681 · math

Problema original de Alexander Ipatov, del XI Concurso Individual Abierto de la Universidad Estatal de los Urales, 13 de marzo de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n elementos se copian en el mismo orden en dos cuadernos, a por página
en el primero y b por página en el segundo. Contar los pares de
elementos que están en una misma página del primer cuaderno pero en
páginas distintas del segundo.

## Entrada

a, b y n (1 ≤ a, b ≤ n ≤ 25 000 000).

## Salida

El número de esos pares.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 4 10
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
2 4 10
```

Salida:

```
0
```

## Solución

La respuesta son los pares en una misma página del primer cuaderno,
n div a páginas llenas de C(a, 2) pares más C(n mod a, 2), menos los
pares en una misma página de ambos. Los saltos de página de los dos
cuadernos cortan la fila en trozos, y los pares en una misma página de
ambos son la suma de C(len, 2) sobre los trozos.

Esa suma se toma página a página sobre el cuaderno de páginas más
grandes: cada una de esas páginas queda cortada por las pequeñas en un
comienzo, algunas páginas pequeñas enteras y una cola, lo que cuesta
O(1) por página grande. Los saltos de ambos cuadernos se repiten cada
L = lcm(a, b) elementos, así que cuando L ≤ n la suma de un periodo se
multiplica por n div L y se suma el resto. En cualquier caso se
recorren a lo sumo unas √n páginas grandes: si L ≤ n hay
L / max(a, b) = min(a, b) / gcd(a, b) por periodo, a lo sumo √L, y si
L > n entonces max(a, b) > √n. El trabajo es `O(√n)`.

En el primer ejemplo las páginas de 3 tienen 3 pares cada una, 9 en
total, y los saltos en 3, 4, 6, 8 y 9 cortan la fila en trozos de 3, 1,
2, 2, 1 y 1 elementos con 5 pares: 9 − 5 = 4.

Trampas:

- la respuesta llega a unos 3·10¹⁴, más de 32 bits;
- recorrer los n elementos es demasiado lento en algunos lenguajes, y
  recorrer cada página del tamaño menor también cuando es diminuto;
- lcm(a, b) puede llegar a 6·10¹⁴, así que se calcula como a / gcd · b
  en 64 bits.

Las respuestas coinciden con un recuento par a par en 300 casos
pequeños, un recuento lineal en 60 más grandes y una implementación
aceptada independiente en 100 casos hasta los límites.

## Soluciones optimizadas

Se cuentan primero las parejas de las páginas pequeñas. Un corte de página grande dentro de una pequeña descarta el producto de las longitudes de ambos lados. Se suma ese producto por fórmula en cada período completo y solo se recorren los cortes del prefijo restante.

El envío 11318053 en Java tardó 0.109 s y usó 404 KB. La versión sencilla tardó 0.156 s y usó 1572 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321937 · Java 1.8 №11321939 · Python 3.12 x64 №11321885 · Rust 1.75 x64 №11321938 · Go 1.14 x64 №11322287.

Go suma con una fórmula las contribuciones de los períodos completos y recorre los cortes restantes. Go 1.14 x64, envío 11321947. Tiempo 0,031 → 0,015 s, memoria 1132 → 288 KB.

Rust cuenta los pares con sumas recursivas de valores redondeados hacia abajo, de sus cuadrados y de sus productos por los índices. Rust 1.75 x64, envío 11323414. Tiempo 0,046 → 0,046 s, memoria 212 → 60 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1760_math.cpp](1760_math.cpp) | G++ 13.2 x64 | math | O(sqrt(n)) | AC | 0.015 s | 112 KB | 11321937 |
| [1760_math.go](1760_math.go) | Go 1.14 x64 | math | O(sqrt(n)) | AC | 0.031 s | 1132 KB | 11322287 |
| [1760_math.java](1760_math.java) | Java 1.8 | math | O(sqrt(n)) | AC | 0.156 s | 1572 KB | 11321939 |
| [1760_math.py](1760_math.py) | Python 3.12 x64 | math | O(sqrt(n)) | AC | 0.093 s | 552 KB | 11321885 |
| [1760_math.rs](1760_math.rs) | Rust 1.75 x64 | math | O(sqrt(n)) | AC | 0.046 s | 212 KB | 11321938 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1760_math_optimized.java](1760_math_optimized.java) | Java 1.8 | math | O(sqrt(n)) | AC | 0.109 s | 404 KB | 11318053 |
| [1760_math_optimized.go](1760_math_optimized.go) \* | Go 1.14 x64 | math | O(sqrt(n)) | AC | 0.015 s | 288 KB | 11321947 |
| [1760_number_theory_math.rs](1760_number_theory_math.rs) \* | Rust 1.75 x64 | number_theory, math | O(log n) | AC | 0.046 s | 60 KB | 11323414 |

\* Las versiones marcadas aún pueden mejorar su clasificación.
