# 2025. Maximizar parejas entre grupos

[Timus 2025](https://acm.timus.ru/problem.aspx?space=1&num=2025) · dificultad 60 · math

Problema original de Alexey Danilyuk, del Concurso Regional Escolar de Programación de los Urales 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Divide `n` objetos distintos en entre dos y `k` grupos no vacíos,
asignando cada objeto a exactamente un grupo. Una pareja no ordenada
aporta uno si sus objetos están en grupos distintos, y cero en otro
caso. Calcula el máximo número de parejas que aportan. Solo se pide el
número, no una partición concreta.

Hay `1 ≤ T ≤ 10` casos independientes, cada uno con `2 ≤ k ≤ n ≤ 10000`.
Límites: 1 segundo y 64 MB.

## Entrada

La primera línea contiene `T`. Cada una de las siguientes `T` líneas
contiene `n` y `k`.

## Salida

Para cada caso, imprime un entero en una línea, respetando el orden de entrada.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
3
6 3
5 5
4 2
```

```
12
10
4
```

## Solución

Lo mejor es usar los k grupos: con menos grupos, alguno tiene al menos
dos objetos, y partirlo añade pares. Con grupos de tamaños s₁, …, s_k,
los pares de grupos distintos son (n² − Σ sᵢ²) / 2, así que la suma de
cuadrados debe ser lo menor posible. Eso ocurre cuando los tamaños
difieren a lo sumo en uno, pues pasar un objeto de un grupo de tamaño a
a uno de tamaño b ≤ a − 2 reduce la suma de cuadrados. Así, r = n mod k
grupos tienen q + 1 objetos y los otros k − r tienen q = n div k, y la
respuesta es (n² − (k − r)·q² − r·(q + 1)²) / 2. `O(1)` por prueba.

Para n = 6, k = 3 los grupos son 2, 2, 2 y la respuesta es 12.

Detalles a tener en cuenta:

- cada par cuenta una vez, de ahí la división entre dos;
- solo aritmética entera, sin medias en coma flotante.

## Soluciones optimizadas

`2025_math_optimized.java`. Java conserva la fórmula de grupos equilibrados. Sean q=N/K y r=N%K: r grupos tienen q+1 personas y K-r tienen q. Calcula en long (N*N-((K-r)*q*q+r*(q+1)*(q+1)))/2. Con N<=10000, el resultado no supera 49995000 y la conversión final a int es exacta. Búferes directos de entrada y salida de 128 bytes evitan BufferedInputStream, StringBuilder y cadenas por respuesta. Hasta diez respuestas ocupan como máximo 90 bytes; el emisor también vacía el búfer de forma segura si se llena. Tiempo O(T), aritmética O(1) por caso y espacio auxiliar O(1).

Accepted exacto Java 1.8 #11327424: 0.093 s / 344 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 4/650, memoria 4/650. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11302162 era 0.14 s / 372 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `2025_math_optimized.java`: 0.093 s / 344 KB; base didáctica conservada `2025_math.java`: 0.125 s / 1628 KB.

`2025_math_optimized.cpp`. Conserva la fórmula de suma de cuadrados de grupos equilibrados con long long exacto. Sustituye scanf por entrada recargable de 256 bytes y un byte centinela; lee completos los números que cruzan recargas. Reúne respuestas en un búfer fijo de 128 bytes y escribe una vez, sin printf por caso. Como máximo diez respuestas de hasta 49995000 ocupan 90 bytes. Aritmética O(1) por caso, O(T) total y espacio auxiliar fijo; conserva la versión matemática simple.

Accepted exacto G++ 13.2 x64 #11327412: 0.015 s / 76 KB. La clasificación pública completa descargada el 2026-11-21 contiene 3066 filas. Excluido nuestro autor y elegidos compiladores C/C++ actuales, el tiempo ocupa 1/463 y la memoria 2/463; empates comparten puesto y tiempos inferiores a 0.015 s usan ese mínimo. Ambas metas de diez primeros pasan, sin asterisco; bajo 1024 KB la admisión estricta permite tiempo solo. El registro optimizado anterior #11303661 era 0.031 s / 128 KB; la base C++ conservada #11292869 es 0.031 s / 444 KB. Son pares independientes, sin mezclar mínimos. No fue necesario reenviar.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`2025_math_optimized.go`. Se conservan el algoritmo y sus casos límite. Se sustituye fmt por conversión de números y palabras y un búfer de salida reutilizable. La entrada completa se guarda en bytes: se intercambia ese espacio por un menor coste de la E/S general.

Accepted #11328621 (Go 1.14 x64): **0.015 s / 980 KB**. Comparación archivada: `2025_math.go` (Go 1.14 x64) — 0.031 s / 1128 KB (#11292876).

## Notas por lenguaje

Ningún lenguaje necesita nada especial.

Restar del total las parejas del mismo grupo. Contar por separado las parejas adicionales de los grupos mayores. El envío aceptado 11324249 tardó 0.140 s y usó 224 KB. La versión sencilla tardó 0.078 s y usó 448 KB. El tiempo registrado es mayor que el de la versión sencilla.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2025_math.cpp](2025_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.031 s | 444 KB | 11292869 |
| [2025_math.go](2025_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1128 KB | 11292876 |
| [2025_math.java](2025_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1628 KB | 11303364 |
| [2025_math.py](2025_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 448 KB | 11292879 |
| [2025_math.rs](2025_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 228 KB | 11292891 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2025_math_optimized.cpp](2025_math_optimized.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 76 KB | 11327412 |
| [2025_math_optimized.java](2025_math_optimized.java) | Java 1.8 | math | O(T) time; O(1) auxiliary space | AC | 0.093 s | 344 KB | 11327424 |
| [2025_math_optimized.py](2025_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.140 s | 224 KB | 11324249 |
| [2025_math_optimized.go](2025_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 980 KB | 11328621 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
