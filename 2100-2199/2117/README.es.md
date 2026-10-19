# 2117. Sumas de dos raíces cuadradas iguales a una raíz dada

[Timus 2117](https://acm.timus.ru/problem.aspx?space=1&num=2117) · dificultad 544 · number_theory

Problema original de Pavel Klimov, de la Olimpiada Académica Universitaria de Informática 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Para un entero C, contar los pares de enteros no negativos A ≤ B con
√A + √B = √C. Los límites son 1 segundo y 256 MB.

## Entrada

C, 0 ≤ C ≤ 10¹⁸.

## Salida

El número de pares.

## Ejemplos

### Ejemplo 1

Entrada:

```
9
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
3
```

Salida:

```
1
```

## Solución

Se escribe C = s² q con q libre de cuadrados. Elevar al cuadrado
√A = √C − √B muestra que √(BC) es entero, y de ahí que A y B son a² q y
b² q con a + b = s; a la inversa, toda división así sirve. Así que la
respuesta es el número de pares a ≤ b con a + b = s, es decir ⌊s/2⌋ + 1
(C = 0 tiene el único par 0, 0).

Queda hallar s, la raíz del mayor cuadrado que divide a C. La división
por tanteo entre d hasta 10⁶ (la raíz cúbica de 10¹⁸) quita d² mientras
divida y luego una d más si la hay, multiplicando s por d por cada d²
quitado. Lo que queda es 1, un primo o un producto de dos primos mayores que 10⁶,
pues tres factores así superarían 10¹⁸. Solo contiene un factor cuadrado
si es el cuadrado de un primo; entonces s gana ese primo. La complejidad
temporal es O(min(10⁶, √C)).

En el primer ejemplo 9 = 3² · 1, así que s = 3 y los pares son 0 + 9 y
1 + 4.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2117_number_theory.cpp](2117_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.031 s | 136 KB |
| [2117_number_theory.go](2117_number_theory.go) | Go 1.14 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.046 s | 1096 KB |
| [2117_number_theory.java](2117_number_theory.java) | Java 1.8 | number_theory | O(min(10⁶, √C)) | AC | 0.140 s | 1604 KB |
| [2117_number_theory.py](2117_number_theory.py) | Python 3.12 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.500 s | 472 KB |
| [2117_number_theory.rs](2117_number_theory.rs) | Rust 1.75 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.062 s | 232 KB |
