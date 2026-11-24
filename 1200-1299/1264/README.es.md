# 1264. Días de trabajo

[Timus 1264](https://acm.timus.ru/problem.aspx?space=1&num=1264) · dificultad 21 · math

Problema original de Den Raskovalov, de la Competición Abierta por Equipos de Programación para Escolares de la Región de Sverdlovsk, 11 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una función cuenta cuántas veces aparece cada valor de 0 a M en un
arreglo de N elementos, escrita con una línea `if` por cada elemento y
cada valor (0 ≤ N, M ≤ 40 000). Escribir una línea lleva un segundo.
¿Cuántos segundos lleva toda la función?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M.

## Salida

El número de segundos.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 1
```

Salida:

```
6
```

## Solución

Hay N elementos y M + 1 valores, así que la respuesta es N · (M + 1).
`O(1)`.

Detalles a tener en cuenta:

- los valores van de 0 a M, así que son M + 1, no M;
- la respuesta llega a 40 000 · 40 001 = 1 600 040 000, cerca del
  límite de 32 bits con signo; C++, Go, Java y Rust usan 64 bits (prueba 05);
- con N = 0 la respuesta es 0 sea cual sea M (pruebas 02, 03).

## Soluciones optimizadas

`1264_math_optimized.java`. Conserva N*(M+1), incluidos ambos límites cero. Con N,M<=40000 el resultado máximo es 1600040000 y cabe exactamente en int. Entrada fija de 256 bytes, salida de 128 y dígitos reutilizados reducen costes de lectura/formato. Aritmética y espacio auxiliar O(1), sin simulación ni cambio del conteo; conserva el fuente simple.

Accepted exacto Java 1.8 #11327465: 0.093 s / 340 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 42/1224, memoria 11/1224. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11303732 era 0.14 s / 296 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1264_math_optimized.java`: 0.093 s / 340 KB; base didáctica conservada `1264_math.java`: 0.109 s / 1552 KB.

`1264_math_optimized.py` se reutiliza byte por byte, sin otro archivo ni un algoritmo nuevo. Su Accepted de fuente exacto en CPython 3.12 #11327022 mide 0.046 s / 596 KB. En el grupo guardado de compiladores actuales de la familia Python, 2026-11-20: puesto temporal 1/597, memoria 524/597. Al usar menos de 1024 KB, el criterio estricto de diez primeros o 15% superior usa solo tiempo; el asterisco conserva la meta de clasificación propia del lenguaje. El mismo archivo tiene también el Accepted anterior en PyPy 3.10 #11324828, 0.109 s / 208 KB. Son pares medidos en ejecuciones distintas: se elige el tiempo y puesto de CPython, mientras PyPy usa menos memoria. Las observaciones anteriores sobre ahorro de memoria en esta sección se refieren a esa medición PyPy, no a la fila CPython. Todos los fuentes didácticos siguen intactos.

`1264_math_optimized.go`. Conserva N*(M+1), incluidos cero elementos y el valor cero entre las M+1 opciones. No simula un arreglo. N,M<=40000 acotan el producto a1600040000; Go mantiene int64 y Python enteros exactos. Entrada numérica por bytes y salida directa reducen sobrecarga, con O(1) tiempo y estado auxiliar. os.Stdin.Read/os.Stdout.Write portables y conversión entera directa usan búferes fijos de entrada y salida de 4096 bytes. Se atienden escrituras parciales antes de reutilizar el búfer de salida. Se conserva la fuente sencilla original con Accepted.

Frente a `1264_math.go`: tiempo 0.031 s → 0.031 s; memoria 1060 KB → 820 KB.

`1264_math_optimized.py`. Conserva N*(M+1), incluidos cero elementos y el valor cero entre las M+1 opciones. No simula un arreglo. N,M<=40000 acotan el producto a1600040000; Go mantiene int64 y Python enteros exactos. Entrada numérica por bytes y salida directa reducen sobrecarga, con O(1) tiempo y estado auxiliar. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1264_math.py`: tiempo 0.093 s → 0.109 s; memoria 320 KB → 208 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1264_math_optimized.go`: puesto de tiempo 1/16 y de memoria 1/16 en esta muestra comparable.

Comparación PyPy anterior: `1264_math_optimized.py`: puesto de tiempo 539/597 y de memoria 1/597 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1264_math.cpp](1264_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11284168 |
| [1264_math.go](1264_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1060 KB | 11284172 |
| [1264_math.java](1264_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1552 KB | 11284181 |
| [1264_math.py](1264_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 320 KB | 11284180 |
| [1264_math.rs](1264_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 232 KB | 11284182 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1264_math_optimized.java](1264_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 340 KB | 11327465 |
| [1264_math_optimized.go](1264_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 820 KB | 11328270 |
| [1264_math_optimized.py](1264_math_optimized.py) | Python 3.12 x64 | math | O(1) | AC | 0.046 s | 596 KB | 11327022 |
