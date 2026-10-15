# 1731. Eneldo

[Timus 1731](https://acm.timus.ru/problem.aspx?space=1&num=1731) · dificultad 106 · constructive

Problema original de Eugene Kurpilyansky (preparado por Sofia Tekhazheva), del Concurso Regional de Programación por Equipos de los Urales 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Elegir las masas de n cajas de eneldo de la primera clase y m cajas de
la segunda, todas enteros positivos distintos hasta 10⁹, de modo que no
haya forma de regalar a dos vecinos una caja de cada clase con pesos
totales iguales.

## Entrada

n y m (2 ≤ n, m ≤ 50).

## Salida

Las n masas de la primera clase en una línea y las m de la segunda en
la siguiente. Se acepta cualquier elección válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3
```

Salida:

```
1 2
5 10 12
```

## Solución

Dos regalos a + b y a′ + b′ no comparten cajas, y dos sumas con una
caja en común ya difieren porque todas las masas son distintas. Así
que la condición es que las n·m sumas a_i + b_j sean todas distintas.

Se toma a_i = i para i = 1..n y b_j = (j + 1)·n + 1 para
j = 0..m − 1. Entonces a_i + b_j = (j + 1)·n + 1 + i, y como i recorre
1..n, la suma determina tanto i como j, igual que un número en base n
determina su última cifra y el resto. Todas las masas son distintas y
la mayor es menor que 3000. `O(n + m)`.

Para el ejemplo salen 1 2 y 3 5 7, con sumas 4, 6, 8, 5, 7, 9.

Trampas:

- la respuesta siempre existe, así que nunca se imprime
  "It is a lie!";
- la segunda clase no debe repetir masas de la primera, por eso empieza
  por encima de n.

El comprobador verifica las cantidades, el rango, que las masas sean
distintas y que todas las sumas difieran.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1731_constructive.cpp](1731_constructive.cpp) | G++ 13.2 x64 | constructive | O(n + m) | AC | 0.015 s | 380 KB |
| [1731_constructive.go](1731_constructive.go) | Go 1.14 x64 | constructive | O(n + m) | AC | 0.046 s | 1104 KB |
| [1731_constructive.java](1731_constructive.java) | Java 1.8 | constructive | O(n + m) | AC | 0.171 s | 1580 KB |
| [1731_constructive.py](1731_constructive.py) | Python 3.12 x64 | constructive | O(n + m) | AC | 0.093 s | 416 KB |
| [1731_constructive.rs](1731_constructive.rs) | Rust 1.75 x64 | constructive | O(n + m) | AC | 0.015 s | 224 KB |
