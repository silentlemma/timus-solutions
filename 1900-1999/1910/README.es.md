# 1910. La terna consecutiva de mayor suma

[Timus 1910](https://acm.timus.ru/problem.aspx?space=1&num=1910) · difficulty 34 · implementation

Problema original de Denis Dublennykh, NEERC 2012, Eastern subregional contest.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una secuencia de valores positivos, encuentra los tres consecutivos
con mayor suma. Imprime esa suma y la posición del elemento central,
numerada desde uno. Se garantiza que la terna óptima es única.
Límites: 1 segundo y 64 MB.

## Entrada

Primero n, 3≤n≤1000, seguido de n enteros aᵢ con 1≤aᵢ≤10⁶.
Los espacios y los saltos de línea son separadores equivalentes.

## Salida

La suma máxima y la posición central numerada desde uno.

## Evaluación

Dos enteros exactos, comparados por tokens.

## Ejemplos

```
6
1 4 4 4 1 1
```

```
12 3
```

## Solución

Se prueba cada sección, de la segunda a la penúltima, como la del medio
de las tres: se suma con sus dos vecinas y se guarda la mayor suma con
su número. El enunciado promete que el mejor trío es único, así que
basta una comparación estricta. `O(n)`; una suma es a lo sumo 3·10⁶ y
cabe en un entero de 32 bits.

Detalles a tener en cuenta:

- la respuesta es el número de la sección del medio, contando desde 1;
- con n = 3 solo hay un trío.

## Soluciones optimizadas

`1910_implementation_optimized.java`. Java conserva el máximo de una terna deslizante. Retiene solo los dos valores anteriores, añade el nuevo y actualiza la mejor suma y la posición central desde uno si mejora estrictamente. La unicidad prometida del máximo basta para esa comparación. Cada suma es como máximo 3000000 y cabe en int. Entrada de bytes fija y salida numérica directa evitan Scanner, concatenaciones y formato general de enteros; nunca guarda la secuencia. Tiempo O(N), espacio auxiliar O(1).

Accepted exacto Java 1.8 #11327450: 0.078 s / 356 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 1/532, memoria 2/532. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11303787 era 0.125 s / 380 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1910_implementation_optimized.java`: 0.078 s / 356 KB; base didáctica conservada `1910_implementation.java`: 0.156 s / 2372 KB.

La solución optimizada en C++ no guarda las secciones: las lee una a una
con `scanf` y recuerda solo las dos anteriores a la actual, que es todo
lo que necesita un trío: 128 KB en lugar de 192 KB, con el mismo tiempo.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1910_implementation_optimized.rs`. La entrada de C llama directamente al solucionador y vacía la salida de Rust antes de volver; se conserva la implementación de entrada habitual.

Accepted #11328940 (Rust 1.75 x64): **0.015 s / 136 KB**. Comparación archivada: `1910_implementation.rs` (Rust 1.75 x64) — 0.031 s / 236 KB (#11303334).

## Notas por lenguaje

Ningún lenguaje necesita nada especial.

Mantener una ventana de tres valores al leer la secuencia y guardar el primer máximo. El envío aceptado 11324269 tardó 0.140 s y usó 240 KB. La versión sencilla tardó 0.062 s y usó 452 KB. El tiempo registrado es mayor que el de la versión sencilla.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1910_implementation.cpp](1910_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 192 KB | 11303319 |
| [1910_implementation.go](1910_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1108 KB | 11303324 |
| [1910_implementation.java](1910_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.156 s | 2372 KB | 11303327 |
| [1910_implementation.py](1910_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.062 s | 452 KB | 11303331 |
| [1910_implementation.rs](1910_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 236 KB | 11303334 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1910_implementation_optimized.cpp](1910_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB | 11303648 |
| [1910_implementation_optimized.java](1910_implementation_optimized.java) | Java 1.8 | implementation | O(N) time; O(1) auxiliary space | AC | 0.078 s | 356 KB | 11327450 |
| [1910_implementation_optimized.py](1910_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(n) | AC | 0.140 s | 240 KB | 11324269 |
| [1910_implementation_optimized.rs](1910_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 136 KB | 11328940 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
