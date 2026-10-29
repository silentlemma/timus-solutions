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

## Soluciones optimizadas

Las tres especies empiezan por mayúsculas distintas, E, L y M, y ni la
palabra «Penguin» ni el número `N` contienen ninguna de ellas, así que
basta con contar esas letras en toda la entrada y elegir la cuenta
mayor. La solución optimizada en C++ no lee ninguna palabra y cuenta las
letras con `getchar`, imprimiendo la respuesta con `puts` en lugar de
`iostream`: 88 KB en lugar de 388 KB, con el mismo tiempo. La solución
optimizada en Java las cuenta mientras lee bloques de 256 bytes: 0.109 s
en lugar de 0.171 s y 328 KB en lugar de 4576 KB.

La solución optimizada en Python cuenta los nombres completos en los
bytes crudos con `bytes.count`: 348 KB en lugar de 512 KB, con el mismo
tiempo.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1585_implementation.cpp](1585_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 388 KB | 11287935 |
| [1585_implementation.go](1585_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1132 KB | 11287937 |
| [1585_implementation.java](1585_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.171 s | 4576 KB | 11287943 |
| [1585_implementation.py](1585_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.062 s | 512 KB | 11287941 |
| [1585_implementation.rs](1585_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 440 KB | 11287944 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1585_implementation_optimized.cpp](1585_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 88 KB | 11303626 |
| [1585_implementation_optimized.java](1585_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.109 s | 328 KB | 11303761 |
| [1585_implementation_optimized.py](1585_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(N) | AC | 0.078 s | 348 KB | 11303762 |

\* No está entre las 10 mejores ni en el 15% mejor de las soluciones de
su lenguaje en el juez actual; quizá se pueda optimizar más.
