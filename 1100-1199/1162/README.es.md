# 1162. ¿Puede una cadena de cambios de divisas con comisiones aumentar el dinero?

[Timus 1162](https://acm.timus.ru/problem.aspx?space=1&num=1162) · dificultad 185 · shortest_paths

Problema original de Nick Durov, de la subregión norte del concurso regional ACM ICPC del noreste de Europa 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N ≤ 100` divisas y `M ≤ 100` casas de cambio, cada una entre dos
divisas en ambos sentidos con su propio tipo y comisión por sentido:
cambiar `x` da `(x − comisión)·tipo`, y la cantidad nunca puede ser
negativa. Empezando con `V` unidades de la divisa `S`, decide si alguna
secuencia de cambios termina en la divisa `S` con más de `V`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`, `M`, `S` y `V`, y luego `M` líneas con dos divisas y el tipo y la
comisión en cada sentido.

`1 ≤ S ≤ N ≤ 100`, `1 ≤ M ≤ 100` y `0 ≤ V ≤ 1000`.
Los tipos están en `[0.01, 100]` y las comisiones en `[0, 100]`, ambos con
un máximo de dos decimales. Los decimales de `V` no están limitados.
Para cualquier secuencia que utilice cada casa de cambio como máximo una
vez, la razón entre la cantidad final y la inicial es menor que `10000`.

## Salida

`YES` o `NO`.

## Evaluación

Tokens exactos. Cada fuente nueva tiene pruebas completas del entorno destino, comparaciones matemáticas independientes y Accepted propio ligado al hash; las bases conservan sus propias medidas.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 2 1 10.0
1 2 1.0 1.0 1.0 1.0
2 3 1.1 1.0 1.1 1.0
```

Salida:

```
NO
```

### Ejemplo 2

Entrada:

```
3 2 1 20.0
1 2 1.0 1.0 1.0 1.0
2 3 1.1 1.0 1.1 1.0
```

Salida:

```
YES
```

## Solución

Cada moneda es un vértice y cada dirección una arista. Si `x≥fee`,
el cambio da `(x−fee)·rate`. Las cinco bases usan Bellman–Ford síncrono:
tras `j` rondas, `best[c]` maximiza el capital con hasta `j` cambios; la
siguiente ronda solo lee ese vector y escribe otro. Las tasas positivas
hacen monótono todo sufijo: basta el máximo por moneda. Diferenciar un
estado inalcanzable de un cero alcanzable.

La aritmética es exacta. Sea `P=max(2, cifras fraccionarias de V)` y
`D=10^P` el denominador inicial. Tasas/comisiones son centésimas enteras
`R,C`. Omitir si el numerador `x<C·D/100`; si no, el nuevo numerador es
`(x−C·D/100)·R`, con denominador `100D`. Escalar también por 100 los
importes conservados y el capital inicial en cada ronda. No se truncan
decimales de V ni se usan flotantes o epsilon.

Responder YES al superar el capital inicial en S. Una ronda sin mejoras
es un punto fijo y prueba NO. Una mejora en la ronda N revela un ciclo
rentable: si todos los segmentos repetidos de la ruta no aumentasen su
capital de entrada, eliminarlos conservaría la viabilidad y no empeoraría
el sufijo monótono. Quedaría una ruta simple de como máximo N−1 aristas,
contradicción. El ciclo es `A·x−B`, `B≥0`; una mejora estricta con `x≥0`
implica `A>1`, y repetirlo crece sin límite. Cada punto tiene dirección
inversa de tasa positiva; con suficiente dinero se paga el regreso a S
y se supera V. Un capital inicial cero no puede crecer.

Tras N rondas hay `O(P+N)` cifras por estado. Relajaciones y copias cuestan
`O(N(N+M)(P+N))` operaciones de dígito; una cota conservadora que incluye
leer decimales es `O(P²+N(N+M)(P+N))`. Estados vivos: `O(N(P+N))` cifras,
más `O(M)` aristas de tamaño fijo. C++/Rust usan dígitos en base 100,
Go `big.Int`, Java `BigInteger`, Python enteros arbitrarios. Solo se
nombran las funciones del literal 100 y se aplica el formato; las cinco
bases tienen Accepted nuevo de su SHA exacto. Se respaldan todos los
bytes originales y se mantienen los algoritmos.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1162_shortest_paths.cpp`; fuente que cubre `1162_shortest_paths_optimized.cpp`; puestos tiempo/memoria 380/107, registros de otros autores 426/426.

- Go: base didáctica preferida `1162_shortest_paths.go`; fuente que cubre `1162_shortest_paths_optimized.go`; puestos tiempo/memoria 3/5, registros de otros autores 5/5.

- Java: base didáctica preferida `1162_shortest_paths.java`; fuente que cubre `1162_shortest_paths_optimized.java`; puestos tiempo/memoria 43/46, registros de otros autores 117/117.

- Python/PyPy: base didáctica preferida `1162_shortest_paths.py`; fuente que cubre `1162_shortest_paths_optimized.py`; puestos tiempo/memoria 75/1, registros de otros autores 77/77.

- Rust: base didáctica preferida `1162_shortest_paths.rs`; fuente que cubre `1162_shortest_paths.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones optimizadas

**C++, Go, Java.** Las tres versiones optimizadas mantienen Jacobi exacto y el sufijo
`_optimized`. Se restringen a la componente no dirigida de S: los puntos
son bidireccionales, las otras componentes nunca ayudan. Con C vértices
retenidos bastan C rondas. Es poda estructural, no garantiza poder pagar
cualquier comisión.

Go reutiliza buffers `big.Int` con almacenamiento propio y temporales;
copia con `Set`, sin asignar superficialmente la estructura. C++/Java
usan base `10^9`, lectura por bloques de nueve cifras y reutilización
de capacidad/temporales, evitando dígitos cortos u objetos inmutables.
Con comisión cero se omite la resta. Siempre se leen estados anteriores,
sin convertir el algoritmo en relajación en el mismo vector.

Con `B=10^9`, cada dígito es menor que B y el factor como máximo 10000:
producto más acarreo menor que `B·10000=10^13`, seguro en `uint64_t`
de C++ y `long` de Java. Restar solo si hay capital; préstamo 0 o 1,
representable en los tipos elegidos. Multiplicar con alias lee cada
dígito antiguo antes de escribir; buffers distintos poseen su memoria.
Se cubren cero, potencias de la base y cadenas de préstamos. La cota
asintótica es igual; se reducen dígitos, asignaciones y vértices.

**Python/PyPy.** Python mantiene Bellman–Ford síncrono exacto y la reserva 100^N: hastaNintercambios dividen por 100 sin perder dígitos. El decimal inicial se convierte en bloques de hasta 1000 dígitos, sin el límite de una conversión única. Las tuplas conservan comisiones exactas precalculadas. Cada ocho líneas se recogen objetos muertos del análisis; solo cambia su vida en memoria, nunca cantidades ni accesibilidad. Se intercambia tiempo de recolección por memoria máxima. Permanecen las cinco bases exactas claras. O(NM)relajaciones exactas y O(N+M)registros, más la recolección medida.

- `1162_shortest_paths_optimized.cpp`: 0.031 s / 244 KB; base `1162_shortest_paths.cpp`: 0.046 s / 676 KB; cambio respecto a la base: tiempo -32.6%, memoria -63.9%.
- `1162_shortest_paths_optimized.go`: 0.031 s / 1304 KB; base `1162_shortest_paths.go`: 0.031 s / 5436 KB; cambio respecto a la base: tiempo -0.0%, memoria -76.0%.
- `1162_shortest_paths_optimized.java`: 0.125 s / 1224 KB; base `1162_shortest_paths.java`: 0.125 s / 4932 KB; cambio respecto a la base: tiempo -0.0%, memoria -75.2%.
- `1162_shortest_paths_optimized.py`: 0.156 s / 416 KB; base `1162_shortest_paths.py`: 0.078 s / 708 KB; cambio respecto a la base: tiempo +100.0%, memoria -41.2%.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1162_shortest_paths.cpp](1162_shortest_paths.cpp) | G++ 13.2 x64 | shortest_paths | O(P^2 + N(N+M)(P+N)) | AC | 0.046 s | 676 KB | 11308458 |
| [1162_shortest_paths.go](1162_shortest_paths.go) | Go 1.14 x64 | shortest_paths | O(P^2 + N(N+M)(P+N)) | AC | 0.031 s | 5436 KB | 11308459 |
| [1162_shortest_paths.java](1162_shortest_paths.java) | Java 1.8 | shortest_paths | O(P^2 + N(N+M)(P+N)) | AC | 0.125 s | 4932 KB | 11308466 |
| [1162_shortest_paths.py](1162_shortest_paths.py) | Python 3.12 x64 | shortest_paths | O(P^2 + N(N+M)(P+N)) | AC | 0.078 s | 708 KB | 11308471 |
| [1162_shortest_paths.rs](1162_shortest_paths.rs) | Rust 1.75 x64 | shortest_paths | O(P^2 + N(N+M)(P+N)) | AC | 0.046 s | 300 KB | 11308481 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1162_shortest_paths_optimized.cpp](1162_shortest_paths_optimized.cpp) \* | G++ 13.2 x64 | shortest_paths | O(NM) exact relaxations; O(N+M) records; explicit GC overhead in Python | AC | 0.031 s | 244 KB | 11308451 |
| [1162_shortest_paths_optimized.go](1162_shortest_paths_optimized.go) \* | Go 1.14 x64 | shortest_paths | O(NM) exact relaxations; O(N+M) records; explicit GC overhead in Python | AC | 0.031 s | 1304 KB | 11308453 |
| [1162_shortest_paths_optimized.java](1162_shortest_paths_optimized.java) \* | Java 1.8 | shortest_paths | O(NM) exact relaxations; O(N+M) records; explicit GC overhead in Python | AC | 0.125 s | 1224 KB | 11308454 |
| [1162_shortest_paths_optimized.py](1162_shortest_paths_optimized.py) \* | PyPy 3.10 x64 | shortest_paths | O(NM) exact relaxations; O(N+M) records; explicit GC overhead in Python | AC | 0.156 s | 416 KB | 11309920 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
