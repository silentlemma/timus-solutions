# 1399. El director ahorrador

[Timus 1399](https://acm.timus.ru/problem.aspx?space=1&num=1399) · dificultad 8299 · dp, local_search

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

El coste mínimo de un viaje depende solo de su conjunto de clientes.
C++, Go y Rust lo calculan para los 2ᴹ conjuntos con Held-Karp: hasta
2²⁰·20 casillas de 16 bits guardan caminos mínimos desde el almacén por
cada conjunto hasta cada cliente, que solo se extienden fuera del conjunto. Java guarda
conjuntos factibles y extremos interiores; Python estima vueltas bajo
demanda.

Después, el plan es elegir un viaje para cada artículo. Se empieza con
la inserción más barata: cada artículo va al viaje cuya vuelta crece
menos, o a uno nuevo, respetando la capacidad. Luego vienen hasta 300 000
rondas de búsqueda de vecindad grande: se sacan algunos artículos
(algunos al azar, un viaje entero o todos los de un cliente), se
devuelven uno a uno en orden aleatorio por inserción más barata, y la
ronda se deshace si el total creció más que un umbral que baja
linealmente del 2% del primer plan a cero. Se imprime el mejor plan
visto, con cada ruta recuperada de la tabla en las versiones con DP.
Aquí R cuenta rondas, T posiciones de viajes, S conjuntos de clientes
en caché y B llamadas de ramificación y poda.

Detalles a tener en cuenta:

- los artículos de un cliente pueden necesitar varios viajes (prueba 03
  y prueba generada 6), así que el plan es por artículo y no por
  cliente;
- un viaje vaciado se reutiliza antes de abrir uno nuevo; si no, las
  posiciones de viajes vacíos pueden acumularse con las rondas;
- los números aleatorios salen del mismo generador xorshift y la
  aceptación usa solo enteros, así que C++, Go, Java y Rust imprimen el
  mismo plan; Python busca con un presupuesto de tiempo, por lo que la
  longitud de sus planes puede variar según el entorno de ejecución y
  la máquina.

Los planes se compararon con el óptimo exacto, hallado con una búsqueda
sobre todas las particiones de los artículos, en 300 instancias pequeñas
aleatorias, y todos fueron óptimos; en el ejemplo el total es 34, como
el del jurado. El verificador valida el plan y permite un total hasta
un 10 % mayor que el de la prueba. La aceptación de Python no da una
garantía general de aproximación.

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

- Python se ejecuta con PyPy, evitando la tabla densa de subconjuntos
  que junto con la búsqueda llevaba 2,03 s en la prueba 24 del juez.
  Elimina clientes sin artículos y guarda vueltas hechas desde conjuntos
  vecinos o por inserción más barata, mejoradas con 2-opt, traslados de
  hasta tres clientes y reinicios que intercambian tramos contiguos en
  tres puntos de corte. Si todos los artículos caben en un viaje, o cada
  subconjunto propio de clientes activos cabe con todos sus artículos,
  intenta resolver exactamente uno o dos viajes con cotas de 1-árboles
  y ramificación y poda, volviendo a la heurística tras 10 000 nodos.
  La búsqueda principal apunta a 1,4 s de tiempo total de procesador,
  comprobado cada 256 rondas, y termina al alcanzar una cota inferior;
  el umbral baja con las rondas o el tiempo, lo que se agote antes.
  El intento exacto y la mejora final quedan fuera de esa comprobación:
  1,39 s en el juez.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1399_dp.cpp](1399_dp.cpp) | G++ 13.2 x64 | dp | O(2^M·M^2 + R·N·T) | AC | 0.531 s | 44860 KB |
| [1399_dp.go](1399_dp.go) | Go 1.14 x64 | dp | O(2^M·M^2 + R·N·T) | AC | 0.906 s | 52476 KB |
| [1399_dp.java](1399_dp.java) | Java 1.8 | dp | O(2^M·M^2 + R·N·T) | AC | 1.484 s | 32160 KB |
| [1399_local_search.py](1399_local_search.py) | PyPy 3.10 x64 | local_search | O(R·N·T + (S+1)·M^3 + B·M^2) | AC | 1.390 s | 11836 KB |
| [1399_dp.rs](1399_dp.rs) | Rust 1.75 x64 | dp | O(2^M·M^2 + R·N·T) | AC | 0.750 s | 49288 KB |
