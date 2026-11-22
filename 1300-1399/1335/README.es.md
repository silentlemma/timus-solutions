# 1335. La Tesis Blanca

[Timus 1335](https://acm.timus.ru/problem.aspx?space=1&num=1335) · dificultad 182 · math

Problema original de Den Raskovalov, del Décimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 16 de octubre de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dado N, 2 ≤ N ≤ 30 000, hay que hallar tres números enteros distintos A,
B y C entre N² y (N + 1)², ambos incluidos, tales que A² + B² sea
divisible por C, o imprimir `No solution` si no los hay. Se acepta
cualquier terna así.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

El número N.

## Salida

A, B y C, o `No solution`.

## Comprobación

El comprobador del repositorio exige tres enteros distintos A,B,C en [N²,(N+1)²] y verifica (A²+B²) mod C=0. Siempre existe una terna; No solution no se acepta.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
8 6 4
```

### Ejemplo 2

Entrada:

```
1000
```

Salida:

```
1000000 1000756 1000976
```

## Solución

Se toma C = N² + 1, A = N² y B = N² + N + 1. Módulo C el primer número
es −1 y el segundo es N, así que A² + B² ≡ 1 + N², que es el propio C,
y la suma es divisible por C. Los tres están entre N² y (N + 1)², ya que
N² + N + 1 < N² + 2N + 1, y son distintos para todo N ≥ 1. Por tanto la
respuesta existe siempre y `No solution` nunca ocurre. `O(1)`.

La terna se encontró listando todas las soluciones con A = N² para N
pequeños y viendo que (N² + N + 1, N² + 1) aparecía siempre.

Detalles a tener en cuenta:

- los números llegan a unos 9 · 10⁸, y sus cuadrados, que solo necesita
  el comprobador, a 8 · 10¹⁷, más de lo que caben en 32 bits;
- los ejemplos muestran otras ternas; se acepta cualquiera correcta.

## Soluciones optimizadas

`1335_math_optimized.java`. Conserva A=N², B=N²+N+1, C=N²+1. Calcula una vez N² en int: N<=30000 limita la salida máxima a 900030001. Búferes de entrada/salida de 1024 bytes y arreglo de dígitos evitan concatenación e impresión long general. Conserva la identidad modular y prueba de valores distintos; aritmética acotada y espacio O(1). Todos los N=2..30000 se comprobaron con identidad independiente de 64 bits.

Accepted exacto Java 1.8 #11327452: 0.093 s / 356 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 4/41, memoria 1/41. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11307311 era 0.109 s / 360 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1335_math_optimized.java`: 0.093 s / 356 KB; base didáctica conservada `1335_math.java`: 0.125 s / 1612 KB.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

`1335_math_optimized.py`. Conserva A=N², B=N²+N+1, C=N²+1 y calcula N² una vez. Módulo C los dos primeros son -1 y N, así que A²+B² es divisible por C; para N>=2 son distintos y pertenecen al intervalo. Aritmética acotada y espacio O(1). Reutiliza el cuadrado calculado y emite los tres enteros en una llamada. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1335_math.py`: tiempo 0.078 s → 0.125 s; memoria 392 KB → 168 KB.

`1335_math_optimized.rs`. Conserva A=N², B=N²+N+1, C=N²+1 y calcula N² una vez. Módulo C los dos primeros son -1 y N, así que A²+B² es divisible por C; para N>=2 son distintos y pertenecen al intervalo. Aritmética acotada y espacio O(1). Usa i64 con signo y salida numérica directa; N<=30000 mantiene todos los valores muy por debajo del límite de i64. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1335_math.rs`: tiempo 0.046 s → 0.015 s; memoria 244 KB → 56 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1335_math_optimized.py`: puesto de tiempo 18/26 y de memoria 1/26 en esta muestra comparable.

`1335_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1335_math.cpp](1335_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11285027 |
| [1335_math.go](1335_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1064 KB | 11285028 |
| [1335_math.java](1335_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1612 KB | 11285030 |
| [1335_math.py](1335_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 392 KB | 11285029 |
| [1335_math.rs](1335_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 244 KB | 11285032 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1335_math_optimized.java](1335_math_optimized.java) \* | Java 1.8 | math | O(1) | AC | 0.093 s | 356 KB | 11327452 |
| [1335_math_optimized.py](1335_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.125 s | 168 KB | 11324910 |
| [1335_math_optimized.rs](1335_math_optimized.rs) \* | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 56 KB | 11325094 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
