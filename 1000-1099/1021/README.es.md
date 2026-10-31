# 1021. Un par de dos listas ordenadas con una suma dada

[Timus 1021](https://acm.timus.ru/problem.aspx?space=1&num=1021) · dificultad 148 · two_pointers, hashing

Problema original de la Segunda Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 7 de octubre de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan dos listas de enteros: la primera ordenada de forma creciente y la
segunda de forma decreciente (`1 ≤ N_i ≤ 50 000` números cada una, cada
número entre -32768 y 32767). Decide si se puede elegir un número de cada
lista de modo que sumen exactamente 10000.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

La primera lista: su tamaño y luego sus números, uno por línea. Después la
segunda lista con el mismo formato.

## Salida

`YES` si existe tal par, `NO` en caso contrario.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
-5
3
9998
3
10
7
2
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
3
1
2
3
3
9000
50
0
```

Salida:

```
NO
```

## Solución

**Dos punteros.** Se pone un puntero `i` al principio de la lista creciente
y `j` al principio de la decreciente, así que `up[i]` es el menor número que
queda de la primera lista y `down[j]` el mayor de la segunda. Se compara
`up[i] + down[j]` con 10000:

- igual: el par está encontrado;
- menor: `up[i]` no puede formar parte de ningún par, porque ni siquiera el
  mayor `down[j]` restante alcanza: se avanza `i`;
- mayor: `down[j]` no puede formar parte de ningún par, porque incluso el
  menor `up[i]` restante se pasa: se avanza `j`.

Cuando un puntero sale de su lista, no hay par. Cada paso descarta un
número: `O(N_1 + N_2)`.

**Hash.** Se meten `10000 - b` para cada `b` de la segunda lista en un
conjunto y se comprueba si algún número de la primera está en él; también
es lineal en promedio y no necesita el orden.

Detalles a tener en cuenta:

- la segunda lista está ordenada al revés: recorre ambas listas desde el
  principio;
- la suma 10000 puede requerir valores extremos, como `32767 + (-22767)`.

## Soluciones optimizadas

La solución optimizada en C++ analiza los números a mano desde un búfer
de 4 KB que se rellena con `fread`, en lugar de `scanf`. Guarda solo la
lista creciente, en `int16_t`, que admite cualquier número entre -32768
y 32767, y avanza su puntero mientras lee la lista decreciente, de modo
que la segunda lista nunca se guarda: {1021_two_pointers_optimized.cpp}.

La solución optimizada en Go analiza los números byte a byte desde un
`bufio.Reader` en lugar de `fmt.Fscan`. Guarda solo la lista creciente,
en `int16`, que admite cualquier número entre -32768 y 32767, y avanza
su puntero mientras lee la lista decreciente, de modo que la segunda
lista nunca se guarda: {1021_two_pointers_optimized.go}.

La solución optimizada en Java analiza los números a mano desde un búfer
de 4 KB que se rellena desde `System.in`, en lugar de `StreamTokenizer`.
Guarda solo la lista creciente, en `short`, que admite cualquier número
entre -32768 y 32767, y avanza su puntero mientras lee la lista
decreciente, de modo que la segunda lista nunca se guarda:
{1021_two_pointers_optimized.java}.

La solución optimizada en Python aprovecha que cada número va en su
propia línea y convierte cada línea según llega, en lugar de partir toda
la entrada en una lista. En vez de un conjunto, marca los números de la
primera lista en un `bytearray` de 65536 celdas, una por cada valor
posible entre -32768 y 32767. Para cada `b` de la segunda lista
comprueba primero que `10000 - b` está en ese intervalo y solo entonces
lo busca allí: {1021_hashing_optimized.py}.

La solución optimizada en Rust analiza los números a mano desde un búfer
de 4 KB que se rellena desde la entrada estándar, en lugar de leer toda
la entrada en un `String`. Guarda solo la lista creciente, en `i16`, que
admite cualquier número entre -32768 y 32767, y avanza su puntero
mientras lee la lista decreciente, de modo que la segunda lista nunca se
guarda: {1021_two_pointers_optimized.rs}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1021_two_pointers_optimized.cpp`: reducción de tiempo +80.77%;
  reducción de memoria +63.89%; base: `1021_two_pointers.cpp`.

- `1021_two_pointers_optimized.go`: reducción de tiempo +50.00%;
  reducción de memoria +57.25%; base: `1021_two_pointers.go`.

- `1021_two_pointers_optimized.java`: reducción de tiempo +37.60%;
  reducción de memoria +45.58%; base: `1021_two_pointers.java`.

- `1021_hashing_optimized.py`: reducción de tiempo -39.74%; reducción de
  memoria +95.36%; base: `1021_hashing.py`.

- `1021_two_pointers_optimized.rs`: reducción de tiempo +67.39%;
  reducción de memoria +86.55%; base: `1021_two_pointers.rs`.

## Notas por lenguaje

- **C++**, **Go**, **Java**, **Rust**: dos punteros.
- **Python**: una intersección de conjuntos, que corre a velocidad de C.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1021_two_pointers.cpp](1021_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N1 + N2) | AC | 0.078 s | 576 KB | 11278250 |
| [1021_two_pointers.go](1021_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N1 + N2) | AC | 0.062 s | 2620 KB | 11278252 |
| [1021_two_pointers.java](1021_two_pointers.java) | Java 1.8 | two_pointers | O(N1 + N2) | AC | 0.125 s | 904 KB | 11278257 |
| [1021_hashing.py](1021_hashing.py) | Python 3.12 x64 | hashing | O(N1 + N2) on average | AC | 0.078 s | 10700 KB | 11278255 |
| [1021_two_pointers.rs](1021_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N1 + N2) | AC | 0.046 s | 2112 KB | 11278259 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1021_two_pointers_optimized.cpp](1021_two_pointers_optimized.cpp) | G++ 13.2 x64 | two_pointers | O(N1 + N2) | AC | 0.015 s | 208 KB | 11304533 |
| [1021_two_pointers_optimized.go](1021_two_pointers_optimized.go) | Go 1.14 x64 | two_pointers | O(N1 + N2) | AC | 0.031 s | 1120 KB | 11304534 |
| [1021_two_pointers_optimized.java](1021_two_pointers_optimized.java) | Java 1.8 | two_pointers | O(N1 + N2) | AC | 0.078 s | 492 KB | 11304535 |
| [1021_hashing_optimized.py](1021_hashing_optimized.py) \* | Python 3.12 x64 | hashing | O(N1 + N2) on average | AC | 0.109 s | 496 KB | 11304537 |
| [1021_two_pointers_optimized.rs](1021_two_pointers_optimized.rs) | Rust 1.75 x64 | two_pointers | O(N1 + N2) | AC | 0.015 s | 284 KB | 11304536 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
