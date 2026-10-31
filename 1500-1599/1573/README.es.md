# 1573. Alquimia

[Timus 1573](https://acm.timus.ru/problem.aspx?space=1&num=1573) · dificultad 108 · math

Problema original de Alexander Ipatov, del USU Junior Contest (XIV Campeonato Abierto por Equipos de Programación para Escolares de la Región de Sverdlovsk), octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Sandro tiene tres bolsas de reactivos distintos: B azules, R rojos y Y
amarillos (de 1 a 100 cada una). Una poción necesita un reactivo de cada
color de su receta, todos de colores distintos. Hay que contar los
conjuntos de reactivos con los que se hace la poción.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

B, R e Y, y luego un K positivo y los K colores distintos de la receta
(Blue, Red o Yellow).

## Salida

El número de maneras.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3 5
3
Red
Yellow
Blue
```

Salida:

```
30
```

## Solución

Cada color de la receta toma un reactivo de su propia bolsa, y las
elecciones son independientes, así que la respuesta es el producto de
los tamaños de las bolsas que nombra la receta. Es como mucho
100³ = 10⁶. `O(K)`.

Detalles a tener en cuenta:

- la entrada da las bolsas en el orden azul, rojo, amarillo, mientras
  que la receta del ejemplo empieza por el rojo;
- solo cuentan los colores de la receta (pruebas 02, 03).

## Soluciones optimizadas

La solución optimizada en C++ lee con `scanf` en lugar de `iostream` y
elige la bolsa por la primera letra del color, ya que Blue, Red y Yellow
empiezan por letras distintas, en lugar de buscar el nombre en un
`std::map` de cadenas. Cada color se lee en un búfer de 7 bytes,
suficiente para el nombre más largo, Yellow, y el producto se guarda en
`int`, que basta porque no pasa de 10⁶: {1573_math_optimized.cpp}.

La solución optimizada en Java analiza los números cifra a cifra
directamente desde `System.in` en lugar de crear un `Scanner`, y elige
la bolsa por la primera letra del color, saltándose el resto de la
palabra, ya que Blue, Red y Yellow empiezan por letras distintas, en
lugar de buscar el nombre en un `HashMap` de valores `Long`
empaquetados. El producto se guarda en `int`, que basta porque no pasa
de 10⁶: {1573_math_optimized.java}.

La solución optimizada en Rust guarda los tamaños de las tres bolsas en
tres variables y elige uno con un `match` sobre el nombre del color en
lugar de construir un `HashMap`: {1573_math_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1573_math_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +69.23%; base: `1573_math.cpp`.

- `1573_math_optimized.java`: reducción de tiempo +12.80%; reducción de
  memoria +79.85%; base: `1573_math.java`.

- `1573_math_optimized.rs`: reducción de tiempo -206.67%; reducción de
  memoria +45.10%; base: `1573_math.rs`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1573_math.go](1573_math.go).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1573_math.cpp](1573_math.cpp) | G++ 13.2 x64 | math | O(K) | AC | 0.015 s | 416 KB | 11287812 |
| [1573_math.go](1573_math.go) | Go 1.14 x64 | math | O(K) | AC | 0.015 s | 1084 KB | 11287815 |
| [1573_math.java](1573_math.java) | Java 1.8 | math | O(K) | AC | 0.125 s | 1628 KB | 11287819 |
| [1573_math.py](1573_math.py) | Python 3.12 x64 | math | O(K) | AC | 0.078 s | 452 KB | 11287817 |
| [1573_math.rs](1573_math.rs) | Rust 1.75 x64 | math | O(K) | AC | 0.015 s | 408 KB | 11287824 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1573_math_optimized.cpp](1573_math_optimized.cpp) | G++ 13.2 x64 | math | O(K) | AC | 0.015 s | 128 KB | 11304264 |
| [1573_math_optimized.java](1573_math_optimized.java) | Java 1.8 | math | O(K) | AC | 0.109 s | 328 KB | 11304267 |
| [1573_math_optimized.rs](1573_math_optimized.rs) | Rust 1.75 x64 | math | O(K) | AC | 0.046 s | 224 KB | 11304268 |
