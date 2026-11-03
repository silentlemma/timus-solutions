# 1033. El área visible de las paredes de un laberinto

[Timus 1033](https://acm.timus.ru/problem.aspx?space=1&num=1033) · dificultad 237 · bfs, bitmask, dfs, graphs

Problema original de Vladimir Pinaev, del III Campeonato Universitario por Equipos de Programación de los Urales, 1999.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un laberinto es una cuadrícula `N × N` (`3 ≤ N ≤ 33`) de celdas de 3 × 3
metros: `.` es vacía y `#` es un bloque macizo. El laberinto está rodeado
por un muro exterior, salvo en las celdas superior izquierda e inferior
derecha, que son las dos entradas (siempre vacías). Las paredes miden 3
metros de alto. Un visitante camina entre celdas vacías que comparten un
lado; los bloques que se tocan por una esquina no dejan hueco. Halla el área
total de las superficies de pared que un visitante puede ver desde las
partes del laberinto alcanzables desde las entradas.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas de `N` caracteres `.` y `#`.

## Salida

El área de pared visible en metros cuadrados.

## Evaluación

Comparar un token entero. Rust pasó 569 ejecuciones contra BFS por casilla: 128 laberintos 3x3 con esquinas libres, aleatorios, lados 31/32/33, entradas juntas/separadas, espacios/fronteras de bloque y 11 casos del repositorio.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
....
.##.
.#..
....
```

Salida:

```
180
```

### Ejemplo 2

Entrada:

```
3
...
...
...
```

Salida:

```
72
```

## Solución

Una cara visible es un lado de una casilla vacía alcanzable desde una
entrada que mira a un bloque o al borde exterior. Se recorre por cuatro
vecinos desde ambas entradas, marcando al insertar para no duplicar una
componente compartida. Se cuenta cada lado hacia `#` o fuera del tablero;
no se cuentan lados hacia otra casilla vacía.

Así se enumeran exactamente las caras visibles: cada una tiene una única
casilla vacía incidente y esta debe ser alcanzable. Distintas caras de un
mismo bloque cuentan por separado; las salas cerradas quedan excluidas.
Se restan los cuatro lados exteriores de las dos esquinas de entrada,
que son aberturas, y se multiplica por 9: anchura 3 m y altura 3 m.

Las bases C++, Go, Java y Rust usan cola de casillas; Python usa pila.
El orden no cambia el conjunto ni la cuenta. Cada casilla se inserta una
vez y tiene cuatro vecinos: `O(N²)` tiempo y espacio. Solo los lados
compartidos permiten pasar; el contacto diagonal no. Las entradas pueden
estar desconectadas.

## Soluciones optimizadas

Los C++/Java/Python de máscaras agrupan operaciones horizontales en palabras de anchura acotada; el Python previo conserva todos los tokens y sigue usando almacenamiento cuadrático. Se preservan los BFS/DFS por casilla para enseñar.

Rust inunda máscaras sin asignaciones dinámicas. Marca ambas entradas, cierra horizontalmente la fila cambiada dentro de casillas abiertas y propaga bits nuevos a filas vecinas. Un bitmap evita duplicar filas; cola circular fija y contador explícito permiten las N filas simultáneamente. Cada planificación y expansión horizontal se carga a una casilla nueva: `O(N²)` operaciones de palabra. N≤33 cabe en 64 bits. Contar las cuatro direcciones de pared con popcount, incluir el borde externo y restar cuatro caras de entrada antes de multiplicar por nueve. La unión de componentes se cuenta una vez. Solo retiene máscaras, índices y 128 bytes de entrada. POSIX read/write manejan buffers acotados directamente sin stdio ni formateador; el decimal se convierte en un array fijo. Lecturas, desplazamientos e índices respetan la cota.

- `1033_graphs_bitmask.cpp`: 0.001 s / 112 KB; base `1033_bfs.cpp`: 0.001 s / 416 KB; cambio respecto a la base: tiempo -0.0%, memoria -73.1%.
- `1033_graphs_bitmask.java`: 0.078 s / 376 KB; base `1033_bfs.java`: 0.125 s / 1644 KB; cambio respecto a la base: tiempo -37.6%, memoria -77.1%.
- `1033_graphs_bitmask.py`: 0.046 s / 576 KB; base `1033_dfs.py`: 0.078 s / 452 KB; cambio respecto a la base: tiempo -41.0%, memoria +27.4%.
- `1033_graphs_bitmask.rs`: 0.015 s / 140 KB; base `1033_bfs.rs`: 0.015 s / 228 KB; cambio respecto a la base: tiempo -0.0%, memoria -38.6%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1033_bfs.cpp`; fuente que cubre `1033_graphs_bitmask.cpp`; puestos tiempo/memoria 1/3, registros de otros autores 119/119.

- Go: base didáctica preferida `1033_bfs.go`; fuente que cubre `1033_bfs.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1033_bfs.java`; fuente que cubre `1033_graphs_bitmask.java`; puestos tiempo/memoria 1/1, registros de otros autores 7/7.

- Python/PyPy: base didáctica preferida `1033_dfs.py`; fuente que cubre `1033_graphs_bitmask.py`; puestos tiempo/memoria 2/2, registros de otros autores 29/29.

- Rust: base didáctica preferida `1033_bfs.rs`; fuente que cubre `1033_graphs_bitmask.rs`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1033_bfs.cpp](1033_bfs.cpp) | G++ 13.2 x64 | bfs | O(N^2) time and total space | AC | 0.001 s | 416 KB | 11278438 |
| [1033_bfs.go](1033_bfs.go) | Go 1.14 x64 | bfs | O(N^2) time and total space | AC | 0.015 s | 1124 KB | 11278439 |
| [1033_bfs.java](1033_bfs.java) | Java 1.8 | bfs | O(N^2) time and total space | AC | 0.125 s | 1644 KB | 11278443 |
| [1033_dfs.py](1033_dfs.py) | Python 3.12 x64 | dfs | O(N^2) time and total space | AC | 0.078 s | 452 KB | 11278441 |
| [1033_bfs.rs](1033_bfs.rs) | Rust 1.75 x64 | bfs | O(N^2) time and total space | AC | 0.015 s | 228 KB | 11278445 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1033_graphs_bitmask.cpp](1033_graphs_bitmask.cpp) | G++ 13.2 x64 | graphs, bitmask | O(N^2) time and total space | AC | 0.001 s | 112 KB | 11308624 |
| [1033_graphs_bitmask.java](1033_graphs_bitmask.java) | Java 1.8 | graphs, bitmask | O(N^2) time and total space | AC | 0.078 s | 376 KB | 11308630 |
| [1033_graphs_bitmask.py](1033_graphs_bitmask.py) \* | Python 3.12 x64 | graphs, bitmask | O(N^2) time and total space | AC | 0.046 s | 576 KB | 11308634 |
| [1033_graphs_bitmask.rs](1033_graphs_bitmask.rs) | Rust 1.75 x64 | graphs, bitmask | O(N^2) time; O(N) masks/buffer | AC | 0.015 s | 140 KB | 11309560 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
