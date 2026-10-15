# 1690. Ejército de magos

[Timus 1690](https://acm.timus.ru/problem.aspx?space=1&num=1690) · dificultad 637 · constructive

Problema original de Eugene Kurpilyanskiy, del Ural SU Contest en el campus de invierno de Petrozavodsk, febrero de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay 5n candidatos que viven en puntos enteros distintos. Dos magos se
respetan cuando el segmento entre sus casas pasa por otro punto entero.
Elegir n candidatos que se respeten todos entre sí, o informar de que
es imposible.

## Entrada

n (1 ≤ n ≤ 5000), y luego las 5n casas, enteros de valor absoluto a lo
sumo 10000.

## Salida

OK y los números de los candidatos elegidos, o IMPOSSIBLE. Se acepta
cualquier ejército válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
1 1
5 5
0 0
2 2
0 10
6 6
7 7
8 8
9 9
10 10
```

Salida:

```
OK
2 1
```

## Solución

El segmento de (x1, y1) a (x2, y2) tiene un punto entero interior
exactamente cuando gcd(|x1 − x2|, |y1 − y2|) ≥ 2. En particular, dos
casas con la misma paridad de x y de y difieren en cantidades pares,
así que el punto medio de su segmento es entero.

Solo hay cuatro clases de paridad, y 5n casas en cuatro clases ponen al
menos ⌈5n / 4⌉ ≥ n casas en una de ellas. Así que la respuesta siempre
es OK: se toman n casas cualesquiera de la clase mayor. `O(n)`.

Trampas:

- IMPOSSIBLE nunca ocurre;
- la paridad de una coordenada negativa debe salir 0 o 1: −3 es impar,
  lo que `x & 1` resuelve bien en complemento a dos, mientras que
  `x % 2` da −1 en los lenguajes tipo C (test 03).

El verificador acepta cualesquiera n candidatos distintos que se
respeten por pares, comprobando todos los pares salvo que compartan
clase de paridad. Las respuestas de una implementación aceptada
independiente también lo pasan.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1690_constructive.cpp](1690_constructive.cpp) | G++ 13.2 x64 | constructive | O(n) | AC | 0.046 s | 304 KB |
| [1690_constructive.go](1690_constructive.go) | Go 1.14 x64 | constructive | O(n) | AC | 0.062 s | 4412 KB |
| [1690_constructive.java](1690_constructive.java) | Java 1.8 | constructive | O(n) | AC | 0.140 s | 1840 KB |
| [1690_constructive.py](1690_constructive.py) | Python 3.12 x64 | constructive | O(n) | AC | 0.093 s | 6088 KB |
| [1690_constructive.rs](1690_constructive.rs) | Rust 1.75 x64 | constructive | O(n) | AC | 0.046 s | 2120 KB |
