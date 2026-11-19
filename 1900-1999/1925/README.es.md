# 1925. El último valor para igualar una suma total

[Timus 1925](https://acm.timus.ru/problem.aspx?space=1&num=1925) · difficulty 70 · math

Problema original de Pavel Ageev, del concurso escolar regional de los Urales de 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se conocen n rondas anteriores. En la ronda i se mostró bᵢ, la entrada
prevista era bᵢ−2 y la real fue gᵢ. Ahora se muestra k. Solo se comprueba
el total de las n+1 rondas: la suma real debe igualar la prevista.
Encontrar un entero no negativo para la ronda actual, o declarar que no
existe. Las rondas pasadas no necesitan ser correctas individualmente.
Límites: 1 segundo, 64 MB.

## Entrada

n,k con 1≤n,k≤100, seguidos de n pares bᵢ,gᵢ, cada valor entre 0 y 100.

## Salida

El entero no negativo necesario, incluido cero. La salida no está
limitada a 100. Si es imposible, escribir exactamente `Big Bang!`,
respetando espacio, mayúsculas y signo de exclamación.

## Evaluación

Comparación exacta de tokens: un entero o los tokens `Big` y `Bang!`.

## Ejemplos

```
6 5
3 1
3 1
5 3
6 5
5 5
7 2
```

```
3
```

```
1 3
4 6
```

```
Big Bang!
```

## Solución

Sea x la entrada de hoy. La comprobación compara las sumas de las n + 1
rondas: g₁ + … + gₙ + x = (b₁ − 2) + … + (bₙ − 2) + (k − 2). Por tanto
x = k − 2 + Σ(bᵢ − gᵢ − 2); si es negativo, ninguna entrada sirve y la
respuesta es `Big Bang!`. `O(n)`.

Detalles a tener en cuenta:

- la suma parcial puede volverse negativa a mitad de camino y acabar
  siendo no negativa, así que se decide solo al final;
- cero es una respuesta válida;
- cada ronda, la de hoy incluida, resta 2.

## Soluciones optimizadas

`1925_math_optimized.py`. Conserva current-2+sum(displayed-entered-2). Procesa todas las parejas antes de decidir: un saldo negativo intermedio puede recuperarse. Emite el entero final, incluido cero, o exactamente Big Bang! solo si resulta negativo. Tiempo O(N), estado aritmético constante bajo los límites. Incluye el acumulador sin llamada a required_input mediante generador de parejas. Los tokens de entrada aún ocupan O(N); no es un analizador en flujo de espacio constante. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1925_math.py`: tiempo 0.093 s → 0.156 s; memoria 504 KB → 232 KB.

`1925_math_optimized.rs`. Conserva current-2+sum(displayed-entered-2). Procesa todas las parejas antes de decidir: un saldo negativo intermedio puede recuperarse. Emite el entero final, incluido cero, o exactamente Big Bang! solo si resulta negativo. Tiempo O(N), estado aritmético constante bajo los límites. Lee y suma cada pareja directamente, eliminando vector histórico y entrada decodificada. Estado auxiliar O(1). La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1925_math.rs`: tiempo 0.031 s → 0.062 s; memoria 236 KB → 56 KB.

La solución optimizada en C++ lee los pares con `scanf` en lugar de
`iostream` y los suma al momento en lugar de guardar el historial:
124 KB en lugar de 428 KB.

La solución optimizada en Java lee la entrada en bloques de 1 KB y la
analiza a mano en lugar de usar `Scanner`, y suma las lecturas a medida
que las lee en lugar de guardarlas: 0.078 s en lugar de 0.140 s y 364 KB
en lugar de 1796 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1925_math_optimized.py`: puesto de tiempo 57/59 y de memoria 1/59 en esta muestra comparable.

`1925_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1925_math.cpp](1925_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 428 KB | 11291544 |
| [1925_math.go](1925_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1088 KB | 11291551 |
| [1925_math.java](1925_math.java) | Java 1.8 | math | O(n) | AC | 0.140 s | 1796 KB | 11291560 |
| [1925_math.py](1925_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.093 s | 504 KB | 11291556 |
| [1925_math.rs](1925_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 236 KB | 11291566 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1925_math_optimized.cpp](1925_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 124 KB | 11303650 |
| [1925_math_optimized.java](1925_math_optimized.java) | Java 1.8 | math | O(n) | AC | 0.078 s | 364 KB | 11303789 |
| [1925_math_optimized.py](1925_math_optimized.py) \* | PyPy 3.10 x64 | math | O(N) | AC | 0.156 s | 232 KB | 11324844 |
| [1925_math_optimized.rs](1925_math_optimized.rs) \* | Rust 1.75 x64 | math | O(N) | AC | 0.062 s | 56 KB | 11324855 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
