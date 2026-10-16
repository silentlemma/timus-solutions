# 1816. Problemas con Pollard

[Timus 1816](https://acm.timus.ru/problem.aspx?space=1&num=1816) · dificultad 2273 · number_theory

Problema original del Tavrida NU Akai Contest, sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para descomponer n, un programa se detiene si n es primo. Si no, toma
un r aleatorio de 1 a 10¹⁸ y g = mcd(n, r), repite mientras g sea 1 o
n, y luego descompone g y n/g de la misma forma. Hallar el número
esperado de cálculos del mcd, con error absoluto o relativo de como mucho 10⁻⁶.

## Entrada

n (2 ≤ n ≤ 10⁹).

## Salida

El número esperado de cálculos del mcd.

## Ejemplos

### Ejemplo 1

Entrada:

```
12
```

Salida:

```
4.8571428571
```

### Ejemplo 2

Entrada:

```
8
```

Salida:

```
6.6666666667
```

## Solución

Como 10¹⁸ es mucho mayor que n, r mod n es uniforme salvo un error
despreciable, y el mcd se descompone por las potencias de primos de n.
Si p aparece en m con exponente e, el exponente de p en mcd(m, r) es
c < e con probabilidad (1 − 1/p)/pᶜ y e con probabilidad 1/pᵉ, de
forma independiente para cada primo. Para un m compuesto el paso se
repite hasta que el mcd es propio, así que
E(m) = (1 + Σ P(g)·(E(g) + E(m/g))) / (1 − P(1) − P(m)), con la suma
sobre los divisores 1 < g < m, y E vale 0 en los primos.

Todos los números que aparecen son divisores de n, como mucho 1344
bajo 10⁹. Escribiendo un divisor como su vector de exponentes en base
mixta, cada divisor propio de un divisor recibe un número menor, así
que E se rellena en orden creciente. El par g y m/g son los números d
e índice − d. La suma recorre todos los divisores de todos los divisores
de n, unos 1,4·10⁵ términos en el peor caso. `O(√n + Σ d(m))` sobre los
divisores m de n.

En el segundo ejemplo 8 = 2³: el mcd es 1, 2, 4 u 8 con probabilidades
1/2, 1/4, 1/8 y 1/8. E(4) = 4, y
E(8) = (1 + 1/4·4 + 1/8·4) / (3/8) = 20/3.

Trampas:

- E(m) aparece en ambos lados, pues un mcd inútil repite el paso;
- las probabilidades dependen de los primos, no solo de la forma de los
  exponentes;
- los primos no necesitan ningún mcd, así que E(p) = 0.

Las respuestas coinciden con una implementación aceptada independiente
en los ejemplos, primos, potencias de primos, el número con más
divisores y valores aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1816_number_theory.cpp](1816_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sqrt(n) + sum of d(m) over divisors m of n) | AC | 0.015 s | 248 KB |
| [1816_number_theory.go](1816_number_theory.go) | Go 1.14 x64 | number_theory | O(sqrt(n) + sum of d(m) over divisors m of n) | AC | 0.015 s | 2372 KB |
| [1816_number_theory.java](1816_number_theory.java) | Java 1.8 | number_theory | O(sqrt(n) + sum of d(m) over divisors m of n) | AC | 0.125 s | 2280 KB |
| [1816_number_theory.py](1816_number_theory.py) | Python 3.12 x64 | number_theory | O(sqrt(n) + sum of d(m) over divisors m of n) | AC | 0.093 s | 708 KB |
| [1816_number_theory.rs](1816_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sqrt(n) + sum of d(m) over divisors m of n) | AC | 0.031 s | 324 KB |
