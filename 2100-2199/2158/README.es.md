# 2158. Partir un multiconjunto en una progresión aritmética y una geométrica

[Timus 2158](https://acm.timus.ru/problem.aspx?space=1&num=2158) · dificultad 1856 · math, greedy

Problema original de Valentin Zuev, del Concurso Escolar de Programación de los Urales 2021.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Partir N enteros no negativos en una progresión aritmética no vacía y una
progresión geométrica no vacía de razón no nula, usando cada número una
vez, e imprimir ambas, o −1. Se acepta cualquier partición válida. Los
límites son 2 segundos y 256 MB.

## Entrada

N, 2 ≤ N ≤ 50 000, y luego los números, 0 ≤ aᵢ ≤ 10⁹.

## Salida

−1, o la longitud de la progresión aritmética, sus términos en orden y
los términos de la geométrica en orden.

## Evaluación

Un comprobador verifica el multiconjunto y ambas progresiones, y compara
−1 con la respuesta guardada.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
0 2 3 4 6 8
```

Salida:

```
3
0 3 6
2 4 8
```

### Ejemplo 2

Entrada:

```
6
4 4 6 6 8 9
```

Salida:

```
3
4 6 8
4 6 9
```

### Ejemplo 3

Entrada:

```
4
0 0 0 0
```

Salida:

```
1
0
0 0 0
```

### Ejemplo 4

Entrada:

```
5
0 0 1 1 2
```

Salida:

```
-1
```

## Solución

Se ordenan los números. La cota clave: una progresión geométrica de razón
q ≠ 1 tiene a lo sumo unos 30 términos, porque sus términos son enteros
hasta 10⁹ y la razón p / r irreducible obliga a que el primer término sea
múltiplo de r^(t−1), así que los términos crecen al menos como 2^(t−1).
Los ceros solo caben en una progresión de ceros. Las progresiones de
razón 1 o paso 0 constan de números iguales, y estos casos se tratan
primero:

- uno o dos valores distintos: cada valor aparte;
- exactamente un valor repetido: sus copias forman la progresión
  constante, quizá dejando una copia a la otra, y se comprueba el resto;
- a lo sumo 31 números: se prueba cada número suelto como una de las
  progresiones.

Si no, todos los números son distintos donde importa, la parte
geométrica tiene a lo sumo 30 términos y la aritmética el resto. Con N
grande el paso aritmético es la mediana de las diferencias entre
vecinos, y su primer término está entre los 31 primeros números; con N
menor se prueban los dos primeros términos entre los 32 primeros. Para
un inicio y un paso, una pasada voraz toma cada número igual al
siguiente término aritmético y deja el resto a la parte geométrica,
rindiéndose cuando esta pasa de 30 números. Los últimos uno o dos
términos aritméticos pueden pertenecer a la parte geométrica, así que
también se comprueban esas pocas variantes. Todas las comprobaciones son
comparaciones enteras exactas.

En el segundo ejemplo 4, 6, 8 tiene paso 2 y 4, 6, 9 razón 3 / 2.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2158_math_greedy.cpp](2158_math_greedy.cpp) | G++ 13.2 x64 | math, greedy | O(N log N + 30^2 N) | AC | 0.031 s | 2148 KB |
| [2158_math_greedy.go](2158_math_greedy.go) | Go 1.14 x64 | math, greedy | O(N log N + 30^2 N) | AC | 0.031 s | 7880 KB |
| [2158_math_greedy.java](2158_math_greedy.java) | Java 1.8 | math, greedy | O(N log N + 30^2 N) | AC | 0.156 s | 7108 KB |
| [2158_math_greedy.py](2158_math_greedy.py) | Python 3.12 x64 | math, greedy | O(N log N + 30^2 N) | AC | 0.265 s | 8684 KB |
| [2158_math_greedy.rs](2158_math_greedy.rs) | Rust 1.75 x64 | math, greedy | O(N log N + 30^2 N) | AC | 0.046 s | 2892 KB |
