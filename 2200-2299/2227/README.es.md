# 2227. Medir y cortar un polígono convexo por sus diagonales

[Timus 2227](https://acm.timus.ru/problem.aspx?space=1&num=2227) · dificultad 1200 · geometry, fenwick

Problema original de Vadim Barinov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un polígono convexo de N vértices recibe Q acciones por diagonales del
polígono actual: una medición informa la mayor de las dos áreas, y un
corte tira la parte menor (en empate, la parte con un vértice numerado
fuera del par elegido) e informa su área. Imprimir cada área informada
con error 10⁻⁹. Los límites son 0.5 segundos y 256 MB.

## Entrada

N y Q, 4 ≤ N ≤ 10⁵, 1 ≤ Q ≤ 10⁵, luego los vértices en sentido
antihorario con coordenadas de valor absoluto hasta 10⁹, y luego las
acciones "m l r" o "c l r".

## Salida

Un área por acción.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 4
2 0
3 1
2 2
0 2
0 0
m 5 3
m 2 4
c 1 3
m 4 1
```

Salida:

```
3.0
4.0
1.0
2.0
```

## Solución

Todas las áreas se guardan duplicadas, como enteros exactos, así que
toda respuesta termina en ".0" o ".5". Con l < r, el área duplicada del
polígono l, l + 1, …, r de los vértices originales es un tramo de las
sumas de prefijo de la fórmula del cordón más el término de cierre
x_r y_l − y_r x_l.

Los cortes solo quitan piezas, y cada pieza cortada por una diagonal
del polígono actual queda a un lado de toda diagonal posterior. Una
pieza cortada del arco l … r se anota en la primera arista l + 1 de ese
arco en un árbol de Fenwick; una pieza por fuera del arco se anota en la
arista r + 1, fuera de todo arco posterior. Para una diagonal posterior
(l, r), la parte del polígono actual en el arco interior es el área
original del arco menos las anotaciones en las aristas l + 1 … r, y la
otra parte es el total actual menos ella.

Una medición imprime la parte mayor. Un corte tira la parte menor, o la
exterior en empate, la anota como se ha dicho y reduce el total.

En el ejemplo la primera medición divide el pentágono de área 5 por la
diagonal 5–3 en partes de 3 y 2 e imprime 3.

Esto cuesta O(N + Q log N).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2227_geometry_fenwick.cpp](2227_geometry_fenwick.cpp) | G++ 13.2 x64 | geometry, fenwick | O(N + Q log N) | AC | 0.171 s | 2900 KB |
| [2227_geometry_fenwick.go](2227_geometry_fenwick.go) | Go 1.14 x64 | geometry, fenwick | O(N + Q log N) | AC | 0.078 s | 12032 KB |
| [2227_geometry_fenwick.java](2227_geometry_fenwick.java) | Java 1.8 | geometry, fenwick | O(N + Q log N) | AC | 0.218 s | 13944 KB |
| [2227_geometry_fenwick.py](2227_geometry_fenwick.py) | PyPy 3.10 x64 | geometry, fenwick | O(N + Q log N) | AC | 0.343 s | 52180 KB |
| [2227_geometry_fenwick.rs](2227_geometry_fenwick.rs) | Rust 1.75 x64 | geometry, fenwick | O(N + Q log N) | AC | 0.046 s | 11220 KB |
