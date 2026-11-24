# 1700. Despertar

[Timus 1700](https://acm.timus.ru/problem.aspx?space=1&num=1700) · dificultad 482 · implementation

Problema original de Pavel Atnashev, del XIII Campeonato de los Urales de Programación Competitiva, 4 de abril de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada objeto tiene un conjunto de asociaciones. Para cada uno de varios
grupos de objetos, imprimir en orden alfabético las asociaciones comunes
a todos ellos, o «No solution.» si no hay ninguna.

## Entrada

n (2 ≤ n ≤ 1000) líneas «nombre: asociación asociación …», y luego m
(1 ≤ m ≤ 1000) líneas, cada una un grupo de al menos dos nombres de
objetos. Las palabras son de letras latinas minúsculas y las líneas
tienen a lo sumo 250 caracteres.

## Salida

Una línea por grupo.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
whale: big black water animal
penguin: black white ice beak
piano: keyboard black white wire
jackboot: leather heel black
train: rail wheel black
rose: red green thorn
3
whale penguin piano jackboot train
penguin piano
jackboot rose
```

Salida:

```
black
black white
No solution.
```

## Solución

Se guardan las asociaciones de cada objeto como un conjunto, por su
nombre. Para un grupo se intersecan los conjuntos de sus miembros y se
imprime el resultado ordenado, o «No solution.» si queda vacío. Todas
las líneas son cortas; un grupo requiere `O(L²)` consultas a
conjuntos. `O((n + m · L) · L log(n + L))` para líneas de longitud
L.

Trampas:

- una asociación puede aparecer dos veces en un objeto, pero se
  imprime una vez (test 02);
- un grupo puede nombrar dos veces el mismo objeto (test 03);
- un objeto puede no tener ninguna asociación, y entonces su línea
  acaba justo después de los dos puntos.

Las respuestas coinciden con una implementación aceptada independiente.

## Soluciones optimizadas

C++/Go internan asociaciones en IDs compartidos y guardan listas ordenadas sin duplicados. La consulta copia la más corta, intersecta con dos índices y ordena las grafías supervivientes al emitir. No modifica objetos; repeticiones no alteran el conjunto. Python lee frozensets de cadenas internadas y copia el menor. Todos transmiten respuestas. Con T caracteres de entrada, A asociaciones máximas, K miembros y W longitud de palabra: intersección O(KA), ordenación O(A log A·W), hash con cotas esperadas. Se comparten grafías sin guardar toda entrada/salida. Se conservan bases de conjuntos; Java/Rust reutilizan las admitidas.

El envío aceptado en Go 1.14 x64 tarda 0.062 s frente a 0.765 s de la base y usa 10 348 KB frente a 8908 KB.

En la instantánea de comparación anterior, las implementaciones base [1700_implementation.java](1700_implementation.java), [1700_implementation.rs](1700_implementation.rs) cumplían la regla de inclusión del 15% superior o de las diez primeras posiciones en ambas métricas. Sus mediciones se conservan en la tabla de versiones sencillas.

Guardar cada conjunto de asociaciones en un arreglo ordenado e intersectarlos con dos punteros. Escribir cada respuesta al procesarla. El envío aceptado 11324225 tardó 0.250 s y usó 8 536 KB. La versión sencilla tardó 0.437 s y usó 12376 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1700_hashing_sorting_optimized.rs`. Se internan las palabras con identificadores en orden lexicográfico y se intersectan conjuntos enteros ordenados, empezando por el menor. Cada objeto se busca una vez. A cuenta asociaciones, Q los nombres consultados, W las longitudes de conjuntos participantes e I/O el tamaño de entrada y salida. La entrada de C llama directamente al solucionador y vacía la salida de Rust antes de volver; se conserva la implementación de entrada habitual.

Accepted #11329024 (Rust 1.75 x64): **0.046 s / 5216 KB**. Comparación archivada: `1700_implementation.rs` (Rust 1.75 x64) — 0.593 s / 3584 KB (#11289079).

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1700_implementation.cpp](1700_implementation.cpp) | G++ 13.2 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.343 s | 7776 KB | 11329300 |
| [1700_implementation.go](1700_implementation.go) | Go 1.14 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.765 s | 8908 KB | 11289071 |
| [1700_implementation.java](1700_implementation.java) | Java 1.8 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.421 s | 12352 KB | 11329305 |
| [1700_implementation.py](1700_implementation.py) | Python 3.12 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.359 s | 13596 KB | 11329306 |
| [1700_implementation.rs](1700_implementation.rs) | Rust 1.75 x64 | implementation | O((n + m · L) · L log(n + L)) | AC | 0.546 s | 3604 KB | 11329307 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1700_hashing_sorting.cpp](1700_hashing_sorting.cpp) | G++ 13.2 x64 | hashing, sorting | O(T + nA log A + m(KA + A log A·W)) expected | AC | 0.046 s | 6148 KB | 11315323 |
| [1700_hashing_sorting.go](1700_hashing_sorting.go) | Go 1.14 x64 | hashing, sorting | O(T + nA log A + m(KA + A log A·W)) expected | AC | 0.062 s | 10348 KB | 11315329 |
| [1700_implementation_optimized.py](1700_implementation_optimized.py) | Python 3.12 x64 | implementation | O(T + m(KA + A log A·W)) expected | AC | 0.343 s | 8920 KB | 11315330 |
| [1700_sorting.java](1700_sorting.java) | Java 1.8 | sorting | O((n + m · L) · L log(n + L)) | AC | 0.250 s | 8 536 KB | 11324225 |
| [1700_hashing_sorting_optimized.rs](1700_hashing_sorting_optimized.rs) | Rust 1.75 x64 | hashing, sorting | O(A log A + Q log Q + W + I + O) expected time; O(A+I+O) space | AC | 0.046 s | 5216 KB | 11329024 |

**Mediciones actuales.** Las tablas registran las últimas ejecuciones Accepted del código exacto conservado. Las comparaciones anteriores describen ejecuciones históricas; la admisión actual sigue los [criterios compartidos](../../RATING_CRITERIA.md).
