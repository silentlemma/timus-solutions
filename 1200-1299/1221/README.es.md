# 1221. El mayor cuadrado negro con un rombo blanco dentro

[Timus 1221](https://acm.timus.ru/problem.aspx?space=1&num=1221) · dificultad 424 · implementation

Problema original de Nikita Shamgunov, del séptimo concurso universitario de programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una hoja de `N × N` casillas, `N ≤ 100`, está pintada de negro (1) y
blanco (0). Hay que recortar el mayor cuadrado, con lados sobre la
cuadrícula, que sea negro salvo un cuadrado blanco girado 45 grados cuyos
vértices tocan el centro de sus lados. Se imprime su tamaño, o
`No solution`. La entrada trae varias hojas y termina con `0`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Cada hoja empieza con entero `1 ≤ N ≤ 100`, seguido de N filas de N celdas binarias (`1` negro, `0` blanco), con o sin espacios entre celdas. El `0` final termina la entrada y no es una hoja.

## Salida

Para cada hoja, el tamaño de la mayor figura así o `No solution`.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
1011
0001
1011
1111
1
0
0
```

Salida:

```
3
No solution
```

## Solución

El rombo blanco tiene una casilla central y llega al centro de cada lado,
así que la figura tiene tamaño impar `2r + 1` con `r ≥ 1`: una casilla a
desplazamiento `(d, e)` del centro es blanca exactamente cuando
`|d| + |e| ≤ r`. La fila `d` de la figura es, por tanto, `|d|` casillas
negras, un tramo blanco de `2(r − |d|) + 1` casillas y otra vez `|d|`
negras, y con sumas prefijas de casillas negras por fila cada fila se
comprueba en tiempo constante.

Se prueban los radios de mayor a menor y, para cada uno, todos los
centros; la primera figura encontrada es la respuesta. La mayoría de los
candidatos caen al instante por tres casillas sueltas (el centro y la
punta superior deben ser blancos, la esquina superior izquierda negra), y
el resto suele fallar en la primera fila comprobada. `O(N⁴)` en el peor
caso, mucho menos en la práctica.

Detalles a tener en cuenta:

- una sola casilla blanca no es una figura: el rombo necesita sitio
  dentro de un cuadrado negro, así que la figura más pequeña es de
  3 × 3;
- las figuras solo tienen tamaño impar;
- varias hojas se suceden hasta el `0`.

Las respuestas se compararon con una solución escrita aparte en 300
archivos de hojas aleatorias, con figuras plantadas y de un solo color.

Para S hojas y lado máximo N, la comprobación por filas guarda `O(N²)` entradas vivas de cuadrícula/prefijos y busca en hasta `O(Σ N_i⁴)` tiempo, más lectura de I bytes. C++/Go procesan una hoja y emiten respuestas con búferes acotados. Java guarda todas las respuestas: añade `O(S)` espacio. Python/Rust sencillos retienen además toda la entrada: `O(I + S)` adicional a la hoja `O(N²)`; Python mantiene también lista plana temporal. Python optimizado lee bloques acotados y usa bytes para celdas/prefijos (cuentas por fila≤100), pero conserva las S respuestas: espacio `O(N² + S + B + T)` con bloque B y token máximo T, sin entrada completa. Sigue buscando en O(N⁴), no usa prefijos transformados. Go de prefijos tiene tablas lógicas O(N²), pero arrays reales fijos M=100 con 101²+200² entradas uint16 más búferes. Limpiar cuesta O(M²) por hoja, construir O(N²), buscar O(N³); espacio asignado O(M²+B) incluso con hoja pequeña.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

Go usa dos tablas de prefijos 2D de celdas blancas: la cuadrícula original y la transformación u=row+column, v=row−column+N−1. El rombo de radio r se convierte en rectángulo; los huecos de paridad aportan cero. Contiene A=2r(r+1)+1 celdas reales. Se exigen A blancas en ese rectángulo y exactamente A en el cuadrado exterior de lado 2r+1. Así el rombo es totalmente blanco y el resto negro. Cada comprobación cuesta O(1); todos los centros y radios, O(N³), con preparación y espacio O(N²). Los conteos ≤10000 caben en uint16.

El envío aceptado en Go 1.14 x64 tarda 0.031 s frente a 0.001 s de la base y usa 352 KB frente a 2116 KB.

La caché exacta y los [criterios compartidos](../../RATING_CRITERIA.md) confirman todas salvo Python sencillo. Python rápido es #11328771 con 0.156 s / 924 KB: bajo 1024 KB solo exige tiempo. La base #11283692 de 0.140 s / 1908 KB cumple tiempo pero falla memoria exigida (límite 901.6 KB). Puede cumplir una ejecución registrada algo más lenta sin afirmar aceleración algorítmica. C++/Java/Rust y Go optimizado solo comparan tiempo; Go sencillo con 2116 KB necesita ambas y grupo del mismo lenguaje. Python/Rust usan referencias exactas aplicables. Las bases didácticas significativas quedan sin estrella, y los pares se conservan.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1221_implementation_optimized.py`. Las filas y sus sumas prefijas se guardan en arreglos compactos de bytes. Se procesan las cuadrículas sucesivamente, conservando la búsqueda de la figura mayor y sus condiciones. El programa independiente vacía ambos flujos de salida antes de os._exit(0), evitando la limpieza del intérprete tras escribir la respuesta completa. Cambia el cierre del proceso, no el algoritmo matemático; se conserva la versión sencilla.

Accepted #11328771 (Python 3.12 x64): **0.156 s / 924 KB**. Comparación archivada: `1221_implementation.py` (Python 3.12 x64) — 0.14 s / 1908 KB (#11283692).

Accepted #11328771 y su admisión numérica corresponden al fuente histórico exacto. El linter exige nombrar `WHITESPACE_LIMIT` el límite existente de blancos 32; invertir la sustitución restaura exactamente los bytes previos. Se conservan algoritmo, comentarios y Python sencillo. El hash nuevo requiere Accepted propio en el lote posterior; el par anterior no certifica bytes nuevos.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes leen las casillas cifra a cifra, así que valen las
  filas con o sin espacios.

## Evaluación

`tests/tests.json` usa `lines`: conserva orden de hojas y una línea por respuesta, ignorando blancos iniciales/finales y repetidos dentro de cada línea. Importan número de líneas, texto/mayúsculas (`No solution`) y orden de tokens; no se responde al 0 final. El ejemplo propio y casos pequeños se verifican comparando cada celda candidata con el color por distancia Manhattan, sin prefijos.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1221_implementation.cpp](1221_implementation.cpp) | G++ 13.2 x64 | implementation | O(N⁴) | AC | 0.015 s | 316 KB | 11283690 |
| [1221_implementation.go](1221_implementation.go) | Go 1.14 x64 | implementation | O(N⁴) | AC | 0.001 s | 2116 KB | 11283691 |
| [1221_implementation.java](1221_implementation.java) | Java 1.8 | implementation | O(N⁴) | AC | 0.062 s | 936 KB | 11283693 |
| [1221_implementation.py](1221_implementation.py) | Python 3.12 x64 | implementation | O(N⁴) | AC | 0.14 s | 1908 KB | 11283692 |
| [1221_implementation.rs](1221_implementation.rs) | Rust 1.75 x64 | implementation | O(N⁴) | AC | 0.031 s | 500 KB | 11283694 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1221_prefix_sums.go](1221_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N³) | AC | 0.031 s | 352 KB | 11314933 |
| [1221_implementation_optimized.py](1221_implementation_optimized.py) | Python 3.12 x64 | implementation | O(N⁴) | AC | 0.171 s | 932 KB | 11331077 |
