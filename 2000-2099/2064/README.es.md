# 2064. El más alto de muchos zigzags

[Timus 2064](https://acm.timus.ru/problem.aspx?space=1&num=2064) · dificultad 976 · math, prefix_sums

Problema original de Nikita Sivukhin, preparado por Alexey Danilyuk y Nikita Sivukhin, del Concurso Regional de Programación por Equipos de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n orugas salen del suelo en el instante 0. La oruga i sube a 1 cm por
minuto durante tᵢ minutos, luego baja a la misma velocidad durante tᵢ
minutos hasta el suelo, y repite esto para siempre. Para cada uno de q
instantes, hallar la altura de la oruga más alta. Los límites son 3
segundos y 64 MB.

## Entrada

El número de orugas n, 1 ≤ n ≤ 10⁶, luego los n valores tᵢ,
1 ≤ tᵢ ≤ 10⁹, después el número de instantes q, 1 ≤ q ≤ 10⁶, y los q
instantes x, uno por línea, 1 ≤ x ≤ 10⁶.

## Salida

Para cada instante, la mayor altura en su propia línea.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
1 3 2 1
12
1
2
3
4
5
6
7
8
9
10
11
12
```

Salida:

```
1
2
3
2
1
2
1
2
3
2
1
0
```

## Solución

En el instante x la oruga de parámetro t está a la altura t − |x − c|,
donde c es el múltiplo impar de t más cercano a x: su gráfica es una
fila de «tiendas» de altura t con cimas en t, 3t, 5t, … y pies en los
múltiplos pares. Dicho de otro modo, la altura es la distancia de x al
múltiplo de 2t más cercano. La respuesta en x es el punto más alto de
todas las tiendas, es decir, el máximo de h − |x − c| sobre todas ellas;
una tienda que no cubre x da allí como mucho 0 y nunca gana.

Sea X el mayor instante. Una oruga con t ≥ X sigue subiendo en todos los
instantes, a altura x, que es justo lo que da una tienda de altura X con
cima en X. Para t < X solo las tiendas con cima hasta 2X pueden ser las
más cercanas a un instante x ≤ X. Así que se ponen las tiendas en un
arreglo: height[c] es la tienda más alta con cima en c, y se rellena
recorriendo c = t, 3t, 5t, … hasta 2X para cada t distinto. En total son
O(X log X) pasos.

Después best[x] = máximo sobre c de height[c] − |x − c| es una
transformada de distancia con pendiente 1: un barrido de izquierda a
derecha toma best[x] = max(height[x], best[x − 1] − 1) para las tiendas
de la izquierda, y otro de derecha a izquierda hace lo mismo para las de
la derecha. La respuesta de cada instante se lee del arreglo. Con
ordenación, el tiempo es O(n log n + X log X + q) y la memoria O(n + X + q).

En el ejemplo las tiendas tienen altura 1 en los instantes impares, 2 en
2, 6, 10, … y 3 en 3, 9, 15, … En el instante 12 las cimas más cercanas
10, 11, 13, 14 y 15 dan 0, así que la respuesta es 0.

Trampas:

- el mismo t puede aparecer muchas veces: solo importan los valores
  distintos;
- una oruga más alta que todos los instantes también cuenta, con altura
  x;
- las tiendas con cima más allá del mayor instante importan para los
  instantes justo antes.

## Notas por lenguaje

Leer dos millones de números exige entrada rápida en todos los
lenguajes. La solución en Python usa una tabla de presencia de tamaño
T = 10⁶ + 1 en vez de ordenar y corre en PyPy, con bucles simples que
el JIT compila bien; CPython tarda unos seis segundos en las pruebas más
grandes. Partir toda la entrada en palabras le cuesta a PyPy más de
64 MB, así que los números se leen cifra a cifra de trozos pequeños de
la entrada, se guardan en arrays y las respuestas se imprimen en
porciones pequeñas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2064_math_prefix_sums.cpp](2064_math_prefix_sums.cpp) | G++ 13.2 x64 | math, prefix_sums | O(n log n + X log X + q) | AC | 0.453 s | 33928 KB |
| [2064_math_prefix_sums.go](2064_math_prefix_sums.go) | Go 1.14 x64 | math, prefix_sums | O(n log n + X log X + q) | AC | 0.562 s | 33868 KB |
| [2064_math_prefix_sums.java](2064_math_prefix_sums.java) | Java 1.8 | math, prefix_sums | O(n log n + X log X + q) | AC | 0.468 s | 53828 KB |
| [2064_math_prefix_sums.py](2064_math_prefix_sums.py) | PyPy 3.10 x64 | math, prefix_sums | O(n + T + X log X + q) | AC | 0.875 s | 18808 KB |
| [2064_math_prefix_sums.rs](2064_math_prefix_sums.rs) | Rust 1.75 x64 | math, prefix_sums | O(n log n + X log X + q) | AC | 0.265 s | 64076 KB |
