# 1349. Granja

[Timus 1349](https://acm.timus.ru/problem.aspx?space=1&num=1349) · dificultad 51 · math

Problema original atribuido a Pierre Fermat, del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dado n, 0 ≤ n ≤ 100, hay que hallar tres enteros distintos a, b, c de 1
a 100 con aⁿ + bⁿ = cⁿ, el de menor a, luego menor b y luego menor c, o
imprimir −1 si no hay ninguno.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número n.

## Salida

a, b y c, o −1.

## Ejemplos

### Ejemplo 1

Entrada:

```
0
```

Salida:

```
-1
```

### Ejemplo 2

Entrada:

```
1
```

Salida:

```
1 2 3
```

## Solución

- n = 0: toda potencia vale 1, y 1 + 1 nunca es 1, así que no hay
  respuesta.
- n = 1: a + b = c, y la menor elección con tres números distintos es
  1 2 3.
- n = 2: la menor terna pitagórica, 3 4 5, es la primera en el orden
  pedido.
- n ≥ 3: por el último teorema de Fermat, aⁿ + bⁿ = cⁿ no tiene solución
  en enteros positivos.

`O(1)`.

Detalles a tener en cuenta:

- n = 0 no tiene respuesta aunque todas las potencias sean iguales
  (prueba 01);
- los números deben ser distintos, lo que descarta respuestas como
  1 1 2 para n = 1.

Una búsqueda sobre todas las ternas hasta 100 para n de 0 a 5 dio las
mismas respuestas.

## Notas por lenguaje

- Las cinco soluciones imprimen los tres casos directamente.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1349_math.cpp](1349_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 124 KB |
| [1349_math.go](1349_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1064 KB |
| [1349_math.java](1349_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1612 KB |
| [1349_math.py](1349_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 336 KB |
| [1349_math.rs](1349_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.062 s | 232 KB |
