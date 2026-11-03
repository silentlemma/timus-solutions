# 1220. Mil pilas en tres cuartos de megabyte

[Timus 1220](https://acm.timus.ru/problem.aspx?space=1&num=1220) · dificultad 281 · implementation

Problema original de Pavel Atnashev, del séptimo concurso universitario de programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que ejecutar hasta `10⁵` operaciones sobre 1000 pilas: `PUSH A B`
pone el número `B ≤ 10⁹` en la pila `A`, y `POP A` quita la cima de la
pila `A` y la imprime. Cada `POP` encuentra su pila no vacía. El límite
de memoria es de solo 0,75 MB.

Límite de tiempo: 0.5 segundos. Límite de memoria: 0.75 MB.

## Entrada

`N` y luego las operaciones, una por línea.

## Salida

El valor de cada `POP`, uno por línea, en orden.

## Evaluación

Se comparan los tokens exactos; los espacios no afectan.

- `1220_implementation_optimized.rs` (Rust 1.75 x64): 13 pruebas del repositorio; 8 comparaciones adicionales de fuente exacta.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
PUSH 1 100
PUSH 1 200
PUSH 2 300
PUSH 2 400
POP 2
POP 1
POP 2
```

Salida:

```
400
200
300
```

## Solución

Guardar cada valor con un enlace de 32 bits al que tiene debajo ocuparía
unos 800 KB para `10⁵` valores, ya por encima del límite de memoria,
y un arreglo aparte por pila desperdiciaría espacio en las vacías.

Así que cada pila es una cadena de bloques de 10 valores, el bloque más
nuevo primero, y cada bloque recuerda el siguiente bloque más antiguo de
la misma pila. El tamaño de la pila dice cuán lleno está su bloque más
nuevo, así que no hace falta un contador por bloque: apilar en un bloque
lleno (o en una pila vacía) toma un bloque de una lista libre, y
desapilar hasta vaciar el bloque más nuevo lo devuelve. Solo el bloque
más nuevo de cada pila puede estar a medias, así que nunca hay más de
`10⁵/10 + 1000` bloques en uso, unos 460 KB en total. Unos búferes fijos
pequeños para leer y escribir hacen rápidas la entrada y la salida sin
gastar mucha memoria. `O(N)`.

Detalles a tener en cuenta:

- la biblioteca de flujos de C++ ya cuesta bastante memoria por sí sola,
  así que el programa lee y escribe con `fread` y `fwrite`;
- un bloque debe devolverse en cuanto se vacía, o una pila que crece y
  mengua una y otra vez agotaría la reserva;
- bastan números de bloque de 16 bits, porque hay menos de 32.768
  bloques.

La salida se comparó con una simulación sencilla con listas en todas las
pruebas, incluidas 100.000 operaciones de varios tipos.

## Soluciones optimizadas

Aquí el juez solo admite C++ y Rust; se conservan ambas bases. Rust compacto mantiene LIFO, pero enlaza bloques de ocho valores en vez de asignaciones ampliables por pila. Cada valor<=10^9<2^30: ocho ocupan30bytes. Un enlace u16 apunta al bloque anterior; los vacíos vuelven a una lista libre. Hay como máximo1000bloques superiores parciales; los completos contienen ocho valores vivos. Bastan100000/8+1000+1huecos, indexables con u16. Cada operación toca cuatro/cinco bytes preservando celdas vecinas. Arreglos globales y E/S acotada ABI C evitan heap/arranque no usado. Tiempo O(Q), espacio O(Q+S), S=1000. Fuente exacta:13tests del repositorio y8estrés independientes, con100000operaciones y reutilización.

- `1220_implementation_optimized.rs`: 0.031 s / 436 KB; base `1220_implementation.rs`: 0.031 s / 672 KB; cambio respecto a la base: tiempo -0.0%, memoria -35.1%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1220_implementation.cpp`; fuente que cubre `1220_implementation.cpp`; puestos tiempo/memoria 1/4, registros de otros autores 55/55.

- Rust: base didáctica preferida `1220_implementation.rs`; fuente que cubre `1220_implementation_optimized.rs`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1220_implementation.cpp](1220_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 540 KB | 11283689 |
| [1220_implementation.rs](1220_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.031 s | 672 KB | 11286809 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1220_implementation_optimized.rs](1220_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(Q) time; O(Q+S) bounded storage | AC | 0.031 s | 436 KB | 11309741 |
