# 1799. Sasha y las cadenas con estilo

[Timus 1799](https://acm.timus.ru/problem.aspx?space=1&num=1799) · dificultad 4368 · strings

Problema original de Oleksandr Kulkov, del campus de entrenamiento de verano de Petrozavodsk 2015, Moscow IPT Contest.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se construye el trie de todos los sufijos de una cadena y se funde cada
cadena de aristas que pasa por nodos con un solo hijo, sin ningún
marcador de fin. En cada arista de este árbol comprimido se cuentan las
subcadenas no vacías distintas de su etiqueta, y se suman. Responder
para cada una de varias cadenas.

## Entrada

n (1 ≤ n ≤ 10⁵) y luego n cadenas de letras minúsculas con longitud
total de a lo sumo 10⁵.

## Salida

La suma de cada cadena, una por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
umqra
umnik
merkurev
```

Salida:

```
35
35
101
```

### Ejemplo 2

Entrada:

```
1
abaaa
```

Salida:

```
17
```

## Solución

Los subárboles iguales del árbol de sufijos están fundidos en el
autómata de sufijos, así que se construye el autómata y se comprime de
la misma forma: se conservan el estado inicial y todo estado cuyo
número de transiciones de salida no sea 1, y cada camino por los demás
se sustituye por una arista. Como en el árbol, así desaparecen los
estados donde un sufijo simplemente termina. Una arista de u a w con
cierta etiqueta representa tantas aristas del árbol como caminos hay
del inicio a u, contados en orden creciente de longitud. Cada etiqueta
es la subcadena s[l..r] que termina en la primera aparición de las
cadenas de w, así que falta el número de subcadenas distintas de
s[l..r] para cada arista.

Estas consultas por rangos se responden fuera de línea, ordenadas por
r. Mientras el prefijo crece hasta r, count[p] es el número de
subcadenas distintas de s[0..r] cuya última aparición empieza en p;
entonces la respuesta para s[l..r] es la suma de count[p] para p ≥ l.
Añadir una letra hace que todos los sufijos del prefijo aparezcan por
última vez en el nuevo final: son los estados del camino de enlaces de
sufijo desde el nuevo prefijo hasta el inicio. Se mueven en cadenas
enteras de estados que compartían su último final anterior. Como en los
árboles link–cut, hay en promedio O(log n) de esas cadenas por letra.
Para una cadena los inicios antiguos forman un rango, así que dos
árboles de Fenwick con suma en rango y consulta en rango llevan count.
Un árbol de segmentos sobre el recorrido de Euler del árbol de enlaces
de sufijo da el último final de un estado, el prefijo más tardío en su
subárbol. `O(n log² n)` sobre todas las cadenas.

En el segundo ejemplo el árbol comprimido tiene las aristas a, aa,
baaa y baaa, con 1, 2, 7 y 7 subcadenas distintas. Las dos aristas
baaa provienen de una arista del autómata a cuyo origen llegan dos
caminos desde el inicio.

Trampas:

- el final de un sufijo no detiene la compresión: para aa el árbol es
  una sola arista aa;
- etiquetas iguales en aristas distintas cuentan ambas, de lo que se
  encargan los números de caminos del autómata;
- la suma supera los 32 bits;
- con hasta 10⁵ cadenas, cada arreglo debe medirse por su propia
  cadena, no por el máximo.

Las respuestas coinciden con un trie de sufijos comprimido explícito en
más de mil cadenas cortas, y con una implementación aceptada
independiente en cadenas largas aleatorias, periódicas y de Fibonacci.
La solución en Python corre en PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1799_strings.cpp](1799_strings.cpp) | G++ 13.2 x64 | strings | O(n log^2 n) | AC | 0.250 s | 55692 KB |
| [1799_strings.go](1799_strings.go) | Go 1.14 x64 | strings | O(n log^2 n) | AC | 0.437 s | 94932 KB |
| [1799_strings.java](1799_strings.java) | Java 1.8 | strings | O(n log^2 n) | AC | 0.484 s | 50828 KB |
| [1799_strings.py](1799_strings.py) | PyPy 3.10 x64 | strings | O(n log^2 n) | AC | 1.218 s | 191384 KB |
| [1799_strings.rs](1799_strings.rs) | Rust 1.75 x64 | strings | O(n log^2 n) | AC | 0.312 s | 99724 KB |
