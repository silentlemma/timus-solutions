# 1214. Deshacer un procedimiento extraño

[Timus 1214](https://acm.timus.ru/problem.aspx?space=1&num=1214) · dificultad 103 · math

Problema original de Anatoly Uglov, del USU Open Collegiate Programming Contest, octubre de 2002, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un procedimiento recibe dos enteros `x` e `y`. Si ambos son positivos,
ejecuta `x + y` veces un cuerpo de bucle que hace `y ← x² + y`, luego
`x ← x² + y`, luego `y ← ⌊√(x − y)⌋`, y después resta `y` de `x` `2y`
veces; al final imprime `x` e `y`. A partir de lo impreso, ambos de
`−32000` a `32000`, hay que recuperar la entrada. Ninguna variable se
desborda nunca.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Los valores impresos `x` e `y`.

## Salida

Los valores de entrada `x` e `y`.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 7
```

Salida:

```
7 4
```

## Solución

Se sigue una vuelta del bucle desde `(x, y)`. Primero `y` pasa a valer
`x² + y`, luego `x` pasa a valer `2x² + y`. Su diferencia es `x²`, así que
la nueva `y` es `x`. Restarla `2x` veces quita `2x²` de `2x² + y` y deja
`y`. Así que cada vuelta solo intercambia los dos números, y la suma
`x + y`, que fija el número de vueltas, no cambia. Tras `x + y` vueltas
los números quedan intercambiados exactamente cuando la suma es impar.

Por tanto, el procedimiento intercambia su entrada cuando ambos números
son positivos y su suma es impar, y no cambia nada en otro caso. Esa
transformación es su propia inversa: se aplica la misma regla al par
impreso. `O(1)`.

Detalles a tener en cuenta:

- con un número cero o negativo el bucle no se ejecuta, así que ese par
  se imprime sin cambios;
- la paridad la decide la suma, no los números por separado.

Ejecutar el procedimiento en cada par de `−3` a `15` y deshacer el
resultado devolvió cada vez el par original.

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

`1214_math_optimized.java`. Conserva involución: intercambia solo si ambos son positivos y de paridad distinta. Rango ±32000 permite magnitudes int. Lee con 64 bytes; serializa y luego x hacia atrás en 32 bytes, con signos, espacio y salto. Elimina formateador long general y arreglo de cifras. Escribe y vacía todo antes de System.exit(0). Aritmética/estado constantes para estos límites; base intacta. Nuevo par 0.093 s/436 KB usa más memoria que 0.109 s/384 KB; admisión estricta por ranking, sin afirmar mejora de recursos del 30%.

Accepted de fuente exacta Java 1.8 #11327866: 0.093 s / 436 KB. Comparación guardada del 2026-11-20: tiempo 5/75, memoria 4/75. Cumple el criterio temporal compartido bajo 1024 KB sin meta separada de primer puesto ni asterisco. El optimizado anterior #11303725 de 0.109 s / 384 KB es un par histórico distinto, no el comprobante del archivo actual. Java sencillo se conserva intacto.

- `1214_math_optimized.java`: 0.093 s / 436 KB; base didáctica conservada `1214_math.java`: 0.125 s / 1584 KB.

`1214_math_optimized.py`. Conserva la misma involución: intercambia los valores solo si ambos son positivos y su suma es impar. Cero o valores negativos evitan el intercambio. Los valores impresos tienen valor absoluto hasta 32000, por lo que la suma cabe en i64. Tiempo y estado aritmético O(1). Analiza tokens de bytes en vez de una línea decodificada y prueba la paridad con bits, sin simular el procedimiento. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1214_math.py`: tiempo 0.078 s → 0.125 s; memoria 444 KB → 204 KB.

`1214_math_optimized.rs`. Conserva la misma involución: intercambia los valores solo si ambos son positivos y su suma es impar. Cero o valores negativos evitan el intercambio. Los valores impresos tienen valor absoluto hasta 32000, por lo que la suma cabe en i64. Tiempo y estado aritmético O(1). Lee solo dos enteros con signo, sin línea decodificada ni vector de valores. La transformación matemática no cambia. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1214_math.rs`: tiempo 0.046 s → 0.046 s; memoria 212 KB → 60 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1214_math_optimized.go`. Se conservan el algoritmo y sus casos límite. Se sustituye fmt por conversión de números y palabras y un búfer de salida reutilizable. La entrada completa se guarda en bytes: se intercambia ese espacio por un menor coste de la E/S general.

Accepted #11328523 (Go 1.14 x64): **0.031 s / 948 KB**. Comparación archivada: `1214_math.go` (Go 1.14 x64) — 0.015 s / 1068 KB (#11283657).

Go Accepted #11328523 y su admisión corresponden a bytes históricos exactos. Esta revisión nombra `numericBitSize` la anchura existente de 64 bits en cuatro llamadas strconv; sustituir 64 restaura exactamente el archivo previo. Se conservan algoritmo, comentarios y Go sencillo.

## Notas por lenguaje

Los registros exactos guardados siguen los [criterios compartidos](../../RATING_CRITERIA.md). Cumplen C++ sencillo, Go/Java optimizados, CPython sencillo y ambos Rust. Go sencillo de 0.015 s / 1068 KB falla memoria exigida; Go optimizado de 0.031 s / 948 KB cumple solo por tiempo: no se afirma que sea más rápido. Java sencillo falla el umbral numérico; las bases significativas quedan didácticas sin estrella. Bajo 1024 KB solo cuenta tiempo; por encima ambas métricas. Go usa referencia de compilador exacto aplicable y Rust el grupo del mismo lenguaje. No hay admisión independiente por falta de rivales, primer puesto o mejora del 30%.

La comparación PyPy guardada del 2026-11-18 es histórica: #11324914 de 0.125 s / 204 KB tenía puesto 29/40 en tiempo y 1/40 en memoria. Sigue fallando tiempo y mantiene marca pese a ahorrar memoria. CPython sencillo #11283658 de 0.078 s / 444 KB cubre Python rápido. Las parejas actuales quedan en tablas; las instantáneas anteriores no son rankings actuales nuevos ni garantías entre ejecuciones.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1214_math.cpp](1214_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11283656 |
| [1214_math.go](1214_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1068 KB | 11283657 |
| [1214_math.java](1214_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1584 KB | 11283659 |
| [1214_math.py](1214_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 444 KB | 11283658 |
| [1214_math.rs](1214_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 212 KB | 11283660 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1214_math_optimized.java](1214_math_optimized.java) | Java 1.8 | math | O(1) bounded arithmetic and storage | AC | 0.093 s | 436 KB | 11327866 |
| [1214_math_optimized.py](1214_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.125 s | 204 KB | 11324914 |
| [1214_math_optimized.rs](1214_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 60 KB | 11324868 |
| [1214_math_optimized.go](1214_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 936 KB | 11330996 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
