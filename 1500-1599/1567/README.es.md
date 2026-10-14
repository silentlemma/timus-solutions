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

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1567_implementation.cpp](1567_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 376 KB |
| [1567_implementation.go](1567_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1048 KB |
| [1567_implementation.java](1567_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 424 KB |
| [1567_implementation.py](1567_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 380 KB |
| [1567_implementation.rs](1567_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 224 KB |
