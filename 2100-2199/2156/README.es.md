# 2156. Repartir las diferencias alrededor de un círculo en mitades iguales

[Timus 2156](https://acm.timus.ru/problem.aspx?space=1&num=2156) · dificultad 649 · math, constructive

Problema original de Semyon Trifochkin, del Concurso Escolar de Programación de los Urales 2020.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n amigos con interés a₁ … aₙ se sientan alrededor de una mesa, y la
conversación entre los vecinos i e i + 1 (n y 1 la última) tiene interés
|aᵢ − aᵢ₊₁|. Repartir las n conversaciones en dos conjuntos no vacíos con
el mismo interés total, o imprimir NO. Se acepta cualquier reparto
válido. Los límites son 1 segundo y 256 MB.

## Entrada

n, 3 ≤ n ≤ 10⁵, y luego a₁ … aₙ, 1 ≤ aᵢ ≤ 10⁹.

## Salida

YES, y luego el tamaño y los números del primer conjunto y del segundo,
o NO.

## Evaluación

Un comprobador verifica que los dos conjuntos no estén vacíos, repartan
todas las conversaciones y tengan sumas iguales.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
1 2 3
```

Salida:

```
YES
2
1 2
1
3
```

## Solución

La respuesta siempre es YES. Dando una vuelta a la mesa, las diferencias
con signo aᵢ − aᵢ₊₁ suman 0. Así que las conversaciones donde el valor
baja (aᵢ > aᵢ₊₁) tienen el mismo interés total que aquellas donde sube,
y las conversaciones entre vecinos iguales tienen interés 0 y pueden ir
a cualquier lado.

Si los valores no son todos iguales, hay al menos una bajada y una
subida, así que ambos conjuntos no están vacíos. Si son todos iguales,
cada conversación tiene interés 0, y vale una conversación contra las
otras n − 1. El trabajo es O(n).

En el ejemplo el valor solo baja de 3 a 1, así que la conversación 3
(interés 2) equilibra las conversaciones 1 y 2 (interés 1 cada una).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2156_math_constructive.cpp](2156_math_constructive.cpp) | G++ 13.2 x64 | math, constructive | O(n) | AC | 0.093 s | 2668 KB |
| [2156_math_constructive.go](2156_math_constructive.go) | Go 1.14 x64 | math, constructive | O(n) | AC | 0.125 s | 9912 KB |
| [2156_math_constructive.java](2156_math_constructive.java) | Java 1.8 | math, constructive | O(n) | AC | 0.140 s | 9008 KB |
| [2156_math_constructive.py](2156_math_constructive.py) | Python 3.12 x64 | math, constructive | O(n) | AC | 0.140 s | 21040 KB |
| [2156_math_constructive.rs](2156_math_constructive.rs) | Rust 1.75 x64 | math, constructive | O(n) | AC | 0.046 s | 9448 KB |
