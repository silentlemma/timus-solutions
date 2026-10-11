# 1245. Tapar manchas redondas con como mucho dos cuadros

[Timus 1245](https://acm.timus.ru/problem.aspx?space=1&num=1245) · dificultad 948 · geometry

Problema original de Alexander Petrov (enunciado de Leonid Volkov), del Concurso Individual de la Universidad Estatal de los Urales, 1 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N manchas redondas (0 < N ≤ 1000) de radio y centro enteros, todos como
mucho 10 000, deben quedar tapadas por uno o dos cuadros rectangulares de
lados paralelos a los ejes. Cada lado de un cuadro mide al menos 100, dos
cuadros no pueden solaparse y cada mancha debe quedar entera bajo un solo
cuadro. Hay que hallar la menor área total.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego cada mancha como `R X Y`.

## Salida

La menor área total.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
50 50 50
50 250 50
10 150 250
```

Salida:

```
40000
```

## Solución

Un cuadro es un rectángulo de lados paralelos a los ejes, así que tapa
una mancha justo cuando tapa su cuadrado circunscrito
`[X − R, X + R] × [Y − R, Y + R]`. El cuadro para un grupo de manchas es
entonces la caja que rodea sus cuadrados, ensanchada hasta 100 donde sea
más estrecha: `max(w, 100) · max(h, 100)`.

Dos rectángulos que no se solapan quedan separados por una recta vertical
u horizontal, y cada uno puede ensancharse hasta 100 en su propio lado de
esa recta sin tocar al otro. Así que se prueba un solo cuadro y luego
todas las formas de separar las manchas con una recta vertical y con una
horizontal.

Para una recta vertical se ordenan los cuadrados por su borde izquierdo.
Toda separación válida es un prefijo de ese orden: todo lo de la
izquierda termina no más tarde de donde empieza todo lo de la derecha, y
un cuadrado empieza antes de terminar. Un prefijo de k cuadrados puede
colgar aparte del resto justo cuando su borde derecho es como mucho el
borde izquierdo del cuadrado k. Con las cajas de todos los prefijos y
sufijos, cada separación cuesta O(1). `O(N log N)`.

Detalles a tener en cuenta:

- los dos cuadros pueden tocarse por un borde: la prueba 04 lo necesita;
- el mínimo de 100 milímetros vale para cada cuadro: una sola mancha
  diminuta ya necesita un cuadro de 100 × 100 (prueba 02);
- un borde de un cuadrado puede ser negativo cuando R > X; solo importan
  las diferencias.

Las respuestas se compararon con la prueba de todas las particiones de
las manchas en dos grupos en 800 casos pequeños aleatorios.

## Notas por lenguaje

- Python y Java guardan una caja como una tupla o un arreglo de cuatro
  números; C++, Go y Rust usan una estructura pequeña.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1245_geometry.cpp](1245_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.015 s | 264 KB |
| [1245_geometry.go](1245_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.031 s | 1284 KB |
| [1245_geometry.java](1245_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.125 s | 2944 KB |
| [1245_geometry.py](1245_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.078 s | 1260 KB |
| [1245_geometry.rs](1245_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.031 s | 228 KB |
