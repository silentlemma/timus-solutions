# 1775. Bolos espaciales

[Timus 1775](https://acm.timus.ru/problem.aspx?space=1&num=1775) · dificultad 934 · geometry

Problema original de Alexander Mironenko, del XV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n bolos redondos de diámetro 1 están en un plano con centros enteros
distintos. Una bola del diámetro elegido, lanzada desde cualquier punto,
rueda en línea recta y derriba todos los bolos que toca. Hallar el menor
diámetro que derriba al menos k bolos de un solo lanzamiento.

## Entrada

n y k (1 ≤ k ≤ n ≤ 200) y luego los centros xᵢ, yᵢ
(|xᵢ|, |yᵢ| ≤ 10⁵).

## Salida

El menor diámetro con un error absoluto o relativo de a lo sumo 10⁻⁶, o
0 si sirve cualquier bola, por pequeña que sea.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 4
0 4
0 6
6 4
6 6
3 0
```

Salida:

```
1.0000000000
```

## Solución

Una bola de diámetro D toca un bolo cuando el centro del bolo está a no
más de (D + 1)/2 de la recta que sigue el centro de la bola, es decir,
dentro de una franja de anchura D + 1. Lanzando desde lo bastante
lejos, la bola puede recorrer cualquier recta entera, así que la tarea
es la franja más estrecha que contiene k centros, y la respuesta es su
anchura menos 1, pero no por debajo de 0.

Para una dirección fija, la franja más estrecha sale de ordenar los
centros por su distancia a lo ancho de esa dirección y tomar los k más
juntos seguidos. Al girar la dirección, la anchura de cada grupo cambia
como |sin| entre los momentos en que dos centros se alinean, y |sin| no
tiene mínimo interior allí, así que la mejor dirección es una en la que
dos centros se alinean a lo largo de la franja. Quedan n(n − 1)/2
direcciones, cada una con una ordenación; las distancias a lo ancho
usan el producto vectorial entero con la dirección, dividido por su
longitud solo al final. `O(n³ log n)`.

En el ejemplo los cuatro centros (0, 4), (0, 6), (6, 4), (6, 6) caben en
una franja horizontal de anchura 2, así que una bola de diámetro 1 los
derriba todos.

Trampas:

- k centros en una recta, o k = 1, dan 0;
- una franja más estrecha que 1 también da 0, nunca un diámetro
  negativo;
- el lanzador puede empezar en cualquier sitio, así que el camino es
  una recta entera, no un rayo desde un bolo.

Las respuestas coinciden con una implementación aceptada independiente,
que busca el diámetro por bisección, en 60 casos aleatorios con hasta
200 bolos. La solución en Python corre en PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1775_geometry.cpp](1775_geometry.cpp) | G++ 13.2 x64 | geometry | O(n^3 log n) | AC | 0.109 s | 228 KB |
| [1775_geometry.go](1775_geometry.go) | Go 1.14 x64 | geometry | O(n^3 log n) | AC | 0.375 s | 2480 KB |
| [1775_geometry.java](1775_geometry.java) | Java 1.8 | geometry | O(n^3 log n) | AC | 0.375 s | 2240 KB |
| [1775_geometry.py](1775_geometry.py) | PyPy 3.10 x64 | geometry | O(n^3 log n) | AC | 0.640 s | 5944 KB |
| [1775_geometry.rs](1775_geometry.rs) | Rust 1.75 x64 | geometry | O(n^3 log n) | AC | 0.109 s | 272 KB |
