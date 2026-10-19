# 1848. Caza de moscas

[Timus 1848](https://acm.timus.ru/problem.aspx?space=1&num=1848) · dificultad 4252 · geometry

Problema original de Denis Dublennykh, del Ural SU Contest en la sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n moscas están en puntos distintos de una pared. m amigos golpean la
pared con matamoscas y dejan marcas que son polígonos simples sin puntos
comunes. Una mosca muere si está dentro de una marca o en su borde.
Contar las moscas que mató cada matamoscas.

## Entrada

n (1 ≤ n ≤ 10⁵) y las coordenadas de las moscas, luego m
(1 ≤ m ≤ 30 000) y las marcas, cada una con su número de vértices y los
vértices en sentido antihorario. Hay como mucho 10⁵ vértices en total,
y todas las coordenadas son enteros de valor absoluto hasta 10⁷.

## Salida

El número de moscas que mató cada matamoscas, en el orden de entrada.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
0 0
1 1
4 4
3
3 -2 -2 -3 -3 -2 -3
3 0 0 2 0 1 1
3 3 0 5 0 4 6
```

Salida:

```
0
2
1
```

## Solución

Las marcas son disjuntas, así que ninguna está dentro de otra, y una
mosca que no está en ningún borde está dentro de una marca exactamente
cuando el lado más cercano justo encima de ella es un lado de esa marca
con el interior debajo. En un polígono antihorario el interior queda a
la izquierda de cada lado, así que los lados que van de derecha a
izquierda son los que tienen el interior debajo.

Una recta vertical de barrido avanza de izquierda a derecha y guarda los
lados que la cortan, ordenados de abajo arriba. Para esquivar los
vértices, una mosca en x se busca justo a la derecha de x: un lado de
x₁ a x₂ (x₁ < x₂) está activo para x₁ ≤ x < x₂, y en cada columna los
lados que terminan salen antes de que entren los que empiezan. Una mosca
en un vértice sí está dentro, así que los vértices se guardan en una
tabla hash, y los lados verticales, que nunca entran en el barrido, se
guardan por x como intervalos ordenados. Cualquier otra mosca en un
borde está sobre un lado activo.

Los lados no se cortan, así que dos lados activos se ordenan con una
sola prueba de orientación: se toma el que tiene el extremo izquierdo
más a la derecha y se prueba ese extremo contra la recta del otro; si el
extremo está sobre ella, ambos lados salen de un vértice común de una
marca y decide el otro extremo. Una mosca se compara igual, como un lado
de longitud cero. Todos los productos quedan por debajo de 4·10¹⁴. El
primer lado activo que no está debajo de la mosca o pasa por ella o es
el más cercano por encima. Los lados están en un árbol de búsqueda
equilibrado (un treap en Go, una lista de cubetas ordenadas cortas en
Python, que corre en PyPy). `O((n + V) log V)` para V vértices. La
solución en Python guarda las aristas y las coordenadas en arreglos
planos de enteros y ocupa 25 MB en el juez; una versión anterior con
tuplas y diccionarios ocupaba 70 MB en la prueba 11 del juez.

En el ejemplo las moscas (0, 0) y (1, 1) son vértices del segundo
triángulo. Justo a la derecha de x = 4 el lado más cercano encima de
(4, 4) es el del tercer triángulo de (5, 0) a (4, 6), que va de derecha
a izquierda, así que esa mosca también está dentro.

Trampas:

- moscas en la vertical de un vértice: buscar justo a la derecha de x
  evita los empates entre los dos lados de un pico;
- los lados verticales y los vértices se comprueban aparte del barrido;
- lados dados de arriba abajo hacen que cada inserción caiga al fondo,
  lo que a una lista ordenada simple le cuesta tiempo cuadrático.

Los conteos coinciden con una prueba directa de cada mosca contra cada
marca cercana en paredes aleatorias de hasta 30 000 marcas, con moscas
en rejillas, en vértices y en lados, y con una implementación aceptada
independiente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1848_geometry.cpp](1848_geometry.cpp) | G++ 13.2 x64 | geometry | O((n + V) log V) | AC | 0.421 s | 18080 KB |
| [1848_geometry.go](1848_geometry.go) | Go 1.14 x64 | geometry | O((n + V) log V) | AC | 0.312 s | 36780 KB |
| [1848_geometry.java](1848_geometry.java) | Java 1.8 | geometry | O((n + V) log V) | AC | 0.671 s | 35404 KB |
| [1848_geometry.py](1848_geometry.py) | PyPy 3.10 x64 | geometry | O((n + V) log V) | AC | 0.906 s | 25480 KB |
| [1848_geometry.rs](1848_geometry.rs) | Rust 1.75 x64 | geometry | O((n + V) log V) | AC | 0.109 s | 25816 KB |
