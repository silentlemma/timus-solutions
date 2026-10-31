# 1192. Cuánto avanza una pelota que rebota en un sueño

[Timus 1192](https://acm.timus.ru/problem.aspx?space=1&num=1192) · dificultad 110 · math

Problema original de Igor Goldberg, del Quinto Campeonato por Equipos de Programación para Escolares, 2 de marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Desde un suelo plano infinito se lanza una pelota con un ángulo de `a`
grados sobre la horizontal y velocidad `V` m/s, con gravedad `10` m/s² y
sin aire. Rebota con el mismo ángulo, perdiendo energía cinética por un
factor `K > 1` en cada rebote, y pi se toma como `3.1415926535`. Hay que
hallar hasta qué distancia del punto de lanzamiento puede llegar la
pelota, con dos decimales.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Tres números separados por espacios: los enteros `V`
(`0 ≤ V ≤ 500000`) y `a` (`0 ≤ a ≤ 90`), y un real `K > 1`.

## Salida

La distancia en metros, redondeada a dos decimales.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 15 2.50
```

Salida:

```
2.08
```

## Solución

Un vuelo a velocidad `v` y ángulo `a` recorre `v²·sin(2a)/g`. Un rebote
mantiene el ángulo y divide la energía cinética, es decir `v²`, entre `K`.
Los vuelos forman una serie geométrica de razón `1/K`, cuya suma es el
primer vuelo por `K/(K − 1)`. `O(1)`.

Detalles a tener en cuenta:

- pi debe ser el `3.1415926535` dado: con él, un lanzamiento en vertical a
  la mayor velocidad aún se desplaza unos metros, y las respuestas
  esperadas lo incluyen;
- el resultado puede llegar a unos `2.5·10¹⁴` cuando `K` es cercano a 1,
  pero un double ya no distingue centésimas a esa escala;
- `V = 0` o `a = 0` dan `0.00`.

Las respuestas se compararon con una solución escrita aparte en todas las
pruebas.

## Soluciones optimizadas

La solución optimizada en Java reúne los tres números de `System.in`
carácter a carácter y los convierte con `Double.parseDouble` en lugar de
crear un `Scanner`, cuya preparación cuesta más que todo el cálculo; la
fórmula y la salida son las mismas: {1192_math_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1192_math_optimized.java`: reducción de tiempo +25.60%; reducción de
  memoria +50.42%; base: `1192_math.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1192_math.cpp](1192_math.cpp).
- [1192_math.go](1192_math.go).
- [1192_math.rs](1192_math.rs).

- Java imprime con la configuración regional de EE. UU. para que el
  separador decimal sea un punto.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1192_math.cpp](1192_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 152 KB | 11283452 |
| [1192_math.go](1192_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1096 KB | 11283453 |
| [1192_math.java](1192_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1920 KB | 11283457 |
| [1192_math.py](1192_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 416 KB | 11283454 |
| [1192_math.rs](1192_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 248 KB | 11283458 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1192_math_optimized.java](1192_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 952 KB | 11304273 |
