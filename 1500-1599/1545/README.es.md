# 1545. Jeroglíficos

[Timus 1545](https://acm.timus.ru/problem.aspx?space=1&num=1545) · dificultad 50 · implementation

Problema original de Evgeny Krokhalev, del XI Campeonato Universitario por Equipos de Programación de los Urales, Ekaterimburgo, 21 de abril de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un diccionario contiene N ≤ 1000 jeroglíficos, cada uno escrito con dos
letras minúsculas. Dada una letra tecleada, hay que escribir los
jeroglíficos que empiezan por ella.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, las N entradas de dos letras y luego la letra.

## Salida

Las entradas que coinciden, una por línea, en cualquier orden; nada si
no hay ninguna.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
na
no
ni
ki
ka
ku
k
```

Salida:

```
ka
ki
ku
```

## Solución

Se compara la primera letra de cada entrada con la tecleada y se
escriben las coincidencias en el orden de entrada. `O(N)`.

Detalles a tener en cuenta:

- sin coincidencias la salida queda vacía (pruebas 02, 05);
- una entrada que aparece dos veces se escribe dos veces (prueba 03);
- la letra debe ir primero: una coincidencia en el segundo lugar no
  cuenta (prueba 05).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1545_implementation.cpp](1545_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 392 KB |
| [1545_implementation.go](1545_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.031 s | 1104 KB |
| [1545_implementation.java](1545_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 1804 KB |
| [1545_implementation.py](1545_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 460 KB |
| [1545_implementation.rs](1545_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.046 s | 236 KB |
