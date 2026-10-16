# 1762. En busca del escondite

[Timus 1762](https://acm.timus.ru/problem.aspx?space=1&num=1762) · dificultad 1684 · math

Problema original de Alexander Larin, del XI Concurso Individual Abierto de la Universidad Estatal de los Urales, 13 de marzo de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una sala de n por m baldosas tiene salidas en sus cuatro esquinas. Un
caminante entra por una esquina y avanza en diagonal, una baldosa por
paso, girando 90° en cada pared, hasta llegar a una esquina. Cada
baldosa pisada se da la vuelta, de blanco a gris o al revés. Contar las
baldosas grises al final.

## Entrada

n y m (2 ≤ n, m ≤ 1 000 000).

## Salida

El número de baldosas grises.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 5
```

Salida:

```
11
```

### Ejemplo 2

Entrada:

```
2 3
```

Salida:

```
3
```

## Solución

Se numeran las baldosas de 0 a a = n − 1 a lo ancho y de 0 a
b = m − 1 a lo largo. Desplegado en las paredes, el camino es una
diagonal recta, y llega por primera vez a una esquina tras
L = lcm(a, b) pasos, así que pisa L + 1 baldosas contando repeticiones.
Una baldosa visitada solo puede pisarse una vez en cada una de las dos
direcciones diagonales, así que queda gris salvo que el camino se
cruce allí consigo mismo, y la respuesta es L + 1 menos el doble del
número de cruces.

Con g = gcd(a, b), el camino solo recorre las rectas x − y ≡ 0 y
x + y ≡ 0 módulo 2g, ya que su tiempo t coincide con ±x módulo 2a y con
±y módulo 2b. Una baldosa en rectas de ambos tipos tiene x e y
divisibles por g, con x/g e y/g de la misma paridad. Dentro de la sala
cada uno de esos puntos es un cruce; en una pared el camino solo rebota
en él. Así, con A = a/g y B = b/g, los cruces son los pares
1 ≤ X < A, 1 ≤ Y < B de la misma paridad: ⌊A/2⌋·⌊B/2⌋ pares impares más
⌊(A−1)/2⌋·⌊(B−1)/2⌋ pares. `O(log n)` por el gcd.

En el primer ejemplo a = 6, b = 4, g = 2, L = 12, A = 3, B = 2, y el
único cruce es X = Y = 1, la baldosa (2, 2): 13 − 2 = 11.

Trampas:

- L llega a unos 10¹², así que hacen falta 64 bits;
- un rebote en una pared pisa esa baldosa una vez, no dos;
- simular el camino requiere hasta 10¹² pasos.

La fórmula coincide con una simulación del camino para todas las salas
de hasta 69 por 69 baldosas y con una implementación aceptada
independiente en 100 casos hasta los límites.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1762_math.cpp](1762_math.cpp) | G++ 13.2 x64 | math | O(log n) | AC | 0.015 s | 128 KB |
| [1762_math.go](1762_math.go) | Go 1.14 x64 | math | O(log n) | AC | 0.031 s | 1084 KB |
| [1762_math.java](1762_math.java) | Java 1.8 | math | O(log n) | AC | 0.140 s | 1568 KB |
| [1762_math.py](1762_math.py) | Python 3.12 x64 | math | O(log n) | AC | 0.078 s | 444 KB |
| [1762_math.rs](1762_math.rs) | Rust 1.75 x64 | math | O(log n) | AC | 0.046 s | 244 KB |
