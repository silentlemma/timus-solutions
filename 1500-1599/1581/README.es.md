# 1581. Trabajo en equipo

[Timus 1581](https://acm.timus.ru/problem.aspx?space=1&num=1581) · dificultad 41 · implementation

Problema original de Alex Samsonov, del USU Junior Contest (XIV Campeonato Abierto por Equipos de Programación para Escolares de la Región de Sverdlovsk), octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una secuencia de N ≤ 1000 números del 1 al 10 se dicta por tramos: para
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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1581_implementation.cpp](1581_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 196 KB |
| [1581_implementation.go](1581_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.031 s | 1268 KB |
| [1581_implementation.java](1581_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.125 s | 2404 KB |
| [1581_implementation.py](1581_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.078 s | 404 KB |
| [1581_implementation.rs](1581_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 328 KB |
