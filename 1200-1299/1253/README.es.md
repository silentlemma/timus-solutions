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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1253_strings.cpp](1253_strings.cpp) | G++ 13.2 x64 | strings | O(S + L + 10^N) | AC | 0.015 s | 2280 KB |
| [1253_strings.go](1253_strings.go) | Go 1.14 x64 | strings | O(S + L + 10^N) | AC | 0.015 s | 972 KB |
| [1253_strings.java](1253_strings.java) | Java 1.8 | strings | O(S + L + 10^N) | AC | 0.093 s | 6120 KB |
| [1253_strings.py](1253_strings.py) | Python 3.12 x64 | strings | O(N(S + L)) | AC | 0.078 s | 4556 KB |
| [1253_strings.rs](1253_strings.rs) | Rust 1.75 x64 | strings | O(S + L + 10^N) | AC | 0.015 s | 2080 KB |
