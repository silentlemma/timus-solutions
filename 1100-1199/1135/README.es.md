# 1135. Contar los giros de reclutas cara a cara hasta que la fila se estabiliza

[Timus 1135](https://acm.timus.ru/problem.aspx?space=1&num=1135) · dificultad 160 · math

Problema original del cuarto de final de la región central de Rusia, Rybinsk, 17–18 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`1 ≤ N ≤ 30000` reclutas están en fila, cada uno mirando a la izquierda
(`<`) o a la derecha (`>`). Cada segundo, todas las parejas de vecinos
que se miran (`><`) se dan la vuelta a la vez. Cuenta los giros de
parejas hasta que nada cambia, o imprime `NO` si el proceso no termina
nunca.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego exactamente `N` caracteres `<` y `>` repartidos en líneas de
hasta 255 caracteres.

## Salida

El número de giros de parejas.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
>><<><
```

Salida:

```
7
```

## Solución

Una pareja que gira, `><`, se convierte en `<>`: en cuanto a las
direcciones, es un intercambio de dos vecinos. Cada intercambio elimina
exactamente un par de reclutas (no necesariamente vecinos) con un `>`
antes de un `<`, y no crea ninguno. La fila es estable justo cuando no
queda ningún `><`, es decir, cuando todos los `<` están antes de todos los
`>`, y entonces no hay ningún par así. Por tanto el proceso siempre
termina, `NO` nunca se imprime, y el número de giros es el número de
pares con `>` antes de `<`. Una pasada los cuenta: se lleva el número de
`>` vistos hasta el momento y se suma en cada `<`. `O(N)`.

Detalles a tener en cuenta:

- se cuentan giros de parejas, no segundos transcurridos: la prueba `01`
  tiene siete giros de parejas en cuatro segundos;
- la fila está repartida en varias líneas, quizá con alguna vacía, así
  que se leen caracteres hasta reunir `N`;
- la respuesta llega a `15000² = 2,25·10⁸`, que aún cabe en 32 bits, pero
  los contadores de 64 bits no cuestan nada;
- el orden de los giros dentro de un segundo no afecta a la cuenta.

Las respuestas se compararon con una simulación segundo a segundo en 200
filas aleatorias de hasta 300 reclutas.

## Soluciones optimizadas

`1135_math_optimized.py`. Conserva sumar > anteriores por cada <, exactamente N símbolos relevantes saltando separadores. Bytes sin decodificar ni unir filas. Desactiva JIT opcional de este trabajo PyPy corto para evitar trazas calientes, vacía y sale directamente; CPython omite ajuste opcional. O(I) tiempo/espacio para I bytes; conserva conteo legible.

Frente a `1135_math.py`: tiempo 0.078 s → 0.125 s; memoria 420 KB → 288 KB.

`1135_math_optimized.go`. Al leer < suma todos los > anteriores, consumiendo exactamente N símbolos relevantes y saltando separadores. Solo contador y total, sin cadena completa. O(N+I) tiempo para I bytes y espacio auxiliar constante. Buffers acotados de entrada de 256 bytes y salida de 64 usan syscall.Read/Write de Go 1.14, reintentan EINTR/escrituras parciales y tratan EOF de cero bytes. Elimina inicialización fmt/bufio/os.File. Pruebas Linux y compilación cruzada Windows validan funcionamiento y construcción; las métricas pareadas siguientes vienen de nuestro Accepted exacto en juez Windows. Se conserva fuente didáctica legible.

Frente a `1135_math.go`: tiempo 0.031 s → 0.031 s; memoria 1100 KB → 332 KB.

La implementación rápida de Java conserva el conteo de inversiones, pero lee directamente con un búfer reutilizable de 4 KB en lugar de lectores de caracteres. Omite los saltos de línea y cuenta exactamente `N` direcciones. Mantiene tiempo `O(N)` y espacio auxiliar constante. La versión con lectores de caracteres sigue siendo la básica.

{1135_math_optimized.java}.

Ejecuciones Accepted correspondientes al código: versión básica 0.125 s / 532 KB; esta versión 0.078 s / 364 KB (envío 11307457). Cumple el objetivo de clasificación en la instantánea del 2026-10-31.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1135_math_optimized.java`: reducción de tiempo +37.60%; reducción de
  memoria +31.58%; base: `1135_math.java`.

`1135_math_optimized.rs`. Lee exactamente N símbolos de dirección omitiendo espacios. Cuenta los símbolos hacia la derecha ya vistos; cada nuevo símbolo hacia la izquierda aporta ese número de parejas enfrentadas. Cuenta cada inversión una vez sin guardar la fila: O(N) tiempo y O(1) espacio de trabajo con el límite de longitud de línea. Rust usa el entorno de C para entrada y salida, evitando cadenas String completas decodificadas y el formato de Rust. La fuente sencilla aceptada se conserva sin cambios.

Frente a `1135_math.rs`: tiempo 0.031 s → 0.015 s; memoria 248 KB → 56 KB.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1135_math.cpp](1135_math.cpp).
- [1135_math.go](1135_math.go).
- [1135_math.rs](1135_math.rs).

- Todos los lenguajes saltan los saltos de línea y llevan la misma cuenta
  acumulada.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1135_math.cpp](1135_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 132 KB | 11279403 |
| [1135_math.go](1135_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 1100 KB | 11279405 |
| [1135_math.java](1135_math.java) | Java 1.8 | math | O(N) | AC | 0.125 s | 532 KB | 11279408 |
| [1135_math.py](1135_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.078 s | 420 KB | 11279406 |
| [1135_math.rs](1135_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.031 s | 248 KB | 11279409 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1135_math_optimized.java](1135_math_optimized.java) | Java 1.8 | math | O(N) | AC | 0.078 s | 364 KB | 11307457 |
| [1135_math_optimized.rs](1135_math_optimized.rs) \* | Rust 1.75 x64 | math | O(N) | AC | 0.015 s | 56 KB | 11325144 |
| [1135_math_optimized.go](1135_math_optimized.go) \* | Go 1.14 x64 | math | O(N+I) time; O(1) space | AC | 0.031 s | 332 KB | 11325651 |
| [1135_math_optimized.py](1135_math_optimized.py) \* | PyPy 3.10 x64 | math | O(I) time; O(I) space | AC | 0.125 s | 288 KB | 11325852 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
