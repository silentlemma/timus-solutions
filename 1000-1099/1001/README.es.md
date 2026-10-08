# 1001. Raíces cuadradas en orden inverso

[Timus 1001](https://acm.timus.ru/problem.aspx?space=1&num=1001) · dificultad 14 · math

Problema original preparado por Dmitry Kovalev.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La entrada es una secuencia de enteros `A1, A2, ..., An` con `0 ≤ Ai ≤ 10^18`.
Imprime sus raíces cuadradas en orden inverso: primero `√An`, al final `√A1`.

La cantidad `n` no se indica: los números siguen hasta el final de la entrada,
cuyo tamaño total es como máximo 256 KB (así que `n` es como mucho unos 131 000).

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

Los enteros `Ai`, separados por cualquier cantidad de espacios y saltos de
línea (incluidas líneas vacías).

## Salida

`n` líneas: `√An, √An-1, ..., √A1`, una por línea, cada una con al menos cuatro
cifras después del punto decimal.

## Evaluación

Cada número impreso debe estar a no más de `10^-4` de la raíz cuadrada exacta
(error absoluto, o relativo para valores grandes).

## Ejemplos

### Ejemplo 1

Entrada:

```
  16   2

 1000000000000000000   
0
```

Salida:

```
0.0000
1000000000.0000
1.4142
4.0000
```

### Ejemplo 2

Entrada:

```
7
```

Salida:

```
2.6458
```

## Solución

Leer todos los números hasta el final de la entrada en un arreglo, luego
recorrerlo al revés e imprimir `sqrt(Ai)` con cuatro decimales. Tiempo y
memoria `O(n)`.

La raíz en doble precisión es suficientemente exacta: al convertir un valor de
hasta `10^18` a double el error relativo es como mucho `2^-53`, así que la raíz
(como mucho `10^9`) difiere en menos de `10^-6`, muy por debajo del `10^-4`
permitido.

Detalles a tener en cuenta:

- la cantidad no se indica, así que hay que leer hasta el final de la entrada;
- los separadores son arbitrarios: varios espacios, saltos de línea, líneas vacías;
- los valores no caben en 32 bits: hay que usar enteros de 64 bits;
- hasta unas 131 000 líneas de salida: la salida debe ir con búfer.

## Notas por lenguaje

- **C++**: `scanf("%llu")` en un bucle, `printf("%.4f\n")`.
- **Go**: un analizador byte a byte sobre `bufio.Reader` y `strconv.AppendFloat`
  en un `bufio.Writer`; llamar a `fmt.Printf` por cada línea es lento.
- **Python**: leer toda la entrada con `sys.stdin.buffer.read().split()`, armar
  todas las líneas y escribirlas con un solo `join`.
- **Java**: analizar los números desde un búfer de bytes y acumular la salida en
  un `StringBuilder`; formatear con `Locale.US`, de lo contrario el separador
  decimal podría ser una coma.
- **Rust**: leer toda la entrada en un `String`, convertir a `u64` y formatear
  con `{:.4}` en una sola cadena de salida.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1001_math.cpp](1001_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.125 s | 1576 KB |
| [1001_math.go](1001_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 5056 KB |
| [1001_math.java](1001_math.java) | Java 1.8 | math | O(n) | AC | 0.453 s | 11412 KB |
| [1001_math.py](1001_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.125 s | 11492 KB |
| [1001_math.rs](1001_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.046 s | 3096 KB |
