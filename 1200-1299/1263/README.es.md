# 1263. Elecciones

[Timus 1263](https://acm.timus.ru/problem.aspx?space=1&num=1263) · dificultad 42 · implementation

Problema original de Den Raskovalov, de la Competición Abierta por Equipos de Programación para Escolares de la Región de Sverdlovsk, 11 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N candidaturas (1 ≤ N ≤ 10 000) y M votantes (1 ≤ M ≤ 10 000); cada
votante elige una candidatura. Para cada una, hay que imprimir su parte
de los votos en porcentaje, con dos cifras tras el punto y el signo `%`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, luego M números de candidatura del 1 al N.

## Salida

N líneas con los porcentajes.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 6
1
2
3
2
1
1
```

Salida:

```
50.00%
33.33%
16.67%
```

## Solución

Se cuentan los votos de cada candidatura y se imprime 100 · votos / M
con dos decimales. `O(N + M)`.

Detalles a tener en cuenta:

- las candidaturas sin votos también tienen su línea, `0.00%`
  (prueba 03);
- una parte puede terminar justo en la mitad de la última cifra
  impresa, como 1/32 = 3.125% (pruebas 04, 05). Estas soluciones
  redondean esos empates al par, como `printf` en C: 3.12%;
- imprimir línea a línea es lento en algunos lenguajes con N = 10 000:
  conviene juntar la salida primero.

## Soluciones optimizadas

La solución optimizada en Python lee los votos línea a línea mediante un
generador en lugar de partir toda la entrada de una vez, y formatea el
porcentaje de cada cantidad distinta de votos una sola vez: los
candidatos con la misma cantidad comparten la línea ya formateada. Las
líneas salen una a una por el `sys.stdout.write` con búfer en lugar de
unirse antes: 856 KB en lugar de 1948 KB, con el mismo tiempo.

La solución optimizada en C++ analiza los números con `getchar` en lugar
de `scanf` y cuenta los votos en un arreglo fijo de contadores de 16
bits: 128 KB en lugar de 252 KB, con el mismo tiempo. La solución
optimizada en Rust analiza los números a mano desde los bytes de
`stdin().lock()` en lugar de leer toda la entrada en una cadena, cuenta
con contadores de 16 bits y escribe a través de un búfer de 1 KB: 252 KB
en lugar de 468 KB, con el mismo tiempo.

## Notas por lenguaje

- C++, Go, Python y Rust formatean el double directamente; los cuatro
  redondean el valor exacto del double con la mitad al par.
- `String.format` de Java redondea la mitad hacia arriba, así que Java
  toma un `BigDecimal` del mismo double y lo redondea con `HALF_EVEN`.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1263_implementation.cpp](1263_implementation.cpp) | G++ 13.2 x64 | implementation | O(N + M) | AC | 0.031 s | 252 KB | 11284152 |
| [1263_implementation.go](1263_implementation.go) | Go 1.14 x64 | implementation | O(N + M) | AC | 0.031 s | 1456 KB | 11284153 |
| [1263_implementation.java](1263_implementation.java) | Java 1.8 | implementation | O(N + M) | AC | 0.156 s | 5696 KB | 11284158 |
| [1263_implementation.py](1263_implementation.py) | Python 3.12 x64 | implementation | O(N + M) | AC | 0.078 s | 1948 KB | 11284154 |
| [1263_implementation.rs](1263_implementation.rs) | Rust 1.75 x64 | implementation | O(N + M) | AC | 0.015 s | 468 KB | 11284161 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1263_implementation_optimized.cpp](1263_implementation_optimized.cpp) \* | G++ 13.2 x64 | implementation | O(N + M) | AC | 0.031 s | 128 KB | 11303730 |
| [1263_implementation_optimized.py](1263_implementation_optimized.py) | Python 3.12 x64 | implementation | O(N + M) | AC | 0.078 s | 856 KB | 11303586 |
| [1263_implementation_optimized.rs](1263_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(N + M) | AC | 0.015 s | 252 KB | 11303731 |

\* No está entre las 10 mejores ni en el 15% mejor de las soluciones de
su lenguaje en el juez actual; quizá se pueda optimizar más.
