# 1644. Un montón de nueces

[Timus 1644](https://acm.timus.ru/problem.aspx?space=1&num=1644) · dificultad 100 · implementation

Problema original de Alexey Samsonov, del USU Junior Contest, octubre de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En cada uno de n experimentos el loro comió entre 3 y 9 nueces y anotó
si seguía con hambre o quedó satisfecho. La saciedad es monótona: más
nueces nunca dejan más hambre. Se sabe que diez nueces siempre bastan y
dos nunca. Hay que hallar el menor número de nueces que seguro basta, o
decir que las anotaciones se contradicen.

## Entrada

n (0 ≤ n ≤ 100) y luego n líneas: un número de nueces y `hungry` o
`satisfied`.

## Salida

El menor número de nueces que seguro basta, o `Inconsistent`.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
4 hungry
7 satisfied
5 hungry
8 satisfied
```

Salida:

```
7
```

### Ejemplo 2

Entrada:

```
2
6 hungry
5 satisfied
```

Salida:

```
Inconsistent
```

## Solución

Se toma la mayor cantidad con hambre, empezando en 2, y la menor
cantidad satisfecha, empezando en 10. Las anotaciones encajan con un
umbral monótono exactamente cuando la segunda es mayor; entonces la
respuesta es la menor cantidad satisfecha, pues nada menor se ha visto
saciar. Si no, `Inconsistent`. `O(n)`.

Detalles a tener en cuenta:

- sin anotaciones la respuesta es 10 (prueba 03), y con solo anotaciones
  de hambre sigue siendo 10 (prueba 04);
- la misma cantidad anotada de las dos maneras es una contradicción
  (prueba 06).

Las respuestas coinciden con una implementación aceptada independiente
en 180 conjuntos aleatorios de anotaciones.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1644_implementation.cpp](1644_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 392 KB |
| [1644_implementation.go](1644_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1084 KB |
| [1644_implementation.java](1644_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 1708 KB |
| [1644_implementation.py](1644_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.109 s | 444 KB |
| [1644_implementation.rs](1644_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 220 KB |
