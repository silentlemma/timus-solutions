# 1797. Summit Online Judge. Versión 2

[Timus 1797](https://acm.timus.ru/problem.aspx?space=1&num=1797) · dificultad 4672 · number_theory

Problema original de Xie Lingxi, basado en el problema 1720 de Alex Samsonov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada concurso tiene x o y problemas. Un tamaño de volumen es correcto
si algunos concursos, al menos uno, suman exactamente ese número de
problemas. Contar los tamaños correctos de l a r. Hay hasta 100 casos.

## Entrada

El número de casos y luego x, y, l, r de cada uno
(1 ≤ x, y, l, r ≤ 10¹⁸, l ≤ r).

## Salida

Para cada caso, el número de tamaños correctos.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
4 5 7 13
```

Salida:

```
5
```

## Solución

Se cuentan los tamaños a·x + b·y (a, b ≥ 0, no ambos cero) hasta un
límite N; la respuesta es la cuenta hasta r menos la cuenta hasta
l − 1. Dividir x, y y N entre g = gcd(x, y) hace a x e y coprimos.
Entonces cada tamaño alcanzable tiene exactamente una forma con
0 ≤ b < x, así que la cuenta hasta N es la suma sobre b de 0 a
B = min(x − 1, ⌊N/y⌋) de ⌊(N − b·y)/x⌋ + 1, menos uno por el cero.
Escribiendo i = B − b la cuenta pasa a ser
B + Σ ⌊(y·i + (N − y·B))/x⌋ para i de 0 a B, una suma de suelos, que la
reducción al estilo de Euclides calcula en O(log max(x, y)) pasos: se
sacan las partes enteras de la pendiente y del desplazamiento, y luego
se intercambian los papeles de la pendiente y el módulo. Con estos
límites, todos los cálculos intermedios caben en 64 bits, aunque el
código usa aritmética más ancha para pendiente × términos +
desplazamiento. `O(log max(x, y))` por caso.

En el ejemplo 8, 9, 10, 12 y 13 se forman con cuatros y cincos,
mientras que 7 y 11 no.

Trampas:

- x e y pueden compartir un factor, y entonces solo cuentan sus
  múltiplos;
- B y el rango llegan a 10¹⁸, así que la suma sobre b no se puede
  recorrer término a término;
- la suma de suelos usa aritmética ancha: la solución en Java usa
  BigInteger, la de Go bits.Mul64 y bits.Div64;
- el cero, el conjunto vacío de concursos, no es un tamaño.

Las respuestas coinciden con un recuento directo de los tamaños
alcanzables en 3000 casos pequeños, y con una implementación aceptada
independiente en 4500 grandes, incluidos factores comunes, tamaños 1 y
tamaños iguales.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1797_number_theory.cpp](1797_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log max(x, y)) per case | AC | 0.015 s | 408 KB |
| [1797_number_theory.go](1797_number_theory.go) | Go 1.14 x64 | number_theory | O(log max(x, y)) per case | AC | 0.015 s | 1092 KB |
| [1797_number_theory.java](1797_number_theory.java) | Java 1.8 | number_theory | O(log max(x, y)) per case | AC | 0.109 s | 2492 KB |
| [1797_number_theory.py](1797_number_theory.py) | Python 3.12 x64 | number_theory | O(log max(x, y)) per case | AC | 0.078 s | 440 KB |
| [1797_number_theory.rs](1797_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log max(x, y)) per case | AC | 0.015 s | 236 KB |
