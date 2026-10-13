# 1359. Obra

[Timus 1359](https://acm.timus.ru/problem.aspx?space=1&num=1359) · dificultad 1166 · dp

Problema original de Den Raskovalov (enunciado de Aleksandr Bikbaev), del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un barril en reposo tiene que bajar n metros a la izquierda y m metros
hacia abajo, 1 ≤ n, m ≤ 50, rodando por una cadena de tablas. Cada
tabla tiene extremos enteros, con el inferior estrictamente más bajo
que el superior y no a su derecha. No hay rozamiento, g = 10, y en cada
unión el barril conserva el valor de su velocidad y solo gira. Hay que
imprimir el menor tiempo de bajada con un error de a lo sumo 10⁻³.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Los números n y m.

## Salida

El menor tiempo en segundos.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 2
```

Salida:

```
0.8614
```

## Solución

Sin rozamiento se conserva la energía: a profundidad d el barril va a
v(d) = √(2·g·d), sea cual sea el camino que lo llevó allí. A lo largo de
una tabla la aceleración es constante, así que el barril recorre la
longitud L a la media de las velocidades de sus extremos, y la tabla
tarda 2L / (v₁ + v₂).

Así que solo importan los puntos de la red. Una tabla va de (x, e) a
(y, d) con y ≥ x y d > e, midiendo x hacia la izquierda y la
profundidad hacia abajo, y
best[d][y] = min(best[e][x] + 2L / (v(e) + v(d))). La respuesta es
best[m][n]. Hay unas n² · m² / 4 transiciones, 1,6 millones para
n = m = 50. `O(n² · m²)`.

Detalles a tener en cuenta:

- la primera tabla empieza con velocidad 0, que la fórmula 2L / (0 + v)
  ya cubre;
- una tabla no puede ir a la derecha ni quedar horizontal, pero sí
  vertical;
- en una pendiente suave el barril va despacio y la respuesta puede ser
  grande: 22,3652 para n = 50, m = 1 (prueba 04).

Para n = m = 1 la única tabla da 2√2 / √20 = 0,6325 (prueba 02), lo que
coincide con la cuenta hecha a mano.

## Notas por lenguaje

- Python calcula una vez los tiempos de todas las tablas entre dos filas
  y actualiza una fila entera con `map(min, …)`, con lo que el caso más
  grande tarda alrededor de un cuarto de segundo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1359_dp.cpp](1359_dp.cpp) | G++ 13.2 x64 | dp | O(n²·m²) | AC | 0.031 s | 248 KB |
| [1359_dp.go](1359_dp.go) | Go 1.14 x64 | dp | O(n²·m²) | AC | 0.046 s | 1128 KB |
| [1359_dp.java](1359_dp.java) | Java 1.8 | dp | O(n²·m²) | AC | 0.140 s | 1872 KB |
| [1359_dp.py](1359_dp.py) | Python 3.12 x64 | dp | O(n²·m²) | AC | 0.484 s | 776 KB |
| [1359_dp.rs](1359_dp.rs) | Rust 1.75 x64 | dp | O(n²·m²) | AC | 0.046 s | 280 KB |
