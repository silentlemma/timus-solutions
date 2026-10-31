# 1306. Mediana de una sucesión

[Timus 1306](https://acm.timus.ru/problem.aspx?space=1&num=1306) · dificultad 145 · sorting

Problema original del Segundo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 3–4 de abril de 1998.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que hallar la mediana de 1 ≤ N ≤ 250 000 enteros de 0 a 2³¹ − 1: el
elemento central de la sucesión ordenada si N es impar, y la media de
los dos centrales si N es par. Se imprime con un decimal.

Límite de tiempo: 1 segundo. Límite de memoria: 1 MB. El enunciado
admite C, C++ y Pascal; el formulario de envío ofrece además Rust.

## Entrada

N y luego los N números, uno por línea.

## Salida

La mediana con un decimal.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
3
6
4
5
```

Salida:

```
4.5
```

## Solución

La sucesión entera ocupa 250 000 · 4 bytes, alrededor de 1 MB, que es
todo el límite de memoria. Pero solo importa la mitad menor: la mediana
es el mayor, o la media de los dos mayores, de los ⌊N/2⌋ + 1 números más
pequeños.

Así que un montículo de máximo guarda los ⌊N/2⌋ + 1 números más
pequeños vistos hasta ahora, unos 500 KB. Cada número nuevo entra
mientras el montículo no está lleno, o sustituye a la cima si es menor
que ella. Al final:

- con N impar la cima es la mediana;
- con N par la cima y, tras sacarla, la nueva cima son los dos
  elementos centrales.

`O(N log N)` en tiempo y `O(N / 2)` en memoria.

Detalles a tener en cuenta:

- la suma de dos números cerca de 2³¹ − 1 puede desbordar un entero de
  32 bits con signo (prueba 04), pero cabe en uno sin signo; el código usa 64 bits;
- la media es entera o termina en .5, así que se imprime exacta, sin
  coma flotante (pruebas 01 y 08);
- aquí los flujos de C++ gastan demasiada memoria, así que el programa
  lee con `scanf`.

## Soluciones optimizadas

La solución optimizada en C++ analiza los números a mano desde un búfer
de 4 KB en lugar de `scanf`. Construye de una vez el montículo con los
primeros ⌊N/2⌋ + 1 números mediante `std::make_heap`, en tiempo lineal,
en lugar de insertarlos uno a uno, y reemplaza la cima con un solo
hundimiento en lugar de `pop_heap` seguido de `push_heap`:
{1306_sorting_optimized.cpp}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1306_sorting_optimized.cpp`: reducción de tiempo +84.73%; reducción
  de memoria +8.97%; base: `1306_sorting.cpp`.

## Notas por lenguaje

- El enunciado solo admite C, C++ y Pascal, pero el formulario de envío
  de Timus ofrece además Rust 1.75, así que hay soluciones en C++ y Rust;
  Go, Python y Java no se pueden enviar.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1306_sorting.cpp](1306_sorting.cpp) | G++ 13.2 x64 | sorting | O(N log N) | AC | 0.203 s | 624 KB | 11284855 |
| [1306_sorting.rs](1306_sorting.rs) | Rust 1.75 x64 | sorting | O(N log N) | AC | 0.046 s | 700 KB | 11304528 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1306_sorting_optimized.cpp](1306_sorting_optimized.cpp) | G++ 13.2 x64 | sorting | O(N log N) | AC | 0.031 s | 568 KB | 11304527 |
