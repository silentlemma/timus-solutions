# 1187. Tablas cruzadas de una encuesta con porcentajes que suman 100

[Timus 1187](https://acm.timus.ru/problem.aspx?space=1&num=1187) · dificultad 2051 · strings

Problema original de Roman Elizarov, del concurso regional ACM ICPC del noreste de Europa 2001–2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una encuesta tiene hasta 100 preguntas con 2 a 10 respuestas de un
carácter cada una, y hasta 10000 respuestas registradas en total. Para
cada par de preguntas pedido hay que imprimir una tabla cruzada: cuántas
personas dieron cada par de respuestas, con totales por fila y columna, y
bajo cada número su porcentaje del total de la fila y del total de la
columna. Los porcentajes son enteros, cada uno redondeado hacia abajo o
hacia arriba desde el valor exacto, de modo que los porcentajes de una
fila (o columna) sin su total sumen exactamente 100; un porcentaje de un
total cero se imprime como `-`. El formato de la tabla está fijado al
carácter.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El nombre de la encuesta, las preguntas con sus respuestas, `#`, una
línea de códigos de respuesta por persona, `#`, las tablas pedidas, `#`.

## Salida

Para cada tabla: un título, las dos preguntas copiadas, una línea vacía y
una tabla de celdas de 6 caracteres; las tablas se separan con una línea
vacía.

## Evaluación

Se acepta cualquier redondeo en el que cada porcentaje redondee su valor
exacto hacia abajo o hacia arriba, filas y columnas sin totales sumen
100%, los totales muestren `100%` y los totales cero muestren `-`; todo
otro carácter debe coincidir exactamente.

## Ejemplos

### Ejemplo 1

Entrada:

```
New Year Phone Survey for ACM ICPC
Q01 Hello!
 H Hello!
 Y Yes!
 * Uhm...
 . (silence)
 @ (other)
Q02 How are you?
 H Hello!
 Y Yes!
 F Fine!
 Q Who are you?
 @ (other)
BYE Happy New Year!
 Y You too.
 * (censored)
 @ (other)
 . (hang up)
#
.@.
HH@
.@.
YFY
HQ*
H@.
YYY
.H@
HFY
HH@
#
Q01 Q02 Health vs greeting style
Q02 BYE Politeness matrix
#
```

Salida:

```
New Year Phone Survey for ACM ICPC - Health vs greeting style
Q01 Hello!
 H Hello!
 Y Yes!
 * Uhm...
 . (silence)
 @ (other)
Q02 How are you?
 H Hello!
 Y Yes!
 F Fine!
 Q Who are you?
 @ (other)

       Q02:H Q02:Y Q02:F Q02:Q Q02:@ TOTAL
 Q01:H     2     0     1     1     1     5
         40%    0%   20%   20%   20%  100%
         66%    0%   50%  100%   33%   50%
 Q01:Y     0     1     1     0     0     2
          0%   50%   50%    0%    0%  100%
          0%  100%   50%    0%    0%   20%
 Q01:*     0     0     0     0     0     0
           -     -     -     -     -     -
          0%    0%    0%    0%    0%    0%
 Q01:.     1     0     0     0     2     3
         33%    0%    0%    0%   67%  100%
         34%    0%    0%    0%   67%   30%
 Q01:@     0     0     0     0     0     0
           -     -     -     -     -     -
          0%    0%    0%    0%    0%    0%
 TOTAL     3     1     2     1     3    10
         30%   10%   20%   10%   30%  100%
        100%  100%  100%  100%  100%  100%

New Year Phone Survey for ACM ICPC - Politeness matrix
Q02 How are you?
 H Hello!
 Y Yes!
 F Fine!
 Q Who are you?
 @ (other)
BYE Happy New Year!
 Y You too.
 * (censored)
 @ (other)
 . (hang up)

       BYE:Y BYE:* BYE:@ BYE:. TOTAL
 Q02:H     0     0     3     0     3
          0%    0%  100%    0%  100%
          0%    0%  100%    0%   30%
 Q02:Y     1     0     0     0     1
        100%    0%    0%    0%  100%
         33%    0%    0%    0%   10%
 Q02:F     2     0     0     0     2
        100%    0%    0%    0%  100%
         67%    0%    0%    0%   20%
 Q02:Q     0     1     0     0     1
          0%  100%    0%    0%  100%
          0%  100%    0%    0%   10%
 Q02:@     0     0     0     3     3
          0%    0%    0%  100%  100%
          0%    0%    0%  100%   30%
 TOTAL     3     1     3     3    10
         30%   10%   30%   30%  100%
        100%  100%  100%  100%  100%
```

## Solución

Se cuentan los pares en una tabla y se añaden los totales de fila como
una columna más y los de columna como una fila más; la esquina contiene
el número de personas.

Para redondear, sea una fila (o columna) de valores `v` con total `T`. Se
redondea cada porcentaje `100·v/T` hacia abajo. A la suma le falta algún
`d` para 100, y como las fracciones descartadas suman exactamente `d`, al
menos `d` valores tienen fracción. Se suben en uno los `d` valores con
las mayores fracciones. Así se hace en cada fila y columna sin su total,
incluidas la propia fila de totales y la columna de totales, mientras las
celdas de total reciben `100%` (o `-` si su total es cero).
`O(personas + tamaño de la tabla)` por tabla.

El resto es imprimir con cuidado: cada celda alineada a la derecha con
ancho 6, la segunda y tercera línea de cada fila empiezan con 6 espacios,
y las preguntas se copian tal como están en la entrada.

Detalles a tener en cuenta:

- los totales no deben entrar en los vectores que suman 100, o cada suma
  daría 200;
- el ejemplo redondea 2/3 hacia abajo y 1/3 hacia arriba en una misma
  columna, que es solo otra elección válida, así que las salidas difieren
  de él y hace falta un comprobador;
- una fila con total cero sigue teniendo porcentajes por columna, que son
  0% salvo que el total de la columna también sea cero.

Cada salida se validó con el comprobador en 100 encuestas aleatorias, y
el mismo comprobador aceptó allí la salida de una solución escrita
aparte.

## Notas por lenguaje

- Todos los lenguajes redondean igual: una ordenación estable por resto
  sube primero los mayores restos y, entre iguales, la celda anterior, así
  que los cinco imprimen las mismas tablas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1187_strings.cpp](1187_strings.cpp) | G++ 13.2 x64 | strings | O(people + table) per table | AC | 0.015 s | 1008 KB |
| [1187_strings.go](1187_strings.go) | Go 1.14 x64 | strings | O(people + table) per table | AC | 0.031 s | 4656 KB |
| [1187_strings.java](1187_strings.java) | Java 1.8 | strings | O(people + table) per table | AC | 0.265 s | 10196 KB |
| [1187_strings.py](1187_strings.py) | Python 3.12 x64 | strings | O(people + table) per table | AC | 0.125 s | 2564 KB |
| [1187_strings.rs](1187_strings.rs) | Rust 1.75 x64 | strings | O(people + table) per table | AC | 0.031 s | 1296 KB |
