# 1225. Filas de franjas blancas, azules y rojas

[Timus 1225](https://acm.timus.ru/problem.aspx?space=1&num=1225) · dificultad 35 · dp

Problema original del cuarto de final de la región central de Rusia del ACM ICPC 2002–2003, Rybinsk, octubre de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una fila de `N ≤ 45` franjas se hace con franjas blancas, azules y rojas.
Dos franjas vecinas no comparten color, y una franja azul debe estar
entre una blanca y una roja. Hay que contar las filas posibles.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`.

## Salida

El número de filas.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
```

Salida:

```
2
```

## Solución

Una franja azul necesita vecinas a ambos lados, así que una fila nunca
acaba en azul; acaba en blanco o en rojo. Sea `f(n)` el número de filas
válidas de longitud `n`. Antes de una última franja blanca hay o una
roja, que cierra una fila válida de longitud `n − 1` acabada en rojo, o
una azul precedida de una roja, que cierra una fila válida de longitud
`n − 2` acabada en rojo; lo mismo vale para el rojo con los colores
cambiados. Por simetría, la mitad de las filas de cada longitud acaba en
rojo, así que `f(n) = f(n − 1) + f(n − 2)` con `f(1) = f(2) = 2`: el
doble de los números de Fibonacci. `O(N)`.

Detalles a tener en cuenta:

- una sola franja puede ser blanca o roja pero no azul, así que
  `f(1) = 2`;
- para `N = 45` la cuenta es 2.269.806.340, más de lo que cabe en enteros
  de 32 bits con signo.

La fórmula se comprobó por fuerza bruta con todas las coloraciones de
hasta 12 franjas, y cada `N` de 1 a 45 se comparó con una solución
escrita aparte.

## Soluciones optimizadas

La solución optimizada en Java analiza el número byte a byte desde
`System.in` en lugar de usar `Scanner`: 0.093 s en lugar de 0.125 s y
316 KB en lugar de 1576 KB.

## Notas por lenguaje

- Mismo bucle; Python usa enteros de precisión arbitraria y los demás, de 64 bits.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1225_dp.cpp](1225_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 128 KB | 11283710 |
| [1225_dp.go](1225_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 1072 KB | 11283711 |
| [1225_dp.java](1225_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 1576 KB | 11283713 |
| [1225_dp.py](1225_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.093 s | 372 KB | 11283712 |
| [1225_dp.rs](1225_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 216 KB | 11283714 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1225_dp_optimized.java](1225_dp_optimized.java) | Java 1.8 | dp | O(N) | AC | 0.093 s | 316 KB | 11303728 |
