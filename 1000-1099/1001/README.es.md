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

Cada raíz cuadrada debe imprimirse con al menos cuatro cifras después del
punto decimal.

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
(cuatro decimales).

Detalles a tener en cuenta:

- la cantidad no se indica, así que hay que leer hasta el final de la entrada;
- los separadores son arbitrarios: varios espacios, saltos de línea, líneas vacías;
- los valores no caben en 32 bits: hay que usar enteros de 64 bits;
- hasta unas 131 000 líneas de salida: la salida debe ir con búfer.

## Soluciones optimizadas

Las soluciones optimizadas (C++, Go, Java, Rust) guardan la entrada como
texto y no como un arreglo de números. C++, Go y Java la leen en un solo
búfer y analizan los números desde el final hacia atrás, que es justo el
orden de la salida; Rust recorre los tokens del texto al revés. La raíz se
imprime a mano: se multiplica por `10^4`, se redondea y se escribe como
parte entera y cuatro cifras de la parte fraccionaria, sin el lento
formateo de números de coma flotante. En lugar de un arreglo de hasta
131 000 números, en memoria quedan solo los 256 KB de la entrada. C++:
0.031 s en lugar de 0.125 s y 356 KB en lugar de 1576 KB; Go: 0.015 s en
lugar de 0.125 s y 1180 KB en lugar de 6588 KB; Java: 0.125 s en lugar
de 0.593 s y 872 KB en lugar de 11728 KB; Rust: 0.015 s en lugar de
0.046 s y 464 KB en lugar de 3072 KB.

La solución optimizada en Python escribe las respuestas por bloques
desde el final de la entrada: corta unos 4 KB de números cada vez, en un
separador, así que nunca construye a la vez la lista de todas las
raíces: 2052 KB en lugar de 11492 KB, aunque el tiempo sube de 0.125 s a
0.156 s.

## Notas por lenguaje

- **C++**: la solución simple usa `scanf("%llu")` en un bucle y
  `printf("%.4f\n")`.
- **Go**: la solución simple lee con `fmt.Fscan` sobre un `bufio.Reader`
  y escribe con `fmt.Fprintf` en un `bufio.Writer`; llamar a
  `fmt.Printf` sobre la salida sin búfer por cada línea es lento.
- **Python**: la solución simple lee toda la entrada con
  `sys.stdin.buffer.read().split()`, arma todas las líneas y las escribe con
  un solo `join`.
- **Java**: la solución simple lee con `BufferedReader` y
  `StringTokenizer` y acumula la salida en un `StringBuilder`; formatea
  con `Locale.US`, de lo contrario el separador decimal podría ser una
  coma.
- **Rust**: la solución simple lee toda la entrada en un `String`,
  convierte a `u64` y formatea con `{:.4}` en una sola cadena de salida.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1001_math.cpp](1001_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.125 s | 1576 KB | 11277417 |
| [1001_math.go](1001_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.125 s | 6588 KB | 11303052 |
| [1001_math.java](1001_math.java) | Java 1.8 | math | O(n) | AC | 0.593 s | 11728 KB | 11303054 |
| [1001_math.py](1001_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.125 s | 11492 KB | 11277419 |
| [1001_math.rs](1001_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.046 s | 3072 KB | 11303271 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1001_math_optimized.cpp](1001_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.031 s | 356 KB | 11303536 |
| [1001_math_optimized.go](1001_math_optimized.go) | Go 1.14 x64 | math | O(n) | AC | 0.015 s | 1180 KB | 11303537 |
| [1001_math_optimized.java](1001_math_optimized.java) | Java 1.8 | math | O(n) | AC | 0.125 s | 872 KB | 11303449 |
| [1001_math_optimized.py](1001_math_optimized.py) | Python 3.12 x64 | math | O(n) | AC | 0.156 s | 2052 KB | 11303694 |
| [1001_math_optimized.rs](1001_math_optimized.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.015 s | 464 KB | 11303538 |
