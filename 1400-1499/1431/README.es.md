# 1431. Diplomas

[Timus 1431](https://acm.timus.ru/problem.aspx?space=1&num=1431) · dificultad 362 · greedy

Problema original de Stanislav Vasiliev, del Séptimo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 25 de febrero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay N tipos de diplomas (N ≤ 18), de 1 a 30 de cada uno. Todos los
diplomas de un tipo cuelgan en una fila. Una fila tiene un tipo, o dos
tipos que se alternan estrictamente, y cada fila debe ser simétrica
respecto al centro de la pared. Hay que hallar el menor número de filas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, luego el número de diplomas de cada tipo.

## Salida

El menor número de filas.

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
8 15 13 8 14 8
```

Salida:

```
5
```

## Solución

Una fila de un solo tipo siempre vale. Dos tipos que se alternan
estrictamente forman ABAB…, y esa fila se lee igual al revés solo si
empieza y acaba con el mismo tipo, A B A … B A, así que las cantidades
difieren exactamente en uno. La respuesta es N menos el mayor número de
pares disjuntos de tipos cuyas cantidades difieren en uno.

Los pares unen valores vecinos de una cadena 1, 2, …, 30. Subiendo por
la cadena, los tipos de cantidad c aún sin pareja solo pueden
emparejarse ya con la cantidad c + 1, así que emparejar en seguida tantos
como se pueda nunca es peor. `O(N + 30)`.

Detalles a tener en cuenta:

- cantidades iguales no pueden compartir fila: una fila alterna de
  longitud par no es simétrica (prueba 06);
- en 1, 2, 3, 4 los pares son 1–2 y 3–4, no 2–3 (prueba 07);
- varios tipos pueden tener la misma cantidad (pruebas 08, 12).

## Soluciones optimizadas

`1431_greedy_optimized.py`. Conserva el emparejamiento voraz de sobrantes c con c+1 por frecuencias. Lee enteros en bloques de 4096 bytes y guarda solo 31 frecuencias, sin línea ni lista completa de tokens. Con V=30, O(n+V) tiempo y O(V+B) espacio para tokens acotados y bloque B. Mantiene el emparejamiento y la fórmula n-pairs. La fila Accepted indica el runtime real y sus medidas emparejadas. Vacía salida antes de os._exit(0), que omite cierre del intérprete; la mejora medida de memoria depende del runtime y no implica aceleración asintótica.

Frente a `1431_greedy.py`: tiempo 0.078 s → 0.156 s; memoria 420 KB → 256 KB.

Go y Rust guardan las frecuencias de cantidades de uno a 30 en vectores de bytes. En cada cantidad emparejan tantos tipos como sea posible con los pendientes de la cantidad anterior. Cada pareja elimina una fila necesaria. Solo trasladan el resto sin pareja, sin lista ordenada ni grafo de emparejamiento. Ambas usan búferes fijos de bytes para la entrada y la salida decimal. Go accede directamente a los descriptores de entrada y salida estándar y Rust usa la biblioteca de ejecución de C.

El envío aceptado en Rust 1.75 x64 tarda 0.031 s frente a 0.015 s de la base y usa 56 KB frente a 220 KB.

Las implementaciones base aceptadas [1431_greedy.cpp](1431_greedy.cpp), [1431_greedy.java](1431_greedy.java), [1431_greedy.py](1431_greedy.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

`1431_greedy_optimized.java`. Java conserva el algoritmo y las estructuras descritas para la versión sencilla. Un búfer fijo de bytes y FastInput sustituyen Scanner y su maquinaria de expresiones regulares y configuración regional. Los enteros se analizan directamente; las cadenas siguen decodificándose como UTF-8 cuando se solicitan y los decimales mantienen conversión numérica explícita. La anticipación guarda un token solo cuando hace falta. El algoritmo de salida no cambia. Se elimina el coste del análisis general; la tabla describe el trabajo algorítmico, con lectura lineal en bytes y un búfer acotado.

Frente a `1431_greedy.java`: tiempo 0.156 s → 0.109 s; memoria 1644 KB → 440 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1431_greedy_optimized.java`: puesto de tiempo 8/13 y de memoria 2/13 en esta muestra comparable.

`1431_greedy_optimized.py`: puesto de tiempo 32/36 y de memoria 1/36 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1431_greedy.cpp](1431_greedy.cpp) | G++ 13.2 x64 | greedy | O(N + 30) | AC | 0.015 s | 128 KB | 11286206 |
| [1431_greedy.go](1431_greedy.go) | Go 1.14 x64 | greedy | O(N + 30) | AC | 0.015 s | 1076 KB | 11286207 |
| [1431_greedy.java](1431_greedy.java) \* | Java 1.8 | greedy | O(N + 30) | AC | 0.156 s | 1644 KB | 11286209 |
| [1431_greedy.py](1431_greedy.py) \* | Python 3.12 x64 | greedy | O(N + 30) | AC | 0.078 s | 420 KB | 11286208 |
| [1431_greedy.rs](1431_greedy.rs) | Rust 1.75 x64 | greedy | O(N + 30) | AC | 0.015 s | 220 KB | 11286210 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1431_greedy_optimized.go](1431_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(N + 30) | AC | 0.015 s | 348 KB | 11311231 |
| [1431_greedy_optimized.rs](1431_greedy_optimized.rs) \* | Rust 1.75 x64 | greedy | O(N + 30) | AC | 0.031 s | 56 KB | 11311246 |
| [1431_greedy_optimized.java](1431_greedy_optimized.java) \* | Java 1.8 | greedy | O(N + 30) | AC | 0.109 s | 440 KB | 11324802 |
| [1431_greedy_optimized.py](1431_greedy_optimized.py) \* | PyPy 3.10 x64 | greedy | O(n+V) time; O(V+B) space | AC | 0.156 s | 256 KB | 11325486 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
