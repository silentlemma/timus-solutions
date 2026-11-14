# 1754. Explosión en una pirámide

[Timus 1754](https://acm.timus.ru/problem.aspx?space=1&num=1754) · dificultad 644 · geometry

Problema original de Alexander Ipatov, del XI Concurso Individual Abierto de la Universidad Estatal de los Urales, 13 de marzo de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una pirámide triangular hueca tiene las esquinas de la base en
(x₁, y₁, 0), (x₂, y₂, 0), (x₃, y₃, 0) y el vértice en (x₄, y₄, H). Un
liche sube de (x₀, y₀, 0) a (x₀, y₀, h), lo que cuesta h de maná, y crea
alrededor de ese punto un campo esférico que cuesta su radio en maná.
La pirámide se derrumba si el campo toca una pared o el suelo. Con m de
maná, ¿puede el liche derrumbarla?

## Entrada

m, h y H (1 ≤ m, h, H ≤ 1000) y luego los cinco puntos xᵢ, yᵢ
(−1000 ≤ xᵢ, yᵢ ≤ 1000). El punto (x₀, y₀, h) está estrictamente dentro
de la pirámide.

## Salida

`YES` o `NO`.

## Ejemplos

### Ejemplo 1

Entrada:

```
13 6 30
6 6
0 0
0 30
30 0
0 0
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
11 6 30
6 6
0 0
0 30
30 0
0 0
```

Salida:

```
NO
```

## Solución

Tras subir quedan m − h de maná, y el campo debe alcanzar el punto más
cercano de la superficie de la pirámide. Desde un punto dentro de un
cuerpo convexo, esa es la distancia al más cercano de los planos de sus
caras: h al suelo y |n·(P − A)| / |n| a una pared por las esquinas A, B
y el vértice, donde n es el producto vectorial de B − A y
(vértice − A). La respuesta es `YES` cuando m − h ≥ 0 y alguna de esas
distancias es a lo sumo m − h.

Una distancia puede ser exactamente m − h, como con una pared vertical,
así que se compara sin redondeo: |n·(P − A)| ≤ k·|n| pasa a ser
(n·(P − A))² ≤ k²·|n|², con k = m − h. El lado izquierdo llega a unos
1,6·10¹⁹, más de 64 bits con signo, así que los productos se hacen en 128 bits, o
con números grandes donde el lenguaje no ofrece otra cosa. `O(1)`.

En los ejemplos el suelo y las dos paredes verticales x = 0 e y = 0
están a 6 y la pared inclinada a unos 6,93, así que hacen falta
6 + 6 = 12 de maná: 13 basta, 11 no.

Trampas:

- con m < h el liche ni siquiera puede subir;
- la coma flotante con tolerancia puede equivocarse con una distancia
  que se queda justo por encima de m − h;
- las esquinas de la base pueden venir en cualquier sentido.

Las respuestas coinciden con una implementación aceptada independiente
en 450 pirámides aleatorias, un tercio de ellas con paredes verticales a
distancias enteras y el maná cerca del umbral.

## Soluciones optimizadas

Las versiones optimizadas calculan directamente las coordenadas de la normal de cada cara lateral y comparan los cuadrados de los productos para comprobar el alcance restante.

Python 3.12 x64, envío 11318516. Tiempo 0,078 → 0,109 s, memoria 592 → 508 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321958 · Java 1.8 №11321955 · Python 3.12 x64 №11321956 · Rust 1.75 x64 №11321957 · Go 1.14 x64 №11322211.

Go comprueba cada cara de la pirámide mediante comparaciones enteras exactas de las distancias pertinentes. Go 1.14 x64, envío 11322932. Tiempo 0,015 → 0,015 s, memoria 1092 → 276 KB.

Java 1.8, envío 11321993. Tiempo 0,14 → 0,125 s, memoria 1664 → 376 KB.

Rust compara las distancias al cuadrado al plano sin dividir por la longitud de su vector normal. Rust 1.75 x64, envío 11323317. Tiempo 0,031 → 0,046 s, memoria 224 → 48 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1754_geometry.cpp](1754_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 108 KB | 11321958 |
| [1754_geometry.go](1754_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 1092 KB | 11322211 |
| [1754_geometry.java](1754_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.14 s | 1664 KB | 11321955 |
| [1754_geometry.py](1754_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 592 KB | 11321956 |
| [1754_geometry.rs](1754_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 224 KB | 11321957 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1754_geometry_optimized.py](1754_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(1) | AC | 0.109 s | 508 KB | 11318516 |
| [1754_geometry_optimized.go](1754_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 276 KB | 11322932 |
| [1754_geometry_optimized.java](1754_geometry_optimized.java) \* | Java 1.8 | geometry | O(1) | AC | 0.125 s | 376 KB | 11321993 |
| [1754_geometry_optimized.rs](1754_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 48 KB | 11323317 |

\* Las versiones marcadas aún pueden mejorar su clasificación.
