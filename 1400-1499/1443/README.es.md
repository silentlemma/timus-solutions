# 1443. Rieles

[Timus 1443](https://acm.timus.ru/problem.aspx?space=1&num=1443) · dificultad 670 · math

Problema original de Stanislav Vasiliev, del Décimo Campeonato Universitario de Programación por Equipos de los Urales, 24–25 de marzo de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un ferrocarril mágico de N vías (1 ≤ N ≤ 18) de S metros cada una
(1 ≤ S ≤ 10000) se tiende con rieles de longitud L (10 ≤ L ≤ 10000).
Los rieles se pueden cortar y los trozos se pueden unir, y cada unión
crea una junta. El número de juntas debe ser el menor posible y, entre
esos planes, el número de rieles usados también. Las longitudes se dan
con precisión de una décima de milímetro. Hay que imprimir ese número de
rieles.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

N, S y L, uno por línea.

## Salida

El menor número de rieles.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
1005.6712
20.0001
```

Salida:

```
151
```

## Solución

Las longitudes se leen exactas, como enteros de décimas de milímetro,
porque la coma flotante emborronaría casos como una vía una décima de
milímetro más larga que un riel. Se escribe S = q L + rest con
0 ≤ rest < L. Una vía hecha de k trozos tiene k − 1 juntas y necesita
k L ≥ S, así que el mínimo de juntas se logra con ⌈S / L⌉ trozos en cada
vía.

Si rest = 0, cada vía son q rieles enteros, N q en total. Si no, cada vía
toma q rieles enteros y un trozo corto de longitud rest, y los trozos
cortos se reparten en rieles, ⌊L / rest⌋ por riel, lo que da
N q + ⌈N / ⌊L / rest⌋⌉. Repartir lo que falta entre varios trozos de una
vía no ahorra ningún riel: cada trozo de una vía mide al menos rest,
porque los otros q trozos miden como mucho L. `O(1)`.

Detalles a tener en cuenta:

- las longitudes pueden tener menos de cuatro decimales o ninguno
  (pruebas 02, 09, 10);
- una vía apenas más larga o más corta que un riel (pruebas 05, 11);
- la vía puede ser más corta que un solo riel (pruebas 03, 08);
- cinco vías con dos trozos cortos por riel necesitan tres rieles extra,
  no los dos que sugiere la longitud total (prueba 07).

## Soluciones optimizadas

Las versiones optimizadas expresan las longitudes en unidades enteras de 0,0001 m y cuentan los rieles completos y los recortes mediante división entera.

Java 1.8, envío 11319248. Tiempo 0,109 → 0,093 s, memoria 1652 → 512 KB.

Rust 1.75 x64, envío 11319421. Tiempo 0,015 → 0,015 s, memoria 228 → 244 KB.

Python 3.12 x64, envío 11319468. Tiempo 0,078 → 0,093 s, memoria 404 → 396 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321871 · Go 1.14 x64 №11322257 · Java 1.8 №11322258 · Python 3.12 x64 №11322259 · Rust 1.75 x64 №11322260.

Go lee las dos longitudes como enteros escalados y cuenta por separado los rieles completos y los que hacen falta para los tramos restantes. Go 1.14 x64, envío 11322863. Tiempo 0,031 → 0,015 s, memoria 1068 → 300 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1443_math.cpp](1443_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 388 KB | 11321871 |
| [1443_math.go](1443_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1068 KB | 11322257 |
| [1443_math.java](1443_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1652 KB | 11322258 |
| [1443_math.py](1443_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 404 KB | 11322259 |
| [1443_math.rs](1443_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 228 KB | 11322260 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1443_math_optimized.java](1443_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 512 KB | 11319248 |
| [1443_math_optimized.rs](1443_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 244 KB | 11319421 |
| [1443_math_optimized.py](1443_math_optimized.py) \* | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 396 KB | 11319468 |
| [1443_math_optimized.go](1443_math_optimized.go) \* | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 300 KB | 11322863 |

\* Las versiones marcadas aún pueden mejorar su clasificación.
