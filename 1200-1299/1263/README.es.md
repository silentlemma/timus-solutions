# 1263. Elecciones

[Timus 1263](https://acm.timus.ru/problem.aspx?space=1&num=1263) · dificultad 43 · implementation

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

## Notas por lenguaje

- C++, Go, Python y Rust formatean el double directamente; los cuatro
  redondean el valor exacto del double con la mitad al par.
- `String.format` de Java redondea la mitad hacia arriba, así que Java
  toma un `BigDecimal` del mismo double y lo redondea con `HALF_EVEN`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1263_implementation.cpp](1263_implementation.cpp) | G++ 13.2 x64 | implementation | O(N + M) | AC | 0.031 s | 252 KB |
| [1263_implementation.go](1263_implementation.go) | Go 1.14 x64 | implementation | O(N + M) | AC | 0.031 s | 1456 KB |
| [1263_implementation.java](1263_implementation.java) | Java 1.8 | implementation | O(N + M) | AC | 0.156 s | 5696 KB |
| [1263_implementation.py](1263_implementation.py) | Python 3.12 x64 | implementation | O(N + M) | AC | 0.078 s | 1948 KB |
| [1263_implementation.rs](1263_implementation.rs) | Rust 1.75 x64 | implementation | O(N + M) | AC | 0.015 s | 468 KB |
