# 1778. Hockey chino 2

[Timus 1778](https://acm.timus.ru/problem.aspx?space=1&num=1778) · dificultad 3901 · greedy

Problema original de Alex Samsonov, del XV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n aficionados numerados de 1 a n viajan en m autobuses numerados de 1 a
m, cada uno con entre a y b de ellos, y un autobús de número mayor lleva
aficionados de números mayores. Algunos aficionados dicen en qué autobús
van. Hallar todos los autobuses en que puede ir el aficionado r, o
informar de que las respuestas se contradicen.

## Entrada

n, m, a y b (2 ≤ m ≤ n ≤ 10⁵, 1 ≤ a ≤ b ≤ n, m·a ≤ n ≤ m·b), luego r,
luego s (1 ≤ s ≤ n − 1) y s pares de un aficionado rᵢ ≠ r y un autobús
fᵢ.

## Salida

`IMPOSSIBLE`, o el número de autobuses posibles y los autobuses en
orden creciente.

## Ejemplos

### Ejemplo 1

Entrada:

```
16 4 1 16
3
2
2 2
4 3
```

Salida:

```
2
2 3
```

## Solución

El autobús i lleva a los aficionados tras el límite P(i − 1) hasta el
límite P(i), con P(0) = 0, P(m) = n y a ≤ P(i) − P(i − 1) ≤ b. Un
aficionado x en el autobús f significa P(f) ≥ x y P(f − 1) ≤ x − 1, así
que cada límite empieza con un intervalo propio. De izquierda a derecha,
cada límite debe además quedar de a a b después del intervalo del
anterior, y de derecha a izquierda, de a a b antes del intervalo del
siguiente; una cadena de tales restricciones mantiene cada conjunto de
valores posibles como un intervalo. Tras ambas pasadas cada intervalo
contiene exactamente los valores que ese límite toma en algún reparto
completo, y un intervalo vacío significa que las respuestas se
contradicen.

El aficionado r va en el autobús k cuando P(k − 1) ≤ r − 1 y P(k) ≥ r en
algún reparto. Cortando los dos intervalos en r y comprobando que algún
par de valores en ellos dista de a a b —las diferencias entre dos
intervalos también forman un intervalo— se responde para cada autobús
de inmediato. `O(n + m)`.

En el ejemplo el aficionado 2 en el autobús 2 y el 4 en el autobús 3
dan P(1) ≤ 1, P(2) = 2 o 3, P(3) ≥ 4. El aficionado 3 va en el autobús 2
si P(2) = 3, y en el 3 si P(2) = 2.

Trampas:

- hay que hacer las dos pasadas: la de la izquierda sola pierde límites
  que vienen del otro extremo;
- el aficionado 1 siempre va en el autobús 1 y el n en el m;
- si cada intervalo tiene un solo valor, como con a = b, todo el reparto queda fijo.

Las respuestas coinciden con una búsqueda sobre todos los repartos en
500 casos aleatorios de hasta 5 autobuses y con una implementación
aceptada independiente en 80 casos de hasta 10⁵ aficionados.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1778_greedy.cpp](1778_greedy.cpp) | G++ 13.2 x64 | greedy | O(n + m) | AC | 0.093 s | 976 KB |
| [1778_greedy.go](1778_greedy.go) | Go 1.14 x64 | greedy | O(n + m) | AC | 0.140 s | 5860 KB |
| [1778_greedy.java](1778_greedy.java) | Java 1.8 | greedy | O(n + m) | AC | 0.140 s | 3784 KB |
| [1778_greedy.py](1778_greedy.py) | Python 3.12 x64 | greedy | O(n + m) | AC | 0.390 s | 27208 KB |
| [1778_greedy.rs](1778_greedy.rs) | Rust 1.75 x64 | greedy | O(n + m) | AC | 0.031 s | 4736 KB |
