# 1709. Pingüino-Avia

[Timus 1709](https://acm.timus.ru/problem.aspx?space=1&num=1709) · dificultad 153 · dsu

Problema original de Alexander Ipatov, del XIII Campeonato de los Urales de Programación Competitiva, 4 de abril de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una aerolínea vuela entre algunos pares de n aeropuertos, dados por una
matriz simétrica de 0 y 1. La nueva red debe unir cualquier par de
aeropuertos, quizá con escalas, y usar tan pocos vuelos como cualquier
red conexa. Cancelar un vuelo cuesta d y abrir uno cuesta a. Hallar el
cambio más barato e imprimirlo como matriz con d en un vuelo cancelado,
a en uno nuevo y 0 en el resto.

## Entrada

n (2 ≤ n ≤ 100), luego d y a (1 ≤ d, a ≤ 10⁶) y luego las n filas de
la matriz.

## Salida

La suma mínima y luego el plan de n × n, simétrico. Se acepta cualquier
plan óptimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
2 3
011000
101000
110000
000011
000101
000110
```

Salida:

```
7
0d0000
d00000
000a00
00a0d0
000d00
000000
```

## Solución

Una red conexa con la menor cantidad de vuelos es un árbol generador
con n − 1 vuelos. Si el árbol conserva k de los m vuelos antiguos, el
plan cancela m − k y abre n − 1 − k, así que conservar más es más
barato sean cuales sean d y a. Los vuelos conservados forman un bosque
dentro de la red antigua, así que k es a lo sumo n − c, donde c es su
número de componentes conexas, y un bosque generador lo alcanza.

Así que se construye un bosque generador con unión de conjuntos
disjuntos: un vuelo antiguo entre dos árboles distintos se conserva y
cualquier otro se cancela. Después se unen los c árboles con c − 1
vuelos nuevos desde el aeropuerto 1 hasta un aeropuerto de cada otro
árbol. La suma es d(m − n + c) + a(c − 1). `O(n²)`.

Trampas:

- la suma llega a 4851 · 10⁶ cuando existen todos los vuelos, lo que
  exige 64 bits (test 04);
- un vuelo nuevo entre dos árboles nunca repite uno antiguo, pues un
  vuelo antiguo ya los habría unido;
- las filas de la matriz se escriben sin espacios.

Un comprobador acepta cualquier plan óptimo. Revisa la suma, la
simetría, que d y a estén solo en vuelos existentes y ausentes, y que
el resultado sea un árbol generador. Las respuestas coinciden con una
implementación aceptada independiente en 800 grafos aleatorios.

## Soluciones optimizadas

La solución optimizada en C++ lee la matriz fila a fila con `scanf` en
un búfer de 101 bytes y procesa en el acto los vuelos de esa fila, así
que la matriz nunca se guarda; el plan es un arreglo global de 100 filas
de 101 caracteres, ya que n ≤ 100, y se imprime con `puts`. Usa `stdio`
en lugar de `iostream` y `std::string`: {1709_dsu_optimized.cpp}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1709_dsu_optimized.cpp`: reducción de tiempo +0.00%; reducción de
  memoria +71.30%; base: `1709_dsu.cpp`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1709_dsu.go](1709_dsu.go).
- [1709_dsu.java](1709_dsu.java).
- [1709_dsu.py](1709_dsu.py).
- [1709_dsu.rs](1709_dsu.rs).

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1709_dsu.cpp](1709_dsu.cpp) | G++ 13.2 x64 | dsu | O(n²) | AC | 0.015 s | 460 KB | 11304077 |
| [1709_dsu.go](1709_dsu.go) | Go 1.14 x64 | dsu | O(n²) | AC | 0.031 s | 1188 KB | 11289190 |
| [1709_dsu.java](1709_dsu.java) | Java 1.8 | dsu | O(n²) | AC | 0.093 s | 796 KB | 11289192 |
| [1709_dsu.py](1709_dsu.py) | Python 3.12 x64 | dsu | O(n²) | AC | 0.078 s | 636 KB | 11304078 |
| [1709_dsu.rs](1709_dsu.rs) | Rust 1.75 x64 | dsu | O(n²) | AC | 0.015 s | 288 KB | 11289193 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1709_dsu_optimized.cpp](1709_dsu_optimized.cpp) | G++ 13.2 x64 | dsu | O(n²) | AC | 0.015 s | 132 KB | 11305852 |
