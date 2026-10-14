# 1585. Pingüinos

[Timus 1585](https://acm.timus.ru/problem.aspx?space=1&num=1585) · dificultad 38 · implementation

Problema original de Vladimir Yakovlev, de la subregión oriental del NEERC del ACM ICPC 2007–2008, Ekaterimburgo, 27 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un cuaderno anota N ≤ 1000 pingüinos, cada uno como «Emperor Penguin»,
«Little Penguin» o «Macaroni Penguin». Hay que imprimir la especie que
aparece más veces; es única.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego una especie por línea.

## Salida

La especie más frecuente.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
Emperor Penguin
Macaroni Penguin
Little Penguin
Emperor Penguin
Macaroni Penguin
Macaroni Penguin
Little Penguin
```

Salida:

```
Macaroni Penguin
```

## Solución

Se cuentan las anotaciones por su primera palabra y se imprime la
especie con la cuenta mayor, seguida de «Penguin». `O(N)`.

Detalles a tener en cuenta:

- cada anotación tiene un espacio dentro, así que se lee como línea
  entera o como dos palabras;
- puede faltar alguna especie por completo (prueba 03).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1585_implementation.cpp](1585_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 388 KB |
| [1585_implementation.go](1585_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1132 KB |
| [1585_implementation.java](1585_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.171 s | 4576 KB |
| [1585_implementation.py](1585_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 512 KB |
| [1585_implementation.rs](1585_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 440 KB |
