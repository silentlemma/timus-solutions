# 1038. Contar errores de mayúsculas

[Timus 1038](https://acm.timus.ru/problem.aspx?space=1&num=1038) · dificultad 489 · implementation

Problema original de Alexander Galperin, del V Campeonato por Equipos de Programación de la Universidad Estatal de los Urales, octubre de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un texto de como mucho 10000 caracteres consta de letras latinas, dígitos,
los signos `. , ; : - ! ?` y espacios en blanco. Una palabra es una
secuencia máxima de letras; cualquier otro carácter, incluido el salto de
línea, la termina. Una oración termina en `.`, `?` o `!`; el comienzo del
texto también inicia una oración. Cuenta los errores de dos tipos:

- la primera letra de una oración es minúscula;
- una letra mayúscula no es la primera letra de su palabra (cada una de
  esas letras es un error aparte).

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

El texto, posiblemente en varias líneas.

## Salida

El número de errores.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
This sentence iz correkt! -It Has,No mista;.Kes et oll.
But there are two BIG mistakes in this one!
and here is one more.
```

Salida:

```
3
```

### Ejemplo 2

Entrada:

```
hello. World? yes!
OK, fine.
```

Salida:

```
3
```

## Solución

Una pasada por los caracteres con dos indicadores:

- `new_sentence`: no ha aparecido ninguna letra desde el comienzo del
  texto o desde el último `.`, `?`, `!`;
- `in_word`: el carácter anterior era una letra.

Para una letra: si es minúscula y `new_sentence` está activo, es un error
del primer tipo; si es mayúscula y `in_word` está activo, es un error del
segundo tipo. Después se desactiva `new_sentence` y se activa `in_word`.
Cualquier otro carácter desactiva `in_word`, y un final de oración activa
`new_sentence`. `O(L)` para un texto de longitud `L`.

Detalles a tener en cuenta:

- la primera letra de una oración no tiene por qué iniciarla: antes puede
  haber dígitos, espacios u otros signos (`2nd place.` tiene un error en
  la `n`);
- un dígito no es una letra, así que `3Rd` es una palabra `Rd` que empieza
  con mayúscula: no hay error;
- toda la entrada es el texto: hay que leerla hasta el final, con los
  saltos de línea.

## Soluciones optimizadas

Go/Python conservan las dos banderas leyendo bloques4096. El estado continúa entre bloques, incluso con palabras cortadas. Go compara rangos ASCII; Python traduce con una tabla256 de clases, no respuestas, y recorre clases enteras. Dígitos y blancos terminan palabras, solo .?! inicia frase. Tiempo O(L), espacio fijo. La admisión depende del juez real, especialmente del arranque Python. Se conservan bases; C++, Java y Rust reutilizan las admitidas.

El envío aceptado en Python 3.12 x64 tarda 0.078 s frente a 0.109 s de la base y usa 496 KB frente a 364 KB.

Las implementaciones base aceptadas [1038_implementation.cpp](1038_implementation.cpp), [1038_implementation.java](1038_implementation.java), [1038_implementation.rs](1038_implementation.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1038_implementation_parsing_optimized.rs`. Los errores se cuentan al consumir bloques nativos, manteniendo solo el estado de frase y palabra entre recargas. No cambian las reglas ASCII y de puntuación; no se guarda todo el texto. La salida directa se especializa a los tipos usados, evitando despacho genérico y cadenas temporales. El texto fijo usa escrituras nativas y los números se convierten exactamente con el signo requerido. Se conservan decisiones matemáticas y versiones simples.

Accepted #11329194 (Rust 1.75 x64): **0.015 s / 60 KB**. Comparación archivada: `1038_implementation.rs` (Rust 1.75 x64) — 0.031 s / 252 KB (#11278496).

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes leen la entrada completa (byte a byte o como una
  cadena) y hacen la misma pasada con dos indicadores.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1038_implementation.cpp](1038_implementation.cpp) | G++ 13.2 x64 | implementation | O(L) | AC | 0.015 s | 108 KB | 11278488 |
| [1038_implementation.go](1038_implementation.go) | Go 1.14 x64 | implementation | O(L) | AC | 0.031 s | 1052 KB | 11278490 |
| [1038_implementation.java](1038_implementation.java) | Java 1.8 | implementation | O(L) | AC | 0.109 s | 392 KB | 11278493 |
| [1038_implementation.py](1038_implementation.py) | Python 3.12 x64 | implementation | O(L) | AC | 0.109 s | 364 KB | 11278492 |
| [1038_implementation.rs](1038_implementation.rs) | Rust 1.75 x64 | implementation | O(L) | AC | 0.031 s | 252 KB | 11278496 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1038_implementation_optimized.go](1038_implementation_optimized.go) | Go 1.14 x64 | implementation | O(L) | AC | 0.015 s | 292 KB | 11315352 |
| [1038_implementation_optimized.py](1038_implementation_optimized.py) | Python 3.12 x64 | implementation | O(L) | AC | 0.078 s | 496 KB | 11315358 |
| [1038_implementation_parsing_optimized.rs](1038_implementation_parsing_optimized.rs) | Rust 1.75 x64 | implementation, parsing | O(text length) time; O(1) state + bounded I/O buffers | AC | 0.015 s | 60 KB | 11329194 |
