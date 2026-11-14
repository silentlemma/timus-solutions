# 1253. Desplegar plantillas de necrológicas

[Timus 1253](https://acm.timus.ru/problem.aspx?space=1&num=1253) · dificultad 690 · strings

Problema original de Leonid Volkov, del Concurso Abierto por Equipos de la Universidad Estatal de los Urales, 15 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay N plantillas (N ≤ 9) de hasta 1000 caracteres cada una, quizá en
varias líneas. En una plantilla, `*M` es una referencia a la plantilla M
(hasta 10 referencias en cada una). Hay que desplegar la plantilla 1,
sustituyendo cada referencia por el texto de su plantilla una y otra vez
hasta que no quede ninguna. Se imprime el resultado si es finito y tiene
como mucho 10⁶ caracteres, y `#` en otro caso.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N en la primera línea y luego las plantillas, cada una empezando en una
línea nueva y terminando con `#`.

## Salida

El texto desplegado, o `#`.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
She w*7s *7 *2 wom*7n.
*3#
wonderful#
Everyone loved her *5.
We will miss her *5.#
Some text *6#
very much#
Another text *4#
a#
```

Salida:

```
She was a wonderful woman.
Everyone loved her very much.
We will miss her very much.
```

## Solución

Desplegar la plantilla 1 no termina nunca justo cuando desde ella se
alcanza un ciclo de referencias; si no, su longitud queda fijada por
`size(i) = caracteres normales + Σ size(plantillas referidas)`. Una
búsqueda en profundidad desde la plantilla 1 calcula esas longitudes y
marca las plantillas que se están desplegando; volver a encontrar una así
es un ciclo. Las longitudes se cortan justo por encima de 10⁶, porque
ocho niveles de diez referencias llegan a 10⁸ · 1000 caracteres. Si no
hay ciclo y `size(1)` ≤ 10⁶, el texto se escribe con la misma recursión.
Tiempo: `O(S + L + 10^N)`, o `O(N(S + L))` en Python, con tamaño de entrada S
y longitud de salida L.

Detalles a tener en cuenta:

- un ciclo entre plantillas a las que la plantilla 1 no llega es
  inofensivo (prueba 03);
- el límite es inclusivo: exactamente 10⁶ caracteres se imprimen, uno
  más ya es `#` (gen1 y gen2);
- el salto de línea justo después de cada `#` separa las plantillas, pero
  los saltos de línea dentro de una plantilla son parte de su texto, y una
  plantilla puede estar vacía;
- los números de plantilla tienen una cifra, así que `*21` es una
  referencia a la plantilla 2 seguida de la cifra 1 (prueba 08).

## Notas por lenguaje

- Python parte cada plantilla por `*` una sola vez y guarda los
  despliegues ya hechos; los demás lenguajes recorren los caracteres y
  escriben el texto directamente en un búfer.

## Soluciones optimizadas

La versión en C++ calcula primero la longitud de la expansión y luego escribe los tramos literales en el búfer de salida. Omite las referencias cuya expansión es vacía y evita guardar el resultado completo. Con S caracteres de entrada, L de salida y N plantillas, el tiempo es O(S + NL) y el espacio adicional es O(S + N). Las métricas corresponden al envío 11317000.

La versión para Java 1.8 guarda las plantillas en arreglos de bytes, mide la expansión y escribe los tramos en un búfer sin construir el resultado completo. El envío 11317131 tardó 0.062 s y usó 432 KB frente a 0.109 s y 6088 KB de la base.

La versión para Rust 1.75 x64 divide las plantillas en tramos y referencias, mide la expansión y escribe los tramos en un búfer sin construir el resultado completo. El envío 11317130 tardó 0.015 s y usó 212 KB frente a 0.015 s y 2032 KB de la base.

La versión para Python 3.12 x64 calcula primero las longitudes, guarda las expansiones de hasta 4096 bytes y escribe las más largas por partes. El envío 11317128 tardó 0.062 s y usó 660 KB frente a 0.078 s y 4356 KB de la base.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322206 · Go 1.14 x64 №11322207 · Java 1.8 №11322208 · Python 3.12 x64 №11322209 · Rust 1.75 x64 №11322210.

Go calcula las longitudes antes de escribir y emite los fragmentos literales y las referencias en un flujo. Para salidas grandes guarda en caché las expansiones que caben en un búfer fijo. Go 1.14 x64, envío 11322833. Tiempo 0,015 → 0,015 s, memoria 940 → 400 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1253_strings.cpp](1253_strings.cpp) | G++ 13.2 x64 | strings | O(S + L + 10^N) | AC | 0.015 s | 2264 KB | 11322206 |
| [1253_strings.go](1253_strings.go) | Go 1.14 x64 | strings | O(S + L + 10^N) | AC | 0.015 s | 940 KB | 11322207 |
| [1253_strings.java](1253_strings.java) | Java 1.8 | strings | O(S + L + 10^N) | AC | 0.109 s | 6088 KB | 11322208 |
| [1253_strings.py](1253_strings.py) | Python 3.12 x64 | strings | O(N(S + L)) | AC | 0.078 s | 4356 KB | 11322209 |
| [1253_strings.rs](1253_strings.rs) | Rust 1.75 x64 | strings | O(S + L + 10^N) | AC | 0.015 s | 2032 KB | 11322210 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1253_strings_optimized.cpp](1253_strings_optimized.cpp) | G++ 13.2 x64 | strings | O(S + NL) | AC | 0.015 s | 172 KB | 11317000 |
| [1253_strings_optimized.py](1253_strings_optimized.py) | Python 3.12 x64 | strings | O(S + NL) | AC | 0.062 s | 660 KB | 11317128 |
| [1253_strings_optimized.rs](1253_strings_optimized.rs) | Rust 1.75 x64 | strings | O(S + NL) | AC | 0.015 s | 212 KB | 11317130 |
| [1253_strings_optimized.java](1253_strings_optimized.java) | Java 1.8 | strings | O(S + NL) | AC | 0.062 s | 432 KB | 11317131 |
| [1253_strings_optimized.go](1253_strings_optimized.go) \* | Go 1.14 x64 | strings | O(S + L + 10^N) | AC | 0.015 s | 400 KB | 11322833 |

\* Las versiones marcadas aún pueden mejorar su clasificación.
