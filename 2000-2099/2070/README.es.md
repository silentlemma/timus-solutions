# 2070. Potencias de primos con un número primo de divisores

[Timus 2070](https://acm.timus.ru/problem.aspx?space=1&num=2070) · dificultad 235 · number_theory

Problema original de Alexey Danilyuk, del Concurso Regional de Programación por Equipos de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una persona considera interesante un entero si es primo, y otra si su
número de divisores positivos es primo. Un entero es satisfactorio si
ambas coinciden, en un sentido o en el otro. Contar los enteros
satisfactorios de [L; R]. Los límites son 2 segundos y 64 MB.

## Entrada

L y R, 2 ≤ L ≤ R ≤ 10¹².

## Salida

El número de enteros satisfactorios de [L; R].

## Ejemplos

### Ejemplo 1

Entrada:

```
3 7
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
2 2
```

Salida:

```
1
```

### Ejemplo 3

Entrada:

```
77 1010
```

Salida:

```
924
```

## Solución

Un primo tiene 2 divisores, y 2 es primo, así que ambas consideran
interesante todo primo. Un número compuesto es satisfactorio salvo que
su número de divisores sea primo. Para x = p₁^a₁ · … · pₛ^aₛ ese número
es (a₁ + 1) · … · (aₛ + 1), y un producto es primo solo si tiene un único
factor. Por tanto los números no satisfactorios son exactamente las
potencias p^k de un primo con k ≥ 2 y k + 1 primo, y la respuesta es
R − L + 1 menos su cantidad en [L; R].

Como p^k ≤ 10¹² con k ≥ 2, todo p así es a lo sumo 10⁶. Una criba hasta
10⁶ da los primos, y para cada primo p con p² ≤ R se recorren las
potencias p², p³, … hasta R, contando las que son al menos L y cuyo
exponente más uno es primo. Los primos mayores que 10⁴ solo tienen el
cuadrado, así que el recorrido es corto; el trabajo lo domina la criba,
O(N log log N) con N = 10⁶.

En el primer ejemplo 4 = 2² tiene 3 divisores, así que es el único no
satisfactorio entre 3 … 7 y la respuesta es 4.

## Notas por lenguaje

En C++, Go, Java y Rust se compara cada potencia con R / p antes de
multiplicar, así que nunca pasa de 10¹² · 10⁶ y cabe en 64 bits. La solución en Python cuenta los
cuadrados como los primos entre √L y √R con un solo corte de la criba y
recorre solo los primos hasta ∛R, para ir rápido en CPython.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2070_number_theory.cpp](2070_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log log N) | AC | 0.031 s | 304 KB |
| [2070_number_theory.go](2070_number_theory.go) | Go 1.14 x64 | number_theory | O(N log log N) | AC | 0.031 s | 2136 KB |
| [2070_number_theory.java](2070_number_theory.java) | Java 1.8 | number_theory | O(N log log N) | AC | 0.140 s | 2632 KB |
| [2070_number_theory.py](2070_number_theory.py) | Python 3.12 x64 | number_theory | O(N log log N) | AC | 0.109 s | 2816 KB |
| [2070_number_theory.rs](2070_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log log N) | AC | 0.062 s | 1212 KB |
