# 1612. El foro del tranvía

[Timus 1612](https://acm.timus.ru/problem.aspx?space=1&num=1612) · dificultad 152 · strings

Problema original de Alexander Ipatov, preparado por Denis Musin, del XII Campeonato de los Urales de Programación Competitiva, 29 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un mensaje del foro de como mucho 10000 caracteres, con letras latinas
minúsculas, espacios, saltos de línea y los signos `. , - : ! ?`, lo
escribe un conductor de tranvía si la palabra `tram` aparece en él más
veces que `trolleybus`, uno de trolebús si es al revés, y uno de autobús
en otro caso. Las palabras son tramos de letras. ¿Quién lo escribió?

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

El mensaje.

## Salida

`Tram driver`, `Trolleybus driver` o `Bus driver`.

## Ejemplos

### Ejemplo 1

Entrada:

```
of course, tram is the best transport
in the world!
```

Salida:

```
Tram driver
```

### Ejemplo 2

Entrada:

```
yes, yekaterinburg trams are the
best trams in the world, but
i like my trolleybus too.
```

Salida:

```
Trolleybus driver
```

### Ejemplo 3

Entrada:

```
read forum.tr.ru every day!
you can learn much about tram 
drivers and trolleybus drivers.
```

Salida:

```
Bus driver
```

## Solución

Se parte el mensaje en palabras en cada carácter que no es letra, se
cuentan las palabras iguales a `tram` y a `trolleybus` y se comparan las
dos cuentas: `O(n)`. Las respuestas se compararon con una implementación
independiente en mensajes generados.

Detalles a tener en cuenta:

- solo cuentan las palabras enteras: `trams`, `tramway` o el `tr` de
  `forum.tr.ru` no son la palabra `tram` (ejemplos 2 y 3);
- los signos también separan palabras, así que `tram-tram` tiene dos
  tranvías y `tram,trolleybus` uno de cada (pruebas 06 y 07);
- con cuentas iguales, cero incluido, es un conductor de autobús.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1612_strings.cpp](1612_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 156 KB |
| [1612_strings.go](1612_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1124 KB |
| [1612_strings.java](1612_strings.java) | Java 1.8 | strings | O(n) | AC | 0.109 s | 840 KB |
| [1612_strings.py](1612_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.093 s | 444 KB |
| [1612_strings.rs](1612_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.015 s | 232 KB |
