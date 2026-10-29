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

## Soluciones optimizadas

La solución optimizada en C++ guarda las entradas de dos letras en un
arreglo local de cadenas C de tres bytes en lugar de `std::string`,
leídas con `scanf("%2s")` e impresas con `puts`: 120 KB en lugar de
392 KB, con el mismo tiempo.

Cada jeroglífico son dos letras. La solución optimizada en Java los
guarda en arreglos de bytes llenados desde bloques de 256 bytes y
escribe la respuesta desde un solo arreglo de bytes, sin `Scanner` ni
cadenas: 392 KB en lugar de 1804 KB, con el mismo tiempo. La solución
optimizada en Rust guarda cada jeroglífico como un par de bytes y
escribe con un `BufWriter` de búfer pequeño: 0.015 s en lugar de 0.046 s
y 196 KB en lugar de 236 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1545_implementation.cpp](1545_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 392 KB | 11287555 |
| [1545_implementation.go](1545_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.031 s | 1104 KB | 11287556 |
| [1545_implementation.java](1545_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 1804 KB | 11287558 |
| [1545_implementation.py](1545_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 460 KB | 11287557 |
| [1545_implementation.rs](1545_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.046 s | 236 KB | 11287559 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1545_implementation_optimized.cpp](1545_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 120 KB | 11303617 |
| [1545_implementation_optimized.java](1545_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.109 s | 392 KB | 11303759 |
| [1545_implementation_optimized.rs](1545_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 196 KB | 11303760 |
