# 1515. Reforma financiera

[Timus 1515](https://acm.timus.ru/problem.aspx?space=1&num=1515) · dificultad 215 · greedy

Problema original de Ilya Grebnov, Nikita Rybak y Dmitry Kovalioff, de Timus Top Coders: Third Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay un billete de cada uno de N valores (1 ≤ N ≤ 100), dados en orden
creciente, cada uno de 1 a 10⁶. Hay que hallar el menor valor positivo
que no es la suma de algunos de esos billetes; un solo billete cuenta
como suma.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego los N valores en orden creciente.

## Salida

El menor valor que ningún conjunto de billetes suma.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
1 2 4 9 100
```

Salida:

```
8
```

## Solución

Se recorren los valores en orden creciente guardando reach, el mayor
número tal que toda suma de 1 a reach se puede pagar. Si el siguiente
valor d es como mucho reach + 1, también se puede pagar toda suma hasta
reach + d: las sumas hasta reach como antes, y las mayores como d más
una suma hasta reach. Si d > reach + 1, entonces reach + 1 no se puede
pagar: los valores tomados suman solo reach, y cualquier otro valor ya
es mayor que reach + 1 por sí solo. La respuesta es reach + 1. `O(N)`.

Detalles a tener en cuenta:

- sin un billete de 1 la respuesta es 1 (pruebas 03, 06);
- la respuesta puede superar todos los valores, hasta la suma de todos
  más uno (pruebas 04, 05, gen2);
- el primer hueco termina el recorrido y ningún valor posterior lo
  llena: con 1 y 3 falta la suma 2 (prueba 07).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1515_greedy.cpp](1515_greedy.cpp) | G++ 13.2 x64 | greedy | O(N) | AC | 0.015 s | 196 KB |
| [1515_greedy.go](1515_greedy.go) | Go 1.14 x64 | greedy | O(N) | AC | 0.031 s | 1096 KB |
| [1515_greedy.java](1515_greedy.java) | Java 1.8 | greedy | O(N) | AC | 0.109 s | 500 KB |
| [1515_greedy.py](1515_greedy.py) | Python 3.12 x64 | greedy | O(N) | AC | 0.078 s | 428 KB |
| [1515_greedy.rs](1515_greedy.rs) | Rust 1.75 x64 | greedy | O(N) | AC | 0.015 s | 228 KB |
