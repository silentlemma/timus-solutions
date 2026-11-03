# 1944. Un mapa ASCII con prioridad para los puntos

[Timus 1944](https://acm.timus.ru/problem.aspx?space=1&num=1944) · difficulty 238 · implementation

Original problem from Open Ural FU Personal Contest 2012 | by Andrey Demidov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dibujar puntos enteros distintos en una cuadrícula cartesiana: x crece
a la derecha e y hacia arriba, una celda por coordenada. Usar * para
puntos, + para origen, - para eje x, | para eje y y . como fondo.
Un punto tapa ejes y origen; incluso pueden ocultarse todos los ejes.
Dibujar el rectángulo mínimo que contiene puntos y origen.
Límites: 1 segundo, 64 MB.

## Entrada

n con 1≤n≤250, seguido de n pares enteros distintos (x,y), −100≤x,y≤100.
No hay dos puntos coincidentes.

## Salida

Filas desde U=max(0,max y) bajando hasta D=min(0,min y), inclusive.
Columnas desde L=min(0,min x) hasta R=max(0,max x). Hay H=U−D+1 filas
de W=R−L+1 símbolos. Imprimir solo el dibujo.

## Evaluación

Se compara cada símbolo y salto de línea del dibujo completo, no solo
tokens separados por espacios. Cada programa nuevo publicado pasó los 26
casos del repositorio y 69 entradas extra independientes en su compilador
Docker objetivo. Se volvieron a leer las salidas reales y códigos de salida
contra un oráculo independiente por coordenada: punto ocupado, origen,
ejes y fondo. Se cubren origen, una fila o columna, ejes ocultos, cuadrantes,
±100, 250 puntos, signo más explícito, CRLF y EOF. El candidato Python
separado también pasó esas 69 ejecuciones objetivo y 2048 ejecuciones en
el anfitrión, incluidos todos los subconjuntos no vacíos de la rejilla 3×3.
Esas 2048 no se atribuyen a C++ o Java. Los tres candidatos tienen Accepted
de sus bytes exactos; el criterio de admisión se comprueba por separado.

## Ejemplos

```
8
-10 5
-7 3
-4 2
-9 4
0 1
6 -1
3 0
8 -3
```

```
*.........|........
.*........|........
...*......|........
......*...|........
..........*........
----------+--*-----
..........|.....*..
..........|........
..........|.......*
```

## Solución

Iniciar los cuatro límites en cero y ampliarlos con los puntos.
(x,y) se transforma en row=U−y, column=x−L, biyección a índices
0..H−1 y 0..W−1 con la orientación requerida.

Rellenar una matriz H×W de puntos. Poner | en columna −L de cada fila.
Rellenar fila U de -, después cambiar su columna −L por +. Finalmente
sobrescribir con * cada punto de entrada. Emitir filas en orden de índice.

El relleno representa el fondo; las dos pasadas marcan exactamente x=0
e y=0. Su intersección se sustituye por + y la última pasada da prioridad
a los puntos, que se mapean a celdas distintas. Los límites iniciados
en cero incluyen el origen aunque todos los puntos estén en un cuadrante;
ningún rectángulo menor contiene todas las coordenadas necesarias.
Así quedan probados forma, símbolos y orientación, incluso con una fila
o una columna.

Tiempo y espacio O(n+WH), incluyendo puntos y salida. W,H≤201 y la
salida máxima ocupa H(W+1)≤40602 bytes ASCII con saltos, menos de 64 KiB.
Los índices y límites caben en enteros ordinarios con signo.

Incluir cero en ambos rangos. Al crecer la fila disminuye y; no confundir
desplazamientos de fila/columna. El origen solo es + si no hay punto;
un punto sobre un eje sigue siendo *. No añadir etiquetas, espacios,
marcos o márgenes.

## Soluciones optimizadas

Se dibuja por filas sin asignar toda la cuadrícula. Ordenar coordenadas empaquetadas agrupa los puntos de cada fila. Se rellena el fondo y eje visible, se construyen eje horizontal y origen cuando corresponda y se superponen los puntos al final. Se conservan prioridades y orden vertical decreciente. El búfer se reutiliza: la memoria depende de puntos y anchura, no del área. Ordenar no elimina el tiempo de imprimir cada celda.

- `1944_implementation_optimized.cpp`: 0.015 s / 116 KB; base `1944_implementation.cpp`: 0.015 s / 472 KB; cambio respecto a la base: tiempo -0.0%, memoria -75.4%.
- `1944_implementation_optimized.java`: 0.125 s / 476 KB; base `1944_implementation.java`: 0.125 s / 844 KB; cambio respecto a la base: tiempo -0.0%, memoria -43.6%.
- `1944_implementation_optimized.py`: 0.140 s / 332 KB; base `1944_implementation.py`: 0.093 s / 636 KB; cambio respecto a la base: tiempo +50.5%, memoria -47.8%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1944_implementation.cpp`; versión que cubre `1944_implementation_optimized.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 50/50.

- Go: base didáctica preferida `1944_implementation.go`; versión que cubre `1944_implementation.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1944_implementation.java`; versión que cubre `1944_implementation.java`; puestos tiempo/memoria 1/1, registros de otros autores 2/2.

- Python/PyPy: base didáctica preferida `1944_implementation.py`; versión que cubre `1944_implementation_optimized.py`; puestos tiempo/memoria 11/1, registros de otros autores 11/11.

- Rust: base didáctica preferida `1944_implementation.rs`; versión que cubre `1944_implementation.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1944_implementation.cpp](1944_implementation.cpp) | G++ 13.2 x64 | implementation | O(n+WH) | AC | 0.015 s | 472 KB | 11291904 |
| [1944_implementation.go](1944_implementation.go) | Go 1.14 x64 | implementation | O(n+WH) | AC | 0.031 s | 1420 KB | 11291906 |
| [1944_implementation.java](1944_implementation.java) | Java 1.8 | implementation | O(n+WH) | AC | 0.125 s | 844 KB | 11291912 |
| [1944_implementation.py](1944_implementation.py) | Python 3.12 x64 | implementation | O(n+WH) | AC | 0.093 s | 636 KB | 11291907 |
| [1944_implementation.rs](1944_implementation.rs) | Rust 1.75 x64 | implementation | O(n+WH) | AC | 0.031 s | 348 KB | 11291920 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1944_implementation_optimized.cpp](1944_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N log N+WH) | AC | 0.015 s | 116 KB | 11308709 |
| [1944_implementation_optimized.java](1944_implementation_optimized.java) | Java 1.8 | implementation | O(N log N+WH) | AC | 0.125 s | 476 KB | 11308715 |
| [1944_implementation_optimized.py](1944_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(N log N+WH) | AC | 0.140 s | 332 KB | 11309399 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
