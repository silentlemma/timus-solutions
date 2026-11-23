# 1437. Gasolinera

[Timus 1437](https://acm.timus.ru/problem.aspx?space=1&num=1437) · dificultad 493 · bfs

Problema original de Alexey Lakhtin, del Séptimo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 25 de febrero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Tres bidones caben de 0 a 255 litros cada uno. El surtidor solo puede
llenar un bidón hasta el borde, la gasolina puede pasarse de un bidón a
otro hasta que el primero se vacíe o el segundo se llene, y no se puede
derramar nada. Solo después de todos los trasvases, algunos bidones se
vacían en el depósito. ¿Cuántos volúmenes positivos distintos puede
recibir el depósito?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Las tres capacidades, una por línea.

## Salida

El número de volúmenes.

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

## Ejemplos

### Ejemplo 1

Entrada:

```
0
3
4
```

Salida:

```
6
```

## Solución

Se recorren todos los estados (x, y, z) de los bidones desde todos
vacíos, con tres movimientos de llenar un bidón y seis de verter uno en
otro. Tras cualquier movimiento algún bidón está vacío o lleno, así que
como mucho unos 3·2·256² de los 256³ estados son alcanzables. Cada
estado alcanzado da las sumas de sus subconjuntos no vacíos de bidones
como volúmenes para el depósito; se cuentan los positivos distintos.
Para capacidades a, b, c, sean P=(a+1)(b+1)(c+1), V=a+b+c+1 y S el número
de estados alcanzados. Incluida la inicialización de marcas, el tiempo
medio es `O(P)`, o `O(P + S log V)` en C++ con su conjunto ordenado.

Detalles a tener en cuenta:

- cero litros no cuentan (pruebas 01, 03);
- un bidón ya lleno no admite más, así que en el ejemplo no se pueden
  obtener 5 litros (prueba 01);
- tres bidones iguales siempre están vacíos o llenos (prueba 05).

## Soluciones optimizadas

`1437_bfs_optimized.java`. Conserva BFS de llenar/verter, codifica ternas en int, visitas en bits de long y cola int[]. Sea S=(a+1)(b+1)(c+1),B=S-product(max(0,capacity-1)). Cada paso deja algún bote vacío/lleno: a lo sumo B estados de frontera en cola, incluido cero con capacidades cero. boolean[] registra sumas de subconjuntos hasta C=a+b+c, sin HashSet. Evita clonar ternas, objetos de volumen y cola de objetos. Inicialización incluida O(S) tiempo, O(S/64+B+C) celdas, mostrando empaquetado. Capacidades<=255 hacen seguro int. Excluye volumen cero; búfer256bytes.

Frente a `1437_bfs.java`: tiempo 0.156 s → 0.109 s; memoria 20420 KB → 4 004 KB.

C++ y Go conservan todos los llenados y trasvases, guardando visitas solo en la superficie de la caja de capacidades. Cada paso deja un recipiente vacío o lleno. Elegir el primero como cara canónica y codificar las otras dos cantidades evita duplicar aristas y esquinas. Con U=256, seis caras U² requieren 49152 bytes de mapa de bits. Cada triple ocupa 24 bits en uint32; la cola tiene como máximo seis U² entradas (1572864 bytes). Un arreglo de 766 marcas sustituye el conjunto de volúmenes. Se comprueban las siete sumas no vacías, excluyendo cero y sin desechar gasolina durante la búsqueda. Para S estados, tiempo O(U²+S) y espacio O(U²), incluida inicialización. Se conservan bases; Java, Python y Rust reutilizan las admitidas.

Las implementaciones base aceptadas [1437_bfs.java](1437_bfs.java), [1437_bfs.py](1437_bfs.py), [1437_bfs.rs](1437_bfs.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1437_bfs_optimized.py`. Tras llenar o verter, cada estado no inicial tiene un recipiente vacío o lleno. Se codifican solo los seis planos frontera en bytes, en vez del cubo completo, manteniendo los movimientos BFS. El límite de estados pasa a O(ab + ac + bc). El programa independiente vacía ambos flujos de salida antes de os._exit(0), evitando la limpieza del intérprete tras escribir la respuesta completa. Cambia el cierre del proceso, no el algoritmo matemático; se conserva la versión sencilla.

Accepted #11328684 (Python 3.12 x64): **0.281 s / 2860 KB**. Comparación archivada: `1437_bfs.py` (Python 3.12 x64) — 0.406 s / 17212 KB (#11286238).

`1437_bfs_optimized.rs`. Se mantienen el algoritmo y los tipos enteros. Los tokens decimales se convierten directamente; los negativos se acumulan con su signo para representar también el mínimo entero con signo. No cambian el almacenamiento de entrada ni la complejidad del algoritmo.

Accepted #11328552 (Rust 1.75 x64): **0.015 s / 3092 KB**. Comparación archivada: `1437_bfs.rs` (Rust 1.75 x64) — 0.062 s / 3104 KB (#11286240).

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1437_bfs_optimized.java`: puesto de tiempo 2/17 y de memoria 2/17 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1437_bfs.cpp](1437_bfs.cpp) | G++ 13.2 x64 | bfs | O(P + S log V) | AC | 0.031 s | 16164 KB | 11286236 |
| [1437_bfs.go](1437_bfs.go) | Go 1.14 x64 | bfs | O(P) | AC | 0.046 s | 10572 KB | 11286237 |
| [1437_bfs.java](1437_bfs.java) | Java 1.8 | bfs | O(P) | AC | 0.156 s | 20420 KB | 11286239 |
| [1437_bfs.py](1437_bfs.py) | Python 3.12 x64 | bfs | O(P) | AC | 0.406 s | 17212 KB | 11286238 |
| [1437_bfs.rs](1437_bfs.rs) | Rust 1.75 x64 | bfs | O(P) | AC | 0.062 s | 3104 KB | 11286240 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1437_bfs_optimized.cpp](1437_bfs_optimized.cpp) | G++ 13.2 x64 | bfs | O(U² + S) | AC | 0.015 s | 332 KB | 11315367 |
| [1437_bfs_optimized.go](1437_bfs_optimized.go) | Go 1.14 x64 | bfs | O(U² + S) | AC | 0.015 s | 1140 KB | 11315371 |
| [1437_bfs_optimized.java](1437_bfs_optimized.java) | Java 1.8 | bfs | O(S) time; O(S/64+B+C) space | AC | 0.109 s | 4004 KB | 11325435 |
| [1437_bfs_optimized.py](1437_bfs_optimized.py) | Python 3.12 x64 | bfs | O(ab + ac + bc) boundary states | AC | 0.281 s | 2860 KB | 11328684 |
| [1437_bfs_optimized.rs](1437_bfs_optimized.rs) | Rust 1.75 x64 | bfs | O(P) | AC | 0.015 s | 3092 KB | 11328552 |
