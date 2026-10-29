# 1446. El Sombrero Seleccionador

[Timus 1446](https://acm.timus.ru/problem.aspx?space=1&num=1446) · dificultad 91 · implementation

Problema original de Stanislav Vasiliev, del Décimo Campeonato Universitario de Programación por Equipos de los Urales, 24–25 de marzo de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N estudiantes de primer año (1 ≤ N ≤ 1000) fueron repartidos en casas;
para cada estudiante, en el orden de la ceremonia, una línea tiene el
nombre (letras latinas, espacios y guiones, como mucho 200 caracteres) y
la siguiente la casa. Hay que imprimir las listas de Slytherin,
Hufflepuff, Gryffindor y Ravenclaw en ese orden: el nombre de la casa
con dos puntos y luego sus estudiantes, uno por línea, en el orden de la
ceremonia, con una línea vacía entre listas. Cada casa recibe al menos
un estudiante.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego 2N líneas: el nombre y la casa de cada estudiante.

## Salida

Las cuatro listas.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
Ivan Ivanov
Gryffindor
Mac Go Nagolo
Hufflepuff
Zlobeus Zlei
Slytherin
Um Bridge
Slytherin
Tatiana Henrihovna Grotter
Ravenclaw
Garry Potnyj
Gryffindor
Herr Mionag-Ranger
Gryffindor
```

Salida:

```
Slytherin:
Zlobeus Zlei
Um Bridge

Hufflepuff:
Mac Go Nagolo

Gryffindor:
Ivan Ivanov
Garry Potnyj
Herr Mionag-Ranger

Ravenclaw:
Tatiana Henrihovna Grotter
```

## Solución

La entrada se lee línea a línea, porque los nombres tienen espacios, y
cada nombre se añade a la lista de su casa; luego se imprimen las listas
en el orden pedido. Del nombre solo se quita el salto de línea, así que
los espacios interiores quedan tal cual. `O(N)` líneas.

Detalles a tener en cuenta:

- leer por palabras parte los nombres (pruebas 01, 03, 04);
- un estudiante puede llamarse como una casa (prueba 03);
- el orden de las casas en la salida no es alfabético.

## Soluciones optimizadas

La solución optimizada en Rust no necesita un mapa por nombre de casa.
Lee la entrada línea a línea en lugar de toda de una vez, busca la casa
en la lista de cuatro y añade cada nombre directamente al búfer de bytes
de su casa: 492 KB en lugar de 980 KB, con el mismo tiempo.

La solución optimizada en Java lee la entrada en bloques de 4 KB,
reconoce la casa por su primera letra, distinta en las cuatro, y copia
los nombres como bytes en un flujo de bytes por casa, sin objetos
`String`: 0.062 s en lugar de 0.125 s y 1180 KB en lugar de 2324 KB. La
solución optimizada en Python lee las líneas como bytes y reúne los
nombres de cada casa en un `bytearray`: 812 KB en lugar de 1520 KB, con
el mismo tiempo.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1446_implementation.cpp](1446_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.031 s | 520 KB | 11286303 |
| [1446_implementation.go](1446_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1672 KB | 11286304 |
| [1446_implementation.java](1446_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.125 s | 2324 KB | 11286306 |
| [1446_implementation.py](1446_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 1520 KB | 11286305 |
| [1446_implementation.rs](1446_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 980 KB | 11286307 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1446_implementation_optimized.java](1446_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.062 s | 1180 KB | 11303748 |
| [1446_implementation_optimized.py](1446_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(N) | AC | 0.078 s | 812 KB | 11303749 |
| [1446_implementation_optimized.rs](1446_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 492 KB | 11303607 |

\* No está entre las 10 mejores ni en el 15% mejor de las soluciones de
su lenguaje en el juez actual; quizá se pueda optimizar más.
