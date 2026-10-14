# 1530. Unos y ceros

[Timus 1530](https://acm.timus.ru/problem.aspx?space=1&num=1530) · dificultad 880 · greedy

Problema original de Dmitry Gozman, del Dmitry Gozman Contest 1 en el campus de invierno de Petrozavodsk, enero de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos sucesiones binarias A y B de longitud n (1 ≤ n ≤ 10⁵) son
compatibles si A XOR B = A + B. Dado un par (p, q), hay que hallar el
primer par compatible después de él, ordenando los pares por la primera
sucesión y luego por la segunda; si no hay ninguno, se escribe el
primer par compatible de todos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n y luego p y q, cada una en su línea, quizá con espacios al final.

## Salida

Las dos sucesiones de la respuesta, cada una en su línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
0
0
```

Salida:

```
0
1
```

### Ejemplo 2

Entrada:

```
2
01
10
```

Salida:

```
10
00
```

## Solución

Sumar dos números binarios da su XOR justo cuando no hay acarreo, es
decir, cuando ninguna posición tiene un 1 en ambos. La respuesta o bien
mantiene a = p con el menor b compatible por encima de q, o bien toma
el siguiente a.

Con a = p, el mejor b coincide con q hasta una posición j, tiene 1 en j
donde q tiene 0, y ceros después. La parte conservada de q debe evitar
los unos de p, así que j está antes de la primera posición donde p y q
tienen ambos 1, y b solo puede poner 1 en j si p tiene 0 allí. El mayor
j así da el menor b. Si no hay ninguno, a debe crecer: la siguiente
sucesión binaria después de p convierte su último 0 en 1 y pone a cero
el resto, y b = 0…0 sirve con cualquier a. Si p es todo unos, se vuelve
a empezar con el par de todo ceros. `O(n)`.

Detalles a tener en cuenta:

- «+» suma las sucesiones como números binarios, así que compatibles
  significa sin unos comunes (todas las pruebas);
- p y q pueden chocar entre sí, y entonces la cola de q no se puede
  conservar (prueba 05);
- si p es todo unos no hay nada después, y la respuesta vuelve al
  principio (pruebas 03, 04, gen3);
- las líneas pueden acabar en espacios, así que la entrada se lee por
  tokens (prueba 06).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1530_greedy.cpp](1530_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.031 s | 816 KB |
| [1530_greedy.go](1530_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.031 s | 2380 KB |
| [1530_greedy.java](1530_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.109 s | 6292 KB |
| [1530_greedy.py](1530_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.078 s | 1040 KB |
| [1530_greedy.rs](1530_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.046 s | 740 KB |
