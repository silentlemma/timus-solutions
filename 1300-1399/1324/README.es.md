# 1324. Espacios de más

[Timus 1324](https://acm.timus.ru/problem.aspx?space=1&num=1324) · dificultad 929 · greedy

Problema original con idea de Stanislav Vasiliev, preparado por Stanislav Vasiliev e Igor Goldberg, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un texto tiene tramos de 1 a L espacios, con L < 2 000 000. Un comando
del editor sustituye cada grupo de exactamente k espacios por un
espacio en una sola pasada de izquierda a derecha, sin volver a mirar
lo que acaba de sustituir. Así, con k = 2 un tramo de seis espacios
queda en tres, no en uno.

Hay que hallar el menor número de comandos, con longitudes k elegidas,
que convierten cualquier tramo de hasta L espacios en un solo espacio.
Entre esos planes se elige uno que resuelva todos los tramos de hasta K
espacios para el mayor K posible. Se acepta cualquier plan así.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

El número L.

## Salida

El número de comandos R y luego R líneas con la longitud que sustituye
cada comando, en el orden en que se ejecutan.

## Comprobación

El comprobador exige el mismo número de comandos que el plan esperado y
calcula, para ambos planes, el mayor K tal que cualquier tramo de 1 a K
espacios acaba en un solo espacio. El plan debe llegar a L y al mismo K
que el plan esperado.

## Ejemplos

### Ejemplo 1

Entrada:

```
22
```

Salida:

```
4
6
3
2
2
```

## Solución

Un comando de longitud k convierte un tramo de n espacios en
n div k + n mod k espacios. Se va hacia atrás desde el final, donde
solo puede quedar un espacio, y sea M el tramo más largo que los
comandos ya elegidos convierten en un espacio. Un tramo de
n = q · k + r espacios queda en q + r, y el primer tramo que queda más
largo que M es (M − k + 2) · k + (k − 1). Así, un comando con
2 ≤ k ≤ M + 1 resuelve todos los tramos de hasta (M + 3 − k) · k − 2
espacios, y un k mayor no gana nada: el tramo de k − 1 espacios queda
igual.

Ese alcance crece con M, así que en cada paso hacia atrás lo mejor es
el k de mayor alcance, k = ⌊(M + 3) / 2⌋, el vértice de la parábola.
Cada paso da entonces el mayor M posible, y el primer R con M ≥ L es el
menor número de comandos. Empezando en M = 1, los alcances son 2, 4,
10, 40, 460, 53 590 y 718 052 410, así que nunca hacen falta más de
siete comandos. El plan se imprime del primer comando al último, al
revés del orden en que se halla. `O(R)`.

Detalles a tener en cuenta:

- para L = 1 no hay nada que sustituir y la respuesta es un solo 0
  (prueba 02);
- con M par hay dos k igual de buenos, así que hay varios planes
  óptimos y hace falta un comprobador: para 22 llegan a 40 tanto
  6, 3, 2, 2 como 7, 4, 3, 2;
- el alcance tras siete comandos, 718 052 410, aún cabe en un entero de
  32 bits, pero las soluciones usan números de 64 bits de todos modos.

La fórmula de un comando se comparó con ejecuciones directas para todo
M hasta 79 y k hasta 89, y los planes con todas las listas de hasta
cuatro longitudes de como mucho 23 para cada L hasta 40.

## Notas por lenguaje

- Las cinco soluciones construyen el plan de la misma manera.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1324_greedy.cpp](1324_greedy.cpp) | G++ 13.2 x64 | greedy | O(R) | AC | 0.015 s | 196 KB |
| [1324_greedy.go](1324_greedy.go) | Go 1.14 x64 | greedy | O(R) | AC | 0.031 s | 1068 KB |
| [1324_greedy.java](1324_greedy.java) | Java 1.8 | greedy | O(R) | AC | 0.109 s | 1620 KB |
| [1324_greedy.py](1324_greedy.py) | Python 3.12 x64 | greedy | O(R) | AC | 0.093 s | 460 KB |
| [1324_greedy.rs](1324_greedy.rs) | Rust 1.75 x64 | greedy | O(R) | AC | 0.031 s | 224 KB |
