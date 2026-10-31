# 1683. Nevera

[Timus 1683](https://acm.timus.ru/problem.aspx?space=1&num=1683) · dificultad 137 · greedy

Problema original de Stanislav Vasilyev, del X Campeonato Abierto Individual de la Universidad Estatal de los Urales, 28 de febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una tira de papel de 1 cm de ancho y n cm de largo se dobla hasta un
cuadrado de 1 × 1 cm con n capas. Cada doblez mide un número entero de
centímetros desde el extremo izquierdo y dobla esa parte hacia la
derecha, de modo que el extremo izquierdo se desplaza esa longitud.
Hallar el menor número de dobleces y las longitudes medidas.

## Entrada

n (1 ≤ n ≤ 10⁹).

## Salida

El número de dobleces y luego las longitudes medidas en orden. Se
acepta cualquier secuencia más corta.

## Ejemplos

### Ejemplo 1

Entrada:

```
12
```

Salida:

```
4
5 3 2 1
```

## Solución

Doblar x cm de una tira de longitud L solo es posible si la solapa cabe
sobre el resto, x ≤ L − x, y entonces queda una tira de
L − x ≥ ⌈L / 2⌉. Así que ningún doblez reduce la tira a menos de la
mitad redondeada hacia arriba, y doblar ⌊L / 2⌋ cada vez lo consigue
exactamente: el número de dobleces es el menor m con 2ᵐ ≥ n.
`O(log n)`.

Trampas:

- n = 1 no necesita dobleces: se imprime 0 y una lista vacía;
- el 5 3 2 1 del ejemplo es una de muchas respuestas, así que un
  verificador compara la cantidad y reproduce los dobleces.

El verificador reproduce cada doblez y compara la cantidad con la del
voraz.

## Soluciones optimizadas

La solución optimizada en C++ guarda los dobleces en un arreglo fijo de
30 números en la pila en lugar de un `std::vector` que crece. Como
n ≤ 10⁹ < 2³⁰, como mucho 30 dobleces por la mitad dejan la tira en
1 cm, así que el arreglo siempre basta y el propio programa no reserva
memoria dinámica: {1683_greedy_optimized.cpp}.

La solución optimizada en Java lee la única línea con un
`BufferedReader` y la convierte con `Long.parseLong` en lugar de crear
un `Scanner`, cuyas expresiones regulares y datos de configuración
regional cuestan mucho más que 30 dobleces por la mitad:
{1683_greedy_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1683_greedy_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +47.92%; base: `1683_greedy.cpp`.

- `1683_greedy_optimized.java`: reducción de tiempo +25.60%; reducción
  de memoria +72.84%; base: `1683_greedy.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1683_greedy.go](1683_greedy.go).
- [1683_greedy.rs](1683_greedy.rs).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1683_greedy.cpp](1683_greedy.cpp) | G++ 13.2 x64 | greedy | O(log n) | AC | 0.015 s | 192 KB | 11288846 |
| [1683_greedy.go](1683_greedy.go) | Go 1.14 x64 | greedy | O(log n) | AC | 0.031 s | 1096 KB | 11288848 |
| [1683_greedy.java](1683_greedy.java) | Java 1.8 | greedy | O(log n) | AC | 0.125 s | 1664 KB | 11288850 |
| [1683_greedy.py](1683_greedy.py) | Python 3.12 x64 | greedy | O(log n) | AC | 0.125 s | 372 KB | 11288849 |
| [1683_greedy.rs](1683_greedy.rs) | Rust 1.75 x64 | greedy | O(log n) | AC | 0.015 s | 244 KB | 11288851 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1683_greedy_optimized.cpp](1683_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(log n) | AC | 0.015 s | 100 KB | 11304447 |
| [1683_greedy_optimized.java](1683_greedy_optimized.java) | Java 1.8 | greedy | O(log n) | AC | 0.093 s | 452 KB | 11304448 |
