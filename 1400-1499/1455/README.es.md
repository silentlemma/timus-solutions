# 1455. Libertad de expresión

[Timus 1455](https://acm.timus.ru/problem.aspx?space=1&num=1455) · dificultad 2023 · shortest_paths

Problema original de Nikita Rybak, Ilya Grebnov y Dmitry Kovalioff, de Timus Top Coders: Second Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un diccionario tiene N palabras distintas (1 ≤ N ≤ 100) de 1 a 100
letras latinas minúsculas. Tras una reforma, los textos se escriben sin
separadores. Hay que hallar un texto de como mucho 20000 letras que se
divida en palabras del diccionario de dos maneras distintas, o imprimir
«NO» si no existe.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego las N palabras.

## Salida

«NO», o «YES» y el texto. Se acepta cualquier texto así.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
ab
acb
bc
abac
babbc
```

Salida:

```
YES
abacbabbc
```

El texto «abacbabbc» es a la vez «abac» + «babbc» y «ab» + «acb» +
«ab» + «bc».

## Solución

Se leen en paralelo dos divisiones distintas de un mismo texto, en el
espíritu de la prueba de Sardinas–Patterson. En cada momento una
división va por delante de la otra en una cola, y esa cola es siempre un
sufijo de una palabra del diccionario, así que hay como mucho 100 · 100
estados. La búsqueda empieza en cada par de palabras u ≠ v en el que u
es prefijo de v, con la cola «v sin u». Desde una cola t, una palabra w
añadida a la división rezagada o bien termina justo con t, lo que cierra
un texto ambiguo; o es más larga y empieza por t, y la otra división se
queda atrás por el resto de w; o es prefijo de t, y deja el resto de t.

El coste de un estado es la longitud del texto escrito hasta entonces,
que solo crece cuando la división rezagada adelanta. El algoritmo de
Dijkstra sobre estos costes encuentra el texto ambiguo más corto, así
que si existe algún texto dentro del límite, el hallado también lo está;
el texto se reconstruye siguiendo las piezas hacia atrás hasta el par
inicial. `O((N² + S · N) · L log(N + S + 2))` con S estados de cola
alcanzados y longitud máxima de palabra L.

Detalles a tener en cuenta:

- una sola palabra, un código prefijo o un código sufijo no tiene texto
  ambiguo (pruebas 02, 05, 09, gen4, gen5);
- una división puede ir delante muchos pasos seguidos, así que la
  búsqueda debe seguir colas y no solo pares de palabras (prueba 13);
- una búsqueda en anchura simple cuenta pasos y no letras, y puede
  devolver un texto más largo de lo necesario.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1455_shortest_paths.cpp](1455_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O((N² + S N) L log(N + S + 2)) | AC | 0.031 s | 3968 KB |
| [1455_shortest_paths.go](1455_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O((N² + S N) L log(N + S + 2)) | AC | 0.031 s | 3668 KB |
| [1455_shortest_paths.java](1455_shortest_paths.java) | Java 1.8 | shortest_paths | O((N² + S N) L log(N + S + 2)) | AC | 0.156 s | 4448 KB |
| [1455_shortest_paths.py](1455_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O((N² + S N) L log(N + S + 2)) | AC | 0.218 s | 2884 KB |
| [1455_shortest_paths.rs](1455_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O((N² + S N) L log(N + S + 2)) | AC | 0.031 s | 2876 KB |
