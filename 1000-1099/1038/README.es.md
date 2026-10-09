# 1038. Contar errores de mayúsculas

[Timus 1038](https://acm.timus.ru/problem.aspx?space=1&num=1038) · dificultad 487 · implementation

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

## Notas por lenguaje

- Todos los lenguajes leen la entrada completa (byte a byte o como una
  cadena) y hacen la misma pasada con dos indicadores.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1038_implementation.cpp](1038_implementation.cpp) | G++ 13.2 x64 | implementation | O(L) | AC | 0.015 s | 108 KB |
| [1038_implementation.go](1038_implementation.go) | Go 1.14 x64 | implementation | O(L) | AC | 0.031 s | 1052 KB |
| [1038_implementation.java](1038_implementation.java) | Java 1.8 | implementation | O(L) | AC | 0.109 s | 392 KB |
| [1038_implementation.py](1038_implementation.py) | Python 3.12 x64 | implementation | O(L) | AC | 0.109 s | 364 KB |
| [1038_implementation.rs](1038_implementation.rs) | Rust 1.75 x64 | implementation | O(L) | AC | 0.031 s | 252 KB |
