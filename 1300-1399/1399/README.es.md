# 1399. El director ahorrador

[Timus 1399](https://acm.timus.ru/problem.aspx?space=1&num=1399) · dificultad 9494 · dp

Problema original de Alexander Ipatov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un solo camión de capacidad Lmax ≤ 3000 reparte N ≤ 50 artículos desde
un almacén a M ≤ 20 clientes. Cada artículo tiene un peso y un cliente,
las distancias entre el almacén y los clientes están dadas y cumplen la
desigualdad triangular, y cada viaje empieza y termina en el almacén.
Hay que planificar los viajes con una distancia total pequeña: un plan
se acepta si no es más largo que el que encuentra el programa del
jurado.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

M, N y Lmax, la matriz de distancias de (M+1)×(M+1) con el almacén como
0, y luego el peso y el cliente de cada artículo.

## Salida

El número de viajes; luego, para cada viaje, sus artículos, su carga, su
ruta de 0 de vuelta a 0 y su longitud; al final la longitud total, con
líneas en blanco entre los bloques como en el ejemplo.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 10 5
0 2 3 4 5 6 5 4
2 0 4 5 6 7 6 5
3 4 0 3 4 5 4 1
4 5 3 0 3 4 1 2
5 6 4 3 0 1 2 3
6 7 5 4 1 0 3 4
5 6 4 1 2 3 0 3
4 5 1 2 3 4 3 0
3 1
5 2
1 3
1 4
2 5
1 6
2 7
1 5
2 2
1 1
```

Salida:

```
4

1 10
4
0 1 0
4

4 5 6 8
5
0 4 5 6 0
14

2
5
0 2 0
6

3 7 9
5
0 3 7 2 0
10

34
```

## Solución

Un viaje cuesta solo la vuelta más corta por su conjunto de clientes,
así que las soluciones la calculan primero para cada uno de los 2ᴹ
conjuntos. Una tabla de Held-Karp guarda el camino más corto desde el
almacén por cada conjunto terminando en cada cliente, números de 16 bits
en 2²⁰·20 casillas; los caminos solo se alargan desde clientes del
conjunto hacia clientes de fuera.

Después, el plan es elegir un viaje para cada artículo. Se empieza con
la inserción más barata: cada artículo va al viaje cuya vuelta crece
menos, o a uno nuevo, respetando la capacidad. Luego vienen 300 000
rondas de búsqueda de vecindad grande: se sacan algunos artículos
(algunos al azar, un viaje entero o todos los de un cliente), se
devuelven uno a uno en orden aleatorio por inserción más barata, y la
ronda se deshace si el total creció más que un umbral que baja
linealmente del 2% del primer plan a cero. Se imprime el mejor plan
visto, con cada ruta recuperada de la tabla. Insertar un artículo cuesta
una consulta por viaje, así que la búsqueda es barata frente a la tabla:
`O(2ᴹ·M²)` más las rondas.

Detalles a tener en cuenta:

- los artículos de un cliente pueden necesitar varios viajes (prueba 03
  y prueba generada 6), así que el plan es por artículo y no por
  cliente;
- un viaje vaciado se reutiliza antes de abrir uno nuevo; si no, el
  número de viajes crece sin fin durante la búsqueda;
- los números aleatorios salen del mismo generador xorshift y la
  aceptación usa solo enteros, así que C++, Go, Java y Rust imprimen el
  mismo plan y las pruebas pueden exigir su longitud; Python, que
  resuelve exactamente los casos de uno o dos viajes, puede imprimir un
  plan más corto.

Los planes se compararon con el óptimo exacto, hallado con una búsqueda
sobre todas las particiones de los artículos, en 300 instancias pequeñas
aleatorias, y todos fueron óptimos; en el ejemplo el total es 34, como
el del jurado. Las pruebas se juzgan con un verificador que comprueba el
plan y exige un total no más largo que el dado en la prueba.

## Notas por lenguaje

- Java guarda la tabla de subconjuntos solo para los recorridos que
  terminan dentro de su conjunto, los de un mismo conjunto contiguos, y
  la llena tomando los valores del conjunto sin el último cliente, así
  que se lee y escribe en orden; con una casilla para cada cliente y
  conjunto excedía el límite de 64 MB. Además omite los clientes sin
  artículos y los conjuntos que ningún viaje puede llevar, genera los
  números aleatorios sin BigInteger y se detiene enseguida si el primer
  plan es óptimo con certeza: 1,48 s en el juez, donde una versión
  anterior excedía el límite de tiempo en la prueba 25.

- Python se ejecuta con PyPy y calcula las longitudes de ronda solo para
  los conjuntos por los que pregunta la búsqueda, con una programación
  dinámica sobre las cantidades de clientes intercambiables y
  ramificación y poda con cotas inferiores de un árbol; cuando bastan
  uno o dos viajes halla directamente el plan óptimo, y si no ejecuta la
  misma búsqueda que los demás lenguajes. Cuatro rondas de estos cambios
  lo llevaron de la prueba 17 del juez a la 24, donde aún excede el
  límite de tiempo (2,03 s): en los casos más duros de aquí, veinte
  clientes y cargas que casi llenan el camión, las tablas de
  subconjuntos siguen necesitando unos 10⁸ pasos, unos 0,7 s solo de
  PyPy. Se mantiene marcada TLE: pasa todas las pruebas de aquí, pero no
  se afirma que sea lo bastante rápida en cada prueba del juez.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1399_dp.cpp](1399_dp.cpp) | G++ 13.2 x64 | dp | O(2^M·M^2) | AC | 0.531 s | 44860 KB |
| [1399_dp.go](1399_dp.go) | Go 1.14 x64 | dp | O(2^M·M^2) | AC | 0.906 s | 52476 KB |
| [1399_dp.java](1399_dp.java) | Java 1.8 | dp | O(2^M·M^2) | AC | 1.484 s | 32160 KB |
| [1399_dp.py](1399_dp.py) | PyPy 3.10 x64 | dp | O(2^M·M^2) | TLE (test 24) | 2.031 s | 32636 KB |
| [1399_dp.rs](1399_dp.rs) | Rust 1.75 x64 | dp | O(2^M·M^2) | AC | 0.750 s | 49288 KB |
