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

La salida se compara exactamente, carácter a carácter; solo puede
diferir el último salto de línea.

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

## Notas por lenguaje

Con longitud `L≤100`, las posiciones solo avanzan y cada frase se copia
una vez: tiempo y memoria `O(L)`. Hay como máximo seis frases; no hace
falta recursión ni un analizador de anidamiento general.

Lea toda la línea, no un token. Mantenga completas las frases de varias
palabras. No capitalice la segunda cláusula ni cada palabra. Python y Go
convierten directamente a minúsculas; Java usa `Locale.ROOT`, C++
entrega caracteres sin signo a las funciones de conversión, y Rust usa
conversión ASCII e índices de bytes. El alfabeto permitido es ASCII, por
lo que son seguros. Extraer grupos con una expresión regular es otra
opción; el recorrido solo necesita la biblioteca estándar.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1993_parsing.cpp](1993_parsing.cpp) | G++ 13.2 x64 | parsing | O(L) | AC | 0.015 s | 388 KB |
| [1993_parsing.go](1993_parsing.go) | Go 1.14 x64 | parsing | O(L) | AC | 0.031 s | 1184 KB |
| [1993_parsing.java](1993_parsing.java) | Java 1.8 | parsing | O(L) | AC | 0.093 s | 504 KB |
| [1993_parsing.py](1993_parsing.py) | Python 3.12 x64 | parsing | O(L) | AC | 0.062 s | 504 KB |
| [1993_parsing.rs](1993_parsing.rs) | Rust 1.75 x64 | parsing | O(L) | AC | 0.046 s | 224 KB |
