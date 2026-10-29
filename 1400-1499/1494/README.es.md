# 1494. Monobillar

[Timus 1494](https://acm.timus.ru/problem.aspx?space=1&num=1494) · dificultad 90 · simulation

Problema original de Alex Samsonov, del Decimotercer Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 14 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las bolas 1, 2, …, N (1 ≤ N ≤ 100000) deben meterse en la única
tronera en este orden. De vez en cuando un inspector sacaba de la
tronera la última bola que había entrado, y al final las sacó todas.
Dado el orden en que el inspector sacó las bolas, hay que escribir
«Cheater» si no pudieron meterse en el orden correcto, y «Not a proof»
en otro caso.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego las N bolas en el orden en que las sacó el inspector.

## Salida

«Cheater» o «Not a proof».

## Ejemplos

### Ejemplo 1

Entrada:

```
2
2
1
```

Salida:

```
Not a proof
```

### Ejemplo 2

Entrada:

```
3
3
1
2
```

Salida:

```
Cheater
```

## Solución

La tronera es una pila: las bolas entran como 1, 2, …, N y el inspector
siempre saca la de arriba. Se repite la partida: se meten las bolas en
orden y, tras cada una, se sacan bolas mientras la de arriba sea la
siguiente de la lista del inspector. Esperar nunca ayuda, porque una
bola que no está arriba sigue tapada hasta que se va todo lo que tiene
encima. Si así se saca toda la lista, el orden era posible. `O(N)`.

Detalles a tener en cuenta:

- una bola tapada por otra posterior no puede salir antes: 3, 4, 1, 2
  es imposible (pruebas 02, 05);
- sacar todas las bolas al final invierte el orden, y sacar cada una al
  momento lo mantiene; ambos son posibles (gen4, gen5);
- un solo intercambio en una partida real suele bastar para hacerla
  imposible (gen3).

## Soluciones optimizadas

Las soluciones optimizadas simulan la tronera mientras leen: para cada
bola sacada meten las bolas hasta ese número, y entonces arriba de la
tronera debe estar esa bola; el primer desacuerdo termina el programa.
Así nunca guardan el orden de las bolas; la tronera es un arreglo usado
como pila. C++ analiza los números con `getchar` (0.031 s en lugar de
0.093 s y 512 KB en lugar de 1540 KB), Go los analiza a mano, escribe la
respuesta sin `fmt` y guarda la tronera en un arreglo de `int32`
reservado de antemano, ya que los números de las bolas son a lo sumo
100 000 (1312 KB en lugar de 7684 KB, con el mismo tiempo), Java lee
bloques de 4 KB y los analiza a mano en lugar de `StreamTokenizer`
(844 KB en lugar de 1300 KB, con el mismo tiempo), Python analiza línea
a línea y guarda la tronera en un `array` (832 KB en lugar de 15568 KB,
aunque el tiempo sube de 0.140 s a 0.171 s) y Rust analiza a mano desde
un búfer de 4 KB (604 KB en lugar de 2704 KB, con el mismo tiempo).

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1494_simulation.cpp](1494_simulation.cpp) | G++ 13.2 x64 | simulation | O(N) | AC | 0.093 s | 1540 KB | 11287211 |
| [1494_simulation.go](1494_simulation.go) | Go 1.14 x64 | simulation | O(N) | AC | 0.062 s | 7684 KB | 11303301 |
| [1494_simulation.java](1494_simulation.java) | Java 1.8 | simulation | O(N) | AC | 0.109 s | 1300 KB | 11303468 |
| [1494_simulation.py](1494_simulation.py) | Python 3.12 x64 | simulation | O(N) | AC | 0.140 s | 15568 KB | 11287213 |
| [1494_simulation.rs](1494_simulation.rs) | Rust 1.75 x64 | simulation | O(N) | AC | 0.031 s | 2704 KB | 11287216 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1494_simulation_optimized.cpp](1494_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(N) | AC | 0.031 s | 512 KB | 11303751 |
| [1494_simulation_optimized.go](1494_simulation_optimized.go) | Go 1.14 x64 | simulation | O(N) | AC | 0.046 s | 1312 KB | 11303612 |
| [1494_simulation_optimized.java](1494_simulation_optimized.java) | Java 1.8 | simulation | O(N) | AC | 0.125 s | 844 KB | 11303752 |
| [1494_simulation_optimized.py](1494_simulation_optimized.py) \* | Python 3.12 x64 | simulation | O(N) | AC | 0.171 s | 832 KB | 11303753 |
| [1494_simulation_optimized.rs](1494_simulation_optimized.rs) | Rust 1.75 x64 | simulation | O(N) | AC | 0.015 s | 604 KB | 11303754 |

\* No está entre las 10 mejores ni en el 15% mejor de las soluciones de
su lenguaje en el juez actual; quizá se pueda optimizar más.
