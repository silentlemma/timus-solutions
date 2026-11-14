# 1234. Un ladrillo por un agujero del suelo

[Timus 1234](https://acm.timus.ru/problem.aspx?space=1&num=1234) · dificultad 687 · geometry

Problema original de Elena Andreeva, del concurso regional ACM ICPC del noreste de Europa 2002–2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que empujar un ladrillo de A × B × C por un agujero rectangular de
D × E que baja recto sin fin. ¿Pasa? Todas las longitudes van de 1 a 10
con como mucho un decimal.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

A, B, C, D y E en una línea.

## Salida

`YES` o `NO`.

## Ejemplos

### Ejemplo 1

Entrada:

```
1.0 2.0 1.5 1.4 1.0
```

Salida:

```
NO
```

### Ejemplo 2

Entrada:

```
1.0 2.0 1.5 1.5 1.0
```

Salida:

```
YES
```

## Solución

El ladrillo baja de punta, así que pasa si una de sus caras cabe en el
rectángulo D × E, y la más fácil es la cara de sus dos lados más cortos,
q ≤ p. Con los lados del agujero b ≤ a hay tres casos:

- q > b: la cara mide al menos q de ancho en cualquier dirección, más
  que el ancho b del agujero, `NO`;
- p ≤ a: cabe recta, `YES`;
- p > a: aún puede caber girada. El criterio de Carver dice que entonces
  un rectángulo p × q cabe en uno a × b justo cuando
  `((a+b)/(p+q))² + ((a−b)/(p−q))² ≥ 2`.

Todas las longitudes son décimas enteras, así que el programa las lee
como enteros de décimas y desarrolla el criterio:
`(a+b)²(p−q)² + (a−b)²(p+q)² ≥ 2(p+q)²(p−q)²`. Así incluso los ajustes
exactos se deciden sin redondeo. `O(1)`.

Detalles a tener en cuenta:

- un ajuste exacto cuenta: el segundo ejemplo y las pruebas 03, 04 y 07
  tocan las paredes del agujero;
- los casos girados pueden quedar muy cerca del límite: en la prueba 05
  el lado izquierdo del criterio es casi 2 − 5·10⁻⁶ y en la 06 casi
  2 + 3·10⁻⁷, así que la coma flotante con una tolerancia holgada falla
  en uno de los dos.

El criterio se comparó con un barrido de ángulos en miles de casos
aleatorios, y con fracciones exactas en los 197 casos de un decimal en
que queda a menos de 2·10⁻⁴ de 2.

## Notas por lenguaje

- Las versiones sencillas pasan cada longitud a décimas redondeando
  (`x · 10` no siempre es entero en coma flotante) y luego usan enteros.

## Soluciones optimizadas

Las versiones optimizadas leen las dimensiones directamente en décimas y aplican el mismo criterio con enteros.

Go lee las dimensiones directamente en décimas y aplica la prueba geométrica exacta con enteros. Go 1.14 x64, envío 11322881. Tiempo 0,015 → 0,015 s, memoria 1080 → 308 KB.

Python 3.12 x64, envío 11318418. Tiempo 0,078 → 0,062 s, memoria 420 → 464 KB.

Java 1.8, envío 11318424. Tiempo 0,109 → 0,109 s, memoria 536 → 364 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321887 · Go 1.14 x64 №11322221 · Java 1.8 №11322222 · Python 3.12 x64 №11322223 · Rust 1.75 x64 №11322224.

Rust comprueba las dos dimensiones menores del ladrillo en décimas y usa una desigualdad entera para el caso girado. Rust 1.75 x64, envío 11323284. Tiempo 0,015 → 0,046 s, memoria 236 → 52 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1234_geometry.cpp](1234_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 124 KB | 11321887 |
| [1234_geometry.go](1234_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 1080 KB | 11322221 |
| [1234_geometry.java](1234_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 536 KB | 11322222 |
| [1234_geometry.py](1234_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 420 KB | 11322223 |
| [1234_geometry.rs](1234_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 236 KB | 11322224 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1234_geometry_optimized.go](1234_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 308 KB | 11322881 |
| [1234_geometry_optimized.py](1234_geometry_optimized.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.062 s | 464 KB | 11318418 |
| [1234_geometry_optimized.java](1234_geometry_optimized.java) \* | Java 1.8 | geometry | O(1) | AC | 0.109 s | 364 KB | 11318424 |
| [1234_geometry_optimized.rs](1234_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 52 KB | 11323284 |

\* Las versiones marcadas aún pueden mejorar su clasificación.
