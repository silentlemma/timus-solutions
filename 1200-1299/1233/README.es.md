# 1233. El lugar de un número en orden de diccionario

[Timus 1233](https://acm.timus.ru/problem.aspx?space=1&num=1233) · dificultad 907 · math

Problema original de Andrew Stankevich, del concurso regional ACM ICPC del noreste de Europa 2002–2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Escribimos los números de 1 a N en orden lexicográfico, como cadenas:
para N = 11 queda 1, 10, 11, 2, 3, …, 9. Dados K y M (1 ≤ K, M ≤ 10⁹),
hay que encontrar el menor N con el que K ocupa el lugar M, o decir que
no existe.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

K y M.

## Salida

El menor N así, o 0 si no existe.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 4
```

Salida:

```
11
```

### Ejemplo 2

Entrada:

```
2 1
```

Salida:

```
0
```

## Solución

Tomamos N ≥ K y contamos los números que van no más tarde que K.

- **No más largos que K.** Para cada longitud l, son los números desde
  `10^(l−1)` hasta las primeras l cifras de K. Todos son como mucho K,
  así que cualquier N ≥ K los contiene; su cantidad B es el lugar de K
  cuando N = K.
- **Más largos que K.** Un número de longitud `len(K) + j` va antes que
  K justo cuando es menor que `K·10^j`, así que hay
  `K·10^j − 10^(len(K)+j−1)` para cada j ≥ 1.

Cuando N crece a partir de K, el lugar de K sube en uno justo cuando el
propio N es uno de los números más largos que van antes que K. Así que si
M < B no hay respuesta, si M = B la respuesta es K, y si no, N es el
(M − B)-ésimo número más largo anterior a K en orden creciente: se restan
longitudes enteras y luego se cuenta dentro de la primera longitud que no
se agota. Al analizar todos los prefijos se procesan `1 + 2 + ... + len(K)`
cifras; el bucle de longitudes mayores hace `O(log M)` iteraciones (como
mucho nueve con estos límites). Con aritmética entera de coste unitario,
el tiempo total es `O((log K)^2 + log M)`.

Detalles a tener en cuenta:

- ninguna potencia de diez tiene antes un número más largo, así que su
  lugar nunca cambia (pruebas 04, 08, 11);
- N puede pasar con creces de 32 bits: antes de K = 100000001 solo van
  `10^j` números de cada longitud mayor, y con M = 10⁹ la respuesta tiene
  18 cifras (prueba 10);
- el número de longitudes mayores depende de M, así que estimar el tiempo
  solo por el análisis de K omite este trabajo (pruebas 09, 10).

## Notas por lenguaje

- C++, Go, Java y Rust usan enteros de 64 bits con signo; Python usa
  enteros de precisión arbitraria. `K·10^j` queda por debajo de 10¹⁸ porque,
  si K no es potencia de diez, el bucle termina en nueve longitudes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1233_math.cpp](1233_math.cpp) | G++ 13.2 x64 | math | O((log K)^2 + log M) | AC | 0.015 s | 200 KB |
| [1233_math.go](1233_math.go) | Go 1.14 x64 | math | O((log K)^2 + log M) | AC | 0.031 s | 1084 KB |
| [1233_math.java](1233_math.java) | Java 1.8 | math | O((log K)^2 + log M) | AC | 0.109 s | 460 KB |
| [1233_math.py](1233_math.py) | Python 3.12 x64 | math | O((log K)^2 + log M) | AC | 0.078 s | 456 KB |
| [1233_math.rs](1233_math.rs) | Rust 1.75 x64 | math | O((log K)^2 + log M) | AC | 0.046 s | 232 KB |
