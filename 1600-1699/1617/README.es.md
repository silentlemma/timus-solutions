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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1617_implementation.cpp](1617_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB |
| [1617_implementation.go](1617_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1092 KB |
| [1617_implementation.java](1617_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 1680 KB |
| [1617_implementation.py](1617_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.093 s | 368 KB |
| [1617_implementation.rs](1617_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 244 KB |
