# 1068. La suma de todos los enteros entre 1 y N

[Timus 1068](https://acm.timus.ru/problem.aspx?space=1&num=1068) · dificultad 37 · math

Problema original de la ronda de prueba del concurso regional ACM ICPC del noreste de Europa 2000–2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se da un entero `N` con `|N| ≤ 10000`. Imprime la suma de todos los
enteros entre 1 y `N`, ambos incluidos.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N`.

## Salida

La suma.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
-3
```

Salida:

```
-5
```

## Solución

Los números entre 1 y `N` forman un intervalo de `|N − 1| + 1` números,
esté `N` al lado que esté de 1. La suma de un intervalo es su longitud por
la media de sus extremos, `(1 + N) / 2`. El producto
`(1 + N) · (|N − 1| + 1)` siempre es par: si `N ≤ 0` sus dos factores suman
un número impar, y si no son `N + 1` y `N`, así que la división es exacta.
`O(1)`.

Detalles a tener en cuenta:

- `N` puede ser cero o negativo: entonces el intervalo va de `N` hasta 1, y
  `N(N + 1)/2` da una respuesta errónea, por ejemplo 0 en lugar de 1 para
  `N = 0`;
- la suma llega a unos `5 · 10^7` en valor absoluto, que cabe en enteros de
  32 bits; aun así las soluciones multiplican en 64 bits (Python, en sus
  enteros sin límite).

Las respuestas se comprobaron sumando los números uno a uno.

## Soluciones optimizadas

`1068_math_optimized.java`. Conserva la suma inclusiva (1+N)*(abs(N-1)+1)/2, también con cero y N negativo. Para |N|<=10000 el producto intermedio cabe en int. Usa entrada de 256 bytes, salida de 128 y arreglo de dígitos reutilizado, sin llamadas de entrada por byte ni impresión decimal general. Trabajo aritmético y espacio auxiliar O(1); conserva la base legible.

Accepted exacto Java 1.8 #11327461: 0.062 s / 364 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 1/1616, memoria 20/1616. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11303705 era 0.125 s / 368 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1068_math_optimized.java`: 0.062 s / 364 KB; base didáctica conservada `1068_math.java`: 0.109 s / 1568 KB.

`1068_math_optimized.go`. Mantiene progresión inclusiva de 1 a N: (abs(N−1)+1)(N+1)/2 en int64 cubre N positivo, cero y negativo sin bucle. Buffers acotados de entrada de 256 bytes y salida de 64 usan syscall.Read/Write de Go 1.14, reintentan EINTR/escrituras parciales y tratan EOF de cero bytes. Elimina inicialización fmt/bufio/os.File. Pruebas Linux y compilación cruzada Windows validan funcionamiento y construcción; las métricas pareadas siguientes vienen de nuestro Accepted exacto en juez Windows. Se conserva fuente didáctica legible.

Frente a `1068_math.go`: tiempo 0.031 s → 0.015 s; memoria 1072 KB → 260 KB.

`1068_math_optimized.py`. Conserva (1+N)*(abs(N-1)+1)//2 para la progresión, incluidos cero y N negativos. Lee el entero acotado de bytes crudos en vez de input(), sin llamada envolvente. Con |N|<=10000 el tiempo y espacio aritméticos siguen siendo O(1). El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1068_math.py`: tiempo 0.078 s → 0.109 s; memoria 448 KB → 196 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1068_math_optimized.py`: puesto de tiempo 644/739 y de memoria 1/739 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1068_math.cpp](1068_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11278883 |
| [1068_math.go](1068_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1072 KB | 11278886 |
| [1068_math.java](1068_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1568 KB | 11278891 |
| [1068_math.py](1068_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 448 KB | 11278889 |
| [1068_math.rs](1068_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 240 KB | 11278892 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1068_math_optimized.java](1068_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.062 s | 364 KB | 11327461 |
| [1068_math_optimized.py](1068_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.109 s | 196 KB | 11324832 |
| [1068_math_optimized.go](1068_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 260 KB | 11325649 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
