# 2001. Mathematicians and Berries

[Timus 2001](https://acm.timus.ru/problem.aspx?space=1&num=2001) · dificultad 22 · math

Problema original de Oleg Merkurev. (Prepared by Kirill Devyatkin), del Concurso Regional Escolar de Programación de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se pesan dos cestas tres veces. Al principio cada una contiene sus
propias bayas. Después se pasan todas las bayas de la segunda a la
primera y se pesan ambas. Finalmente se pasa todo el contenido de la
primera a la segunda y se repite. Recuperar las masas iniciales de
bayas, con masas constantes de las cestas.

## Entrada

Tres parejas cronológicas `a1 b1`, `a2 b2`, `a3 b3`, con lecturas
enteras de 0 a 10000 que corresponden a las transferencias. Tiempo 0,5
segundos y memoria 64 MB.

## Salida

Las masas iniciales de bayas de la primera y segunda cesta, en ese orden.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
1 2
2 1
0 3
```

```
1 1
```

La primera cesta está vacía en la última lectura, pesando 0. La segunda
está vacía en la intermedia, pesando 1. Restar esas masas de las
lecturas iniciales 1 y 2 da 1 y 1.

## Solución

Sean c y d los pesos de las cestas vacías, y x e y los de las bayas. La
primera pesada da a1 = c + x y b1 = d + y. Después de vaciar la segunda
cesta en la primera, b2 = d; después de vaciar la primera en la segunda,
a3 = c. Así x = a1 − a3 e y = b1 − b2; las lecturas a2 y b3 no hacen
falta. `O(1)`.

## Soluciones optimizadas

Las soluciones optimizadas (C++, Java) calculan las mismas dos
diferencias. C++ salta las lecturas a2 y b3 con `%*d` en `scanf` en
lugar de usar `iostream`: 124 KB en lugar de 396 KB, con el mismo
tiempo. Java analiza los números a mano desde `System.in` en lugar de
usar `Scanner`: 0.125 s en lugar de 0.156 s y 344 KB en lugar de
1608 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2001_math.cpp](2001_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 396 KB | 11292438 |
| [2001_math.go](2001_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1088 KB | 11292439 |
| [2001_math.java](2001_math.java) | Java 1.8 | math | O(1) | AC | 0.156 s | 1608 KB | 11303362 |
| [2001_math.py](2001_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 384 KB | 11292440 |
| [2001_math.rs](2001_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 228 KB | 11292442 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2001_math_optimized.cpp](2001_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 124 KB | 11303653 |
| [2001_math_optimized.java](2001_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.125 s | 344 KB | 11303655 |

\* No está entre las 10 mejores ni en el 15% mejor de las soluciones de
su lenguaje en el juez actual; quizá se pueda optimizar más.
