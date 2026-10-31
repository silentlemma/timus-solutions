# 1796. Parque de atracciones

[Timus 1796](https://acm.timus.ru/problem.aspx?space=1&num=1796) · dificultad 111 · math

Problema original de Eugene Kurpilyansky (preparado por Egor Shchelkonogov), del Concurso Regional Escolar de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una maestra paga unas entradas con billetes de 10, 50, 100, 500, 1000 y
5000 rublos. El dinero alcanza para las entradas, pero ya no alcanzaría
si se quitara cualquier billete. Dados los billetes de cada tipo y el
precio de la entrada, listar todos los números posibles de entradas.

## Entrada

Seis cantidades no negativas de billetes, del menor al mayor, y luego el
precio. Todos los números son enteros no mayores que 1000, y el precio
es positivo. Existe al menos una respuesta.

## Salida

El número de respuestas posibles y luego las respuestas en orden
creciente.

## Ejemplos

### Ejemplo 1

Entrada:

```
0 2 0 0 0 0
10
```

Salida:

```
5
6 7 8 9 10
```

### Ejemplo 2

Entrada:

```
1 2 0 0 0 0
10
```

Salida:

```
1
11
```

## Solución

Sea T la suma y s el menor billete entregado. Para k entradas el dinero
debe alcanzar, k·price ≤ T. Sin cualquier billete no debe alcanzar, y
el menor billete es el caso más difícil: si T − s es poco, también lo
es la suma sin cualquier billete mayor. Así que T − s < k·price, y las
respuestas son todos los k de ⌊(T − s)/price⌋ + 1 a ⌊T/price⌋.
`O(answers)`, como mucho 5000.

En el primer ejemplo T = 100 y s = 50: sin un billete 50 rublos no
deben alcanzar, así que más de 5 entradas, y como mucho 10.

Trampas:

- el billete que se quita es el menor de los presentes, no el de 10
  rublos en general;
- con un billete de 5000 rublos y precio 1 hay 5000 respuestas en una
  línea.

Las respuestas coinciden con una implementación aceptada independiente
en 300 casos aleatorios con pocos y con muchos billetes.

## Soluciones optimizadas

La solución optimizada en C++ lee con `scanf` en lugar de `std::cin` e
imprime cada respuesta enseguida con `printf` en lugar de reunir antes
hasta 5000 respuestas en un `std::string`, así que el programa prescinde
de `iostream`: {1796_math_optimized.cpp}.

La solución optimizada en Java lee los siete números cifra a cifra
directamente desde `System.in` en lugar de crear un `Scanner`; las
respuestas se siguen reuniendo en un `StringBuilder`:
{1796_math_optimized.java}.

La solución optimizada en Rust toma los siete números uno a uno del
iterador de tokens en lugar de reunirlos en un vector, y escribe las
respuestas con un `BufWriter` en lugar de crear un `String` para cada
una de las hasta 5000 respuestas y unirlas: {1796_math_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1796_math_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +71.68%; base: `1796_math.cpp`.

- `1796_math_optimized.java`: reducción de tiempo +28.44%; reducción de
  memoria +63.03%; base: `1796_math.java`.

- `1796_math_optimized.rs`: reducción de tiempo -106.67%; reducción de
  memoria +47.90%; base: `1796_math.rs`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1796_math.go](1796_math.go).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1796_math.cpp](1796_math.cpp) | G++ 13.2 x64 | math | O(answers) | AC | 0.015 s | 452 KB | 11304050 |
| [1796_math.go](1796_math.go) | Go 1.14 x64 | math | O(answers) | AC | 0.031 s | 1288 KB | 11289894 |
| [1796_math.java](1796_math.java) | Java 1.8 | math | O(answers) | AC | 0.109 s | 1980 KB | 11304051 |
| [1796_math.py](1796_math.py) | Python 3.12 x64 | math | O(answers) | AC | 0.078 s | 720 KB | 11304052 |
| [1796_math.rs](1796_math.rs) | Rust 1.75 x64 | math | O(answers) | AC | 0.015 s | 476 KB | 11304053 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1796_math_optimized.cpp](1796_math_optimized.cpp) | G++ 13.2 x64 | math | O(answers) | AC | 0.015 s | 128 KB | 11304279 |
| [1796_math_optimized.java](1796_math_optimized.java) | Java 1.8 | math | O(answers) | AC | 0.078 s | 732 KB | 11304331 |
| [1796_math_optimized.rs](1796_math_optimized.rs) | Rust 1.75 x64 | math | O(answers) | AC | 0.031 s | 248 KB | 11304332 |
