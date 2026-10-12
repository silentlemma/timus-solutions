# 1347. Blog

[Timus 1347](https://acm.timus.ru/problem.aspx?space=1&num=1347) · dificultad 1362 · parsing

Problema original de Den Raskovalov, del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ≤ 100 blogueros escriben cada uno un blog y marcan a quienes leen con
`<friend>nombre</friend>`. Para cada bloguero, en el orden de la
entrada, hay que imprimir tres listas ordenadas alfabéticamente: las
personas que menciona, los blogueros que mencionan a ese bloguero y las personas
que están en ambas. Nadie es amigo de sí mismo. Los nombres distinguen
mayúsculas y minúsculas y constan de letras latinas y `_`.

Límite de tiempo: 0,4 segundos. Límite de memoria: 64 MB.

## Entrada

N y luego, para cada blog, el nombre de su autor en una línea y el blog,
que empieza con `<blog>` y acaba con `</blog>`. Un blog tiene hasta
1000 líneas de hasta 255 caracteres, y la última línea de la entrada
puede no tener salto de línea.

## Salida

Para cada bloguero, el nombre y tres líneas que empiezan por `1: `,
`2: ` y `3: ` con los nombres separados por coma y espacio, y una línea
vacía entre blogueros.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
xoposhiy
<blog>
Tomorrow I found <friend>_denplusplus_</friend> to
 be <b>smartest</b> blogger in the net.
Also I received interesting link from
 <friend>strange_human</friend>
</blog>
_denplusplus_
<blog>
Some shit about my work.
</blog>
strange_human
<blog>
<friend>xoposhiy</friend>
<friend>_denplusplus_</friend>
</blog>
```

Salida:

```
xoposhiy
1: _denplusplus_, strange_human
2: strange_human
3: strange_human

_denplusplus_
1: 
2: strange_human, xoposhiy
3: 

strange_human
1: _denplusplus_, xoposhiy
2: xoposhiy
3: xoposhiy
```

## Solución

Cada blog se lee desde la línea del nombre hasta la primera línea con
`</blog>`, que puede ser la misma que la de `<blog>`. Cada `<friend>`
hasta el siguiente `</friend>` da un nombre: lo que hay en medio, sin
otras etiquetas y sin espacios en los bordes. El conjunto de esos
nombres sin el propio bloguero es la lista 1. La lista 2 de un bloguero
es el conjunto de los otros blogueros en cuya lista 1 está su nombre, y
la lista 3 es la intersección. Todas las listas se ordenan por códigos
de carácter, así que `_` va tras las mayúsculas y antes de las
minúsculas. Aquí L es la longitud de la entrada, S la longitud máxima
de un nombre y K el número de nombres distintos (al menos 2); las cotas
para conjuntos hash son esperadas.

Detalles a tener en cuenta:

- las menciones de uno mismo no cuentan (prueba 02);
- una etiqueta de amigo puede tener espacios u otras etiquetas alrededor
  del nombre (prueba 03);
- un blog entero puede ocupar una sola línea (prueba 04);
- las personas sin blog pueden ser amigas pero no mencionan a nadie
  (prueba 05);
- `Bob` y `bob` son personas distintas, y un amigo mencionado muchas
  veces aparece una sola vez (prueba 06);
- una lista vacía se imprime como `1: ` con el espacio.

## Notas por lenguaje

- Las cinco soluciones leen toda la entrada de una vez y buscan las
  etiquetas como texto normal.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1347_parsing.cpp](1347_parsing.cpp) | G++ 13.2 x64 | parsing | O((L + N K S) log K) | AC | 0.015 s | 4996 KB |
| [1347_parsing.go](1347_parsing.go) | Go 1.14 x64 | parsing | O((L + N K S) log K) | AC | 0.031 s | 9156 KB |
| [1347_parsing.java](1347_parsing.java) | Java 1.8 | parsing | O((L + N K S) log K) | AC | 0.140 s | 16724 KB |
| [1347_parsing.py](1347_parsing.py) | Python 3.12 x64 | parsing | O((L + N K S) log K) | AC | 0.140 s | 5328 KB |
| [1347_parsing.rs](1347_parsing.rs) | Rust 1.75 x64 | parsing | O((L + N K S) log K) | AC | 0.015 s | 4076 KB |
