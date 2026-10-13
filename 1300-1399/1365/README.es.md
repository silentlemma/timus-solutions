# 1365. Probando la calculadora

[Timus 1365](https://acm.timus.ru/problem.aspx?space=1&num=1365) · dificultad 4356 · parsing

Problema original de Alexander Klepinin, del Noveno Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 19–24 de abril de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada línea de la entrada es una expresión con los caracteres
`0123456789+*/();`, de como mucho 50, y hay que imprimir su valor
exactamente como lo hace un viejo módulo de cálculo del jurado. Solo se
sabe esto: las operaciones `+`, `*` y `/` (división entera) se escriben en
forma prefija con cualquier número de argumentos, `+3;6;10` da 19; los
términos sin operación se pegan, `3;6;9` da 369; se admiten paréntesis,
`(+3;6)(*2;3)` da 96; y una parte de una expresión se evalúa igual esté
donde esté. El resto había que descubrirlo ejecutando el propio módulo.
Todos los valores intermedios y los resultados están entre 0 y 10⁹.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

Expresiones, una por línea.

## Salida

Para la línea i, `Expression i evaluates to: v` con su valor v.

## Ejemplos

### Ejemplo 1

Entrada:

```
(+3;6)(*2;3)
(+3;6)(/3;2)
```

Salida:

```
Expression 1 evaluates to: 96
Expression 2 evaluates to: 91
```

## Solución

El módulo era un applet de Java que los navegadores actuales ya no
ejecutan, así que estas son las reglas que sigue una solución aceptada:

- un término es un número, un signo de operación con sus argumentos o una
  expresión entera entre paréntesis (puede faltar el `)`);
- los términos seguidos se pegan: sus escrituras decimales se unen y se
  vuelven a leer como número, así que los ceros a la izquierda desaparecen;
- los argumentos de una operación son tramos pegados de términos
  separados por `;`; `/` divide de izquierda a derecha, y dividir entre
  cero da 0;
- fuera de una operación, al principio de la línea o dentro de
  paréntesis, `;` pega el valor de todo lo que sigue a lo anterior:
  `1;+2;3` es 1 pegado a 5, es decir, 15;
- un primer término ausente aporta 1 al tramo pegado;
- `)` cierra el tramo; solo si sobra se ignora el resto de la línea.

Un descenso recursivo de tres funciones sigue estas reglas: un término,
una operación que combina sus argumentos y un tramo pegado, al que se le
dice si está dentro de una operación. Cada línea se lee una vez: `O(n)` en
la longitud de la entrada. Las reglas se comprobaron contra un
evaluador independiente en 10 000 expresiones aleatorias.

Detalles a tener en cuenta:

- la segunda línea del ejemplo: `/3;2` es 1, y pegado tras el 9 da 91;
- `;` fuera de una operación pega todo el resto, no solo el siguiente
  término (prueba 05);
- una línea vacía o `()` da 1, y un `;` solo da 11: falta un término a
  cada lado (prueba 03);
- `(0)(5)` es 5 y `0;0` es 0: la cadena pegada se lee como número
  (prueba 06);
- `/7;0` da 0 (prueba 04).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1365_parsing.cpp](1365_parsing.cpp) | G++ 13.2 x64 | parsing | O(n) | AC | 0.015 s | 412 KB |
| [1365_parsing.go](1365_parsing.go) | Go 1.14 x64 | parsing | O(n) | AC | 0.015 s | 1104 KB |
| [1365_parsing.java](1365_parsing.java) | Java 1.8 | parsing | O(n) | AC | 0.093 s | 676 KB |
| [1365_parsing.py](1365_parsing.py) | Python 3.12 x64 | parsing | O(n) | AC | 0.078 s | 692 KB |
| [1365_parsing.rs](1365_parsing.rs) | Rust 1.75 x64 | parsing | O(n) | AC | 0.031 s | 232 KB |
