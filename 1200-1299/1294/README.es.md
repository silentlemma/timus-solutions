# 1294. Satélites marcianos

[Timus 1294](https://acm.timus.ru/problem.aspx?space=1&num=1294) · dificultad 317 · geometry

Problema original de Vladimir Yakovlev, de la Novena Competición Abierta por Equipos de Programación para Escolares, 13 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuatro satélites A, B, C y D están en una misma órbita circular, en
este orden. Se conocen las distancias AD, AC, BD y BC en miles de
kilómetros (enteros de 1 a 10 000); el radio de la órbita no. Hay que
hallar la distancia CD en kilómetros, redondeada a entero, o indicar
que no se puede determinar de forma única.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

AD, AC, BD y BC.

## Salida

`Distance is X km.` o `Impossible.`

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

## Ejemplos

### Ejemplo 1

Entrada:

```
50 40 40 14
```

Salida:

```
Distance is 30000 km.
```

## Actualización de envíos aceptados

La corrección de espacios de Python tiene Accepted del fuente exacto
#11330228 (`0.093 s / 424 KB`) en la tabla. Medidas anteriores son
históricas. Comparaciones numéricas guardadas confirman C++, Go, Java
y Python; Rust tiene código Accepted sin referencia comparable.
Se conservan las versiones didácticas y optimizadas distintas.

## Solución

Sean a = AD, b = AC, c = BD, d = BC y x = CD. Los puntos A y B están en
el mismo arco que corta la cuerda CD, así que la ven con el mismo
ángulo inscrito t. El teorema del coseno en los triángulos ACD y BCD da

x² = a² + b² − 2ab cos t = c² + d² − 2cd cos t,

dos ecuaciones en x² y cos t. Por tanto

cos t = (a² + b² − c² − d²) / (2 (ab − cd)),

x² = (ab (c² + d²) − cd (a² + b²)) / (ab − cd).

- Si ab = cd, las ecuaciones o se contradicen o no dicen nada sobre t.
  En el segundo caso, por ejemplo un trapecio isósceles, CD de verdad
  puede tomar muchos valores (prueba 02). En ambos casos la respuesta es
  `Impossible.` (pruebas 02 y 03).
- Si |a² + b² − c² − d²| ≥ 2 |ab − cd|, no existe un triángulo no
  degenerado: la igualdad también falla, porque tres puntos distintos
  de una circunferencia no pueden ser colineales (pruebas 04 y 07).
- El teorema de Ptolomeo exige AB · CD = bc − ad > 0 para el orden dado.
  Si bc ≤ ad, la respuesta es `Impossible.` (pruebas 05 y 07). Junto con
  la cota estricta del coseno, esta comprobación garantiza el orden
  correcto de los puntos reconstruidos.
- Si no, x = 1000 · √x² kilómetros, redondeado.

Todas las comprobaciones de existencia usan enteros exactos de 64 bits
(los productos originales son menores que 2 · 10¹⁶). Se normalizan el
numerador y el denominador para que sean positivos. Una raíz cuadrada
en coma flotante estima la parte entera m de la distancia en kilómetros;
se redondea hacia arriba exactamente si
(2m + 1)² ≤ floor(4 · 1000² · num / den). Para evitar desbordamientos,
se calcula la cota como s · (num div den) + (s · (num mod den)) div den,
donde s = 4 · 1000². Los nuevos valores intermedios son menores que
2 · 10¹⁵. El tiempo y el espacio auxiliar son `O(1)`.

Las comprobaciones corregidas y los resultados redondeados se verifican
reconstruyendo AB independientemente, comprobando desigualdades
triangulares estrictas y orden cíclico, luego las cuatro cuerdas y
circunferencia común con coordenadas racionales. También se certifican
Ptolomeo y redondeo exacto. El main Python intacto coincide en las
20736 cuádruplas de `[1, 12]` y 1000 entradas de rango completo con semilla fija.

Detalles a tener en cuenta:

- los datos están en miles de kilómetros y la respuesta en kilómetros
  (prueba 01);
- AD · AC = BD · BC no siempre significa datos contradictorios: a veces
  significa muchas respuestas (pruebas 02 y 03);
- un coseno en [−1, 1] no basta: hay que excluir los triángulos
  degenerados y comprobar el orden cíclico (prueba 07).

Las revisiones de los fuentes descritas arriba ya obtuvieron sus propios Accepted. Las tablas de soluciones indican los envíos finales que corresponden a cada fuente y sus mediciones conjuntas de tiempo y memoria; las observaciones anteriores describen revisiones previas. Se conservan todas las implementaciones sencillas con valor didáctico.

## Soluciones optimizadas

`1294_geometry_optimized.java`. Java conserva el algoritmo y las estructuras descritas para la versión sencilla. Un búfer fijo de bytes y FastInput sustituyen Scanner y su maquinaria de expresiones regulares y configuración regional. Los enteros se analizan directamente; las cadenas siguen decodificándose como UTF-8 cuando se solicitan y los decimales mantienen conversión numérica explícita. La anticipación guarda un token solo cuando hace falta. El algoritmo de salida no cambia. Se elimina el coste del análisis general; la tabla describe el trabajo algorítmico, con lectura lineal en bytes y un búfer acotado.

Frente a `1294_geometry.java`: tiempo 0.109 s → 0.093 s; memoria 1 600 KB → 452 KB.

Rust factoriza el cuadrado de la cuerda en numerador y denominador enteros tras comprobar la unicidad geométrica. Escala el cuadrado racional para obtener el doble de la distancia en kilómetros, separando cociente y resto antes de multiplicar. Corrige la estimación de raíz con cuadrados enteros y usa su parte entera para redondear, sin formato de coma flotante. La entrada y la respuesta completa usan búferes fijos de bytes. Rust lee y escribe mediante la biblioteca de ejecución de C.

El envío aceptado en Rust 1.75 x64 tarda 0.031 s frente a 0.015 s de la base y usa 56 KB frente a 220 KB.

La auditoría guardada ligada al fuente admite C++ y Python sencillos sin
duplicar archivos rápidos. Go sencillo #11325573 (`0.015 s / 1080 KB`)
supera el límite de memoria de grupo pequeño 1016.60 KB; optimizado
#11328935 (`0.015 s / 804 KB`) cumple por tiempo solo. Java sencillo
#11325554 no cumple el ranking necesario de memoria; optimizado
#11325015 con 452 KB cumple ranking ordinario temporal. Se conservan
estas bases para enseñanza. Ambos Rust tienen Accepted verificado,
pero carecen de referencia rival válida en la auditoría: ranking
numérico desconocido, no fallo demostrado. La admisión general de
todas las bases afirmada antes queda obsoleta.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1294_geometry_parsing_implementation_optimized.go`. Se especializan la conversión de tokens y la salida numérica para los tipos usados, eliminando ramas generales innecesarias y conservando algoritmo y comentarios. Un búfer recargable de 8192 bytes sustituye el almacenamiento de toda la entrada, manteniendo tokens, lecturas parciales y fin de archivo.

Accepted #11328935 (Go 1.14 x64): **0.015 s / 804 KB**. Comparación archivada: `1294_geometry.go` (Go 1.14 x64) — 0.015 s / 1080 KB (#11325573).

## Notas por lenguaje

Los [criterios compartidos](../../RATING_CRITERIA.md) rigen todos los lenguajes:
diez primeros o 15% superior para métricas necesarias, sustituidos por
referencia con 1–10 rivales válidos del compilador exacto. Por debajo
de 1024 KB solo se exige tiempo. Se excluyen rivales menores de `0.015 s`;
solo nuestro tiempo se eleva a ese mínimo al comparar. Las medidas
Accepted originales, incluido C++ `0.001 s`, siguen intactas. No hay corte
ID/fecha, primer puesto separado ni admisión solo por mejorar un 30%.

Los puestos Java optimizado del 18 de noviembre de 2026 (tiempo 5/20,
memoria 2/20) son históricos; su ranking ordinario temporal guardado
aún lo admite. Python cumple el límite `0.093 s` de nueve rivales del
compilador. El asterisco de Rust indica ranking numérico desconocido; una revisión cualitativa vinculada a los fuentes ya aprueba el Rust optimizado frente a la referencia C++.
No demuestra fallo numérico del Rust más lento que usa menos memoria.

El Go rápido actual corrige un comentario: `fastFormatted` solo soporta
`%d` para int/int64 con relleno opcional. Usa el formato fijo
`Distance is %d km.\n`; no hay conversiones de carácter, cadena ni
decimal. El lint estricto también exige extraer
la capacidad128 a `inlineTokenBytes`; al sustituir la constante,
algoritmo y tokens ejecutables coinciden.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1294_geometry.cpp](1294_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.001 s | 112 KB | 11325577 |
| [1294_geometry.go](1294_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 1080 KB | 11325573 |
| [1294_geometry.java](1294_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1600 KB | 11325554 |
| [1294_geometry.py](1294_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 424 KB | 11330228 |
| [1294_geometry.rs](1294_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 220 KB | 11325604 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1294_geometry_optimized.rs](1294_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 56 KB | 11311233 |
| [1294_geometry_optimized.java](1294_geometry_optimized.java) | Java 1.8 | geometry | O(1) | AC | 0.093 s | 452 KB | 11325015 |
| [1294_geometry_parsing_implementation_optimized.go](1294_geometry_parsing_implementation_optimized.go) | Go 1.14 x64 | geometry, parsing, implementation | O(1) | AC | 0.015 s | 804 KB | 11331022 |

\* Accepted; el ranking numérico es desconocido por falta de rivales elegibles. El auditor privado registra una aprobación cualitativa vinculada a los fuentes y a la referencia C++; no se asigna puesto numérico.
