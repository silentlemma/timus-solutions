# 1016. El paseo más barato de un cubo rodando por un tablero de ajedrez

[Timus 1016](https://acm.timus.ru/problem.aspx?space=1&num=1016) · dificultad 823 · dijkstra, graphs

Problema original del Ural State University Internal Contest '99 #2.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cubo con un número de 0 a 1000 en cada cara está sobre una casilla de un
tablero de 8×8; su arista mide lo mismo que el lado de una casilla. Un
movimiento lo hace rodar sobre una arista de su cara inferior hasta una
casilla vecina por un lado. El coste de un paseo es la suma de los números
de la cara inferior en todas las casillas en que se apoya, incluidas la
primera y la última (un número se cuenta cada vez que su cara queda abajo).
Encuentra un paseo de coste mínimo entre dos casillas distintas dadas.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

Una línea: la casilla inicial y la final en notación de ajedrez (`a`–`h` y
`1`–`8`), y luego los números de las caras cercana, lejana, superior,
derecha, inferior e izquierda al principio. La «cercana» mira a la fila 1 y
la «derecha» a la columna `h`.

## Salida

Una línea: el coste mínimo y luego las casillas del paseo desde la inicial
hasta la final, separadas por espacios.

## Evaluación

Se acepta cualquier paseo óptimo. El verificador hace rodar el cubo por el
paseo impreso: cada paso debe ir a una casilla vecina por un lado dentro del
tablero, el paseo debe empezar y terminar en las casillas dadas y su coste
debe coincidir con la suma impresa y con el mínimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
b2 b3 0 9 1 3 1 1
```

Salida:

```
5 b2 a2 a1 b1 b2 b3
```

### Ejemplo 2

Entrada:

```
a1 h8 1 1 1 1 1 1
```

Salida:

```
15 a1 a2 a3 a4 a5 a6 b6 b7 c7 c8 d8 e8 f8 g8 h8
```

## Solución

El coste de la siguiente casilla depende de qué cara queda abajo, así que la
casilla sola no basta: el **estado** es la casilla junto con la orientación
del cubo. Un cubo tiene 24 orientaciones, así que hay `64 · 24 = 1536`
estados, cada uno con como mucho 4 movimientos.

**Orientaciones.** Para cada posición (cercana, lejana, superior, derecha,
inferior, izquierda) se guarda el índice de la cara original que está ahí.
Rodar es una permutación fija de posiciones; por ejemplo, rodar hacia la
cara lejana lleva arriba → lejana → abajo → cercana → arriba. Empezando por
la orientación identidad y aplicando los cuatro giros hasta que no aparezca
nada nuevo se obtienen las 24 orientaciones y una tabla de transiciones
`next[orientación][dirección]`.

**Camino mínimo.** Entrar en un estado cuesta el número de su cara
inferior, y el estado inicial cuesta su propia cara inferior. Todos los
costes son no negativos, así que el algoritmo de Dijkstra encuentra el paseo
más barato; se guarda el predecesor de cada estado y, al final, se toma el
más barato de los 24 estados de la casilla final y se siguen los
predecesores hacia atrás. `O(S log S)` con `S = 1536`: instantáneo.

Detalles a tener en cuenta:

- el paseo con menos casillas a menudo no es el más barato: al cubo le
  puede convenir dar una vuelta para bajar una cara barata;
- números iguales en caras distintas: sigue las caras por su posición en la
  entrada, no por sus valores;
- la cara inferior en la casilla inicial también cuenta.

## Notas por lenguaje

El mismo Dijkstra en todos los lenguajes, con la cola de prioridad estándar
de cada uno (`container/heap` en Go, `BinaryHeap` con `Reverse` en Rust).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1016_dijkstra.cpp](1016_dijkstra.cpp) | G++ 13.2 x64 | dijkstra | O(S log S), S = 64 · 24 states | AC | 0.015 s | 428 KB |
| [1016_dijkstra.go](1016_dijkstra.go) | Go 1.14 x64 | dijkstra | O(S log S), S = 64 · 24 states | AC | 0.015 s | 1236 KB |
| [1016_dijkstra.java](1016_dijkstra.java) | Java 1.8 | dijkstra | O(S log S), S = 64 · 24 states | AC | 0.140 s | 3892 KB |
| [1016_dijkstra.py](1016_dijkstra.py) | Python 3.12 x64 | dijkstra | O(S log S), S = 64 · 24 states | AC | 0.046 s | 920 KB |
| [1016_dijkstra.rs](1016_dijkstra.rs) | Rust 1.75 x64 | dijkstra | O(S log S), S = 64 · 24 states | AC | 0.015 s | 468 KB |
