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

## Notas por lenguaje

- **C++**, **Go**, **Java**, **Rust**: dos punteros.
- **Python**: una intersección de conjuntos, que corre a velocidad de C.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1021_hashing.py](1021_hashing.py) | Python 3.12 x64 | hashing | O(N1 + N2) on average | AC | 0.078 s | 10700 KB |
| [1021_two_pointers.cpp](1021_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N1 + N2) | AC | 0.078 s | 576 KB |
| [1021_two_pointers.go](1021_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N1 + N2) | AC | 0.062 s | 2620 KB |
| [1021_two_pointers.java](1021_two_pointers.java) | Java 1.8 | two_pointers | O(N1 + N2) | AC | 0.125 s | 904 KB |
| [1021_two_pointers.rs](1021_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N1 + N2) | AC | 0.046 s | 2112 KB |
