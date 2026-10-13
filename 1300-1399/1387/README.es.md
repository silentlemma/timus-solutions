# 1387. El papá de Vasya

[Timus 1387](https://acm.timus.ru/problem.aspx?space=1&num=1387) · dificultad 1352 · math

Problema original de Alexander Ipatov, del campus de entrenamiento de verano de Petrozavodsk, agosto de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grafo dirigido es bonito si tiene N vértices y N − 1 arcos,
exactamente un vértice sin arcos de entrada y ningún ciclo dirigido. Hay
que contar los grafos bonitos de N vértices, 1 ≤ N ≤ 50, salvo
renumeración de los vértices.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número N.

## Salida

La cantidad de grafos bonitos distintos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
5
```

Salida:

```
9
```

## Solución

Cada vértice salvo la fuente tiene al menos un arco de entrada, y solo
hay N − 1 arcos, así que cada uno tiene exactamente uno. Sin ciclos,
seguir esos arcos hacia atrás siempre termina en la fuente: un grafo
bonito es un árbol con raíz y arcos que se alejan de ella. La respuesta
es, pues, el número a(N) de árboles con raíz sin etiquetas.

Al quitar la raíz queda un multiconjunto de árboles con raíz más
pequeños, y contar esos multiconjuntos da la recurrencia clásica

a(1) = 1, a(m + 1) = (s(1)·a(m) + s(2)·a(m − 1) + … + s(m)·a(1)) / m,

donde s(k) es la suma de d·a(d) sobre los divisores d de k. La división
siempre es exacta. `O(N²)` operaciones con números.

Detalles a tener en cuenta:

- a(50) = 425 976 989 835 141 038 353 no cabe en 64 bits; la suma antes
  de dividir desborda 64 bits con signo desde N = 43 y sin signo desde
  N = 44 (pruebas 18 y 19), así que se usan enteros de 128 bits o enteros grandes;
- el orden de los subárboles hijos no importa; a(8) vale 115 (prueba 06).

Las nueve primeras respuestas se comprobaron construyendo todos los
árboles a partir de otros menores y quedándose con las cadenas canónicas
distintas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1387_math.cpp](1387_math.cpp) | G++ 13.2 x64 | math | O(N^2) | AC | 0.015 s | 196 KB |
| [1387_math.go](1387_math.go) | Go 1.14 x64 | math | O(N^2) | AC | 0.031 s | 1228 KB |
| [1387_math.java](1387_math.java) | Java 1.8 | math | O(N^2) | AC | 0.125 s | 1848 KB |
| [1387_math.py](1387_math.py) | Python 3.12 x64 | math | O(N^2) | AC | 0.078 s | 424 KB |
| [1387_math.rs](1387_math.rs) | Rust 1.75 x64 | math | O(N^2) | AC | 0.015 s | 224 KB |
