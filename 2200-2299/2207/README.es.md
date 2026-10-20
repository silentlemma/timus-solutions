# 2207. El menor alcance Manhattan que llena el mayor número de empleos

[Timus 2207](https://acm.timus.ru/problem.aspx?space=1&num=2207) · dificultad 1757 · geometry, dsu

Problema original de Ivan Kogut, de la Olimpiada Académica Universitaria Escolar de Informática 2022.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n casas albergan aᵢ personas y m granjas ofrecen bⱼ empleos, todas en
casillas distintas. Con alcance D, una persona puede moverse entre una
casa y una granja a distancia Manhattan a lo sumo D tantas veces como
quiera, pero nunca directamente entre dos casas o dos granjas. Hallar
el mayor número de empleos ocupados y el menor D que lo consigue. Los
límites son 2 segundos y 256 MB.

## Entrada

W y H hasta 10⁹, luego n y m, 1 ≤ n, m ≤ 10⁴, y luego las casas y las
granjas como x y cantidad, con cantidades hasta 10⁹.

## Salida

La mejor puntuación y el menor alcance.

## Ejemplos

### Ejemplo 1

Entrada:

```
11 11
4 4
1 1 2
7 1 1
1 11 2
11 11 1
4 4 1
10 4 2
4 11 1
8 11 2
```

Salida:

```
6 7
```

## Solución

Para un D fijo, la gente se mueve libremente dentro de cada componente
conexa del grafo bipartito entre casas y granjas, así que una
componente llena min(personas, empleos) empleos. Cuando D lo conecta
todo, la puntuación es min(Σa, Σb), la mejor posible, y la tarea es el
menor D cuyas componentes llegan a ese total.

Las componentes para cualquier D son las del bosque generador mínimo del
grafo casa–granja con pesos Manhattan, así que las aristas de un árbol
generador mínimo se añaden en orden creciente a una unión de conjuntos
disjuntos que lleva personas y empleos por componente, y la respuesta es
el peso de la arista con la que la puntuación llega por primera vez a
min(Σa, Σb).

El árbol generador se construye con el algoritmo de Borůvka. En cada
ronda cada componente necesita su arista más barata hacia un punto del
otro tipo en otra componente. Para la distancia Manhattan esto se divide
en cuatro cuadrantes de signos: en el cuadrante donde la pareja tiene
x' ≤ x e y' ≤ y, la distancia es (x + y) − (x' + y'), así que un
barrido en orden de x con un árbol de Fenwick sobre y pide el mayor
x' + y' del otro tipo. Cada nodo de Fenwick guarda los dos mejores
valores de componentes distintas, así que la mejor pareja fuera de la
propia componente siempre está disponible. Hay O(log N) rondas de
O(N log N) trabajo cada una.

En el ejemplo hay 6 personas y 6 empleos, y el alcance 7 es el primero
que permite trabajar a todas.

Esto cuesta O(N log² N) con N = n + m.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2207_geometry_dsu.cpp](2207_geometry_dsu.cpp) | G++ 13.2 x64 | geometry, dsu | O(N log² N) | AC | 0.140 s | 3032 KB |
| [2207_geometry_dsu.go](2207_geometry_dsu.go) | Go 1.14 x64 | geometry, dsu | O(N log² N) | AC | 0.218 s | 12280 KB |
| [2207_geometry_dsu.java](2207_geometry_dsu.java) | Java 1.8 | geometry, dsu | O(N log² N) | AC | 0.453 s | 11112 KB |
| [2207_geometry_dsu.py](2207_geometry_dsu.py) | PyPy 3.10 x64 | geometry, dsu | O(N log² N) | AC | 1.390 s | 34872 KB |
| [2207_geometry_dsu.rs](2207_geometry_dsu.rs) | Rust 1.75 x64 | geometry, dsu | O(N log² N) | AC | 0.140 s | 5568 KB |
