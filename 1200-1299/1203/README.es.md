# 1203. A cuántas charlas puede asistir una persona

[Timus 1203](https://acm.timus.ru/problem.aspx?space=1&num=1203) · dificultad 78 · greedy

Problema original de Magaz Asanov, del Concurso por Equipos de la Universidad Estatal de los Urales, marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un congreso tiene `N ≤ 10⁵` charlas interesantes, cada una del minuto
`Ts` al minuto `Te`, `1 ≤ Ts < Te ≤ 30000`. Dos charlas a las que se
asiste no pueden solaparse, y entre ellas debe haber al menos un minuto:
tras una charla que termina en el 15, la siguiente puede empezar como
pronto en el 16. Hay que hallar el mayor número de charlas a las que
puede asistir una persona.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `Ts Te` para cada charla.

## Salida

El mayor número de charlas.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
3 4
1 5
6 7
4 5
1 3
```

Salida:

```
3
```

## Solución

El voraz clásico para planificar intervalos: tomar una y otra vez la
charla que termina antes entre las que empiezan después del final de la
última elegida. Cualquier horario óptimo puede cambiar su primera charla
por esa sin perder nada, y el argumento se repite.

Los tiempos son pequeños, así que no hace falta ordenar: para cada minuto
`e` se guarda el inicio más tardío entre las charlas que terminan en `e`.
Se recorren los minutos en orden; cuando el inicio más tardío en `e` es
posterior al último final elegido, se puede tomar una charla que termina
en `e`, y es la que antes termina de las disponibles. `O(N + T)` con
`T = 30000`.

Detalles a tener en cuenta:

- una charla que empieza en el mismo minuto en que termina la anterior no
  está permitida, así que la comprobación es estricta: «inicio > último
  final»;
- las charlas idénticas repetidas cuentan como mucho una vez.

Las respuestas se compararon con una solución escrita aparte en 300
entradas aleatorias y en todas las pruebas.

## Soluciones optimizadas

Las soluciones optimizadas (C++, Rust) analizan los números a mano
directamente desde el búfer de entrada en lugar de `scanf` o de leer
toda la entrada en una cadena, y guardan los inicios más tardíos como
números de 16 bits, ya que todos los tiempos son a lo sumo 30 000. C++
necesita 0.001 s en lugar de 0.109 s y 164 KB en lugar de 304 KB; Rust,
276 KB en lugar de 4176 KB, con el mismo tiempo.

La solución optimizada en Python lee la entrada en bloques de 16 KB y la
analiza a medida que la necesita, y guarda los inicios más tardíos en un
`array` de números de 16 bits en lugar de una lista: 980 KB en lugar de
14476 KB, aunque el tiempo sube de 0.109 s a 0.140 s.

## Notas por lenguaje

Ningún lenguaje necesita nada especial.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1203_greedy.cpp](1203_greedy.cpp) | G++ 13.2 x64 | greedy | O(N + T) | AC | 0.109 s | 304 KB | 11283566 |
| [1203_greedy.go](1203_greedy.go) | Go 1.14 x64 | greedy | O(N + T) | AC | 0.125 s | 4420 KB | 11303282 |
| [1203_greedy.java](1203_greedy.java) | Java 1.8 | greedy | O(N + T) | AC | 0.109 s | 620 KB | 11303457 |
| [1203_greedy.py](1203_greedy.py) | Python 3.12 x64 | greedy | O(N + T) | AC | 0.109 s | 14476 KB | 11283574 |
| [1203_greedy.rs](1203_greedy.rs) | Rust 1.75 x64 | greedy | O(N + T) | AC | 0.015 s | 4176 KB | 11283580 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1203_greedy_optimized.cpp](1203_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(N + T) | AC | 0.001 s | 164 KB | 11303579 |
| [1203_greedy_optimized.py](1203_greedy_optimized.py) | Python 3.12 x64 | greedy | O(N + T) | AC | 0.140 s | 980 KB | 11303723 |
| [1203_greedy_optimized.rs](1203_greedy_optimized.rs) | Rust 1.75 x64 | greedy | O(N + T) | AC | 0.031 s | 276 KB | 11303580 |
