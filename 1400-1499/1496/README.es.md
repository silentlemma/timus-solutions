# 1496. El spammer

[Timus 1496](https://acm.timus.ru/problem.aspx?space=1&num=1496) · dificultad 49 · implementation

Problema original de Sergey Pupyrev, del Decimotercer Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 14 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En los últimos 10 minutos de un concurso llegaron N envíos
(0 ≤ N ≤ 100), cada uno de un equipo con un nombre de hasta 30 letras
minúsculas y cifras. Hay que escribir, en cualquier orden, todos los
equipos que enviaron más de una vez.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego N nombres de equipo.

## Salida

Los equipos con más de un envío, uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
11
naucoder
iceman
abikbaev
abikbaev
petr
abikbaev
abikbaev
x
abikbaev
acrush
x
```

Salida:

```
x
abikbaev
```

## Solución

Se cuentan los envíos de cada equipo en un diccionario y se escriben
los equipos con más de uno, cada uno una vez. Conservar el orden de
primera aparición no es obligatorio, pero hace la salida estable.
C++: `O(N log N)`; los demás: `O(N)` en promedio.

Detalles a tener en cuenta:

- un equipo que envió muchas veces se escribe una sola vez (prueba 01);
- los nombres son texto, así que «0» y «00» son equipos distintos
  (prueba 04);
- si ningún equipo se repite, la salida queda vacía (pruebas 02, 03,
  05).

## Soluciones optimizadas

Las soluciones optimizadas (C++, Java) no guardan la lista de primeras
apariciones: un equipo entra en la respuesta en cuanto se lee su segundo
envío. C++ lo imprime en ese momento; Java lo añade a un `StringBuilder`
e imprime toda la respuesta al final. El orden de la salida difiere del
de las soluciones sencillas, lo que el enunciado permite.

La solución optimizada en C++ lee los nombres con `scanf` en un búfer de
31 bytes en lugar de `iostream`: 184 KB en lugar de 412 KB, con el mismo
tiempo. La solución optimizada en Java lee la entrada en bloques de
256 bytes y separa a mano cada nombre de equipo, de a lo sumo 30
caracteres, en lugar de usar `Scanner`: 0.093 s en lugar de 0.156 s y
428 KB en lugar de 3944 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1496_implementation.cpp](1496_implementation.cpp) | G++ 13.2 x64 | implementation | O(N log N) | AC | 0.015 s | 412 KB | 11287227 |
| [1496_implementation.go](1496_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1116 KB | 11287228 |
| [1496_implementation.java](1496_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.156 s | 3944 KB | 11287230 |
| [1496_implementation.py](1496_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 336 KB | 11287229 |
| [1496_implementation.rs](1496_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.031 s | 412 KB | 11287231 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1496_implementation_optimized.cpp](1496_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N log N) | AC | 0.015 s | 184 KB | 11303613 |
| [1496_implementation_optimized.java](1496_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 428 KB | 11303755 |
