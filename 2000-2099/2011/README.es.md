# 2011. Al Menos Seis Ordenaciones Distintas

[Timus 2011](https://acm.timus.ru/problem.aspx?space=1&num=2011) · dificultad 103 · combinatorics

Problema original de Alexey Kungurtsev, del Concurso Regional Escolar de Programación de los Urales 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dispones de `n` símbolos de tres tipos posibles. Ordena todos para
formar una palabra de longitud `n`; los símbolos iguales son
indistinguibles. Decide si existen al menos seis palabras diferentes.
Cada símbolo disponible debe usarse exactamente una vez.

## Entrada

La primera línea contiene `n`, `1 ≤ n ≤ 100`. La segunda contiene `n`
enteros entre 1 y 3 que indican los tipos. Tiempo límite 0,5 segundos y
memoria 64 MB.

## Salida

Escribe `Yes` si existen al menos seis palabras, y `No` en caso
contrario. Se distinguen mayúsculas y minúsculas. La respuesta única se
compara por tokens.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
6
1 2 2 3 3 3
```

```
Yes
```

Las multiplicidades son 1, 2 y 3. Hay `6!/(1!·2!·3!)=60` palabras
distintas, de modo que la respuesta es `Yes`.

## Solución

Las piezas de un mismo tipo son iguales, así que k piezas con c₁, c₂, c₃
de cada tipo forman k!/(c₁!·c₂!·c₃!) palabras distintas. Se leen las
piezas una a una y se mantiene esta cuenta para las leídas: cuando llega
la k-ésima pieza y su tipo aparece ahora c veces, la cuenta se
multiplica por k y se divide exactamente entre c. En cuanto la cuenta
llega a 6, la respuesta es `Yes`: las piezas restantes, añadidas en un
orden fijo, mantienen distintas las palabras. Si nunca llega a 6, la
respuesta es `No`. `O(n)`.

Antes de cada paso la cuenta es a lo sumo 5, así que 5 · 100 cabe en
cualquier tipo entero; se multiplica antes de dividir.

Detalles a tener en cuenta:

- exactamente seis palabras ya es `Yes`;
- no hay que calcular los factoriales completos: se desbordan.

## Soluciones optimizadas

`2011_combinatorics_optimized.py`. Mantiene la recurrencia multinomial exacta ways=ways*length/count[value] y termina al llegar a seis. Analiza bloques de 4096 bytes a tres frecuencias sin materializar todos los enteros antes de salir. Añadir un elemento no reduce las permutaciones, por lo que el sufijo no leído no anula el éxito. O(n) tiempo peor caso y O(B) espacio para tokens acotados y bloque B. La fila Accepted indica el runtime real y sus medidas emparejadas. Vacía salida antes de os._exit(0), que omite cierre del intérprete; la mejora medida de memoria depende del runtime y no implica aceleración asintótica.

Frente a `2011_combinatorics.py`: tiempo 0.109 s → 0.156 s; memoria 516 KB → 264 KB.

`2011_combinatorics_optimized.java`. Conserva la cuenta multinomial incremental ways=ways*length/count[newType], parando al alcanzar seis. Añadir un símbolo no reduce la cuenta, así que tras Yes se puede ignorar el resto. Java mantiene la parada temprana y sustituye Scanner. Rust elimina String completo y vector de valores, consumiendo cada tipo directamente. Solo tres contadores: tiempo peor caso O(n), espacio auxiliar O(1). Antes de actualizar ways<=5 y n<=100: producto máximo 500, sin factoriales ni enteros grandes. Mantiene umbral >=6 y mayúsculas Yes/No.

Frente a `2011_combinatorics.java`: tiempo 0.125 s → 0.109 s; memoria 1668 KB → 496 KB.

`2011_combinatorics_optimized.rs`. Conserva la cuenta multinomial incremental ways=ways*length/count[newType], parando al alcanzar seis. Añadir un símbolo no reduce la cuenta, así que tras Yes se puede ignorar el resto. Java mantiene la parada temprana y sustituye Scanner. Rust elimina String completo y vector de valores, consumiendo cada tipo directamente. Solo tres contadores: tiempo peor caso O(n), espacio auxiliar O(1). Antes de actualizar ways<=5 y n<=100: producto máximo 500, sin factoriales ni enteros grandes. Mantiene umbral >=6 y mayúsculas Yes/No.

Frente a `2011_combinatorics.rs`: tiempo 0.062 s → 0.046 s; memoria 232 KB → 64 KB.

La solución optimizada en C++ cuenta los valores al leerlos con `scanf`
en lugar de `iostream` y un vector, e imprime la respuesta en cuanto la
conoce: 116 KB en lugar de 380 KB, con el mismo tiempo.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`2011_combinatorics_optimized.java`: puesto de tiempo 8/127 y de memoria 10/127 en esta muestra comparable.

`2011_combinatorics_optimized.py`: puesto de tiempo 47/52 y de memoria 1/52 en esta muestra comparable.

`2011_combinatorics_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2011_combinatorics.cpp](2011_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n) | AC | 0.031 s | 380 KB | 11292493 |
| [2011_combinatorics.go](2011_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n) | AC | 0.046 s | 1112 KB | 11292495 |
| [2011_combinatorics.java](2011_combinatorics.java) | Java 1.8 | combinatorics | O(n) | AC | 0.125 s | 1668 KB | 11303363 |
| [2011_combinatorics.py](2011_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n) | AC | 0.109 s | 516 KB | 11292497 |
| [2011_combinatorics.rs](2011_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n) | AC | 0.062 s | 232 KB | 11292499 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2011_combinatorics_optimized.cpp](2011_combinatorics_optimized.cpp) | G++ 13.2 x64 | combinatorics | O(n) | AC | 0.015 s | 116 KB | 11303791 |
| [2011_combinatorics_optimized.java](2011_combinatorics_optimized.java) \* | Java 1.8 | combinatorics | O(n) | AC | 0.109 s | 496 KB | 11324782 |
| [2011_combinatorics_optimized.rs](2011_combinatorics_optimized.rs) \* | Rust 1.75 x64 | combinatorics | O(n) | AC | 0.046 s | 64 KB | 11324869 |
| [2011_combinatorics_optimized.py](2011_combinatorics_optimized.py) \* | PyPy 3.10 x64 | combinatorics | O(n) time; O(B) space | AC | 0.156 s | 264 KB | 11325480 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
