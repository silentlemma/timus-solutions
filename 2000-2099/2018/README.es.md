# 2018. Contar Secuencias con Rachas Limitadas

[Timus 2018](https://acm.timus.ru/problem.aspx?space=1&num=2018) · dificultad 102 · dp, prefix_sums

Problema original de Olga Soboleva, preparado por Alex Samsonov, de la subregión oriental del NEERC 2014.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuente las secuencias de longitud `n` formadas por 1 y 2. Una racha de unos
puede tener como máximo `a` posiciones y una de doses, como máximo `b`.
Dos secuencias son distintas si difieren en alguna posición. El resultado
se pide módulo `1 000 000 007`.

Las restricciones son `1 ≤ a,b ≤ 300` y `max(a,b)+1 ≤ n ≤ 50 000`.
Límites: 2 segundos y 64 MB.

## Entrada

La única línea contiene `n a b`.

## Salida

Imprima el número de secuencias válidas módulo `1 000 000 007`.

## Evaluación

Las salidas se comparan token a token.

## Ejemplos

```
3 2 1
```

```
4
```

## Solución

Sea one[i] el número de secuencias válidas de longitud i que terminan
con una racha de unos, y two[i] las que terminan con una racha de doses.
Una secuencia que termina con una racha de r unos, 1 ≤ r ≤ a, es una
secuencia de longitud i − r que termina en doses, seguida de la racha;
la secuencia vacía cuenta una vez de cada lado, one[0] = two[0] = 1.
Así

- one[i] = two[i − 1] + two[i − 2] + … + two[max(0, i − a)],
- two[i] = one[i − 1] + … + one[max(0, i − b)],

y la respuesta es one[n] + two[n] módulo 10⁹ + 7. Cada suma es la
diferencia de dos sumas de prefijos del mismo arreglo, así que cada
longitud cuesta `O(1)`, `O(n)` en total.

En el ejemplo n = 3, a = 2, b = 1 las secuencias son 112, 121, 211 y
212: 22 tiene una racha de doses más larga que b, y 111 una de unos más
larga que a.

Detalles a tener en cuenta:

- la secuencia vacía cuenta una vez en cada suma y nunca como respuesta;
- la diferencia de dos sumas de prefijos módulo 10⁹ + 7 puede ser
  negativa.

## Soluciones optimizadas

`2018_dp_prefix_sums_optimized.py`. Mantiene DP exacto de dos sumas deslizantes y anillos acotados. Índices avanzan con comparación/vuelta a cero, sin módulo. Ventana actualizada estrictamente entre −MOD y 2*MOD: una suma/resta devuelve [0,MOD); solo la respuesta final conserva módulo. Recurrencia, expiraciones y bordes intactos. O(N) tiempo/O(A+B) estado, sin prefijos completos; conserva DP legible.

Accepted exacto CPython 3.12 #11326671: 0.093 s / 536 KB. Comparación guardada 2026-11-20 con compiladores actuales de la familia: tiempo 2/106, memoria 6/106. Por debajo de 1024 KB, admisión estricta solo por tiempo.

- `2018_dp_prefix_sums_optimized.py`: 0.093 s / 536 KB; base didáctica conservada `2018_dp_prefix_sums.py` (Python 3.12 x64): 0.156 s / 8624 KB; cambio de tiempo -40.4%; cambio de memoria -93.8%.

La solución optimizada en Java guarda solo los valores que las sumas aún
necesitan: los últimos a + 1 valores de two y los últimos b + 1 de one,
en búferes circulares, junto con las dos sumas de ventana, que se
desplazan un paso en cada longitud en lugar de salir de sumas de
prefijos. También analiza los tres números a mano en lugar de usar
`Scanner`: 0.093 s en lugar de 0.125 s y 408 KB en lugar de 3140 KB.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`2018_parsing_optimized.go`. Se conservan la recurrencia escalar exacta y el anillo acotado uint32. Cursores explícitos avanzan cada coeficiente retrasado, evitando restos por el tamaño variable del anillo dentro del bucle. Se especializan la conversión de tokens y la salida numérica para los tipos usados, eliminando ramas generales innecesarias y conservando algoritmo y comentarios. Los dígitos completos se convierten dentro del bloque, manteniendo local el cursor hasta un límite. La acumulación negativa admite el mínimo con signo y evita una rama o llamada por dígito, conservando EOF y signos opcionales.

Accepted #11329131 (Go 1.14 x64): **0.031 s / 800 KB**. Comparación archivada: `2018_dp_prefix_sums.go` (Go 1.14 x64) — 0.031 s / 2688 KB (#11303351).

## Notas por lenguaje

- En Python `%` ya da un resto no negativo; C++, Go y Java suman el
  módulo antes de volver a tomar el resto, y Rust usa `rem_euclid`.

Mantener las dos sumas deslizantes y guardar en búferes circulares solo los estados que aún deben salir de las ventanas. El envío aceptado 11292624 tardó 0.015 s y usó 388 KB. La versión sencilla tardó 0.015 s y usó 1368 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2018_dp_prefix_sums.cpp](2018_dp_prefix_sums.cpp) | G++ 13.2 x64 | dp, prefix_sums | O(n) | AC | 0.015 s | 1368 KB | 11303350 |
| [2018_dp_prefix_sums.go](2018_dp_prefix_sums.go) | Go 1.14 x64 | dp, prefix_sums | O(n) | AC | 0.031 s | 2688 KB | 11303351 |
| [2018_dp_prefix_sums.java](2018_dp_prefix_sums.java) | Java 1.8 | dp, prefix_sums | O(n) | AC | 0.125 s | 3140 KB | 11303352 |
| [2018_dp_prefix_sums.py](2018_dp_prefix_sums.py) | Python 3.12 x64 | dp, prefix_sums | O(n) | AC | 0.156 s | 8624 KB | 11303354 |
| [2018_dp_prefix_sums.rs](2018_dp_prefix_sums.rs) | Rust 1.75 x64 | dp, prefix_sums | O(n) | AC | 0.015 s | 1648 KB | 11303355 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [2018_dp_prefix_sums_optimized.java](2018_dp_prefix_sums_optimized.java) | Java 1.8 | dp, prefix_sums | O(n) | AC | 0.093 s | 408 KB | 11303659 |
| [2018_dp_prefix_sums_optimized.cpp](2018_dp_prefix_sums_optimized.cpp) | G++ 13.2 x64 | dp, prefix_sums | O(n) | AC | 0.015 s | 388 KB | 11292624 |
| [2018_dp_prefix_sums_optimized.py](2018_dp_prefix_sums_optimized.py) | Python 3.12 x64 | dp, prefix_sums | O(n) | AC | 0.093 s | 536 KB | 11326671 |
| [2018_parsing_optimized.go](2018_parsing_optimized.go) | Go 1.14 x64 | parsing | O(n) time; O(min(n,a+b)) space | AC | 0.031 s | 800 KB | 11329131 |
