# 2196. El día en que el entorno creciente de un polígono convexo alcanza cada punto

[Timus 2196](https://acm.timus.ru/problem.aspx?space=1&num=2196) · dificultad 1617 · geometry, binary_search

Problema original de Vadim Barinov, de la clasificatoria del Campeonato Regional de los Urales ICPC 2023.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El día 0 se infecta un polígono convexo de N vértices. Cada día
posterior están infectados todos los puntos hasta cierta distancia del
polígono, y su área se duplica cada día. Para cada uno de Q puntos,
hallar el primer día en que está dentro o en el borde de la infección.
Los puntos están al menos a 10⁻⁶ de cada borde posterior. Los límites
son 3 segundos y 256 MB.

## Entrada

N, 3 ≤ N ≤ 10⁵, luego los vértices en sentido antihorario, luego Q,
1 ≤ Q ≤ 10⁵, y los puntos, con todas las coordenadas de valor absoluto
hasta 10⁹.

## Salida

El día de cada punto.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
1 3
1 1
3 1
3 3
4
2 2
1 2
4 1
6 2
```

Salida:

```
0
0
2
4
```

## Solución

El conjunto de puntos a distancia a lo sumo d de un polígono convexo de
área A y perímetro P tiene área A + P d + π d²: el polígono, una franja
a lo largo de cada lado y sectores circulares en las esquinas que suman
un círculo completo. Así el día i tiene el radio dᵢ que resuelve
A + P d + π d² = 2ⁱ A, escrito como
dᵢ = (2ⁱ − 1) A / (P/2 + √(P²/4 + π (2ⁱ − 1) A)) para evitar la
cancelación. Los radios superan la mayor distancia posible tras unos 70
días, y a un punto a distancia D del polígono le corresponde el primer
dᵢ ≥ D.

La distancia a un polígono convexo cuesta O(log N) por punto. Una
búsqueda binaria sobre el abanico de triángulos desde el vértice 0
decide si el punto está dentro (día 0) y, si no, halla un lado que mira
al punto y otro que no. A lo largo de la cadena
que mira al punto la distancia a los lados primero baja y luego sube,
así que una segunda búsqueda binaria, por el signo de una proyección,
halla el lado o vértice más cercano.

Cuando la distancia está a menos de 10⁻⁵ de un radio, la comparación se
repite sin raíces en aritmética double-double: con la distancia como
√(u / v) y E = (2ⁱ − 1) A, el punto está infectado cuando E v − π u ≥ 0
y (E v − π u)² ≥ P² u v.

En el ejemplo el cuadrado tiene A = 4 y P = 8; el punto (6, 2) está a
distancia 3, y el día 4 es el primero con 8d + πd² = 60 en d ≈ 3.28.

Todo cuesta O(N + Q log N).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2196_geometry_binary_search.cpp](2196_geometry_binary_search.cpp) | G++ 13.2 x64 | geometry, binary_search | O(N + Q log N) | AC | 0.171 s | 7904 KB |
| [2196_geometry_binary_search.go](2196_geometry_binary_search.go) | Go 1.14 x64 | geometry, binary_search | O(N + Q log N) | AC | 0.187 s | 30296 KB |
| [2196_geometry_binary_search.java](2196_geometry_binary_search.java) | Java 1.8 | geometry, binary_search | O(N + Q log N) | AC | 0.578 s | 12632 KB |
| [2196_geometry_binary_search.py](2196_geometry_binary_search.py) | PyPy 3.10 x64 | geometry, binary_search | O(N + Q log N) | AC | 1.187 s | 49568 KB |
| [2196_geometry_binary_search.rs](2196_geometry_binary_search.rs) | Rust 1.75 x64 | geometry, binary_search | O(N + Q log N) | AC | 0.171 s | 15164 KB |
