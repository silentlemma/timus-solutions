# 1575. Metro de Ekaterimburgo 2

[Timus 1575](https://acm.timus.ru/problem.aspx?space=1&num=1575) · dificultad 863 · bfs

Problema original de Alexander Ipatov, del USU Junior Contest (XIV Campeonato Abierto por Equipos de Programación para Escolares de la Región de Sverdlovsk), octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El enunciado muestra un plano del metro del futuro: 70 estaciones en 8
líneas, una de ellas circular, con transbordos entre 2 y 4 líneas en
algunas estaciones. Un tramo entre estaciones vecinas tarda un minuto,
y los transbordos y las esperas no tardan nada. Hay que responder hasta
4900 preguntas: el menor número de minutos de una estación a otra.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número de preguntas y luego dos nombres de estación por línea.

## Salida

Un número de minutos por pregunta.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
Prospekt_Kosmonavtov Geologicheskaya
Shevchenko Vilonovskaya
Koltsovo Zelyony_ostrov
Teatralnaya Kamennye_palatki
China_town Italyanskaya
1905_year_square 1905_year_square
```

Salida:

```
6
3
11
3
9
0
```

## Solución

El único trabajo de verdad es copiar el plano de la imagen. Cada línea
se anota como sus estaciones en orden, y la circular une además su
última estación con la primera. Una estación de transbordo se dibuja
como dos o más círculos juntos, a veces con un trozo corto de línea
entre ellos, pero es una sola estación: las ocho líneas nombran
exactamente 70 estaciones, así que cada círculo pertenece a una con
nombre. Teatralnaya, por ejemplo, une las líneas azul claro, azul y
amarilla, y 1905_year_square cuatro líneas.

Con transbordos gratis, la respuesta es el número de tramos de un
camino mínimo en el grafo de estaciones, que da una búsqueda en anchura
desde cada estación una vez. `O(70 · aristas + preguntas)`. El plano se
copió de la imagen de forma independiente y las respuestas de los 4900
pares ordenados coinciden con un programa independiente.

Detalles a tener en cuenta:

- dos estaciones se escriben distinto en la imagen que en la entrada:
  `Prospekt Kosmonavtov` y `Kamennye palatki` aparecen con un espacio y
  un salto de línea, pero llegan con guiones bajos;
- la línea circular es un anillo de 12 estaciones;
- una pregunta puede pedir el camino de una estación a sí misma (0).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1575_bfs.cpp](1575_bfs.cpp) | G++ 13.2 x64 | bfs | O(V E + Q) | AC | 0.015 s | 408 KB |
| [1575_bfs.go](1575_bfs.go) | Go 1.14 x64 | bfs | O(V E + Q) | AC | 0.031 s | 2400 KB |
| [1575_bfs.java](1575_bfs.java) | Java 1.8 | bfs | O(V E + Q) | AC | 0.171 s | 6332 KB |
| [1575_bfs.py](1575_bfs.py) | Python 3.12 x64 | bfs | O(V E + Q) | AC | 0.109 s | 1532 KB |
| [1575_bfs.rs](1575_bfs.rs) | Rust 1.75 x64 | bfs | O(V E + Q) | AC | 0.046 s | 836 KB |
