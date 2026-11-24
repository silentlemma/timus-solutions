# 1197. Cuántas casillas ataca un caballo solitario

[Timus 1197](https://acm.timus.ru/problem.aspx?space=1&num=1197) · dificultad 28 · implementation

Problema original del folclore, del Quinto Campeonato por Equipos de Programación para Escolares, 2 de marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un caballo está solo en un tablero de ajedrez. Para cada una de las
`N ≤ 64` casillas dadas, hay que contar cuántas casillas del tablero
ataca el caballo desde ahí.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` casillas en notación de ajedrez: una letra de la `a` a la
`h` para la columna y una cifra del `1` al `8` para la fila.

## Salida

Para cada casilla, el número de casillas atacadas en su propia línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
a1
d4
g6
```

Salida:

```
2
8
6
```

## Solución

El caballo tiene ocho saltos posibles: dos casillas en una dirección y
una en la perpendicular. Se prueban los ocho y se cuentan los que caen
dentro del tablero. `O(N)`.

Detalles a tener en cuenta:

- cerca de un borde o de una esquina solo algunos saltos quedan dentro
  del tablero, así que hay que comprobar las dos coordenadas de cada
  salto;
- la letra es la columna y la cifra la fila, pero el tablero es
  simétrico, así que confundirlas no cambia la respuesta.

Las respuestas se compararon con una solución escrita aparte en las 64
casillas.

## Soluciones optimizadas

`1197_implementation_optimized.java`. Java cuenta las mismas ocho jugadas de caballo factorizando elecciones independientes por eje. oneX/twoX cuentan los desplazamientos horizontales válidos de una/dos casillas; oneY/twoY hacen lo mismo en vertical. La respuesta es oneX*twoY+twoX*oneY y ambas formas son disjuntas. Elimina el bucle de saltos y arreglos bidimensionales sin una tabla de respuestas. Un búfer de 256 bytes lee coordenadas directamente. Cada respuesta tiene una cifra: el arreglo de salida ocupa exactamente 2*N bytes con saltos de línea. Tiempo O(N), almacenamiento de respuesta O(N), resto fijo. Conserva las bases de enumeración.

Accepted exacto Java 1.8 #11327340: 0.078 s / 192 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 82/745, memoria 1/745. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11303722 era 0.109 s / 296 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1197_implementation_optimized.java`: 0.078 s / 192 KB; base didáctica conservada `1197_implementation.java`: 0.093 s / 1576 KB.

La solución optimizada en C++ lee con `getchar` en lugar de `iostream` y
cuenta los saltos sin tabla. Un salto mueve una coordenada 1 y la otra 2,
cada una en cualquier sentido, y las elecciones de las dos coordenadas
son independientes; por eso la cuenta es
`ways(x, 1) · ways(y, 2) + ways(x, 2) · ways(y, 1)`, donde `ways(p, s)`
dice cuántos de `p - s` y `p + s` quedan dentro del tablero. La solución
ocupa 84 KB en lugar de 396 KB, con el mismo tiempo.

## Notas por lenguaje

- Las soluciones sencillas guardan los ocho saltos en una tabla y la
  recorren.

Leer cada coordenada del tablero en un arreglo de dos bytes y escribir los recuentos en un búfer de bytes. El envío aceptado 11301829 tardó 0.001 s y usó 908 KB. La versión sencilla tardó 0.015 s y usó 1072 KB.

Consultar la tabla del tablero fijo, generada por 1197_math_table.py a partir de los saltos legales del caballo. Leer los bytes directamente y vaciar las respuestas antes de llamar a os._exit(0), omitiendo la limpieza del intérprete. El envío aceptado 11324662 tardó 0.093 s y usó 200 KB. La versión sencilla tardó 0.046 s y usó 328 KB. El tiempo registrado es mayor que el de la versión sencilla.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1197_implementation.cpp](1197_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.001 s | 396 KB | 11283494 |
| [1197_implementation.go](1197_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1072 KB | 11283496 |
| [1197_implementation.java](1197_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 1576 KB | 11283500 |
| [1197_implementation.py](1197_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.046 s | 328 KB | 11283499 |
| [1197_implementation.rs](1197_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 216 KB | 11283504 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1197_implementation_optimized.cpp](1197_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.001 s | 84 KB | 11303578 |
| [1197_implementation_optimized.java](1197_implementation_optimized.java) | Java 1.8 | implementation | O(N) time; O(N) answer space | AC | 0.078 s | 192 KB | 11327340 |
| [1197_implementation_optimized.go](1197_implementation_optimized.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.001 s | 908 KB | 11301829 |
| [1197_math.py](1197_math.py) \* | PyPy 3.10 x64 | math | O(N) | AC | 0.093 s | 200 KB | 11324662 |

\* Las soluciones marcadas aún no alcanzan sus objetivos de tiempo y memoria en los compiladores admitidos y pueden optimizarse más.
