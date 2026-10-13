# 1440. Horario de entrenamientos

[Timus 1440](https://acm.timus.ru/problem.aspx?space=1&num=1440) · dificultad 668 · bruteforce

Problema original de Ekaterina Vasilyeva (idea y texto) y Stanislav Vasiliev (programación), del Décimo Campeonato Universitario de Programación por Equipos de los Urales, 24–25 de marzo de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El equipo de quidditch de Gryffindor entrena en días fijos de la semana,
por ejemplo todos los viernes y domingos. Se puede entrenar desde el 2
de septiembre hasta el día anterior al primer partido, y el partido es
entre el 2 de septiembre y el 24 de diciembre. Debe haber de A a B
entrenamientos (1 ≤ A ≤ B ≤ 200). Dado el día de la semana del 1 de
septiembre y la fecha del partido, hay que elegir un conjunto de días de
la semana que dé ese número de entrenamientos, o indicar que no existe.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

El día de la semana del 1 de septiembre en inglés, la fecha del partido
como «Month Day», y A y B.

## Salida

«Impossible», o el número de días de la semana elegidos seguido de sus
nombres, uno por línea, en cualquier orden. Se acepta cualquier conjunto
válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
Thursday
September 10
9 20
```

Salida:

```
Impossible
```

### Ejemplo 2

Entrada:

```
Tuesday
October 7
12 14
```

Salida:

```
Impossible
```

### Ejemplo 3

Entrada:

```
Friday
October 4
12 14
```

Salida:

```
3
Monday
Wednesday
Saturday
```

## Solución

Se cuenta cuántos días de entrenamiento caen en cada día de la semana:
se recorren los días desde el 2 de septiembre hasta la víspera del
partido, como mucho 113, sumando uno al día de la semana de cada uno. Un
conjunto de días de la semana da la suma de sus contadores, y solo hay
127 conjuntos no vacíos, así que se prueban todos y se imprime el
primero cuya suma esté entre A y B. `O(D + 2⁷ · 7)` con D días antes del
partido.

Detalles a tener en cuenta:

- un partido el 2 de septiembre no deja ningún día de entrenamiento
  (prueba 04);
- 200 entrenamientos nunca caben antes de Navidad (prueba 05);
- a veces solo vale un conjunto, o hacen falta los siete días (pruebas
  06, 09, 10, 13);
- los meses tienen longitudes distintas: el 30 de septiembre y el 1 de
  octubre son días vecinos (pruebas 11, 12).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1440_bruteforce.cpp](1440_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(D + 2^7 · 7) | AC | 0.015 s | 404 KB |
| [1440_bruteforce.go](1440_bruteforce.go) | Go 1.14 x64 | bruteforce | O(D + 2^7 · 7) | AC | 0.031 s | 1164 KB |
| [1440_bruteforce.java](1440_bruteforce.java) | Java 1.8 | bruteforce | O(D + 2^7 · 7) | AC | 0.109 s | 1708 KB |
| [1440_bruteforce.py](1440_bruteforce.py) | Python 3.12 x64 | bruteforce | O(D + 2^7 · 7) | AC | 0.078 s | 428 KB |
| [1440_bruteforce.rs](1440_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(D + 2^7 · 7) | AC | 0.031 s | 220 KB |
