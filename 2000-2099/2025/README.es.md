# 2025. Maximizar parejas entre grupos

[Timus 2025](https://acm.timus.ru/problem.aspx?space=1&num=2025) · dificultad 60 · math

Problema original de Alexey Danilyuk, del Concurso Regional Escolar de Programación de los Urales 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Divide `n` objetos distintos en entre dos y `k` grupos no vacíos,
asignando cada objeto a exactamente un grupo. Una pareja no ordenada
aporta uno si sus objetos están en grupos distintos, y cero en otro
caso. Calcula el máximo número de parejas que aportan. Solo se pide el
número, no una partición concreta.

Hay `1 ≤ T ≤ 10` casos independientes, cada uno con `2 ≤ k ≤ n ≤ 10000`.
Límites: 1 segundo y 64 MB.

## Entrada

La primera línea contiene `T`. Cada una de las siguientes `T` líneas
contiene `n` y `k`.

## Salida

Para cada caso, imprime un entero en una línea, respetando el orden de entrada.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
3
6 3
5 5
4 2
```

```
12
10
4
```

## Solución

Lo mejor es usar los k grupos: con menos grupos, alguno tiene al menos
dos objetos, y partirlo añade pares. Con grupos de tamaños s₁, …, s_k,
los pares de grupos distintos son (n² − Σ sᵢ²) / 2, así que la suma de
cuadrados debe ser lo menor posible. Eso ocurre cuando los tamaños
difieren a lo sumo en uno, pues pasar un objeto de un grupo de tamaño a
a uno de tamaño b ≤ a − 2 reduce la suma de cuadrados. Así, r = n mod k
grupos tienen q + 1 objetos y los otros k − r tienen q = n div k, y la
respuesta es (n² − (k − r)·q² − r·(q + 1)²) / 2. `O(1)` por prueba.

Para n = 6, k = 3 los grupos son 2, 2, 2 y la respuesta es 12.

Detalles a tener en cuenta:

- cada par cuenta una vez, de ahí la división entre dos;
- solo aritmética entera, sin medias en coma flotante.

## Soluciones optimizadas

La solución optimizada en C++ usa la misma fórmula, pero lee y escribe
con `scanf` y `printf` en lugar de `iostream`: 128 KB en lugar de
444 KB, con el mismo tiempo.

## Notas por lenguaje

Ningún lenguaje necesita nada especial.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2025_math.cpp](2025_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 444 KB | 11292869 |
| [2025_math.go](2025_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1128 KB | 11292876 |
| [2025_math.java](2025_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1628 KB | 11303364 |
| [2025_math.py](2025_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 448 KB | 11292879 |
| [2025_math.rs](2025_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 228 KB | 11292891 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2025_math_optimized.cpp](2025_math_optimized.cpp) \* | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 128 KB | 11303661 |

\* No está entre las 10 mejores ni en el 15% mejor de las soluciones de
su lenguaje en el juez actual; quizá se pueda optimizar más.
