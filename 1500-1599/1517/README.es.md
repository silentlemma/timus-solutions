# 1517. La subcadena común más larga

[Timus 1517](https://acm.timus.ru/problem.aspx?space=1&num=1517) · dificultad 240 · suffix_structures

Problema original de Ilya Grebnov, Nikita Rybak y Dmitry Kovalioff, de Timus Top Coders: Third Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan dos cadenas de letras latinas mayúsculas, cada una de longitud `N`, `1 ≤ N ≤ 100000`. Imprime cualquier subcadena contigua de longitud máxima presente en ambas; si no comparten ninguna letra, imprime una línea vacía. Tiempo: 2 segundos. Memoria: 64 MB.

## Entrada

El entero `N`, seguido de las dos cadenas en líneas separadas.

## Salida

Una subcadena común más larga, o una línea vacía si su longitud es cero.

## Evaluación

Se acepta cualquier respuesta óptima. Se verifica que aparezca en ambas cadenas y que su longitud sea máxima; los empates no tienen que coincidir con el ejemplo.

## Ejemplos

### Ejemplo 1

Entrada:

```
28
VOTEFORTHEGREATALBANIAFORYOU
CHOOSETHEGREATALBANIANFUTURE
```

Salida:

```
THEGREATALBANIA
```

## Solución

Construye el autómata de sufijos de la primera cadena. Un estado agrupa
subcadenas con las mismas posiciones finales y guarda longitud máxima,
enlace de sufijo y transiciones. Cada extensión crea un estado nuevo;
si un destino tiene longitud excesiva, se divide su clase mediante un
clon y se redirigen las transiciones correspondientes.

Recorre la segunda cadena manteniendo el sufijo más largo del prefijo
leído que aparece en la primera. Si falta la transición, sigue enlaces
de sufijo acortando la coincidencia hasta encontrarla o alcanzar la raíz.
La mayor longitud y su posición final reconstruyen la respuesta. Toda
subcadena común es sufijo de algún prefijo leído, así que el máximo es
óptimo. Los enlaces reducen la longitud y cada carácter la aumenta a lo
sumo en uno: el recorrido total es lineal.

Hay `O(N)` estados y transiciones. Con el alfabeto fijo de 26 letras,
tiempo y espacio son `O(N)`. Las versiones nativas sencillas guardan filas
completas de transiciones; Python usa diccionarios. Las cinco fuentes
legibles se conservan sin cambios.

## Soluciones optimizadas

`1517_suffix_structures_optimized.py`. Conserva el autómata de sufijos, con una fila densa de 26 índices de transición de 32 bits por cada uno de hasta 2N+1 estados. Longitudes y enlaces usan arrays compactos. El clon copia su fila antes de redirigir enlaces. Evita buscar listas de aristas y diccionarios, reservando 26 entradas por estado. Recorre la segunda cadena con retrocesos por enlaces y devuelve una subcadena común máxima. O(26N+M) tiempo, O(26N) estado más las dos cadenas; conserva la base con diccionarios.

Accepted exacto PyPy 3.10 #11326700: 0.234 s / 25000 KB. Comparación guardada 2026-11-20 de compiladores actuales: tiempo 1/32, memoria 9/32. Ambas métricas exigidas pasan diez primeros o 15% superior, redondeando el corte porcentual hacia arriba. El asterisco sigue la meta separada Python de primer puesto en ambas.

El envío optimizado documentado antes #11308173 (Python 3.12 x64) registró 1.312 s / 9736 KB. El actual PyPy 3.10 registra menor tiempo y mayor memoria. Son medidas emparejadas de ejecuciones distintas; la comparación incluye elección de intérprete y variabilidad del juez.

- `1517_suffix_structures_optimized.py`: 0.234 s / 25000 KB; base didáctica conservada `1517_suffix_structures.py` (Python 3.12 x64): 0.5 s / 56240 KB.

C++, Go, Java y Rust conservan arrays dispersos: una cabeza por estado y letra, destino e índice siguiente por arista. Cada búsqueda recorre hasta 26 aristas; el clon copia su lista antes de redirecciones. Con N<=100000 índices/longitudes caben en 32 bits. Estas cuatro versiones mantienen O(N) trabajo/espacio con alfabeto fijo y menor constante de memoria. La tabla conserva Accepted y comparación de 2 noviembre 2026; Go registró 0.078 s frente a base 0.046 s, un compromiso tiempo/espacio.

Reducciones de memoria registradas frente a las bases de la tabla: C++ 82.9%, Go 70.6%, Java 81.1%, Python 55.5%, Rust 81.0%.

## Notas por lenguaje

El programa Python actual pasó 58 entradas locales en CPython 3.12 y otras 58 en PyPy 3.10 antes de su propio Accepted. Arriba se describe su representación densa; la tabla registra la ejecución PyPy aceptada.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1517_suffix_structures.cpp](1517_suffix_structures.cpp) | G++ 13.2 x64 | suffix_structures | O(N) | AC | 0.093 s | 29044 KB | 11287349 |
| [1517_suffix_structures.go](1517_suffix_structures.go) | Go 1.14 x64 | suffix_structures | O(N) | AC | 0.046 s | 25012 KB | 11287350 |
| [1517_suffix_structures.java](1517_suffix_structures.java) | Java 1.8 | suffix_structures | O(N) | AC | 0.203 s | 35156 KB | 11287352 |
| [1517_suffix_structures.py](1517_suffix_structures.py) | Python 3.12 x64 | suffix_structures | O(N) | AC | 0.500 s | 56240 KB | 11287351 |
| [1517_suffix_structures.rs](1517_suffix_structures.rs) | Rust 1.75 x64 | suffix_structures | O(N) | AC | 0.062 s | 28496 KB | 11287353 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1517_suffix_structures_optimized.cpp](1517_suffix_structures_optimized.cpp) | G++ 13.2 x64 | suffix_structures | O(N) | AC | 0.062 s | 4968 KB | 11308174 |
| [1517_suffix_structures_optimized.go](1517_suffix_structures_optimized.go) | Go 1.14 x64 | suffix_structures | O(N) | AC | 0.078 s | 7356 KB | 11308176 |
| [1517_suffix_structures_optimized.java](1517_suffix_structures_optimized.java) | Java 1.8 | suffix_structures | O(N) | AC | 0.156 s | 6652 KB | 11308178 |
| [1517_suffix_structures_optimized.py](1517_suffix_structures_optimized.py) | PyPy 3.10 x64 | suffix_structures | O(26N+M) time; O(26N+M) space | AC | 0.234 s | 25000 KB | 11326700 |
| [1517_suffix_structures_optimized.rs](1517_suffix_structures_optimized.rs) | Rust 1.75 x64 | suffix_structures | O(N) | AC | 0.062 s | 5408 KB | 11308179 |
