# 1633. Hipogrifos

[Timus 1633](https://acm.timus.ru/problem.aspx?space=1&num=1633) · dificultad 754 · math

Problema original de Igor Chevdar, del XIII Campeonato Abierto de Programación por Equipos de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un hipogrifo con pico de longitud A y garras de longitud B tiene
peligrosidad √(A² + B²). Un elixir las convierte en a₁A + b₁B y
a₂A + b₂B. Su calidad es el mayor factor por el que puede multiplicar la
peligrosidad de cualquier hipogrifo de peligrosidad no nula. Hay que
hallar la calidad.

## Entrada

Dos líneas: a₁ b₁ y luego a₂ b₂, enteros no negativos hasta 10⁶.

## Salida

La calidad, con 9 cifras exactas tras el punto decimal.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 2
3 4
```

Salida:

```
5.4649857042190426504511884932842
```

### Ejemplo 2

Entrada:

```
1 2
2 4
```

Salida:

```
5
```

## Solución

El elixir es la matriz M = [[a₁, b₁], [a₂, b₂]] aplicada al vector (A, B),
y la peligrosidad es la longitud euclídea, así que la calidad es el mayor
estiramiento de M: su mayor valor singular, la raíz del mayor valor
propio de MᵀM.

La fórmula de manual √((T + √(T² − 4D²)) / 2), con
T = a₁² + b₁² + a₂² + b₂² y D = a₁b₂ − b₁a₂, pierde cifras en double:
cuando M es casi un múltiplo de una rotación, T² y 4D² rondan 10²⁵ y son
casi iguales, y su diferencia pierde cifras significativas.
Factorizarla lo evita: T − 2D = (a₁ − b₂)² + (b₁ + a₂)² = Q y
T + 2D = (a₁ + b₂)² + (b₁ − a₂)² = P, y los valores singulares resultan
(√P + √Q) / 2 y |√P − √Q| / 2. P y Q son enteros menores que 2⁵³, exactos en un double,
así que la respuesta (√P + √Q) / 2 es la semisuma de dos raíces bien
redondeadas, con un error de unos 2 · 10⁻¹⁰ incluso cerca de 2 · 10⁶.
`O(1)`.

Detalles a tener en cuenta:

- la fórmula de valores propios en double no alcanza la precisión con
  matrices casi ortogonales (pruebas 06, 07);
- los cuadrados llegan a 4 · 10¹², más allá de los enteros de 32 bits;
- una matriz de rango uno sigue teniendo norma positiva (el segundo
  ejemplo), y la matriz nula tiene 0 (prueba 03).

Las respuestas coinciden con una implementación aceptada independiente
con diferencia menor que 2,4 · 10⁻¹⁰ en 200 elixires aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1633_math.cpp](1633_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 140 KB |
| [1633_math.go](1633_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1088 KB |
| [1633_math.java](1633_math.java) | Java 1.8 | math | O(1) | AC | 0.140 s | 1820 KB |
| [1633_math.py](1633_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.109 s | 496 KB |
| [1633_math.rs](1633_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 264 KB |
