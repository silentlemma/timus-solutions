# 1179. La base en la que un texto contiene más números

[Timus 1179](https://acm.timus.ru/problem.aspx?space=1&num=1179) · dificultad 295 · strings

Problema original de Pavel Atnashev, del Tercer Concurso Individual de Programación de la Universidad Estatal de los Urales, Ekaterimburgo, 16 de febrero de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un texto de hasta 1 MB consta de dígitos, letras latinas mayúsculas,
espacios y saltos de línea; las letras son dígitos de `A = 10` a `Z = 35`.
En base `K`, un número es una racha máxima de caracteres que son dígitos
de la base `K`. Hay que hallar la base `K` de 2 a 36 en la que el texto
tiene más números, la menor en caso de empate, y esa cantidad.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El texto.

## Salida

`K` y el número de números.

## Evaluación

Comparar los dos tokens enteros. Cada una de las siete fuentes nuevas tiene 13 pruebas del repositorio y 159 ejecuciones extra guardadas, incluidas fronteras de bloques y textos máximos. Cada Python suma 62403 ejecuciones anfitrionas contra un contador independiente con regex: parejas/triples de 37 valores, textos cortos exhaustivos y espacios aleatorios. No son totales de ejecuciones nativas.

## Ejemplos

### Ejemplo 1

Entrada:

```
01234B56789
AZA
```

Salida:

```
11 4
```

## Solución

Probar cada base `k=2..36` por separado. Recorrer el texto recordando si
el carácter anterior era un dígito válido. Un número comienza exactamente
en un dígito precedido por un separador. Así se cuenta una vez cada tramo
máximo, incluido el que empieza al principio. Actualizar solo al aumentar
el máximo conserva la menor base en empates. Tiempo `O(35L)`, espacio `O(L)`.

Python hace el mismo recorrido con operaciones nativas de bytes: antepone
un separador, traduce a cero (separador) o uno (dígito) y cuenta `01`, patrón
que no puede solaparse consigo mismo. Amplía la tabla al crecer la base.
Texto vacío o sin dígitos produce `2 0`; espacios y saltos separan números,
y `Z` es dígito en base 36.

## Soluciones optimizadas

Asignar 36 a los separadores e imaginar uno antes del texto. La pareja
`(left,right)` inicia un número en base `k` si `right<k≤left`. Cuando
`right<left` aporta al intervalo `max(2,right+1)..left`. Sumar sus extremos
en un arreglo de diferencias y recorrer las 35 bases. Cada número tiene
una única pareja inicial, lo que prueba la cuenta. Las versiones nativas
previas cuentan parejas en una tabla 37×37; Java/Python nuevos añaden los
eventos directamente al leer bloques acotados, conservando el último valor.
Tiempo `O(L+37²)` para las tablas nativas y `O(L+36)` para las versiones
por bloques; estas usan espacio independiente de L.

El Python anterior traduce el texto completo y cuenta patrones mediante
un número fijo de llamadas nativas: `O(37²L)` al hacer explícito el alfabeto,
no `O(L+37²)`, y `O(L)` memoria. Se conserva como alternativa Accepted sin
etiqueta rápida respecto a la nueva base. Ambos Java de eventos cumplen
30% contra la base directa; el 29,93% de memoria del nuevo contra el viejo
por sí solo no se redondea a 30%.

- `1179_strings.cpp`: 0.031 s / 116 KB; base `1179_bruteforce_strings.cpp`: 0.171 s / 2836 KB; cambio respecto a la base: tiempo -81.9%, memoria -95.9%.
- `1179_strings.go`: 0.015 s / 3160 KB; base `1179_bruteforce_strings.go`: 0.203 s / 3136 KB; cambio respecto a la base: tiempo -92.6%, memoria +0.8%.
- `1179_strings.java`: 0.125 s / 588 KB; base `1179_bruteforce_strings.java`: 0.406 s / 3464 KB; cambio respecto a la base: tiempo -69.2%, memoria -83.0%.
- `1179_strings_optimized.py`: 0.203 s / 396 KB; base `1179_bruteforce_strings.py`: 0.218 s / 3128 KB; cambio respecto a la base: tiempo -6.9%, memoria -87.3%.
- `1179_strings_optimized.java`: 0.109 s / 412 KB; base `1179_bruteforce_strings.java`: 0.406 s / 3464 KB; cambio respecto a la base: tiempo -73.2%, memoria -88.1%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `1179_bruteforce_strings.cpp`; fuente que cubre `1179_strings.cpp`; puestos tiempo/memoria 4/2, registros de otros autores 44/44.

- Go: base didáctica preferida `1179_bruteforce_strings.go`; fuente que cubre `1179_strings.go`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

- Java: base didáctica preferida `1179_bruteforce_strings.java`; fuente que cubre `1179_strings.java`; puestos tiempo/memoria 2/1, registros de otros autores 4/4.

- Python/PyPy: base didáctica preferida `1179_bruteforce_strings.py`; fuente que cubre `1179_strings_optimized.py`; puestos tiempo/memoria 1/1, registros de otros autores 5/5.

- Rust: base didáctica preferida `1179_bruteforce_strings.rs`; fuente que cubre `1179_bruteforce_strings.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1179_bruteforce_strings.cpp](1179_bruteforce_strings.cpp) | G++ 13.2 x64 | bruteforce, strings | O(35 L) time; O(L) space | AC | 0.171 s | 2836 KB | 11309345 |
| [1179_bruteforce_strings.go](1179_bruteforce_strings.go) | Go 1.14 x64 | bruteforce, strings | O(35 L) time; O(L) space | AC | 0.203 s | 3136 KB | 11309346 |
| [1179_bruteforce_strings.java](1179_bruteforce_strings.java) | Java 1.8 | bruteforce, strings | O(35 L) time; O(L) space | AC | 0.406 s | 3464 KB | 11309350 |
| [1179_bruteforce_strings.py](1179_bruteforce_strings.py) | Python 3.12 x64 | bruteforce, strings | O(35 L) time; O(L) space | AC | 0.218 s | 3128 KB | 11309344 |
| [1179_bruteforce_strings.rs](1179_bruteforce_strings.rs) | Rust 1.75 x64 | bruteforce, strings | O(35 L) time; O(L) space | AC | 0.031 s | 2128 KB | 11309349 |

### Otros enfoques Accepted

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1179_strings.py](1179_strings.py) | Python 3.12 x64 | strings | O(37^2 L) time; O(L) space | AC | 0.640 s | 3100 KB | 11283287 |
| [1179_strings.rs](1179_strings.rs) | Rust 1.75 x64 | strings | O(L+37^2) time | AC | 0.015 s | 2124 KB | 11283294 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1179_strings.cpp](1179_strings.cpp) | G++ 13.2 x64 | strings | O(L+37^2) time | AC | 0.031 s | 116 KB | 11283281 |
| [1179_strings.go](1179_strings.go) | Go 1.14 x64 | strings | O(L+37^2) time | AC | 0.015 s | 3160 KB | 11283283 |
| [1179_strings.java](1179_strings.java) \* | Java 1.8 | strings | O(L+37^2) time | AC | 0.125 s | 588 KB | 11283292 |
| [1179_strings_optimized.py](1179_strings_optimized.py) | Python 3.12 x64 | strings | O(L+36) time; bounded block/table space | AC | 0.203 s | 396 KB | 11309351 |
| [1179_strings_optimized.java](1179_strings_optimized.java) \* | Java 1.8 | strings | O(L+36) time; bounded block/table space | AC | 0.109 s | 412 KB | 11309353 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
