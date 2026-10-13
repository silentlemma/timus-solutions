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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1494_simulation.cpp](1494_simulation.cpp) | G++ 13.2 x64 | simulation | O(N) | AC | 0.093 s | 1540 KB |
| [1494_simulation.go](1494_simulation.go) | Go 1.14 x64 | simulation | O(N) | AC | 0.031 s | 8204 KB |
| [1494_simulation.java](1494_simulation.java) | Java 1.8 | simulation | O(N) | AC | 0.109 s | 1336 KB |
| [1494_simulation.py](1494_simulation.py) | Python 3.12 x64 | simulation | O(N) | AC | 0.140 s | 15568 KB |
| [1494_simulation.rs](1494_simulation.rs) | Rust 1.75 x64 | simulation | O(N) | AC | 0.031 s | 2704 KB |
