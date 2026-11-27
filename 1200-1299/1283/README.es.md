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
81 64 20
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
625 256 20
```

Salida:

```
4
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
unos miles de cifras. Para `Y` años e inputs iniciales positivos acotados,
cada producto tiene `O(Y+1)` cifras o bloques de base fija. Las versiones
sencillas necesitan `O((Y+1)²)` operaciones con cifras y `O(Y+1)` cifras/
bloques auxiliares vivos, incluidos los productos temporales. El `+1`
incluye el retorno inmediato de cero años. Entrada y búferes se cuentan
aparte: Rust conserva la cadena completa, Python la línea leída y los
otros usan búferes scanner/stdio acotados. El formato indicado solo
contiene tres números acotados.

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

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

`1283_binary_search_math.py`. Busca primer año Y con G(100−p)^Y≤L100^Y mediante duplicar cota y búsqueda binaria de potencias enteras exactas. Sin logaritmos,importar gcd/math ni multiplicación por cada año. G≤L incluido cero inmediato, igualdades exactas. Bits D y coste M(D): cota O(log²(Y+2)·M(D)) tiempo,O(D) espacio. Algoritmo de búsqueda con nombre propio, conserva versión anual sencilla.

Frente a `1283_math.py`: tiempo 0.078 s → 0.125 s; memoria 480 KB → 264 KB.

La solución optimizada en Java guarda cada lado como un arreglo de
dígitos en base 10⁹ que multiplica en su sitio, ampliando el arreglo
solo cuando aparece un dígito nuevo, en lugar de crear dos objetos
`BigInteger` nuevos cada año; un dígito por como mucho 100 más el
acarreo sigue por debajo de 10¹¹ y cabe en `long`. Lee G, L y p cifra a
cifra directamente desde `System.in` en `int`, que basta porque no pasan
de 2³¹ − 1, en lugar de crear un `Scanner`: [1283_math_optimized.java](1283_math_optimized.java).

### Mejora medida

Los porcentajes siguientes describen los pares históricos de las tablas,
no otro requisito de mejora del 30%. Se conservan las versiones sencillas
significativas. Java utiliza la misma comparación anual exacta con bloques
mutables: con inputs iniciales acotados ocupa `O(Y+1)` bloques vivos más
búferes, incluidos los arrays temporales al ampliar la capacidad.

- `1283_math_optimized.java`: reducción de tiempo +0.00%; reducción de
  memoria +93.57%; base: `1283_math.java`.

`1283_math_optimized.rs`. Conserva la comparación exacta de G*(100-p)^Y y L*100^Y, reduciendo antes G/L y (100-p)/100 por sus mcd. Mantiene ambos productos en u128 mientras la multiplicación comprobada funcione; al desbordar convierte los dos valores previos intactos en dígitos u32 de base 10^9 y continúa exactamente. G<=L devuelve cero antes de reducir. Ningún logaritmo, flotante ni epsilon decide cuándo parar. Con Y años y hasta D dígitos, tiempo O((Y+1)·D), espacio O(D); los dígitos estrechos y la vía de enteros nativos reducen el coste. La versión Rust lee y escribe mediante el entorno de C, sin conservar un String de entrada decodificada ni construir un String de salida con formato. Se conserva la fuente sencilla con Accepted.

Frente a `1283_math.rs`: tiempo 0.015 s → 0.031 s; memoria 232 KB → 68 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

El fuente Go actual solo extrae la capacidad de salida intacta de 24 bytes
en una constante para el linter estructural. Los demás fuentes de
solución siguen intactos.

`1283_parsing_optimized.go`. A diferencia de `1283_math.go`, que usa
`math/big` y los factores sin reducir `100-p` y `100`, introduce bloques
mutables `[]uint32` de base 10⁹, menos significativo primero. Divide los
factores anuales por su mcd antes de aumentar los dos productos exactos;
no reduce el `G/L` inicial. La multiplicación por bloques y la comparación
por longitud y bloques superiores sustituyen la aritmética genérica. Un
búfer recargable de 256 bytes analiza los tres enteros con cursor local
y acumulación decimal negativa; búferes temporales fijos imprimen los años.
La desigualdad de parada y la igualdad se conservan. Con hasta `D` bloques,
tiempo `O((Y+1)·D)` y espacio auxiliar vivo `O(D+B)` para búferes fijos `B`;
los valores iniciales acotados dan `D = O(Y+1)`.

Accepted #11329132 (Go 1.14 x64): **0.015 s / 812 KB**. Comparación archivada: `1283_math.go` (Go 1.14 x64) — 0.031 s / 1276 KB (#11284478).

## Notas por lenguaje

Los [criterios compartidos](../../RATING_CRITERIA.md) rigen todos los lenguajes:
diez primeros o 15% superior para las métricas necesarias, reemplazados
por la referencia con 1–10 rivales del mismo compilador. Por debajo de
1024 KB solo se compara tiempo. Se excluyen rivales más rápidos que
`0.015 s`; solo nuestro tiempo se eleva a ese mínimo. No hay otro
requisito de primer puesto o mejora del 30%, ni corte por fecha o ID.

La auditoría guardada admite ambos fuentes Rust por ranking ordinario
de tiempo, incluido el optimizado (`0.031 s / 68 KB`); la explicación
anterior de falta de referencia queda obsoleta. C++, CPython sencillo y
Java optimizado también cumplen ranking ordinario de tiempo. Go optimizado
cumple la referencia del grupo pequeño del mismo compilador solo por tiempo.
Go y Java sencillos no cumplen sus comparaciones, pero se conservan para
enseñanza. El PyPy binario adicional no cumple tiempo y mantiene su marca;
CPython ya cierra la posición Python. La discusión del 18 de noviembre de
2026 es histórica; se conservan todas las mediciones Accepted emparejadas.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1283_math.cpp](1283_math.cpp) | G++ 13.2 x64 | math | O((Y+1)²) | AC | 0.015 s | 204 KB | 11284476 |
| [1283_math.go](1283_math.go) | Go 1.14 x64 | math | O((Y+1)²) | AC | 0.031 s | 1276 KB | 11284478 |
| [1283_math.java](1283_math.java) | Java 1.8 | math | O((Y+1)²) | AC | 0.109 s | 5600 KB | 11284490 |
| [1283_math.py](1283_math.py) | Python 3.12 x64 | math | O((Y+1)²) | AC | 0.078 s | 480 KB | 11284484 |
| [1283_math.rs](1283_math.rs) | Rust 1.75 x64 | math | O((Y+1)²) | AC | 0.015 s | 232 KB | 11284494 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1283_math_optimized.java](1283_math_optimized.java) | Java 1.8 | math | O((Y+1)²) | AC | 0.109 s | 360 KB | 11304347 |
| [1283_math_optimized.rs](1283_math_optimized.rs) | Rust 1.75 x64 | math | O((Y+1)·D) | AC | 0.031 s | 68 KB | 11325092 |
| [1283_binary_search_math.py](1283_binary_search_math.py) \* | PyPy 3.10 x64 | binary_search, math | O(log²(Y+2)·M(D)) time; O(D) space | AC | 0.125 s | 264 KB | 11325857 |
| [1283_parsing_optimized.go](1283_parsing_optimized.go) | Go 1.14 x64 | parsing | O((Y+1)²) | AC | 0.031 s | 808 KB | 11331000 |

\* Accepted; aún no se alcanza el objetivo de [RATING_CRITERIA.md](../../RATING_CRITERIA.md). Esta versión puede optimizarse más.
