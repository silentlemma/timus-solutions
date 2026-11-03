# 1204. Idempotentes módulo un producto de dos primos

[Timus 1204](https://acm.timus.ru/problem.aspx?space=1&num=1204) · dificultad 230 · number_theory

Problema original de Pavel Atnashev, del Concurso por Equipos de la Universidad Estatal de los Urales, marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un número `x` es idempotente módulo `n` si `x·x ≡ x (mod n)`. Para hasta
1000 valores `n < 10⁹`, cada uno producto de dos primos distintos `p` y
`q`, hay que listar todos los idempotentes de `0` a `n − 1` en orden
creciente.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número de pruebas `k` y luego `n` para cada prueba.

## Salida

Para cada prueba, sus idempotentes en una línea en orden creciente.

## Evaluación

Se comparan los tokens; los espacios adicionales no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
6
15
910186311
```

Salida:

```
0 1 3 4
0 1 6 10
0 1 303395437 606790875
```

## Solución

`x(x − 1) ≡ 0 (mod pq)` significa que cada uno de `p` y `q` divide a `x`
o a `x − 1`, así que módulo cada primo `x` vale 0 o 1. Por el teorema
chino del resto eso da exactamente cuatro idempotentes: 0, 1, el número
que vale 1 módulo `p` y 0 módulo `q`, y el que vale 0 módulo `p` y 1
módulo `q`. El tercero es `x = q·(q⁻¹ mod p)`, con el inverso obtenido
por el algoritmo de Euclides extendido, y el cuarto es `n + 1 − x`,
porque ambos suman 1 módulo los dos primos.

Para factorizar `n` se prueban los primos hasta `√10⁹ < 31623`, hallados
una vez con una criba; el factor menor está entre ellos. Como mucho unas
3400 divisiones por prueba. `O(k·π(√n))`.

Detalles a tener en cuenta:

- los dos idempotentes no triviales deben imprimirse en orden creciente,
  y cualquiera de los dos puede ser el menor;
- solo hay que hallar por división el factor menor; el mayor, de hasta
  `5·10⁸`, es simplemente `n / p`;
- `p` puede ser tan pequeño como 2.

Las respuestas se compararon con una solución escrita aparte en 3000
productos generados de los tres tipos.

## Soluciones optimizadas

La reconstrucción mediante CRT no cambia. Java usa un arreglo primitivo de primos, divisiones enteras y salida ASCII acotada en vez de objetos y cadenas por respuesta. Python usa un árbol de productos de primos: un MCD examina un bloque completo y dirige los factores no triviales hacia bloques menores; las hojas terminan por división de prueba. Cada divisor se verifica exactamente, sin hipótesis probabilísticas. Se contabilizan la construcción y los costes del MCD y la multiplicación de enteros grandes, no como operaciones constantes.

- `1204_number_theory_optimized.java`: 0.109 s / 484 KB; base `1204_number_theory.java`: 0.171 s / 1088 KB; cambio respecto a la base: tiempo -36.3%, memoria -55.5%.
- `1204_number_theory_trees.py`: 0.093 s / 1084 KB; base `1204_number_theory.py`: 0.312 s / 1016 KB; cambio respecto a la base: tiempo -70.2%, memoria +6.7%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1204_number_theory.cpp`; versión que cubre `1204_number_theory.cpp`; puestos tiempo/memoria 3/7, registros de otros autores 75/75.

- Go: base didáctica preferida `1204_number_theory.go`; versión que cubre `1204_number_theory.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1204_number_theory.java`; versión que cubre `1204_number_theory_optimized.java`; puestos tiempo/memoria 2/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `1204_number_theory.py`; versión que cubre `1204_number_theory_trees.py`; puestos tiempo/memoria 1/2, registros de otros autores 13/13.

- Rust: base didáctica preferida `1204_number_theory.rs`; versión que cubre `1204_number_theory.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1204_number_theory.cpp](1204_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(k·π(√n)) | AC | 0.031 s | 228 KB | 11283581 |
| [1204_number_theory.go](1204_number_theory.go) | Go 1.14 x64 | number_theory | O(k·π(√n)) | AC | 0.031 s | 1320 KB | 11283582 |
| [1204_number_theory.java](1204_number_theory.java) | Java 1.8 | number_theory | O(k·π(√n)) | AC | 0.171 s | 1088 KB | 11283585 |
| [1204_number_theory.py](1204_number_theory.py) | Python 3.12 x64 | number_theory | O(k·π(√n)) | AC | 0.312 s | 1016 KB | 11283583 |
| [1204_number_theory.rs](1204_number_theory.rs) | Rust 1.75 x64 | number_theory | O(k·π(√n)) | AC | 0.015 s | 268 KB | 11283586 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1204_number_theory_optimized.java](1204_number_theory_optimized.java) \* | Java 1.8 | number_theory | O(K sqrt N) | AC | 0.109 s | 484 KB | 11309381 |
| [1204_number_theory_trees.py](1204_number_theory_trees.py) \* | Python 3.12 x64 | number_theory, trees | O(log P) bigint gcds per query | AC | 0.093 s | 1084 KB | 11309380 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
