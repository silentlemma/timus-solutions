# 1601. AntiMAYÚSCULAS

[Timus 1601](https://acm.timus.ru/problem.aspx?space=1&num=1601) · dificultad 92 · implementation

Problema original de Denis Musin, del IX Campeonato Abierto Individual de la Universidad Estatal de los Urales, 1 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Angela escribe los mensajes del chat en mayúsculas. Hay que corregir un
mensaje de hasta 10000 caracteres: las oraciones terminan en `.`, `!` o
`?`, la primera letra de cada oración sigue en mayúscula y todas las
demás pasan a minúscula. Los espacios, los saltos de línea y los signos
`,`, `-`, `:` quedan como están.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

El mensaje.

## Salida

El mensaje corregido.

## Ejemplos

### Ejemplo 1

Entrada:

```
HI THERE!
HOW DID YOU KNOW I AM A BLONDE?
```

Salida:

```
Hi there!
How did you know i am a blonde?
```

## Solución

Se recorre el mensaje una vez recordando si la siguiente letra abre una
oración. Así ocurre al principio y tras cada `.`, `!` o `?`; la primera
letra después de eso conserva la mayúscula, y cualquier otra letra pasa a
minúscula. Todo lo demás se copia sin cambios, saltos de línea
incluidos, así que el mensaje se procesa como bytes en bruto: `O(n)`. Los
resultados se compararon byte a byte con una implementación
independiente en mensajes generados.

Detalles a tener en cuenta:

- una oración puede seguir en varias líneas, así que un salto de línea
  no empieza una oración nueva (prueba 04);
- las comas, los guiones y los dos puntos no terminan una oración
  (prueba 02);
- un signo puede ir justo antes de una letra sin espacio (prueba 03), y
  una serie como `?!` termina una oración, no dos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1601_implementation.cpp](1601_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 88 KB |
| [1601_implementation.go](1601_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 936 KB |
| [1601_implementation.java](1601_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 432 KB |
| [1601_implementation.py](1601_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 436 KB |
| [1601_implementation.rs](1601_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 236 KB |
