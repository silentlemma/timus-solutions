# 1283. Enano

[Timus 1283](https://acm.timus.ru/problem.aspx?space=1&num=1283) · dificultad 116 · math

Problema original de Leonid Volkov (preparado por Ivan Dashkevich), del Concurso Individual de la Universidad Estatal de los Urales 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un enano tiene G unidades de oro, y cada año un banco se queda con el p
por ciento como comisión (1 ≤ p ≤ 99), así que el oro queda en
(100 − p)/100 de lo que era. Cuando el oro no pasa de L, la vida del
enano pierde el sentido. G y L son enteros no mayores que 2³¹ − 1.
¿Cuántos años quedan?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

G, L y p.

## Salida

El número de años.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
19 10 50
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
1000 1 1
```

Salida:

```
688
```

## Solución

Tras k años el oro es exactamente G · ((100 − p)/100)^k, y la respuesta
es el primer k con eso como mucho L. En números enteros la prueba es

```text
G · (100 − p)^k ≤ L · 100^k
```

así que cada año se multiplican los dos lados, por 100 − p y por 100,
hasta que el izquierdo deja de ser mayor. El bucle da como mucho unas
2140 vueltas, con G = 2³¹ − 1, L = 1 y p = 1, y los números crecen hasta
unos miles de cifras. `O(Y²)` operaciones con cifras para Y años.

La cota del número de iteraciones supone G y L positivos, y el
enunciado no les da límites inferiores: con G > 0 y L = 0, el oro sigue
siendo positivo tras cualquier número finito de años, y no hay respuesta
finita.

Detalles a tener en cuenta:

- el oro puede caer justo en el límite, y la coma flotante no lo ve:
  300 · 0,81 da 243,00000000000003, un año de más con L = 243
  (prueba 05), y ln(9801/10000) / ln(0,99) redondea hacia arriba a tres
  años en vez de dos (prueba 06);
- si el oro ya no pasa de L, la respuesta es 0 (pruebas 03, 04).

## Soluciones optimizadas

`1283_binary_search_math.py`. Busca primer año Y con G(100−p)^Y≤L100^Y mediante duplicar cota y búsqueda binaria de potencias enteras exactas. Sin logaritmos,importar gcd/math ni multiplicación por cada año. G≤L incluido cero inmediato, igualdades exactas. Bits D y coste M(D): cota O(log²(Y+1)·M(D)) tiempo,O(D) espacio. Algoritmo de búsqueda con nombre propio, conserva versión anual sencilla.

Frente a `1283_math.py`: tiempo 0.078 s → 0.125 s; memoria 480 KB → 264 KB.

La solución optimizada en Java guarda cada lado como un arreglo de
dígitos en base 10⁹ que multiplica en su sitio, ampliando el arreglo
solo cuando aparece un dígito nuevo, en lugar de crear dos objetos
`BigInteger` nuevos cada año; un dígito por como mucho 100 más el
acarreo sigue por debajo de 10¹¹ y cabe en `long`. Lee G, L y p cifra a
cifra directamente desde `System.in` en `int`, que basta porque no pasan
de 2³¹ − 1, en lugar de crear un `Scanner`: {1283_math_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1283_math_optimized.java`: reducción de tiempo +0.00%; reducción de
  memoria +93.57%; base: `1283_math.java`.

`1283_math_optimized.rs`. Conserva la comparación exacta de G*(100-p)^Y y L*100^Y, reduciendo antes G/L y (100-p)/100 por sus mcd. Mantiene ambos productos en u128 mientras la multiplicación comprobada funcione; al desbordar convierte los dos valores previos intactos en dígitos u32 de base 10^9 y continúa exactamente. G<=L devuelve cero antes de reducir. Ningún logaritmo, flotante ni epsilon decide cuándo parar. Con Y años y hasta D dígitos, tiempo O(Y·D), espacio O(D); los dígitos estrechos y la vía de enteros nativos reducen el coste. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1283_math.rs`: tiempo 0.015 s → 0.031 s; memoria 232 KB → 68 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1283_parsing_optimized.go`. Se mantienen productos y comparaciones exactos por pequeños bloques con razón reducida; se especializan las tres entradas enteras y el año final sin conversión genérica de flujos. Se especializan la conversión de tokens y la salida numérica para los tipos usados, eliminando ramas generales innecesarias y conservando algoritmo y comentarios. Los dígitos completos se convierten dentro del bloque, manteniendo local el cursor hasta un límite. La acumulación negativa admite el mínimo con signo y evita una rama o llamada por dígito, conservando EOF y signos opcionales.

Accepted #11329132 (Go 1.14 x64): **0.015 s / 812 KB**. Comparación archivada: `1283_math.go` (Go 1.14 x64) — 0.031 s / 1276 KB (#11284478).

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1283_math_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1283_math.cpp](1283_math.cpp) | G++ 13.2 x64 | math | O(Y²) | AC | 0.015 s | 204 KB | 11284476 |
| [1283_math.go](1283_math.go) | Go 1.14 x64 | math | O(Y²) | AC | 0.031 s | 1276 KB | 11284478 |
| [1283_math.java](1283_math.java) | Java 1.8 | math | O(Y²) | AC | 0.109 s | 5600 KB | 11284490 |
| [1283_math.py](1283_math.py) | Python 3.12 x64 | math | O(Y²) | AC | 0.078 s | 480 KB | 11284484 |
| [1283_math.rs](1283_math.rs) | Rust 1.75 x64 | math | O(Y²) | AC | 0.015 s | 232 KB | 11284494 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1283_math_optimized.java](1283_math_optimized.java) | Java 1.8 | math | O(Y²) | AC | 0.109 s | 360 KB | 11304347 |
| [1283_math_optimized.rs](1283_math_optimized.rs) | Rust 1.75 x64 | math | O(Y·D) | AC | 0.031 s | 68 KB | 11325092 |
| [1283_binary_search_math.py](1283_binary_search_math.py) \* | PyPy 3.10 x64 | binary_search, math | O(log²(Y+1)·M(D)) time; O(D) space | AC | 0.125 s | 264 KB | 11325857 |
| [1283_parsing_optimized.go](1283_parsing_optimized.go) | Go 1.14 x64 | parsing | O(Y²) | AC | 0.015 s | 812 KB | 11329132 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
