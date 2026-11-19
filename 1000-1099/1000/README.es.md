# 1000. Suma de dos enteros

[Timus 1000](https://acm.timus.ru/problem.aspx?space=1&num=1000) · dificultad 16 · math

Problema original de Pavel Atnashev.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan dos enteros `a` y `b`. Imprime su suma `a + b`.

El problema original no indica cotas para `a` y `b`; en las soluciones con
enteros de tamaño fijo, ambos operandos y su suma deben caber en un entero
con signo de 64 bits.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Dos enteros `a` y `b`, separados por espacios en blanco (un espacio o un salto
de línea).

## Salida

Un entero: `a + b`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3
```

Salida:

```
5
```

### Ejemplo 2

Entrada:

```
2000000000 2000000000
```

Salida:

```
4000000000
```

## Solución

Leer los dos números e imprimir su suma. Tiempo y memoria `O(1)`.

Detalles a tener en cuenta:

- la suma de dos valores que caben en 32 bits puede no caber en 32 bits, por eso
  se usa un tipo de 64 bits para los operandos y el resultado;
- los números se leen como tokens separados por espacios en blanco, así que da
  igual si están en una línea o en dos.

## Soluciones optimizadas

`1000_math_optimized.go`. Sigue sumando dos operandos int64 con espacio constante. Buffers acotados de entrada de 256 bytes y salida de 64 usan syscall.Read/Write de Go 1.14, reintentan EINTR/escrituras parciales y tratan EOF de cero bytes. Elimina inicialización fmt/bufio/os.File. Pruebas Linux y compilación cruzada Windows validan funcionamiento y construcción; las métricas pareadas siguientes vienen de nuestro Accepted exacto en juez Windows. Se conserva fuente didáctica legible.

Frente a `1000_math.go`: tiempo 0.015 s → 0.001 s; memoria 1060 KB → 256 KB.

La solución optimizada en Java analiza los dos números byte a byte desde
`System.in` en lugar de usar `Scanner`: 0.046 s en lugar de 0.078 s y
336 KB en lugar de 1548 KB.

La nueva versión de Python lee bytes sin decodificar toda la entrada,
vacía explícitamente la salida y termina sin la limpieza normal del intérprete.
Su propio envío Accepted tarda 0.046 s frente a 0.078 s de la versión sencilla:
reduce el tiempo un 41.0%, aunque la memoria sube de 132 KB a 656 KB.
Se conserva también la base breve y legible. La variante de Rust analiza e
imprime enteros con signo mediante el entorno de C, sin cadenas de entrada
o salida ni formato de Rust: baja de 228 KB a 52 KB, un 77.2% menos.
Ambas mantienen la suma y el espacio auxiliar constante. La nueva fila de
Python lleva asterisco porque no alcanza la meta de clasificación más estricta
del lenguaje; se admite por su mejora de tiempo.

## Notas por lenguaje

- **C++**: `long long` y `scanf("%lld %lld")`.
- **Go**: `int64` con `fmt.Scan`, que omite cualquier espacio en blanco.
- **Python**: los enteros tienen precisión arbitraria; leer todos los tokens con
  `sys.stdin.read().split()` funciona con cualquier distribución en líneas.
- **Java**: la solución sencilla usa `long` y `Scanner`.
- **Rust**: leer toda la entrada en un `String`, dividirla por espacios en blanco
  y convertir a `i64`.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1000_math.cpp](1000_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 124 KB | 11303840 |
| [1000_math.go](1000_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1060 KB | 11277409 |
| [1000_math.java](1000_math.java) | Java 1.8 | math | O(1) | AC | 0.078 s | 1548 KB | 11277412 |
| [1000_math.py](1000_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 132 KB | 11277410 |
| [1000_math.rs](1000_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.001 s | 228 KB | 11303841 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1000_math_optimized.java](1000_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.046 s | 336 KB | 11303693 |
| [1000_math_optimized.py](1000_math_optimized.py) \* | Python 3.12 x64 | math | O(1) | AC | 0.046 s | 656 KB | 11324875 |
| [1000_math_optimized.rs](1000_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.001 s | 52 KB | 11324851 |
| [1000_math_optimized.go](1000_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.001 s | 256 KB | 11325648 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
