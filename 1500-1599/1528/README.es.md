# 1528. Sucesión

[Timus 1528](https://acm.timus.ru/problem.aspx?space=1&num=1528) · dificultad 272 · math

Problema original de Dmitry Gozman, del Dmitry Gozman Contest 1 en el campus de invierno de Petrozavodsk, enero de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Con f(1) = g(1) = 1, f(n) = 1 + f(1)g(1) + … + f(n − 1)g(n − 1) y
g(n) = 1 + 2g(1) + … + 2g(n − 1) − g(n − 1)². Para hasta 5000 casos
(1 ≤ n ≤ 10000, 2 ≤ p ≤ 2·10⁹) hay que escribir f(n) mod p.

Límite de tiempo: 3 segundos. Límite de memoria: 64 MB.

## Entrada

Pares n y p, uno por línea, terminados en 0 0.

## Salida

f(n) mod p para cada caso.

## Evaluación

Se compara la salida completa, incluidos espacios y saltos de línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 2
2 11
0 0
```

Salida:

```
1
2
```

## Solución

Ambas sucesiones tienen forma cerrada. Si g(i) = i para i < n,
entonces g(n) = 1 + (n − 1)n − (n − 1)² = n. Así
f(n) − f(n − 1) = f(n − 1)·(n − 1), de modo que f(n) = n·f(n − 1) = n!.
Cada caso pide n! mod p. Si n ≥ p, el propio p es uno de los factores y
la respuesta es 0. Si no, se multiplica hasta n reduciendo módulo p;
los productos quedan por debajo de 2·10¹³, dentro de 64 bits. Son hasta
5·10⁷ multiplicaciones en total, rápido en lenguajes compilados (O(n) por caso). En
Python el bucle simple tarda unos 6 segundos, así que la solución en
Python guarda los factoriales exactos de cada múltiplo de 100 como
enteros grandes, reduce uno de ellos y multiplica como mucho 99
factores más: O(n log n) operaciones de bits por caso.

Detalles a tener en cuenta:

- las fórmulas parecen pesadas, pero g(n) = n y f(n) = n! (todas las
  pruebas);
- n ≥ p da 0 directamente (prueba 02, gen3);
- p llega a 2·10⁹, así que los productos necesitan 64 bits (prueba 03,
  gen1);
- un primo p justo por encima de n es una buena prueba: el teorema de
  Wilson da (p − 1)! ≡ −1 (prueba 05).

## Soluciones optimizadas

Tras reducir a factorial módulo el módulo pedido, las versiones nativas multiplican factores vecinos antes del resto. Las cotas garantizan un producto válido en 64 bits con signo, sin suponer primalidad ni inversos. Python calcula puntos de control exactos y productos cortos por bloques con multiplicación compilada de enteros grandes, reutilizando colas solo para argumentos iguales. Se calculan a partir de las cotas de entrada y no son constantes de respuestas. Ambas variantes conservan la prueba de la recurrencia factorial simple.

- `1528_math_optimized.cpp`: 0.203 s / 112 KB; base `1528_math.cpp`: 0.328 s / 132 KB; cambio respecto a la base: tiempo -38.1%, memoria -15.2%.
- `1528_math_optimized.go`: 0.218 s / 916 KB; base `1528_math.go`: 0.343 s / 1224 KB; cambio respecto a la base: tiempo -36.4%, memoria -25.2%.
- `1528_math_optimized.java`: 0.375 s / 840 KB; base `1528_math.java`: 0.609 s / 904 KB; cambio respecto a la base: tiempo -38.4%, memoria -7.1%.
- `1528_math_optimized.py`: 0.359 s / 1388 KB; base `1528_math.py`: 0.359 s / 17900 KB; cambio respecto a la base: tiempo -0.0%, memoria -92.2%.
- `1528_math_optimized.rs`: 0.156 s / 444 KB; base `1528_math.rs`: 0.250 s / 520 KB; cambio respecto a la base: tiempo -37.6%, memoria -14.6%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1528_math.cpp`; versión que cubre `1528_math_optimized.cpp`; puestos tiempo/memoria 3/1, registros de otros autores 58/58.

- Go: base didáctica preferida `1528_math.go`; versión que cubre `1528_math.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1528_math.java`; versión que cubre `1528_math_optimized.java`; puestos tiempo/memoria 1/1, registros de otros autores 4/4.

- Python/PyPy: base didáctica preferida `1528_math.py`; versión que cubre `1528_math_optimized.py`; puestos tiempo/memoria 3/1, registros de otros autores 5/5.

- Rust: base didáctica preferida `1528_math.rs`; versión que cubre `1528_math.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1528_math.cpp](1528_math.cpp) | G++ 13.2 x64 | math | O(n) per case | AC | 0.328 s | 132 KB | 11287420 |
| [1528_math.go](1528_math.go) | Go 1.14 x64 | math | O(n) per case | AC | 0.343 s | 1224 KB | 11287421 |
| [1528_math.java](1528_math.java) | Java 1.8 | math | O(n) per case | AC | 0.609 s | 904 KB | 11287423 |
| [1528_math.py](1528_math.py) | Python 3.12 x64 | math | O(n log n) bit operations per case | AC | 0.359 s | 17900 KB | 11287422 |
| [1528_math.rs](1528_math.rs) | Rust 1.75 x64 | math | O(n) per case | AC | 0.250 s | 520 KB | 11287424 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1528_math_optimized.cpp](1528_math_optimized.cpp) | G++ 13.2 x64 | math | O(sum N) | AC | 0.203 s | 112 KB | 11309294 |
| [1528_math_optimized.go](1528_math_optimized.go) | Go 1.14 x64 | math | O(sum N) | AC | 0.218 s | 916 KB | 11309296 |
| [1528_math_optimized.java](1528_math_optimized.java) | Java 1.8 | math | O(sum N) | AC | 0.375 s | 840 KB | 11309295 |
| [1528_math_optimized.py](1528_math_optimized.py) \* | Python 3.12 x64 | math | O(N) product construction + bigint query work | AC | 0.359 s | 1388 KB | 11309298 |
| [1528_math_optimized.rs](1528_math_optimized.rs) | Rust 1.75 x64 | math | O(sum N) | AC | 0.156 s | 444 KB | 11309297 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
