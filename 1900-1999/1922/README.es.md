# 1922. Equipos que impiden cualquier incorporación individual

[Timus 1922](https://acm.timus.ru/problem.aspx?space=1&num=1922) · difficulty 322 · sorting

Problema original de Grigoriy Nazarov, del concurso escolar regional de los Urales de 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n participantes. La persona i acepta un equipo solo si su tamaño
total es al menos aᵢ, contando a esa misma persona. Un equipo no vacío
es efectivo si todos sus miembros aceptan el tamaño. Es fiable si
añadir cualquier persona externa, una sola, lo vuelve inefectivo.
Un equipo efectivo con todas las personas también es fiable.
Enumerar todos los equipos fiables distintos. El vacío no se cuenta.
Límites: 1 segundo, 64 MB.

## Entrada

Primero n, 1≤n≤1000. Después n líneas con aᵢ, 1≤aᵢ≤1000.
Un umbral puede superar n. Los índices originales son de 1 a n.

## Salida

Imprimir la cantidad k. En cada una de las siguientes k líneas, escribir
el tamaño y los índices originales del equipo. Tanto los equipos como
sus miembros admiten cualquier orden. Si no hay equipos, imprimir `0`
sin descripción adicional.

## Evaluación

Un comprobador propio verifica equipos no vacíos, índices válidos distintos,
efectividad, fallo de cada incorporación individual, ausencia de equipos
repetidos y completitud. Ignora los órdenes y no exige una salida canónica.

## Ejemplos

```
5
1
3
3
6
6
```

```
2
1 1
3 2 1 3
```

## Solución

Sea S un equipo efectivo de tamaño s. Todos sus miembros tienen aᵢ≤s,
por lo que aumentar a s+1 no perjudica a ninguno. Añadir una persona
externa j funciona exactamente si aⱼ≤s+1. La fiabilidad equivale a que
todas las personas externas tengan umbral mayor que s+1.

Por tanto, cada persona con aᵢ≤s debe pertenecer a S. Nadie puede tener
umbral s+1: dentro rompería la efectividad y fuera podría incorporarse.
Existe como máximo un equipo fiable por tamaño: todas las personas
con umbral a lo sumo s, siempre que sean exactamente s y ninguna tenga s+1.

Ordenamos pares (umbral, índice original). Para cada s=1..n comprobamos:

```text
máximo umbral de los primeros s pares ≤ s;
y s=n, o el siguiente umbral > s+1.
```

Si se cumplen, imprimimos esos primeros s índices. La primera condición
garantiza efectividad y la segunda bloquea a todas las personas externas.
Recíprocamente, el argumento anterior fuerza a cualquier equipo fiable
a ser ese prefijo, así que no hay omisiones ni repeticiones. Umbrales
iguales no pueden separarse en una frontera válida; su orden no añade equipos.

Para s=n aún hay que comprobar efectividad: un umbral mayor que n
impide que el conjunto completo sea efectivo.

La definición habla de una incorporación, no de maximalidad entre todos
los superconjuntos efectivos. Con umbrales 1,3,3, tanto el equipo de una
persona como el de tres son fiables. Las dos personas de umbral 3 no
pueden incorporarse por separado al primero, aunque juntas sí podrían.

Sea R la cantidad total de índices impresos. Tiempo O(n log n+R) y
espacio O(n+R) al almacenar equipos y salida. Esta puede ser cuadrática:
2,2,4,4,…,1000,1000 genera 500 equipos y 250 500 índices.
Enumerarlos exige ese trabajo de salida.

El umbral externo debe ser estrictamente mayor que s+1, no solo s.
Los internos pueden igualar s. Excluir el vacío, permitir cero respuestas
y mantener índices desde uno. Los umbrales repetidos son personas distintas,
pero no crean equipos fiables alternativos del mismo tamaño.
No sustituir la incorporación individual por maximalidad global ni omitir R.

## Soluciones optimizadas

`1922_sorting_optimized.java`. Conserva equipos fiables como prefijos ordenados: umbral del último<=size y del siguiente ajeno, si existe,>size+1. Empaqueta umbral e ID en long y guarda solo longitudes válidas. Emite miembros desde el orden al necesitarlos, sin copiar prefijos ni retener toda la salida. Con Z IDs emitidos y coste S(N) de ordenar, tiempo O(N+S(N)+Z), usualmente O(N log N+Z), y espacio O(N) aunque Z sea cuadrático. Cero equipos emite solo cero. Empates siguen ID; cualquier orden válido se acepta.

Frente a `1922_sorting.java`: tiempo 0.109 s → 0.125 s; memoria 9 504 KB → 512 KB.

Las versiones en C++, Go y Rust guardan el umbral y el índice original en un solo entero. El índice ocupa los diez bits inferiores, así que al ordenar estos enteros se compara primero el umbral. La condición en cada frontera sigue siendo la misma. Se guardan solo los tamaños de los equipos fiables y luego se imprime directamente cada prefijo ordenado. Si se imprimen R índices, el tiempo es O(n log n + R) y el espacio es O(n).

La revisión C++ conserva la ordenación empaquetada y la misma prueba de prefijos válidos, con búferes de entrada y salida de 16 KB. Su Accepted de fuente exacto mide 0.015 s / 152 KB; la base didáctica, 0.015 s / 1452 KB. La comprobación de clasificación de C++ usa la instantánea guardada del 20 de noviembre de 2026.

Las implementaciones base aceptadas [1922_sorting.java](1922_sorting.java), [1922_sorting.py](1922_sorting.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1922_sorting_optimized.py`. Solo se guarda y ordena el prefijo fiable de equipos. Los registros posteriores actualizan el resultado al leerse, sin retener la lista completa; la regla de orden no cambia. El programa independiente vacía ambos flujos de salida antes de os._exit(0), evitando la limpieza del intérprete tras escribir la respuesta completa. Cambia el cierre del proceso, no el algoritmo matemático; se conserva la versión sencilla.

Accepted #11328776 (Python 3.12 x64): **0.078 s / 1788 KB**. Comparación archivada: `1922_sorting.py` (Python 3.12 x64) — 0.093 s / 7584 KB (#11325598).

## Notas por lenguaje

Las incorporaciones anteriores se compararon con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Conserva los algoritmos didácticos. Las filas básicas revalidadas usan sus nuevas métricas e IDs de Accepted de fuente exacta; estas pruebas no cuentan como optimizaciones.

`1922_sorting_optimized.java`: puesto de tiempo 4/18 y de memoria 1/18 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1922_sorting.cpp](1922_sorting.cpp) | G++ 13.2 x64 | sorting | O(n*log(n) + R) | AC | 0.015 s | 1452 KB | 11291505 |
| [1922_sorting.go](1922_sorting.go) | Go 1.14 x64 | sorting | O(n*log(n) + R) | AC | 0.062 s | 5648 KB | 11291507 |
| [1922_sorting.java](1922_sorting.java) | Java 1.8 | sorting | O(n*log(n) + R) | AC | 0.109 s | 9504 KB | 11325561 |
| [1922_sorting.py](1922_sorting.py) | Python 3.12 x64 | sorting | O(n*log(n) + R) | AC | 0.093 s | 7584 KB | 11325598 |
| [1922_sorting.rs](1922_sorting.rs) | Rust 1.75 x64 | sorting | O(n*log(n) + R) | AC | 0.015 s | 4040 KB | 11291512 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1922_sorting_optimized.cpp](1922_sorting_optimized.cpp) | G++ 13.2 x64 | sorting | O(n*log(n) + R) | AC | 0.015 s | 152 KB | 11326637 |
| [1922_sorting_optimized.go](1922_sorting_optimized.go) | Go 1.14 x64 | sorting | O(n*log(n) + R) | AC | 0.031 s | 932 KB | 11310396 |
| [1922_sorting_optimized.rs](1922_sorting_optimized.rs) | Rust 1.75 x64 | sorting | O(n*log(n) + R) | AC | 0.015 s | 216 KB | 11310393 |
| [1922_sorting_optimized.java](1922_sorting_optimized.java) | Java 1.8 | sorting | O(N+S(N)+Z) | AC | 0.125 s | 512 KB | 11325025 |
| [1922_sorting_optimized.py](1922_sorting_optimized.py) | Python 3.12 x64 | sorting | O(n*log(n) + R) | AC | 0.078 s | 1788 KB | 11328776 |
