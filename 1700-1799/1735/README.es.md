# 1735. El robo del siglo

[Timus 1735](https://acm.timus.ru/problem.aspx?space=1&num=1735) · dificultad 2824 · constructive

Problema original de Alexander Ipatov (idea de Artyom Skrobov), del XIV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n bolsas de k lingotes cada una; cada bolsa tiene solo lingotes de
oro de x kg o solo de platino de y kg, y los lingotes parecen iguales.
Elegir cuántos lingotes tomar de cada bolsa para que una sola pesada
exacta diga qué bolsas tienen platino, o indicar que es imposible.

## Entrada

n, k, x e y (3 ≤ n ≤ 20, 1 ≤ k ≤ 10⁶, 1 ≤ x < y ≤ 10).

## Salida

`YES` y las n cantidades, o `NO`. Se acepta cualquier elección válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 8 9 10
```

Salida:

```
YES
4 5 6 8
```

## Solución

Con cantidades c_i la balanza marca x·Σc_i + (y − x)·P, donde P es la
suma de las cantidades de las bolsas de platino. El primer término es
el mismo en cualquier reparto, así que la pesada distingue las bolsas
de platino justo cuando las 2ⁿ sumas de subconjuntos de las cantidades
son distintas. En particular las cantidades son positivas y distintas,
y x e y no importan.

Así la pregunta es el menor elemento máximo posible de un conjunto de n
enteros positivos con sumas de subconjuntos distintas. La sucesión de
Conway–Guy u₀ = 0, u₁ = 1, u_{m+1} = 2u_m − u_{m−r} con
r = round(√(2m)) da los conjuntos {u_n − u_i : 0 ≤ i < n}, con sumas de
subconjuntos distintas y elemento máximo u_n: 1, 2, 4, 7, 13, 24, 44,
84, 161, 309, … hasta 267 420 para n = 20. El código imprime ese conjunto
si u_n ≤ k; si no, `NO`. `O(n)`.

En el ejemplo u₄ = 7 ≤ 8, y el conjunto es 3, 5, 6, 7.

Trampas:

- las potencias de dos 1, 2, 4, … también sirven, pero necesitan 2ⁿ⁻¹
  lingotes, mucho más que u_n para n grande;
- una cantidad 0 oculta su bolsa por completo, así que de cada bolsa
  hay que tomar al menos un lingote.

Para n hasta 6 una búsqueda muestra que ningún conjunto tiene un
elemento máximo menor; para n mayores hay conjuntos mejores (máximo 1157
para n = 12), aunque estos límites coinciden con una implementación
aceptada independiente para todo n de 3 a 20 a ambos lados de u_n. Cada
conjunto impreso se comprobó con sumas de subconjuntos distintas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1735_constructive.cpp](1735_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.015 s | 372 KB |
| [1735_constructive.go](1735_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.015 s | 1088 KB |
| [1735_constructive.java](1735_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.125 s | 1644 KB |
| [1735_constructive.py](1735_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.093 s | 460 KB |
| [1735_constructive.rs](1735_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 216 KB |
