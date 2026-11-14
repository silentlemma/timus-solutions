# 1592. Relojes chinos

[Timus 1592](https://acm.timus.ru/problem.aspx?space=1&num=1592) · dificultad 588 · math

Problema original de Andrey Demidov, de la subregión oriental del NEERC del ACM ICPC 2007–2008, Ekaterimburgo, 27 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay n ≤ 50000 relojes de esfera de 12 horas, y cada uno marca una hora
h:mm:ss. Las agujas solo se pueden girar hacia delante, y el esfuerzo es
el tiempo total que se mueven las agujas. Hay que elegir una hora para
poner en todos los relojes con el menor esfuerzo total.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n y luego la hora de cada reloj como h:mm:ss, con 1 ≤ h ≤ 12.

## Salida

La hora elegida en el mismo formato.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
11:30:00
12:10:01
6:10:18
```

Salida:

```
12:10:01
```

## Solución

Se cuentan los segundos desde las 12, así que una hora es un número t de
0 a 43199. Pasar un reloj de la hora a a la hora t cuesta
(t − a) mod 43200 segundos de movimiento de agujas. Para un objetivo t,
los relojes que marcan como mucho t cuestan t − a, y los que marcan una
hora posterior cuestan una vuelta entera más, así que el total es
n·t − Σa + 43200·(número de relojes después de t). Retroceder t hasta la
hora de reloj más cercana no aumenta el esfuerzo total, así que el
mejor objetivo es una de las horas de los relojes. Tras ordenar, un
puntero mantiene el número mientras t recorre las horas de los relojes:
`O(n log n)`.

El enunciado no dice qué hora imprimir cuando varias son igual de
buenas; las soluciones imprimen la más temprana contando desde las 12.
Los resultados se contrastaron con probar las 43200 horas en entradas
pequeñas.

Detalles a tener en cuenta:

- las 12 son el inicio de la esfera: valen 0 segundos, y una respuesta
  de 0 segundos se imprime como 12:00:00;
- el esfuerzo total llega a unos 50000·43200 ≈ 2·10⁹, más de lo que
  cabe en enteros de 32 bits;
- los minutos y los segundos se imprimen con dos cifras, y la hora sin
  cero inicial.

## Soluciones optimizadas

La versión optimizada en C++ cuenta los relojes en cada segundo de la esfera. Al recorrer los segundos ocupados en orden se mantiene la cantidad later de relojes cuya hora inicial es estrictamente posterior al objetivo. Para un objetivo t se compara N·t + D·later, con D = 43 200. La suma de las horas iniciales es común a todos los objetivos. El tiempo es O(N + D) y el espacio adicional es O(D). Las métricas corresponden al envío 11316963.

La versión en Java usa el mismo recorrido con un arreglo fijo de contadores de 16 bits y lee los campos de la hora directamente del búfer. El espacio adicional es O(D). Las métricas corresponden al envío 11317056.

La versión en Rust usa el mismo recorrido con un arreglo fijo de contadores de 16 bits y lee los campos de la hora directamente del búfer. El espacio adicional es O(D). Las métricas corresponden al envío 11317053.

La versión en Go usa el mismo recorrido con un arreglo fijo de contadores de 16 bits y lee los campos de la hora directamente del búfer. El espacio adicional es O(D). Las métricas corresponden al envío 11317046.

La versión en Python usa el mismo recorrido con un arreglo compacto de contadores de 16 bits. Lee las horas de los relojes línea por línea, por lo que el espacio adicional es O(D). Las métricas corresponden al envío 11317035.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322161 · Go 1.14 x64 №11322418 · Java 1.8 №11322419 · Python 3.12 x64 №11322420 · Rust 1.75 x64 №11322422.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1592_math.cpp](1592_math.cpp) | G++ 13.2 x64 | math | O(n log n) | AC | 0.062 s | 568 KB | 11322161 |
| [1592_math.go](1592_math.go) | Go 1.14 x64 | math | O(n log n) | AC | 0.046 s | 5704 KB | 11322418 |
| [1592_math.java](1592_math.java) | Java 1.8 | math | O(n log n) | AC | 0.125 s | 6084 KB | 11322419 |
| [1592_math.py](1592_math.py) | Python 3.12 x64 | math | O(n log n) | AC | 0.14 s | 6420 KB | 11322420 |
| [1592_math.rs](1592_math.rs) | Rust 1.75 x64 | math | O(n log n) | AC | 0.031 s | 1248 KB | 11322422 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1592_math_optimized.cpp](1592_math_optimized.cpp) | G++ 13.2 x64 | math | O(N + D) | AC | 0.015 s | 168 KB | 11316963 |
| [1592_math_optimized.java](1592_math_optimized.java) | Java 1.8 | math | O(N + D) | AC | 0.093 s | 528 KB | 11317056 |
| [1592_math_optimized.rs](1592_math_optimized.rs) \* | Rust 1.75 x64 | math | O(N + D) | AC | 0.031 s | 292 KB | 11317053 |
| [1592_math_optimized.go](1592_math_optimized.go) \* | Go 1.14 x64 | math | O(N + D) | AC | 0.031 s | 1212 KB | 11317046 |
| [1592_math_optimized.py](1592_math_optimized.py) \* | Python 3.12 x64 | math | O(N + D) | AC | 0.125 s | 592 KB | 11317035 |

\* Aceptada. Aún queda por alcanzar el objetivo de clasificación de Python. Aceptada. Aún queda por alcanzar el objetivo de clasificación de Go. Aceptada. Aún queda por alcanzar el objetivo de clasificación de Rust.
