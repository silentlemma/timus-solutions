# 1050. Convertir comillas rectas en comillas de TeX

[Timus 1050](https://acm.timus.ru/problem.aspx?space=1&num=1050) · dificultad 1442 · parsing

Problema original de Alexander Galperin, del concurso universitario de programación de la Universidad Estatal de los Urales, 25 de marzo de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un fuente de TeX de como mucho 250 líneas (de como mucho 80 caracteres)
termina con el comando `\endinput`. Cópialo exactamente, salvo las
comillas dobles `"` (código 34):

- dentro de un párrafo, las comillas se sustituyen por turnos por
  ``` `` ``` (apertura) y `''` (cierre);
- una comilla de apertura sin cierre en el mismo párrafo se borra;
- `\"` es el comando de diéresis (como en `\"e`) y se queda como está.

Un párrafo termina en una línea vacía (o varias) y en el comando `\par`.
Los comandos empiezan con `\` y terminan en el primer carácter que no es
una letra latina. El texto puede contener bytes mayores que 127, y la
última línea puede no tener salto de línea.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El texto, terminado en `\endinput`.

## Salida

El texto convertido.

## Evaluación

La salida debe ser igual al texto esperado; solo se ignoran los espacios
en blanco del final. Las pruebas guardan el texto en UTF-8 y se lo dan a
las soluciones en cp1251, una codificación de un byte con letras
cirílicas.

## Ejemplos

### Ejemplo 1

Entrada:

```
There is no "q in this sentence. \par 
"Talk child," said the unicorn. 

She s\"aid, "\thinspace `Enough!', he said." 
\endinput
```

Salida:

```
There is no q in this sentence. \par 
``Talk child,'' said the unicorn. 

She s\"aid, ``\thinspace `Enough!', he said.'' 
\endinput
```

### Ejemplo 2

Entrada:

```
Он сказал: "Привет!" и ушёл, "не закрыв цитату.
   
"Новый абзац" с умлаутом \"o.
\endinput
```

Salida:

```
Он сказал: ``Привет!'' и ушёл, не закрыв цитату.
   
``Новый абзац'' с умлаутом \"o.
\endinput
```

## Solución

Una pasada por los bytes, recordando las posiciones de las comillas del
párrafo actual:

- `\` seguido de `"` es la diéresis: se saltan ambos. Si no, se leen las
  letras latinas tras `\`; si son exactamente `par`, el párrafo termina
  (`\parbox` no lo termina);
- `"` se añade a la lista del párrafo;
- en un salto de línea se mira la línea siguiente: si solo tiene
  espacios, tabuladores y otros espacios en blanco y termina con su propio
  salto de línea, el párrafo termina.

Cuando termina un párrafo, una última comilla impar se marca para
borrarla y las demás alternan entre apertura y cierre. Tras el último
párrafo, se copian los bytes sustituyendo las comillas marcadas. `O(L)`
para un texto de `L` bytes.

Detalles a tener en cuenta:

- el destino de una comilla solo se sabe al final de su párrafo, así que
  la salida se escribe después de la pasada;
- una línea «vacía» puede contener espacios o tabuladores;
- `\par` debe ser un comando completo: `\parbox` y `\partial` no terminan
  el párrafo, mientras que `\par"x` sí;
- el texto son bytes, no UTF-8: las letras mayores que 127 pasan sin
  cambios, y un salto de línea final ausente debe seguir ausente;
- las pruebas evitan una barra invertida doble `\\` justo antes de `"` o
  de letras, donde TeX y una pasada sencilla pueden no coincidir.

## Notas por lenguaje

- Todos los lenguajes leen la entrada completa como bytes y escriben
  bytes: Java no usa un `Reader` con juego de caracteres, Python usa
  `sys.stdin.buffer`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1050_parsing.cpp](1050_parsing.cpp) | G++ 13.2 x64 | parsing | O(L) | AC | 0.015 s | 260 KB |
| [1050_parsing.go](1050_parsing.go) | Go 1.14 x64 | parsing | O(L) | AC | 0.015 s | 1888 KB |
| [1050_parsing.java](1050_parsing.java) | Java 1.8 | parsing | O(L) | AC | 0.093 s | 1348 KB |
| [1050_parsing.py](1050_parsing.py) | Python 3.12 x64 | parsing | O(L) | AC | 0.078 s | 2356 KB |
| [1050_parsing.rs](1050_parsing.rs) | Rust 1.75 x64 | parsing | O(L) | AC | 0.015 s | 536 KB |
