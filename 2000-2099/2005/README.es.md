# 2005. La ruta permitida más corta entre cinco paradas

[Timus 2005](https://acm.timus.ru/problem.aspx?space=1&num=2005) · dificultad 94 · bruteforce

Problema original de Mikhail Rubinchik. (Prepared by Oleg Merkurev), del Concurso Regional Escolar de Programación de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Visitar cinco lugares exactamente una vez, empezando en 1 y terminando
en 5. El lugar 3 no puede ser la penúltima parada. Dadas todas las
distancias, hallar una ruta permitida de distancia total mínima y su
longitud. Se admite cualquier óptimo.

## Entrada

Una matriz entera de distancias de 5 por 5. Sus valores están entre 0 y
10000, la diagonal es cero, la matriz es simétrica y satisface la
desigualdad triangular `d[i][j]≤d[i][k]+d[k][j]`. Tiempo 0,5 segundos,
memoria 64 MB.

## Salida

En la primera línea, la distancia total mínima. En la segunda, los cinco
números de lugar en orden de visita, separados por espacios. Los empates
pueden resolverse libremente.

## Evaluación

Un comprobador verifica que la ruta está permitida, que la longitud
impresa es la suya y que es óptima; se acepta cualquier ruta óptima.

## Ejemplos

```
0 2600 3800 2600 2500
2600 0 5300 3900 4400
3800 5300 0 1900 4500
2600 3900 1900 0 3700
2500 4400 4500 3700 0
```

```
13500
1 2 3 4 5
```

La ruta mostrada cuesta `2600+5300+1900+3700=13500`; su penúltima parada
es 4, por lo que cumple la restricción.

## Solución

El punto 1 va primero y el 5 al final, así que solo varía el orden de
los puntos 2, 3 y 4: seis órdenes, de los que los dos con el 3 justo
antes del 5 están prohibidos. Se prueban los otros cuatro, se suman las
cuatro distancias de cada ruta y se queda la más corta. `O(1)`.

Detalles a tener en cuenta:

- la regla se refiere a la parada justo antes de la última;
- una ruta cuesta de 0 a 40 000, así que el mínimo empieza en «todavía
  ninguno», no en 0 ni en 10 000.

## Notas por lenguaje

- Python toma los órdenes de `itertools.permutations`; los demás
  lenguajes recorren los puntos con tres bucles anidados.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2005_bruteforce.cpp](2005_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(1) | AC | 0.015 s | 124 KB | 11303437 |
| [2005_bruteforce.go](2005_bruteforce.go) | Go 1.14 x64 | bruteforce | O(1) | AC | 0.031 s | 1104 KB | 11303440 |
| [2005_bruteforce.java](2005_bruteforce.java) | Java 1.8 | bruteforce | O(1) | AC | 0.125 s | 1616 KB | 11303442 |
| [2005_bruteforce.py](2005_bruteforce.py) | Python 3.12 x64 | bruteforce | O(1) | AC | 0.093 s | 432 KB | 11303445 |
| [2005_bruteforce.rs](2005_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(1) | AC | 0.031 s | 236 KB | 11303446 |
