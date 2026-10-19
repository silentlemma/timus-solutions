# 1883. El cumpleaños del ent

[Timus 1883](https://acm.timus.ru/problem.aspx?space=1&num=1883) · dificultad 1216 · geometry

Problema original de Denis Mukhametianov, del Concurso Regional por Equipos de Programación de los Urales 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una tarta es el cuadrado de (−10⁹, −10⁹) a (10⁹, 10⁹) con n velas en
puntos enteros distintos estrictamente dentro. Hay que cortar un
polígono convexo de área no nula que contenga exactamente k velas,
contando las del borde. Sus vértices deben ser puntos enteros de la
tarta, en sentido antihorario, sin ángulos llanos ni lados de longitud
cero.

## Entrada

n y k (1 ≤ k < n ≤ 1000) y luego las n velas; todas las coordenadas son
menores que 10⁹ en valor absoluto.

## Salida

El número m de vértices (3 ≤ m ≤ 10 000) y los vértices. Se acepta
cualquier polígono válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 3
1 0
1 2
2 1
3 0
3 2
```

Salida:

```
3
1 0
2 1
1 2
```

## Solución

Se ordenan las velas por x y luego por y, y sea (x, y) la k-ésima. Las
k primeras son todas las velas con x menor junto con las de la columna
x hasta y. Se toma todo hasta la columna x − 1, la columna x hasta
(x, y) y la franja entre las columnas x − 1 y x por
debajo de la recta de (x, y) a (x − 1, 10⁹):

(−10⁹, −10⁹), (x, −10⁹), (x, y), (x − 1, 10⁹), (−10⁹, 10⁹).

Todos los giros son estrictamente a la izquierda. La columna x − 1 queda
dentro entera, porque las velas están por debajo de 10⁹, y las velas
por encima de (x, y) en la columna x quedan fuera del lado inclinado.
Si x − 1 = −10⁹ el cuarto vértice repetiría el quinto, así que se quita
y queda un cuadrilátero. Ordenar cuesta `O(n log n)`.

En el ejemplo la tercera vela en este orden es (2, 1), y el pentágono
(−10⁹, −10⁹), (2, −10⁹), (2, 1), (1, 10⁹), (−10⁹, 10⁹) contiene
(1, 0), (1, 2) y (2, 1), una respuesta distinta pero válida.

Trampas:

- un corte vertical simple falla cuando varias velas comparten columna;
  el lado superior inclinado parte esa columna en la k-ésima vela;
- las velas del borde cuentan, así que la k-ésima vela puede estar en
  un vértice;
- con x − 1 = −10⁹ el vértice (x − 1, 10⁹) coincide con la esquina y
  hay que quitarlo para no tener un lado de longitud cero.

Los trozos pasan un comprobador de convexidad estricta, orientación,
rango de coordenadas y número de velas en 40 tableros pequeños
y en 125 tartas grandes aleatorias, muchas con columnas llenas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1883_geometry.cpp](1883_geometry.cpp) | G++ 13.2 x64 | geometry | O(n log n) | AC | 0.015 s | 208 KB |
| [1883_geometry.go](1883_geometry.go) | Go 1.14 x64 | geometry | O(n log n) | AC | 0.031 s | 1148 KB |
| [1883_geometry.java](1883_geometry.java) | Java 1.8 | geometry | O(n log n) | AC | 0.171 s | 2816 KB |
| [1883_geometry.py](1883_geometry.py) | Python 3.12 x64 | geometry | O(n log n) | AC | 0.078 s | 700 KB |
| [1883_geometry.rs](1883_geometry.rs) | Rust 1.75 x64 | geometry | O(n log n) | AC | 0.046 s | 296 KB |
