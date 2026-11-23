# 1567. Spam por SMS

[Timus 1567](https://acm.timus.ru/problem.aspx?space=1&num=1567) · dificultad 41 · implementation

Problema original de Denis Musin, del XII Campeonato de Programación de la Universidad Estatal de los Urales, 6 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Petya escribe un eslogan de como mucho 1000 caracteres en un teléfono
sin texto predictivo y cobra un rublo por cada pulsación. Un carácter
cuesta tantas pulsaciones como su lugar en su tecla:

| tecla | caracteres |
|-----|------------|
| 1 | a b c |
| 2 | d e f |
| 3 | g h i |
| 4 | j k l |
| 5 | m n o |
| 6 | p q r |
| 7 | s t u |
| 8 | v w x |
| 9 | y z |
| 0 | . , ! |
| # | espacio |

El eslogan tiene palabras en minúsculas, espacios, comas, puntos y
signos de exclamación. Hay que imprimir su precio.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El eslogan en una línea.

## Salida

El número de pulsaciones.

## Ejemplos

### Ejemplo 1

Entrada:

```
pokupaite gvozdi tolko v kompanii gvozdederov i tovarischi!
```

Salida:

```
114
```

## Solución

Una tabla asigna a cada carácter su lugar en su tecla, contando desde 1,
y la respuesta es la suma sobre la línea. La línea se lee entera, ya que
los espacios también cuestan una pulsación. `O(n)`.

Detalles a tener en cuenta:

- la tecla 9 solo tiene y y z, así que z cuesta 2 (prueba 03);
- el espacio es un carácter aparte en la tecla #, una pulsación cada
  uno, también cuando hay dos espacios juntos (prueba 05);
- leer palabra a palabra pierde los espacios.

## Soluciones optimizadas

`1567_implementation_optimized.py`. Genera al inicio un mapa de 256 bytes desde los grupos del teclado: posición implica pulsaciones. Una pasada nativa bytes.translate convierte la línea a pesos y sum los agrega, sin repetidos conteos completos. CR/LF valen cero; conserva pesos de letras, puntuación y espacio. Mapa derivado de reglas, no tabla de respuestas. O(L+256) tiempo/espacio con temporal O(L); vacía antes de salir. Conserva la base por carácter.

Accepted exacto CPython 3.12 #11327006: 0.046 s / 604 KB. Comparación guardada 2026-11-20 con compiladores actuales de la familia: tiempo 1/167, memoria 129/167. Por debajo de 1024 KB, admisión estricta solo por tiempo.

- `1567_implementation_optimized.py`: 0.046 s / 604 KB; base didáctica conservada `1567_implementation.py` (Python 3.12 x64): 0.078 s / 380 KB; cambio de tiempo -41.0%; cambio de memoria +58.9%.

La solución optimizada en C++ convierte las teclas en una tabla de 256
entradas con el número de pulsaciones de cada byte, así que cada
carácter se consulta una sola vez en lugar de buscarlo en todas las
teclas, y lee la línea con `getchar` en lugar de `getline`: 100 KB en
lugar de 376 KB, con el mismo tiempo.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1567_implementation_optimized.rs`. Se conserva la misma recurrencia matemática. Se leen los números desde bytes y se escribe directamente la respuesta numérica de tamaño acotado, evitando el formato numérico general. Se mantiene la implementación más sencilla.

Accepted #11328570 (Rust 1.75 x64): **0.015 s / 216 KB**. Comparación archivada: `1567_implementation.rs` (Rust 1.75 x64) — 0.031 s / 224 KB (#11287750).

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1567_implementation_parsing_optimized.go`. Se especializan la conversión de tokens y la salida numérica para los tipos usados, eliminando ramas generales innecesarias y conservando algoritmo y comentarios.

Accepted #11328868 (Go 1.14 x64): **0.015 s / 804 KB**. Comparación archivada: `1567_implementation.go` (Go 1.14 x64) — 0.015 s / 1048 KB (#11287743).

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1567_implementation.cpp](1567_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 376 KB | 11287740 |
| [1567_implementation.go](1567_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1048 KB | 11287743 |
| [1567_implementation.java](1567_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 424 KB | 11287747 |
| [1567_implementation.py](1567_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 380 KB | 11287745 |
| [1567_implementation.rs](1567_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 224 KB | 11287750 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1567_implementation_optimized.cpp](1567_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 100 KB | 11303623 |
| [1567_implementation_optimized.py](1567_implementation_optimized.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.046 s | 604 KB | 11327006 |
| [1567_implementation_optimized.rs](1567_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 216 KB | 11328570 |
| [1567_implementation_parsing_optimized.go](1567_implementation_parsing_optimized.go) | Go 1.14 x64 | implementation, parsing | O(n) | AC | 0.015 s | 804 KB | 11328868 |
