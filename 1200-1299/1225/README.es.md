# 1225. Filas de franjas blancas, azules y rojas

[Timus 1225](https://acm.timus.ru/problem.aspx?space=1&num=1225) · dificultad 35 · dp

Problema original del cuarto de final de la región central de Rusia del ACM ICPC 2002–2003, Rybinsk, octubre de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una fila de `N ≤ 45` franjas se hace con franjas blancas, azules y rojas.
Dos franjas vecinas no comparten color, y una franja azul debe estar
entre una blanca y una roja. Hay que contar las filas posibles.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N`.

## Salida

El número de filas.

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
```

Salida:

```
2
```

## Solución

Una franja azul necesita vecinas a ambos lados, así que una fila nunca
acaba en azul; acaba en blanco o en rojo. Sea `f(n)` el número de filas
válidas de longitud `n`. Antes de una última franja blanca hay o una
roja, que cierra una fila válida de longitud `n − 1` acabada en rojo, o
una azul precedida de una roja, que cierra una fila válida de longitud
`n − 2` acabada en rojo; lo mismo vale para el rojo con los colores
cambiados. Por simetría, la mitad de las filas de cada longitud acaba en
rojo, así que `f(n) = f(n − 1) + f(n − 2)` con `f(1) = f(2) = 2`: el
doble de los números de Fibonacci. `O(N)`.

Detalles a tener en cuenta:

- una sola franja puede ser blanca o roja pero no azul, así que
  `f(1) = 2`;
- para `N = 45` la cuenta es 2.269.806.340, más de lo que cabe en enteros
  de 32 bits con signo.

La fórmula se comprobó por fuerza bruta con todas las coloraciones de
hasta 12 franjas, y cada `N` de 1 a 45 se comparó con una solución
escrita aparte.

## Soluciones optimizadas

`1225_math.py`. Alternativa exacta por función generadora: 2·Fib(N) banderas. B=2^64 permite extraer coeficiente N−1 de 1/(1−x−x²) como floor(B^(N+1)/(B²−B−1)) mod B y duplicar. Para 1≤N≤45 coeficientes caben en dígito B y cola positiva menor que uno no acarrea. Sin flotantes ni respuestas incrustadas. Una división de enteros O(N) bits, numerador hasta 2945 bits; no costo constante para N ilimitado. Conserva recurrencia didáctica.

Fuente exacto: Python 3.12 x64 Accepted #11327782: 0.062 s / 644 KB. Puestos guardados del grupo de compilador del 2026-11-20, tiempo y luego memoria: 5/366; 329/366. Admisión estricta usa solo tiempo bajo 1024 KB: diez primeros o 15% superior, empates comparten puesto y corte se redondea arriba. Conserva asterisco por la meta propia de primer puesto en ambas. La variante anterior conservada tiene su par propio #11324831 (PyPy 3.10 x64): 0.14 s / 224 KB; no mezclar métricas ni runtimes. Bases didácticas intactas.

- `1225_math.py`: 0.062 s / 644 KB; base didáctica conservada `1225_dp.py` (Python 3.12 x64): 0.093 s / 372 KB.

La solución optimizada en Java analiza el número byte a byte desde
`System.in` en lugar de usar `Scanner`: 0.093 s en lugar de 0.125 s y
316 KB en lugar de 1576 KB.

`1225_dp_optimized.py`. Conserva la recurrencia de dos acumuladores desde (2,2): cada franja cambia la pareja a (current,previous+current), sin tabla. La entrada cruda y la terminación inmediata tras vaciar la salida reducen sobrecarga. Hace O(N) sumas con dos acumuladores enteros acotados por N<=45. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1225_dp.py`: tiempo 0.093 s → 0.14 s; memoria 372 KB → 224 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1225_dp_optimized.py`: puesto de tiempo 363/366 y de memoria 2/366 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1225_dp.cpp](1225_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 128 KB | 11283710 |
| [1225_dp.go](1225_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 1072 KB | 11283711 |
| [1225_dp.java](1225_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 1576 KB | 11283713 |
| [1225_dp.py](1225_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.093 s | 372 KB | 11283712 |
| [1225_dp.rs](1225_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 216 KB | 11283714 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1225_dp_optimized.java](1225_dp_optimized.java) | Java 1.8 | dp | O(N) | AC | 0.093 s | 316 KB | 11303728 |
| [1225_dp_optimized.py](1225_dp_optimized.py) \* | PyPy 3.10 x64 | dp | O(N) | AC | 0.14 s | 224 KB | 11324831 |
| [1225_math.py](1225_math.py) \* | Python 3.12 x64 | math | One O(N)-bit integer division; O(N) bits | AC | 0.062 s | 644 KB | 11327782 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
