# 1481. Posibilidades de ganar

[Timus 1481](https://acm.timus.ru/problem.aspx?space=1&num=1481) · dificultad 2273 · greedy

Problema original de Sergey Pupyrev, del Campeonato de la Universidad Estatal de los Urales, 7 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N pesas distintas (1 ≤ N ≤ 50, enteros positivos hasta 1000) se ponen
una a una en una balanza de platillos, cada una en el platillo
izquierdo o en el derecho. Tras cada pesa se anotó el platillo más
pesado con L o R; la balanza nunca quedó equilibrada. Dadas las pesas y
la anotación, hay que escribir un orden de las pesas con sus platillos
que produzca la anotación, o «I'm too stupid to solve this problem» si
no lo hay.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

N, las pesas y luego la anotación de N letras.

## Salida

N líneas: una pesa y su platillo, en el orden en que se pusieron.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
10 20 30
LRL
```

Salida:

```
10 L
20 R
30 L
```

## Solución

Siempre existe un orden. Se ordenan las pesas y las ya usadas se
mantienen como un tramo contiguo de la lista ordenada en el que las
vecinas están en platillos opuestos. Entonces el platillo con la pesa
mayor pesa estrictamente más: emparejando desde arriba,
(a_k − a_(k−1)) + (a_(k−2) − a_(k−3)) + … es positivo.

Sea c el número de cambios de letra en la anotación. Se empieza con la
pesa que tiene exactamente c pesas más pesadas, en el platillo de la
primera letra. En cada cambio se añade la siguiente pesa más pesada en
el platillo opuesto a la mayor actual, que pasa a ganar. En cada
repetición se añade la siguiente pesa más ligera en el platillo opuesto
a la menor actual; la pesa mayor, y con ella el platillo ganador, no
cambia. Los c cambios gastan justo las c pesas más pesadas y las
repeticiones gastan las más ligeras. `O(N log N)`.

Detalles a tener en cuenta:

- el mensaje no se escribe nunca: toda anotación es posible (todas las
  pruebas);
- cargar siempre el platillo más ligero en orden de peso decreciente
  falla con pesas cercanas: 7, 6, 5 produce LLR en lugar de LLL (prueba 05);
- aquí cada cambio usa una pesa mayor, así que el comienzo debe dejar
  justo las suficientes más pesadas (prueba 04, gen2).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1481_greedy.cpp](1481_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 200 KB |
| [1481_greedy.go](1481_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.031 s | 1108 KB |
| [1481_greedy.java](1481_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.140 s | 1732 KB |
| [1481_greedy.py](1481_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.093 s | 552 KB |
| [1481_greedy.rs](1481_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.046 s | 260 KB |
