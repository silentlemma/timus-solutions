# 1128. Dividir un grafo de grado tres de modo que cada vértice tenga como mucho un vecino en su lado

[Timus 1128](https://acm.timus.ru/problem.aspx?space=1&num=1128) · dificultad 412 · greedy

Problema original de Dmitry Filimonenkov, del sexto concurso universitario de programación de la Universidad Estatal de los Urales, 21 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N ≤ 7163` niños; cada niño tiene como mucho tres enemigos, y la
enemistad es mutua. Divide a los niños en dos grupos de modo que cada
niño tenga como mucho un enemigo en su propio grupo. Imprime el grupo
menor (a igual tamaño, el que tiene al niño 1): su tamaño y luego sus
niños. Imprime `NO SOLUTION` si no hay división posible.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas: el número de enemigos de un niño y luego sus
números.

## Salida

El tamaño del grupo menor y luego sus niños separados por espacios, o
`NO SOLUTION`.

## Evaluación

Se acepta cualquier división válida. El comprobador verifica el tamaño,
que el grupo listado es el menor (o contiene al niño 1 a igual tamaño), y
que cada niño, listado o no, tiene como mucho un enemigo en su lado.

## Ejemplos

### Ejemplo 1

Entrada:

```
8
3 2 3 7
3 1 3 7
3 1 2 7
1 6
0
2 4 8
3 1 2 3
1 6
```

Salida:

```
3
3 6 7
```

## Solución

Siempre existe una división, y una búsqueda local sencilla la encuentra.
Se empieza con todos en un grupo. Mientras algún niño tenga dos o más
enemigos en su propio grupo, se le pasa al otro grupo: como tiene como
mucho tres enemigos, en el otro lado tiene como mucho uno, así que el
número de parejas de enemigos que comparten grupo baja al menos en uno.
Ese número empieza como mucho en `3N/2`, así que los cambios paran tras
como mucho esos pasos, y cuando paran, cada niño tiene como mucho un
enemigo en su lado. Una lista de trabajo guarda los niños por revisar, y
tras un cambio solo se añaden el niño movido y sus enemigos. `O(N)`.

Detalles a tener en cuenta:

- `NO SOLUTION` nunca es la respuesta: con grado como mucho tres siempre
  hay división;
- el grupo impreso debe ser el menor de la división, y a igual tamaño el
  que contiene al niño 1;
- el grupo menor puede estar vacío: se imprime `0` y una línea vacía.

Las respuestas se comprobaron con el comprobador en todas las pruebas y en
60 grafos aleatorios, entre ellos grupos de cuatro niños que se pelean
todos entre sí.

## Notas por lenguaje

- Todos los lenguajes hacen la misma búsqueda con lista de trabajo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1128_greedy.cpp](1128_greedy.cpp) | G++ 13.2 x64 | greedy | O(N) | AC | 0.031 s | 500 KB |
| [1128_greedy.go](1128_greedy.go) | Go 1.14 x64 | greedy | O(N) | AC | 0.031 s | 2704 KB |
| [1128_greedy.java](1128_greedy.java) | Java 1.8 | greedy | O(N) | AC | 0.109 s | 2072 KB |
| [1128_greedy.py](1128_greedy.py) | Python 3.12 x64 | greedy | O(N) | AC | 0.109 s | 3948 KB |
| [1128_greedy.rs](1128_greedy.rs) | Rust 1.75 x64 | greedy | O(N) | AC | 0.046 s | 1048 KB |
