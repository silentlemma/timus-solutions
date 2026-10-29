# 1581. Trabajo en equipo

[Timus 1581](https://acm.timus.ru/problem.aspx?space=1&num=1581) · dificultad 41 · implementation

Problema original de Alex Samsonov, del USU Junior Contest (XIV Campeonato Abierto por Equipos de Programación para Escolares de la Región de Sverdlovsk), octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una secuencia de 1 ≤ N ≤ 1000 números del 1 al 10 se dicta por tramos: para
cada tramo de números iguales se dice primero cuántos hay y luego qué
número es. Hay que imprimir los números dictados.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego los N números.

## Salida

Las longitudes y los valores de los tramos, en orden, en una línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
8
1 1 2 3 3 3 10 10
```

Salida:

```
2 1 1 2 3 3 2 10
```

## Solución

Se recorren los números y se cortan en tramos máximos de valores
iguales; de cada tramo se imprimen su longitud y luego su valor. `O(N)`.

Detalles a tener en cuenta:

- un tramo puede ser la secuencia entera, de hasta 1000 números
  (prueba 05);
- los números iguales que no son vecinos forman tramos distintos
  (prueba 04);
- 10 es un solo número, así que hay que leer números y no caracteres.

## Soluciones optimizadas

Las soluciones optimizadas (Java, Rust) no guardan los números: comparan
cada número con el anterior mientras leen y cierran una racha en cuanto
termina; Java la añade a un `StringBuilder` con toda la respuesta, Rust
la escribe en un `BufWriter`. Los números se analizan a mano, en Java
desde un búfer de 1 KB en lugar de `Scanner`, en Rust desde los bytes de
la entrada en lugar de partir un `String`. Java: 0.093 s en lugar de
0.125 s y 436 KB en lugar de 2404 KB; Rust: 208 KB en lugar de 308 KB,
con el mismo tiempo.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1581_implementation.cpp](1581_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 196 KB | 11287897 |
| [1581_implementation.go](1581_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.031 s | 1268 KB | 11287898 |
| [1581_implementation.java](1581_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.125 s | 2404 KB | 11287900 |
| [1581_implementation.py](1581_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 372 KB | 11303372 |
| [1581_implementation.rs](1581_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 308 KB | 11303373 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1581_implementation_optimized.java](1581_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 436 KB | 11303624 |
| [1581_implementation_optimized.rs](1581_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.031 s | 208 KB | 11303625 |
