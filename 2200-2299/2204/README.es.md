# 2204. Elegir fechas de examen que bloqueen el menor número de viajes

[Timus 2204](https://acm.timus.ru/problem.aspx?space=1&num=2204) · dificultad 1321 · dp, two_pointers

Problema original de Ivan Kogut, de la Olimpiada Académica Universitaria Escolar de Informática 2022.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de n exámenes se puede hacer en uno de dos rangos de días, y
los exámenes van en orden sin solaparse. Hay m viajes disjuntos, también
en orden. Un viaje se pierde si comparte un día con un rango de examen
elegido. Elegir los rangos para conservar el mayor número de viajes. Los
límites son 1 segundo y 256 MB.

## Entrada

n y m, 1 ≤ n, m ≤ 10⁵, luego los dos rangos de cada examen y los rangos
de los viajes, con días hasta 10⁹.

## Salida

El mayor número de viajes conservados.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 5
3 5 7 9
43 50 51 58
100 103 111 114
6 6
47 47
101 101
103 103
112 112
```

Salida:

```
4
```

## Solución

Se minimiza en su lugar el número de viajes perdidos. Los viajes que
tocan un rango de días forman un bloque contiguo de los viajes
ordenados, hallado con dos punteros que solo avanzan, porque los rangos
vienen en orden creciente.

La DP guarda, para cada opción del examen actual, el menor número de
viajes perdidos hasta ahora y el índice del último viaje que bloquea esa
opción. El único solapamiento entre exámenes consecutivos es un viaje
largo que toca ambos rangos elegidos: solo puede ser el último viaje
bloqueado por el rango anterior y el primero bloqueado por el
siguiente. Así, si una opción bloquea c viajes, su coste es c más el
mejor de los dos costes anteriores, cada uno reducido en uno si su
último viaje bloqueado es el primero de esta opción. Un viaje que abarca
tres exámenes también toca el del medio, así que se resta en cada paso y
se cuenta una sola vez.

En el ejemplo los dos primeros exámenes pueden evitar todos los viajes,
y el último bloquea o los viajes de los días 101 y 103 o el del día 112,
así que se pierde un viaje y se conservan cuatro.

Esto cuesta O(n + m).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2204_dp_two_pointers.cpp](2204_dp_two_pointers.cpp) | G++ 13.2 x64 | dp, two_pointers | O(n + m) | AC | 0.109 s | 2084 KB |
| [2204_dp_two_pointers.go](2204_dp_two_pointers.go) | Go 1.14 x64 | dp, two_pointers | O(n + m) | AC | 0.062 s | 20120 KB |
| [2204_dp_two_pointers.java](2204_dp_two_pointers.java) | Java 1.8 | dp, two_pointers | O(n + m) | AC | 0.125 s | 2716 KB |
| [2204_dp_two_pointers.py](2204_dp_two_pointers.py) | Python 3.12 x64 | dp, two_pointers | O(n + m) | AC | 0.546 s | 62660 KB |
| [2204_dp_two_pointers.rs](2204_dp_two_pointers.rs) | Rust 1.75 x64 | dp, two_pointers | O(n + m) | AC | 0.062 s | 13792 KB |
