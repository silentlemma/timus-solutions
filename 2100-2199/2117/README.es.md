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

## Soluciones optimizadas

Los nuevos C++/Go mantienen C=s²q libre de cuadrados y floor(s/2)+1. Para C>0, al cuadrar √A = √C − √B se obtiene 2√(BC) = B + C − A. El lado derecho es par porque su cuadrado es múltiplo de cuatro. Por tanto BC es un cuadrado. Si B>0, los exponentes primos de B y C tienen la misma paridad, así que B=b²q y A=(s−b)²q. Esto da las particiones enteras de s, incluida A=0.

Un cuadrado perfecto, incluido cero, termina con s=sqrt(C). En otro caso eliminan pares y una aparición impar de2 y3, y prueban solo divisores6k±1. Terminan al superar d³ el residuo decreciente R: todos sus factores primos son≥d, de modo que quedan como máximo dos con multiplicidad. Hay otro factor cuadrado exactamente si R es cuadrado. Las estimaciones flotantes de raíz se corrigen por productos enteros exactos; C≤10^18 y el primer cubo fallido caben en uint64. La rueda reduce divisiones y el límite adaptativo suele terminar antes que probar todos los enteros hasta10^6. El peor tiempo es O(C^(1/3)) y el espacio adicional es O(1). Go lee por los descriptores estándar en un búfer de 64 bytes. La respuesta no supera 500 000 001, así que nueve dígitos y un salto de línea caben en diez bytes. Se conservan bases sencillas; Java/Python/Rust reutilizan originales admitidos.

Las implementaciones base aceptadas [2117_number_theory.java](2117_number_theory.java), [2117_number_theory.py](2117_number_theory.py), [2117_number_theory.rs](2117_number_theory.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2117_number_theory.cpp](2117_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.031 s | 136 KB | 11294802 |
| [2117_number_theory.go](2117_number_theory.go) | Go 1.14 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.046 s | 1096 KB | 11294803 |
| [2117_number_theory.java](2117_number_theory.java) | Java 1.8 | number_theory | O(min(10⁶, √C)) | AC | 0.140 s | 1604 KB | 11294808 |
| [2117_number_theory.py](2117_number_theory.py) \* | Python 3.12 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.500 s | 472 KB | 11294805 |
| [2117_number_theory.rs](2117_number_theory.rs) \* | Rust 1.75 x64 | number_theory | O(min(10⁶, √C)) | AC | 0.062 s | 232 KB | 11294811 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2117_number_theory_optimized.cpp](2117_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(C^(1/3)) | AC | 0.015 s | 112 KB | 11315748 |
| [2117_number_theory_optimized.go](2117_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(C^(1/3)) | AC | 0.046 s | 276 KB | 11315923 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
