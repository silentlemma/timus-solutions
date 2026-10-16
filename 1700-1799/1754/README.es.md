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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1754_geometry.cpp](1754_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 124 KB |
| [1754_geometry.go](1754_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 1084 KB |
| [1754_geometry.java](1754_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1688 KB |
| [1754_geometry.py](1754_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 596 KB |
| [1754_geometry.rs](1754_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 224 KB |
