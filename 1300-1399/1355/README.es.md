# 1355. La calva, otra vez

[Timus 1355](https://acm.timus.ru/problem.aspx?space=1&num=1355) · dificultad 212 · number_theory

Problema original de Aleksandr Bikbaev, del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las tabernas se numeran con enteros positivos, y desde la taberna n solo
se puede ir a una taberna cuyo número sea múltiplo de n. Un paseo
empieza en la taberna a y debe acabar en la taberna b, con una jarra de
cerveza en cada taberna del camino, a y b incluidas. Para cada uno de
T ≤ 20 pares con 1 ≤ a, b ≤ 10⁹, hay que imprimir el mayor número de
jarras, o 0 si no se puede llegar a b.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

T, luego T líneas con a y b.

## Salida

T líneas con las respuestas.

## Evaluación

Tokens exactos. Cada fuente nueva tiene pruebas completas del entorno destino, comparaciones matemáticas independientes y Accepted propio ligado al hash; las bases conservan sus propias medidas.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
30 89
2 16
3 243
1 1
2 2
```

Salida:

```
0
4
5
1
1
```

## Solución

Cada número del paseo divide al siguiente, así que solo se llega a b si
a divide a b. Entonces cada paso multiplica el número por un factor
mayor que 1, y el producto de todos los factores es q = b / a. Para
visitar tantas tabernas como sea posible, cada factor debe ser un primo,
de modo que el número de pasos es Ω(q), la cantidad de factores primos
de q contados con repetición. La respuesta es 1 + Ω(q), contando la
propia taberna a.

La división por tanteo hasta √q ≤ 31 623 da Ω(q). `O(T · √(b / a))`.

Detalles a tener en cuenta:

- con a = b se bebe una jarra, no cero (ejemplo);
- si b es menor que a o no es múltiplo suyo, la respuesta es 0
  (prueba 04);
- T puede ser 0, y entonces no se imprimen respuestas (prueba 02);
- q = 2²⁹ da más pasos que nadie, 30 jarras (prueba 03).

## Soluciones optimizadas

`1355_number_theory_optimized.go`. Conserva factorización de R=B/A: cero si no divide, uno para R=1, elimina dos y luego divisores impares. Mismas multiplicidades, sin criba ni lista de factores. O(Σ√R) tiempo total y espacio constante. Buffers acotados de entrada de 256 bytes y salida de 64 usan syscall.Read/Write de Go 1.14, reintentan EINTR/escrituras parciales y tratan EOF de cero bytes. Elimina inicialización fmt/bufio/os.File. Pruebas Linux y compilación cruzada Windows validan funcionamiento y construcción; las métricas pareadas siguientes vienen de nuestro Accepted exacto en juez Windows. Se conserva fuente didáctica legible.

Frente a `1355_number_theory.go`: tiempo 0.015 s → 0.046 s; memoria 1100 KB → 268 KB.

`1355_number_theory_optimized.rs`. Mantiene número de factores primos con multiplicidad de B/A y elemento inicial. Si A no divide B da cero. Extrae doses, prueba solo impares con d<=valor/d y cuenta primo residual. Mismo algoritmo de prueba con menos divisiones, consultas/salida en flujo. O(sum sqrt(B/A)) peor caso para divisibles, O(1) espacio; razón uno sigue dando uno.

Frente a `1355_number_theory.rs`: tiempo 0.015 s → 0.015 s; memoria 212 KB → 44 KB.

La versión didáctica conserva la división por prueba. La versión rápida en Python calcula el MCD del cociente con el producto fijo de todos los primos hasta 1000. El MCD identifica los divisores primos pequeños, que se eliminan del cociente con toda su multiplicidad. Los factores restantes superan 1000 y el cociente no supera 10^9, así que quedan como máximo dos. El segundo producto fijo contiene los primos entre 1001 y 31623. Un resto compuesto tiene un divisor en ese intervalo y un resto primo mayor que 10^6 es coprimo con el producto. Se cuentan dos factores o uno, respectivamente. Los productos se generan con una criba y se guardan como constantes hexadecimales.

- `1355_number_theory_math.py`: 0.062 s / 584 KB; base `1355_number_theory.py`: 0.109 s / 392 KB; cambio respecto a la base: tiempo -43.1%, memoria +49.0%.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1355_number_theory_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1355_number_theory.cpp](1355_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 132 KB | 11285268 |
| [1355_number_theory.go](1355_number_theory.go) | Go 1.14 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 1100 KB | 11285270 |
| [1355_number_theory.java](1355_number_theory.java) | Java 1.8 | number_theory | O(T·√(b/a)) | AC | 0.078 s | 448 KB | 11285272 |
| [1355_number_theory.py](1355_number_theory.py) | Python 3.12 x64 | number_theory | O(T·√(b/a)) | AC | 0.109 s | 392 KB | 11285271 |
| [1355_number_theory.rs](1355_number_theory.rs) | Rust 1.75 x64 | number_theory | O(T·√(b/a)) | AC | 0.015 s | 212 KB | 11285273 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1355_number_theory_math.py](1355_number_theory_math.py) | Python 3.12 x64 | number_theory, math | O(T*(P+log Q)) bounded arithmetic, P=1000 | AC | 0.062 s | 584 KB | 11310243 |
| [1355_number_theory_optimized.rs](1355_number_theory_optimized.rs) | Rust 1.75 x64 | number_theory | O(sum sqrt(B/A)) time; O(1) space | AC | 0.015 s | 44 KB | 11325504 |
| [1355_number_theory_optimized.go](1355_number_theory_optimized.go) | Go 1.14 x64 | number_theory | O(Σ√R) time; O(1) space | AC | 0.046 s | 268 KB | 11325656 |
