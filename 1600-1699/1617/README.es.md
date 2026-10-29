# 1617. Planos en las ruedas

[Timus 1617](https://acm.timus.ru/problem.aspx?space=1&num=1617) · dificultad 65 · implementation

Problema original de Vladimir Yakovlev, del XII Campeonato de los Urales de Programación Competitiva, 29 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un depósito tiene n pares de ruedas (1 ≤ n ≤ 150), cada uno con un
diámetro entero de 600 a 700 mm. Un vagón de tranvía necesita cuatro
pares de ruedas del mismo diámetro. ¿Cuántos vagones se pueden equipar?

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

n, luego los n diámetros.

## Salida

El número de vagones.

## Ejemplos

### Ejemplo 1

Entrada:

```
9
689
690
690
689
689
690
689
688
688
```

Salida:

```
1
```

## Solución

Contamos los pares de cada diámetro. Un diámetro con c pares equipa
⌊c / 4⌋ vagones, y los diámetros no interactúan, así que la respuesta es
la suma sobre todos ellos. `O(n)`.

Detalles a tener en cuenta:

- los pares sobrantes de diámetros distintos no se pueden combinar
  (prueba 01);
- ocho pares de un mismo tamaño equipan dos vagones, no uno (prueba 03).

## Soluciones optimizadas

La solución optimizada en Java lee la entrada en bloques de 1 KB y la
analiza a mano en lugar de usar `Scanner`, y cuenta los diámetros, de
600 a 700, en un arreglo simple de 101 contadores con un desplazamiento
de 600: 0.109 s en lugar de 0.140 s y 336 KB en lugar de 1680 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1617_implementation.cpp](1617_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB | 11288341 |
| [1617_implementation.go](1617_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1092 KB | 11288342 |
| [1617_implementation.java](1617_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 1680 KB | 11288344 |
| [1617_implementation.py](1617_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.093 s | 368 KB | 11288343 |
| [1617_implementation.rs](1617_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 240 KB | 11303771 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1617_implementation_optimized.java](1617_implementation_optimized.java) | Java 1.8 | implementation | O(n) | AC | 0.109 s | 336 KB | 11303764 |
