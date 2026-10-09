# 1041. La base más barata de un conjunto de vectores

[Timus 1041](https://acm.timus.ru/problem.aspx?space=1&num=1041) · dificultad 4654 · math, greedy

Problema original de Dmitry Filimonenkov, del V Campeonato por Equipos de Programación de la Universidad Estatal de los Urales, octubre de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `M` vectores enteros de dimensión `N` (`3 ≤ N ≤ 50`,
`N ≤ M ≤ 2000`, coordenadas de valor absoluto como mucho 2000), cada uno
con un precio de 1 a 15000. Elige `N` vectores linealmente independientes
con el menor precio total. Entre todas las elecciones más baratas, da la
lista lexicográficamente menor de sus números en orden creciente. Si
ningún grupo de `N` vectores es independiente, imprime `0`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`M` y `N`, luego `M` líneas con las coordenadas de los vectores y luego
`M` líneas con sus precios.

## Salida

El menor precio total y luego los `N` números de los vectores elegidos en
orden creciente, uno por línea; o `0`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 3
1 0 0
0 1 0
0 0 1
0 0 2
0 0 3
10
20
30
10
10
```

Salida:

```
40
1
2
4
```

### Ejemplo 2

Entrada:

```
4 3
1 2 3
2 4 6
0 1 1
1 3 4
1
1
1
1
```

Salida:

```
0
```

## Solución

Los conjuntos de vectores linealmente independientes forman un matroide,
y en un matroide el algoritmo voraz es óptimo: se recorren los vectores
desde el más barato y se conserva un vector cuando es independiente de los
conservados hasta ese momento. Con precios iguales, se va en orden
creciente de número. Esto da también la lista lexicográficamente menor.
Todas las bases más baratas contienen una base de cada nivel de precio
`c`, tomada sobre el espacio generado por los vectores más baratos. Las
elecciones en niveles distintos no dependen unas de otras, y en cada nivel
la pasada voraz en orden creciente de número da una base cuyo `k`-ésimo
número más pequeño es el menor posible para todo `k`.

La prueba de independencia es la eliminación gaussiana: los vectores
conservados se guardan en forma escalonada (cada fila tiene una coordenada
pivote igual a 1 y ceros en los pivotes de las filas anteriores). Se
reduce el candidato con cada fila; si queda algo distinto de cero, es
independiente y pasa a ser una fila nueva. Son `O(M · N^2)` operaciones.

La aritmética exacta importa: con coma flotante, vectores enteros casi
paralelos pueden juzgarse mal. Las soluciones calculan módulo el primo
`2^31 − 1`. Un conjunto independiente módulo un primo es independiente
sobre los racionales (algún menor es distinto de cero módulo el primo, y
por tanto distinto de cero). Lo contrario solo falla si el primo divide a
todos los menores `N × N` no nulos, algo prácticamente imposible con estos
tamaños y datos. Las pruebas se comprobaron con fracciones exactas.

Detalles a tener en cuenta:

- no basta con ser voraz por el precio: a igual precio hay que ir en orden
  creciente de número para obtener la lista menor;
- los vectores se imprimen en orden creciente, no en el orden en que se
  eligieron;
- si ni siquiera los `M` vectores generan `N` dimensiones, la respuesta es
  `0`.

## Notas por lenguaje

- **C++**, **Go**, **Java**, **Rust**: enteros de 64 bits; el producto de
  dos residuos menores que `2^31` cabe de sobra.
- **Python**: la base se mantiene completamente reducida (cada fila vale
  cero en los pivotes de todas las demás). Así, el resto de un candidato
  en una coordenada libre es un único producto escalar con sus coordenadas
  pivote, calculado con `sum(map(mul, ...))`, lo bastante rápido en
  CPython.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1041_math_greedy.cpp](1041_math_greedy.cpp) | G++ 13.2 x64 | math, greedy | O(M·N^2) | AC | 0.093 s | 760 KB |
| [1041_math_greedy.go](1041_math_greedy.go) | Go 1.14 x64 | math, greedy | O(M·N^2) | AC | 0.046 s | 3280 KB |
| [1041_math_greedy.java](1041_math_greedy.java) | Java 1.8 | math, greedy | O(M·N^2) | AC | 0.234 s | 4492 KB |
| [1041_math_greedy.py](1041_math_greedy.py) | Python 3.12 x64 | math, greedy | O(M·N^2) | AC | 0.203 s | 10176 KB |
| [1041_math_greedy.rs](1041_math_greedy.rs) | Rust 1.75 x64 | math, greedy | O(M·N^2) | AC | 0.062 s | 1640 KB |
