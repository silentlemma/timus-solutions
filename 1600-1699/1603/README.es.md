# 1603. Erudito

[Timus 1603](https://acm.timus.ru/problem.aspx?space=1&num=1603) · dificultad 255 · implementation

Problema original de Vladimir Yakovlev, del IX Campeonato Abierto Individual de la Universidad Estatal de los Urales, 1 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cuadrícula de 4 × 4 contiene letras minúsculas. Una palabra puede
escribirse en ella a lo largo de un camino de casillas vecinas en
horizontal o vertical, que puede girar en ángulo recto en cualquier
punto pero no pasa dos veces por la misma casilla. Para cada una de hasta
100 palabras de 1 a 16 letras hay que decir si se puede encontrar.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Cuatro filas de la cuadrícula, luego n y las palabras.

## Salida

`word: YES` o `word: NO` para cada palabra.

## Evaluación

Se compara la salida completa, incluidos espacios y saltos de línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
abra
adac
babr
arca
3
abracadabra
ababaab
ababaaba
```

Salida:

```
abracadabra: YES
ababaab: YES
ababaaba: NO
```

## Solución

Se busca en profundidad desde cada casilla con la primera letra,
pasando a una casilla vecina no usada con la letra siguiente. Las
casillas usadas forman una máscara de 16 bits. Las letras repetidas
pueden hacer que la búsqueda vuelva muchas veces a la misma situación:
el mismo conjunto de casillas usadas, la misma última casilla y el mismo
resto de palabra. Así que un par (máscara, casilla) fallido se recuerda
y no se vuelve a explorar; hay como mucho 16·2¹⁶ pares así, y en la
práctica muchos menos alcanzables. Una comprobación rápida descarta
antes la palabra que necesita más de alguna letra de las que hay.

Los resultados se compararon con una implementación independiente en
cuadrículas generadas, incluidas cuadrículas de una sola letra repetida
con palabras largas.

Detalles a tener en cuenta:

- contar las letras permite descartar una palabra antes de buscar:
  quince casillas `a` no bastan para dieciséis letras `a`, y la única
  casilla `b` no puede usarse en ambos extremos de una palabra (prueba 04);
- las letras repetidas pueden llevar a explorar estados repetidos, por
  lo que se recuerdan los pares (máscara, casilla) fallidos; la prueba 07
  tiene catorce casillas `a` y una de cada letra `b` y `c`, y su palabra
  más larga supera la comprobación de cantidades de letras;
- ese NO puede deberse solo a la paridad: si se colorea la cuadrícula
  como un tablero de ajedrez, un camino de 16 casillas siempre termina en
  el otro color, así que una palabra que empieza y acaba en casillas del
  mismo color no puede ocupar las 16 (prueba 07);
- una casilla no puede usarse dos veces, y los pasos son solo
  horizontales o verticales (prueba 03).

## Soluciones optimizadas

La búsqueda sigue celdas vecinas sin repetirlas. Los estados fallidos se memorizan por extremo y máscara visitada; la posición de la palabra viene dada por el tamaño de la máscara. Las máscaras de caracteres y adyacencia podan continuaciones imposibles antes de ramificar. Las palabras iguales reutilizan su resultado. El tablero es fijo y pequeño: se explicita la cota de subconjuntos, sin afirmar que la búsqueda sea polinómica.

- `1603_implementation_optimized.cpp`: 0.015 s / 176 KB; base `1603_implementation.cpp`: 0.031 s / 452 KB; cambio respecto a la base: tiempo -51.6%, memoria -61.1%.
- `1603_implementation_optimized.go`: 0.031 s / 988 KB; base `1603_implementation.go`: 0.031 s / 5708 KB; cambio respecto a la base: tiempo -0.0%, memoria -82.7%.
- `1603_implementation_optimized.java`: 0.093 s / 620 KB; base `1603_implementation.java`: 0.109 s / 5228 KB; cambio respecto a la base: tiempo -14.7%, memoria -88.1%.
- `1603_implementation_optimized.py`: 0.093 s / 1128 KB; base `1603_implementation.py`: 0.359 s / 21264 KB; cambio respecto a la base: tiempo -74.1%, memoria -94.7%.
- `1603_implementation_optimized.rs`: 0.031 s / 292 KB; base `1603_implementation.rs`: 0.062 s / 420 KB; cambio respecto a la base: tiempo -50.0%, memoria -30.5%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1603_implementation.cpp`; versión que cubre `1603_implementation_optimized.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 59/59.

- Go: base didáctica preferida `1603_implementation.go`; versión que cubre `1603_implementation.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1603_implementation.java`; versión que cubre `1603_implementation_optimized.java`; puestos tiempo/memoria 1/2, registros de otros autores 2/2.

- Python/PyPy: base didáctica preferida `1603_implementation.py`; versión que cubre `1603_implementation_optimized.py`; puestos tiempo/memoria 1/1, registros de otros autores 3/3.

- Rust: base didáctica preferida `1603_implementation.rs`; versión que cubre `1603_implementation_optimized.rs`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1603_implementation.cpp](1603_implementation.cpp) | G++ 13.2 x64 | implementation | O(n·16·2^16) | AC | 0.031 s | 452 KB | 11288124 |
| [1603_implementation.go](1603_implementation.go) | Go 1.14 x64 | implementation | O(n·16·2^16) | AC | 0.031 s | 5708 KB | 11288126 |
| [1603_implementation.java](1603_implementation.java) | Java 1.8 | implementation | O(n·16·2^16) | AC | 0.109 s | 5228 KB | 11288130 |
| [1603_implementation.py](1603_implementation.py) | Python 3.12 x64 | implementation | O(n·16·2^16) | AC | 0.359 s | 21264 KB | 11288128 |
| [1603_implementation.rs](1603_implementation.rs) | Rust 1.75 x64 | implementation | O(n·16·2^16) | AC | 0.062 s | 420 KB | 11288131 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1603_implementation_optimized.cpp](1603_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(16*2^16) per distinct word | AC | 0.015 s | 176 KB | 11309250 |
| [1603_implementation_optimized.go](1603_implementation_optimized.go) | Go 1.14 x64 | implementation | O(16*2^16) per distinct word | AC | 0.031 s | 988 KB | 11309252 |
| [1603_implementation_optimized.java](1603_implementation_optimized.java) \* | Java 1.8 | implementation | O(16*2^16) per distinct word | AC | 0.093 s | 620 KB | 11309251 |
| [1603_implementation_optimized.py](1603_implementation_optimized.py) | Python 3.12 x64 | implementation | O(16*2^16) per distinct word | AC | 0.093 s | 1128 KB | 11309249 |
| [1603_implementation_optimized.rs](1603_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(16*2^16) per distinct word | AC | 0.031 s | 292 KB | 11309253 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
