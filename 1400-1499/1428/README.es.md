# 1428. Acertijo Jedi

[Timus 1428](https://acm.timus.ru/problem.aspx?space=1&num=1428) · dificultad 498 · math

Problema original de Ilya Grebnov, Dmitry Kovalioff y Nikita Rybak, de Timus Top Coders: First Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados A, B y C (1 ≤ A, B, C ≤ 32) tales que C − 1 es divisible por A y
por B, hay que hallar enteros X, Y y Z de 1 a 10⁵⁰ con
X^A + Y^B = Z^C. Vale cualquier terna así.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

A, B y C.

## Salida

X, Y y Z, uno por línea.

## Evaluación

El repositorio usa un comprobador semántico y acepta cualquier salida que satisfaga estas condiciones. Emite exactamente tres enteros X,Y,Z de [1,10^50]; el comprobador verifica X^A+Y^B=Z^C con potencias enteras exactas.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 2 3
```

Salida:

```
10
5
5
```

## Solución

Dos mitades iguales hacen un entero: 2^(C−1) + 2^(C−1) = 2^C. Como A y B
dividen a C − 1, se toma X = 2^((C−1)/A) e Y = 2^((C−1)/B), de modo que
X^A = Y^B = 2^(C−1), y Z = 2. Los números son como mucho 2³¹, muy por
debajo de 10⁵⁰, y caben en 64 bits. `O(1)`.

Detalles a tener en cuenta:

- C = 1 da X = Y = 1 y 1 + 1 = 2¹ (pruebas 03, 08);
- el ejemplo imprime otra terna, así que las pruebas usan un
  verificador con enteros grandes (prueba 01).

## Soluciones optimizadas

Go conserva X=2^((C−1)/A), Y=2^((C−1)/B), Z=2. Los exponentes van de cero a 31 y caben en desplazamientos uint64. Lee los tres enteros por el descriptor de entrada estándar y escribe los dígitos decimales en un búfer de 64 bytes. Tiempo y espacio O(1). Los 1537 triples válidos se comprueban con potencias enteras exactas. Los otros cuatro lenguajes reutilizan las bases admitidas.

Las implementaciones base aceptadas [1428_math.cpp](1428_math.cpp), [1428_math.java](1428_math.java), [1428_math.py](1428_math.py), [1428_math.rs](1428_math.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

`1428_math_optimized.java`. Java conserva el algoritmo y las estructuras descritas para la versión sencilla. Un búfer fijo de bytes y FastInput sustituyen Scanner y su maquinaria de expresiones regulares y configuración regional. Los enteros se analizan directamente; las cadenas siguen decodificándose como UTF-8 cuando se solicitan y los decimales mantienen conversión numérica explícita. La anticipación guarda un token solo cuando hace falta. El algoritmo de salida no cambia. Se elimina el coste del análisis general; la tabla describe el trabajo algorítmico, con lectura lineal en bytes y un búfer acotado.

Frente a `1428_math.java`: tiempo 0.156 s → 0.109 s; memoria 1600 KB → 472 KB.


`1428_math_parsing_optimized.rs`. Se conserva la construcción exacta con potencias de dos y se formatean juntos los tres enteros. Se usan formatos C correspondientes a los tipos enteros, se vacía la salida y se termina tras completar la respuesta. MSVC enlaza directamente las exportaciones de la CRT heredada; Linux y Windows GNU mantienen el enlace normal con la biblioteca C.

Este código exacto tiene su propio Accepted y cumple los [criterios compartidos](../../RATING_CRITERIA.md). El tiempo y la memoria siguientes proceden de una misma ejecución; las mediciones repetidas pueden variar. Se conservan las versiones sencillas y optimizadas distintas existentes.

Accepted #11329514 (Rust 1.75 x64): **0.015 s / 84 KB**.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1428_math.cpp](1428_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11286190 |
| [1428_math.go](1428_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1064 KB | 11286191 |
| [1428_math.java](1428_math.java) \* | Java 1.8 | math | O(1) | AC | 0.156 s | 1600 KB | 11286193 |
| [1428_math.py](1428_math.py) \* | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 408 KB | 11286192 |
| [1428_math.rs](1428_math.rs) \* | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 208 KB | 11286194 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1428_math_optimized.go](1428_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 320 KB | 11315833 |
| [1428_math_optimized.java](1428_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 472 KB | 11324977 |
| [1428_math_parsing_optimized.rs](1428_math_parsing_optimized.rs) | Rust 1.75 x64 | math, parsing | O(1) time and space | AC | 0.015 s | 84 KB | 11329514 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
