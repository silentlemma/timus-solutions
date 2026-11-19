# 1993. Reordenar frases marcadas y corregir mayúsculas

[Timus 1993](https://acm.timus.ru/problem.aspx?space=1&num=1993) · dificultad 204 · parsing, strings

Problema original de Denis Dublennykh, preparado por Eugene Kurpilyansky.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Reordene una oración marcada. Cada cláusula contiene exactamente un
objeto en `{llaves}`, un sujeto en `(paréntesis)` y una frase verbal en
`[corchetes]`, en orden arbitrario. Cada grupo tiene una o más palabras.
Hay una cláusula o dos separadas por una única coma. Después de la coma
puede haber una conjunción de una palabra sin marcar; es la única
palabra posible fuera de grupos.

Ordene cada cláusula como objeto, sujeto, verbo, suprima los signos de
agrupación y conserve el orden interno de cada frase. Mantenga la
conjunción antes de la segunda cláusula reordenada. Solo la primera
letra de la primera palabra de toda la salida es mayúscula; las demás
son minúsculas, también después de la coma.

Longitud máxima: 100 caracteres. Las palabras contienen letras latinas.
Al principio solo la primera letra de la primera palabra es mayúscula.
Los grupos no se anidan y sus signos están en límites de palabras. Hay
un espacio entre palabras, ninguno antes de comas o cierres ni después
de aperturas. Tiempo: 1 segundo; memoria: 64 MB.

## Entrada

Una línea completa con la oración marcada.

## Salida

Una línea reordenada. Un espacio entre palabras, ninguno antes de la
coma y uno después. No añada puntuación.

## Evaluación

La salida se compara carácter por carácter, salvo el salto final opcional.

- `1993_parsing_optimized.cpp` (G++ 13.2 x64): 102 pruebas del repositorio; 112 comparaciones adicionales de fuente exacta.

- `1993_parsing_optimized.go` (Go 1.14 x64): 102 pruebas del repositorio; 102 comparaciones adicionales de fuente exacta.

- `1993_parsing_strings.py` (PyPy 3.10 x64): 102 pruebas del repositorio.

## Ejemplos

Entrada:

```
(We) [are] {blind}, if (we) [could not see] {creation of this clone army}
```

Salida:

```
Blind we are, if creation of this clone army we could not see
```

Entrada:

```
{Truly wonderful} (the mind of a child) [is]
```

Salida:

```
Truly wonderful the mind of a child is
```

## Solución

Convierta primero toda la entrada a minúsculas: la palabra inicial puede
pasar al medio y debe perder su mayúscula. Separe por la coma, que no
puede estar dentro de una frase compuesta únicamente por palabras.

Recorra cada cláusula de izquierda a derecha. Al encontrar `{`, `(` o
`[`, busque su cierre, guarde el interior en la casilla de objeto,
sujeto o verbo y salte al final del grupo. Las letras exteriores forman
la conjunción opcional; omita espacios. Una la conjunción, si existe, y
las tres casillas en orden objeto–sujeto–verbo. Una las cláusulas
mediante `, ` y convierta a mayúscula solo el primer carácter del
resultado completo.

La ausencia de anidamiento hace que el cierre termine exactamente la
frase actual. El tipo de apertura determina unívocamente su función y
hay una frase por función. Guardar el interior conserva las palabras y
su orden interno. Como se saltan grupos completos, las letras exteriores
leídas son precisamente la conjunción opcional.

La reconstrucción emite cada frase una vez en el orden requerido y deja
la conjunción delante de la segunda cláusula. La coma sigue separando
las mismas cláusulas. Convertir primero a minúsculas y capitalizar
únicamente el primer carácter final corrige tanto la antigua como la
nueva palabra inicial. Por ello palabras, orden, puntuación y mayúsculas
son correctos.

En el primer ejemplo el objeto pasa al inicio y la conjunción sigue tras
la coma. En el segundo el objeto ya estaba primero y conserva su orden
interno.

## Soluciones optimizadas

`1993_parsing_optimized.rs`. Conserva parser de tres roles y prefijo opcional, espacios de comas y mayúscula solo al primer byte emitido. Un vector de entrada en minúsculas ASCII; guarda rangos de roles/prefijo en vez de cadenas y uniones. Emite rangos directamente. O(L) tiempo/entrada retenida, misma gramática.

Frente a `1993_parsing.rs`: tiempo 0.046 s → 0.015 s; memoria 224 KB → 80 KB.

`1993_parsing_optimized.java`. Conserva orden objeto-sujeto-verbo, guardando índices de inicio/fin en la oración original, sin pasar toda la línea a minúsculas, separar cláusulas ni copiar subcadenas. Emite esas secciones y convierte ASCII al escribir. Solo la primera letra de salida queda mayúscula; la conjunción opcional precede a la segunda cláusula reordenada y sigue minúscula. Mantiene comas y espacios exactos. Tiempo O(L); el String de entrada aún ocupa O(L), pero índices y búfer están acotados. No retiene StringBuilder de respuesta completa.

Frente a `1993_parsing.java`: tiempo 0.109 s → 0.078 s; memoria 472 KB → 528 KB.

Se conserva la prueba del análisis por roles. C++/Go compactos guardan intervalos en un único búfer ASCII acotado, sin copiar frases ni crear objetos de flujo/cadena. El recorrido salta cada grupo completo y registra objeto, sujeto y verbo; una palabra exterior es la conjunción opcional de la segunda cláusula. Se emiten conjunción y roles ordenados, la coma original, todas las letras minúsculas salvo la primera del resultado. Sin anidación y con roles únicos, cada frase sale una vez y mantiene sus palabras. Python usa cortes y flujos existentes. Para L<=100, tiempo y espacio O(L).

- `1993_parsing_optimized.cpp`: 0.015 s / 76 KB; base `1993_parsing.cpp`: 0.015 s / 388 KB; cambio respecto a la base: tiempo -0.0%, memoria -80.4%.
- `1993_parsing_optimized.go`: 0.015 s / 272 KB; base `1993_parsing.go`: 0.031 s / 1184 KB; cambio respecto a la base: tiempo -51.6%, memoria -77.0%.
- `1993_parsing_strings.py`: 0.156 s / 300 KB; base `1993_parsing.py`: 0.062 s / 504 KB; cambio respecto a la base: tiempo +151.6%, memoria -40.5%.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1993_parsing_optimized.java`: puesto de tiempo 2/65 y de memoria 5/65 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1993_parsing.cpp](1993_parsing.cpp) | G++ 13.2 x64 | parsing | O(L) | AC | 0.015 s | 388 KB | 11292395 |
| [1993_parsing.go](1993_parsing.go) | Go 1.14 x64 | parsing | O(L) | AC | 0.031 s | 1184 KB | 11292397 |
| [1993_parsing.java](1993_parsing.java) | Java 1.8 | parsing | O(L) | AC | 0.109 s | 472 KB | 11309216 |
| [1993_parsing.py](1993_parsing.py) | Python 3.12 x64 | parsing | O(L) | AC | 0.062 s | 504 KB | 11292399 |
| [1993_parsing.rs](1993_parsing.rs) | Rust 1.75 x64 | parsing | O(L) | AC | 0.046 s | 224 KB | 11292401 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1993_parsing_optimized.cpp](1993_parsing_optimized.cpp) | G++ 13.2 x64 | parsing | O(L) time and space | AC | 0.015 s | 76 KB | 11308436 |
| [1993_parsing_optimized.go](1993_parsing_optimized.go) | Go 1.14 x64 | parsing | O(L) time and space | AC | 0.015 s | 272 KB | 11309761 |
| [1993_parsing_strings.py](1993_parsing_strings.py) \* | PyPy 3.10 x64 | parsing, strings | O(L) time and space | AC | 0.156 s | 300 KB | 11309689 |
| [1993_parsing_optimized.java](1993_parsing_optimized.java) \* | Java 1.8 | parsing | O(L) | AC | 0.078 s | 528 KB | 11325023 |
| [1993_parsing_optimized.rs](1993_parsing_optimized.rs) \* | Rust 1.75 x64 | parsing | O(L) time; O(L) space | AC | 0.015 s | 80 KB | 11325535 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
