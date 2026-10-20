# 2155. Atrapar un dron que arrastra el viento en una cuadrícula con pesos

[Timus 2155](https://acm.timus.ru/problem.aspx?space=1&num=2155) · dificultad 990 · dijkstra

Problema original de Valentin Zuev, del Concurso Escolar de Programación de los Urales 2020.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En una cuadrícula h × w cada casilla tiene un coste de 1 a 999 999 y una
dirección de viento. Un caminante pasa a una vecina por un lado en
tantos segundos como el coste de esa vecina, o espera donde quiera. Un
dron avanza una casilla por segundo en la dirección del viento de su
casilla y se pierde cuando el viento apunta fuera de la cuadrícula. El
caminante lo atrapa estando en la casilla del dron mientras el dron está
allí; llegar en el momento en que se va es demasiado tarde. Hallar la
captura más temprana, o −1. Los límites son 2 segundos y 256 MB.

## Entrada

h y w, 1 ≤ h, w ≤ 250, las dos casillas de partida, los costes y luego
las letras de viento U, D, L, R.

## Salida

El tiempo más temprano, o −1.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 7
1 1
1 4
1 1 1 1 1 1 1
1 1 1 1 1 1 1
RDRDRDR
URURURU
```

Salida:

```
7
```

### Ejemplo 2

Entrada:

```
2 6
1 1
1 4
1 1 1 1 1 1
1 1 1 1 1 1
RDRDRD
URURUR
```

Salida:

```
-1
```

### Ejemplo 3

Entrada:

```
3 3
2 2
1 1
8 9 8
8 8 8
8 8 8
RRD
URD
ULL
```

Salida:

```
9
```

## Solución

Esperar es gratis, así que el caminante puede estar en una casilla en
cualquier momento a partir de su tiempo de llegada más corto, y el
algoritmo de Dijkstra desde el inicio da esos tiempos para todas las
casillas.

La ruta del dron es fija: es un recorrido por las flechas del viento, y
como cada casilla tiene un único sucesor, o sale de la cuadrícula o
entra en un ciclo. Se sigue hasta que una casilla se repite o el dron se
pierde, anotando el tiempo t de cada visita. El dron está en su casilla
en el instante t, así que atraparlo allí en t es posible exactamente
cuando la llegada más corta es a lo sumo t. Las casillas del ciclo se
visitan de nuevo cada periodo p, así que para ellas también cuenta la
primera visita no anterior a la llegada, t + ⌈(llegada − t) / p⌉ · p. La
respuesta es el menor de estos tiempos. El trabajo es O(hw log(hw)).

En el segundo ejemplo el dron se aleja siempre por un camino que sale de
la cuadrícula antes de que el caminante pueda adelantarse.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2155_dijkstra.cpp](2155_dijkstra.cpp) | G++ 13.2 x64 | dijkstra | O(hw log(hw)) | AC | 0.031 s | 1972 KB |
| [2155_dijkstra.go](2155_dijkstra.go) | Go 1.14 x64 | dijkstra | O(hw log(hw)) | AC | 0.031 s | 4784 KB |
| [2155_dijkstra.java](2155_dijkstra.java) | Java 1.8 | dijkstra | O(hw log(hw)) | AC | 0.125 s | 2720 KB |
| [2155_dijkstra.py](2155_dijkstra.py) | Python 3.12 x64 | dijkstra | O(hw log(hw)) | AC | 0.234 s | 16068 KB |
| [2155_dijkstra.rs](2155_dijkstra.rs) | Rust 1.75 x64 | dijkstra | O(hw log(hw)) | AC | 0.031 s | 4140 KB |
