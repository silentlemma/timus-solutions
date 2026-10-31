# 1788. Sobre la utilidad de los paraguas

[Timus 1788](https://acm.timus.ru/problem.aspx?space=1&num=1788) · dificultad 162 · greedy

Problema original de Sofia Tekhazheva (preparado por Denis Dublennykh), del Concurso Regional Escolar de Programación de los Urales 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n chicas sin paraguas y m chicos con paraguas salen de una fiesta bajo
la lluvia. Cada chico puede acompañar a una chica bajo su paraguas. Una
chica que se moja se disgusta en gᵢ. Un chico que no acompaña a nadie
se disgusta en bⱼ·k, donde k es el número de chicos que sí acompañan a
una chica. Las chicas y chicos en pareja no se disgustan. Hallar el
menor disgusto total.

## Entrada

n y m (1 ≤ n, m ≤ 100), luego g₁, …, gₙ, luego b₁, …, bₘ, todos de 1 a
1000.

## Salida

El menor disgusto total.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 4
1 100
10 8 6 4
```

Salida:

```
19
```

## Solución

Se fija el número de parejas k. Entonces conviene mantener secas a las
k chicas con mayor gᵢ y que acompañen los k chicos con mayor bⱼ, ya que
cada persona sola cuesta su propio valor (multiplicado por k en los
chicos). Así el total es la suma de los n − k menores gᵢ más k por la
suma de los m − k menores bⱼ. Se ordenan ambas listas y se prueba cada
k de 0 a min(n, m). `O((n + m)²)`.

En el ejemplo sin parejas el coste es 101, y con dos parejas los chicos
con 6 y 4 dan 2·10 = 20. Una pareja, con la chica que se disgustaría en
100, deja a la chica con 1 y a los chicos con 8, 6 y 4 en 1·18, 19 en
total.

Trampas:

- el coste de los chicos crece con k, así que más parejas no siempre es
  mejor;
- también hay que probar k = 0: entonces ningún chico se disgusta;
- los totales intermedios pueden alcanzar 2.550.000 (prueba 06, k = 49 o
  50), incluso cuando la respuesta es cero; la mayor respuesta óptima
  posible es 99.000. Ambos valores caben en enteros de 32 bits.

Las respuestas coinciden con una implementación aceptada independiente
en 150 grupos aleatorios: grupos cualesquiera, pequeños, y chicas
sensibles con chicos tranquilos.

## Soluciones optimizadas

La solución optimizada en C++ lee e imprime con `scanf` y `printf` en
lugar de `iostream`, cuyo entorno de ejecución sobra para a lo sumo 202
números; la ordenación y las sumas son las mismas:
{1788_greedy_optimized.cpp}.

La solución optimizada en Java lee la entrada en bloques de 4 KB y
analiza los números a mano en lugar de usar `Scanner`, cuya maquinaria
de expresiones regulares tarda en cargarse y ocupa memoria; la
ordenación y las sumas son las mismas: {1788_greedy_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1788_greedy_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +57.43%; base: `1788_greedy.cpp`.

- `1788_greedy_optimized.java`: reducción de tiempo +25.60%; reducción
  de memoria +78.62%; base: `1788_greedy.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1788_greedy.go](1788_greedy.go).
- [1788_greedy.rs](1788_greedy.rs).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1788_greedy.cpp](1788_greedy.cpp) | G++ 13.2 x64 | greedy | O((n + m)^2) | AC | 0.015 s | 404 KB | 11304222 |
| [1788_greedy.go](1788_greedy.go) | Go 1.14 x64 | greedy | O((n + m)^2) | AC | 0.031 s | 1100 KB | 11289825 |
| [1788_greedy.java](1788_greedy.java) | Java 1.8 | greedy | O((n + m)^2) | AC | 0.125 s | 1852 KB | 11304227 |
| [1788_greedy.py](1788_greedy.py) | Python 3.12 x64 | greedy | O((n + m)^2) | AC | 0.093 s | 448 KB | 11304230 |
| [1788_greedy.rs](1788_greedy.rs) | Rust 1.75 x64 | greedy | O((n + m)^2) | AC | 0.046 s | 232 KB | 11304233 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1788_greedy_optimized.cpp](1788_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O((n + m)^2) | AC | 0.015 s | 172 KB | 11307198 |
| [1788_greedy_optimized.java](1788_greedy_optimized.java) | Java 1.8 | greedy | O((n + m)^2) | AC | 0.093 s | 396 KB | 11307199 |
