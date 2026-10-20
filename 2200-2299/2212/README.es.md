# 2212. Sumas de prefijo aplicadas Q veces como una sola convolución

[Timus 2212](https://acm.timus.ru/problem.aspx?space=1&num=2212) · dificultad 1009 · math, combinatorics

Problema original de Yackov Malin, de la Olimpiada Académica Universitaria Escolar de Informática 2024.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un arreglo de N números se sustituye Q veces seguidas por sus sumas de
prefijo. Imprimir el resultado módulo 998 244 353. Los límites son
2 segundos y 256 MB.

## Entrada

N y Q, 2 ≤ N ≤ 10⁵, 1 ≤ Q ≤ 10⁷, y luego el arreglo con valores de 1 a
10⁸.

## Salida

El arreglo final módulo 998 244 353.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 2
1 2 3
```

Salida:

```
1 4 10
```

## Solución

Una suma de prefijo multiplica la función generatriz del arreglo por
1 / (1 − x), así que Q de ellas la multiplican por 1 / (1 − x)^Q, cuyos
coeficientes son C(Q + k − 1, k). La respuesta es la convolución

pᵢ = Σ sobre j ≤ i de C(Q + i − j − 1, i − j) · vⱼ.

Los coeficientes se obtienen unos de otros: el k-ésimo es el anterior
por (Q + k − 1) / k, con los inversos modulares de 1 … N calculados con
la recurrencia lineal habitual.

La convolución se hace módulo 998 244 353 con la transformada teórica de
números, para la que se eligió este módulo. Python en cambio empaqueta
ambas sucesiones en números decimales enormes, 22 dígitos por elemento.
Cada coeficiente exacto del producto es menor que 10⁵ · 10⁸ · 10⁹, así
que las casillas no se desbordan entre sí, y la multiplicación decimal
incorporada hace internamente la transformada rápida; luego cada
casilla se reduce módulo 998 244 353.

En el ejemplo Q = 2 da los coeficientes 1, 2, 3, así que el último valor
es 3 · 1 + 2 · 2 + 1 · 3 = 10.

Esto cuesta O(N log N).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2212_math_combinatorics.cpp](2212_math_combinatorics.cpp) | G++ 13.2 x64 | math, combinatorics | O(N log N) | AC | 0.093 s | 2180 KB |
| [2212_math_combinatorics.go](2212_math_combinatorics.go) | Go 1.14 x64 | math, combinatorics | O(N log N) | AC | 0.125 s | 9012 KB |
| [2212_math_combinatorics.java](2212_math_combinatorics.java) | Java 1.8 | math, combinatorics | O(N log N) | AC | 0.500 s | 9564 KB |
| [2212_math_combinatorics.py](2212_math_combinatorics.py) | Python 3.12 x64 | math, combinatorics | O(N log N) | AC | 0.765 s | 31896 KB |
| [2212_math_combinatorics.rs](2212_math_combinatorics.rs) | Rust 1.75 x64 | math, combinatorics | O(N log N) | AC | 0.062 s | 8384 KB |
