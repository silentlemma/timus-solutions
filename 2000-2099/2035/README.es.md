# 2035. Dividir un total bajo dos cotas superiores

[Timus 2035](https://acm.timus.ru/problem.aspx?space=1&num=2035) · dificultad 78 · math

Problema original de Kirill Borozdin, del Concurso Regional Escolar de Programación de los Urales 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados enteros `X,Y,C`, con `0 ≤ X,Y,C ≤ 1000000000`, encuentra cualquier
pareja entera `A,B` tal que `0 ≤ A ≤ X`, `0 ≤ B ≤ Y` y `A+B=C`.
Límites: 0,5 segundos y 64 MB.

## Entrada

Una línea `X Y C`, una sola instancia sin cantidad inicial de pruebas.

## Salida

Cualquier pareja válida `A B` o la palabra exacta `Impossible` si no existe.
La pareja `0 0` es válida cuando `C=0`.

## Evaluación

Un comprobador verifica ambos límites y la suma; `Impossible` solo se
acepta si no existe ninguna pareja. Se acepta cualquier pareja válida.

## Ejemplos

```
2 7 5
```

```
2 3
```

```
9 15 100
```

```
Impossible
```

## Solución

Se toma A lo mayor posible, A = min(X, C), y B = C − A. Si B ≤ Y, el
par sirve; si no, no sirve ninguno, porque cualquier otro A es menor y
solo hace mayor a B. `O(1)`.

Detalles a tener en cuenta:

- tomar A = X sin limitarlo por C puede dejar B negativo;
- se admiten sumandos cero, y se acepta cualquier par válido.

## Soluciones optimizadas

`2035_math_optimized.py`. Conserva A=min(X,C), B=C-A. Son no negativos y A<=X; si B>Y no existe pareja válida, si no, la emite. C=0 da 0 0. Solo usa tres entradas y pocos enteros acotados, O(1) tiempo y estado. Incluye la lógica sin envolventes solve/main y analiza bytes crudos; no cambia el algoritmo de factibilidad. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `2035_math.py`: tiempo 0.078 s → 0.14 s; memoria 436 KB → 200 KB.

`2035_math_optimized.rs`. Conserva A=min(X,C), B=C-A. Son no negativos y A<=X; si B>Y no existe pareja válida, si no, la emite. C=0 da 0 0. Solo usa tres entradas y pocos enteros acotados, O(1) tiempo y estado. Lee tres i64 directamente y emite números sin String ni formato. El dominio no negativo del enunciado garantiza restas seguras. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `2035_math.rs`: tiempo 0.031 s → 0.046 s; memoria 228 KB → 68 KB.

La solución optimizada en C++ analiza los tres números a mano con
`getchar` en lugar de `iostream`: 100 KB en lugar de 400 KB, con el
mismo tiempo.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`2035_math_optimized.py`: puesto de tiempo 47/54 y de memoria 1/54 en esta muestra comparable.

`2035_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2035_math.cpp](2035_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 400 KB | 11293165 |
| [2035_math.go](2035_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 1088 KB | 11293168 |
| [2035_math.java](2035_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 492 KB | 11303531 |
| [2035_math.py](2035_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 436 KB | 11293171 |
| [2035_math.rs](2035_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 228 KB | 11293174 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2035_math_optimized.cpp](2035_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 100 KB | 11303670 |
| [2035_math_optimized.py](2035_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.14 s | 200 KB | 11324848 |
| [2035_math_optimized.rs](2035_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 68 KB | 11324857 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
