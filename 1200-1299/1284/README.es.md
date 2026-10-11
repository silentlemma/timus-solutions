# 1284. Póquer espacial

[Timus 1284](https://acm.timus.ru/problem.aspx?space=1&num=1284) · dificultad 2284 · bruteforce

Problema original de Leonid Volkov, del Concurso Individual de la Universidad Estatal de los Urales 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una mano de N ≤ 20 cartas distintas está en fila; cada carta tiene un
valor de 1 a 100 y un palo de 1 a 10. Los palos impares son azules y
los pares amarillos, y el número de palos azules y amarillos de la mano
difiere como mucho en uno. Un movimiento toma una carta y la pone en
cualquier lugar de la fila. Hay que hallar el menor número de
movimientos tras los que cada palo queda junto, los palos azules y
amarillos se alternan, y dentro de cada palo los valores están
ordenados, todos los palos igual (todos crecientes o todos
decrecientes).

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego las N cartas como valor y palo, de izquierda a derecha.

## Salida

El menor número de movimientos.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
10 1
12 2
8 2
4 4
7 4
```

Salida:

```
2
```

## Solución

Las cartas que nunca se mueven conservan su orden relativo, y cada
carta movida puede dejarse directamente en su lugar final. Así que para
una disposición objetivo fija la respuesta es N menos la subsecuencia
más larga de la mano que ya va en el orden objetivo: se da a cada carta
su puesto en el objetivo y se toma la subsecuencia creciente más larga
de puestos.

Los objetivos solo difieren en el orden de los palos azules, el de los
amarillos, qué color va primero (fijado si un color tiene más palos) y
el sentido de la ordenación. Con como mucho cinco palos de cada color
son como mucho 5! · 5! · 2 · 2 = 57 600 objetivos, cada uno comprobado
con una subsecuencia creciente más larga en `O(N log N)`.

Detalles a tener en cuenta:

- el sentido es común: un palo creciente y otro decreciente no vale;
- si un color tiene más palos, debe empezar y acabar la fila
  (prueba 08);
- una mano ya ordenada no necesita movimientos (pruebas 04, 06).

Las respuestas se compararon con una búsqueda en anchura sobre todas
las disposiciones alcanzables con movimientos sueltos en 200 manos
aleatorias de hasta seis cartas.

## Notas por lenguaje

- C++ recorre los órdenes de palos con `next_permutation`; los demás
  lenguajes intercambian elementos de forma recursiva.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1284_bruteforce.cpp](1284_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(5!² · N log N) | AC | 0.031 s | 208 KB |
| [1284_bruteforce.go](1284_bruteforce.go) | Go 1.14 x64 | bruteforce | O(5!² · N log N) | AC | 0.046 s | 5948 KB |
| [1284_bruteforce.java](1284_bruteforce.java) | Java 1.8 | bruteforce | O(5!² · N log N) | AC | 0.156 s | 5880 KB |
| [1284_bruteforce.py](1284_bruteforce.py) | Python 3.12 x64 | bruteforce | O(5!² · N log N) | AC | 0.531 s | 608 KB |
| [1284_bruteforce.rs](1284_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(5!² · N log N) | AC | 0.046 s | 228 KB |
