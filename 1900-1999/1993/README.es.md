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

Se conserva la prueba del análisis por roles. C++/Go compactos guardan intervalos en un único búfer ASCII acotado, sin copiar frases ni crear objetos de flujo/cadena. El recorrido salta cada grupo completo y registra objeto, sujeto y verbo; una palabra exterior es la conjunción opcional de la segunda cláusula. Se emiten conjunción y roles ordenados, la coma original, todas las letras minúsculas salvo la primera del resultado. Sin anidación y con roles únicos, cada frase sale una vez y mantiene sus palabras. Python usa cortes y flujos existentes. Para L<=100, tiempo y espacio O(L).

- `1993_parsing_optimized.cpp`: 0.015 s / 76 KB; base `1993_parsing.cpp`: 0.015 s / 388 KB; cambio respecto a la base: tiempo -0.0%, memoria -80.4%.
- `1993_parsing_optimized.go`: 0.015 s / 272 KB; base `1993_parsing.go`: 0.031 s / 1184 KB; cambio respecto a la base: tiempo -51.6%, memoria -77.0%.
- `1993_parsing_strings.py`: 0.156 s / 300 KB; base `1993_parsing.py`: 0.062 s / 504 KB; cambio respecto a la base: tiempo +151.6%, memoria -40.5%.

## Notas por lenguaje

Instantáneas guardadas: 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en ambas métricas; las otras familias exigen el primer puesto en ambas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

Se usa el perfil guardado de compiladores actuales, sin nuestro autor ni registros antiguos inferiores a 0,015 s; salvo C++, se exige ID de envío ≥10770000. La memoria de C++ se compara con las primeras 1000 filas admisibles. Los tiempos propios inferiores a 0,015 s se consideran 0,015 s. El corte por ID es una regla fija, no un filtro exacto de fechas.

- C++: base didáctica preferida `1993_parsing.cpp`; fuente que cubre `1993_parsing_optimized.cpp`; puestos tiempo/memoria 1/1, registros de otros autores 63/63.

- Go: base didáctica preferida `1993_parsing.go`; fuente que cubre `1993_parsing_optimized.go`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

- Java: base didáctica preferida `1993_parsing.java`; fuente que cubre `1993_parsing.java`; puestos tiempo/memoria 1/1, registros de otros autores 3/3.

- Python/PyPy: base didáctica preferida `1993_parsing.py`; fuente que cubre `1993_parsing_strings.py`; puestos tiempo/memoria 13/4, registros de otros autores 12/12.

- Rust: base didáctica preferida `1993_parsing.rs`; fuente que cubre `1993_parsing.rs`; puestos tiempo/memoria 1/1, registros de otros autores 0/0.

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

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
