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

`1204_number_theory_optimized.rs`. Conserva factorización por prueba de n=pq y construcción CRT de cuatro raíces idempotentes con Euclides extendido. Criba solo impares compuestos y guarda primos u16 en vez de i64. Procesa consultas y raíces en flujo sin buffers completos. R=31623, Q consultas: O(R log log R+Q(pi(R)+log N)) tiempo, O(R+pi(R)) espacio; primos distintos garantizan inversa. Mantiene orden 0,1,min(x,y),max(x,y).

Frente a `1204_number_theory.rs`: tiempo 0.015 s → 0.015 s; memoria 268 KB → 92 KB.

La reconstrucción mediante CRT no cambia. Java usa un arreglo primitivo de primos, divisiones enteras y salida ASCII acotada en vez de objetos y cadenas por respuesta. Python usa un árbol de productos de primos: un MCD examina un bloque completo y dirige los factores no triviales hacia bloques menores; las hojas terminan por división de prueba. Cada divisor se verifica exactamente, sin hipótesis probabilísticas. Se contabilizan la construcción y los costes del MCD y la multiplicación de enteros grandes, no como operaciones constantes.

- `1204_number_theory_optimized.java`: 0.109 s / 484 KB; base `1204_number_theory.java`: 0.171 s / 1088 KB; cambio respecto a la base: tiempo -36.3%, memoria -55.5%.
- `1204_number_theory_trees.py`: 0.093 s / 1084 KB; base `1204_number_theory.py`: 0.312 s / 1016 KB; cambio respecto a la base: tiempo -70.2%, memoria +6.7%.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1204_number_theory_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

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
| [1204_number_theory_optimized.rs](1204_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(R log log R+Q(pi(R)+log N)) | AC | 0.015 s | 92 KB | 11325500 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
