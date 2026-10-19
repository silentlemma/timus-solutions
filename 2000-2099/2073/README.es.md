# 2073. Una tabla resumen de registros de concursos

[Timus 2073](https://acm.timus.ru/problem.aspx?space=1&num=2073) · dificultad 242 · implementation

Problema original de Kirill Borozdin, preparado por Kirill Borozdin y Alexey Danilyuk, del Concurso Regional por Equipos de Programación de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan n ≤ 100 registros de concursos: un nombre de 1 a 30 letras,
dígitos y espacios, una fecha DD.MM.YY, el número de problemas p ≤ 13 y
de envíos s ≤ 100, y después s envíos, cada uno una letra de problema y
un veredicto. Imprimir una tabla dibujada con `+`, `-` y `|`: una fila
de encabezado y una fila por concurso con el nombre rellenado hasta 30
caracteres, la fecha (8 caracteres) y 13 marcas, una por letra A … M.
Una marca es `o` si el problema se aceptó al menos una vez, `x` si se
envió pero nunca se aceptó, `.` si estaba en el concurso pero no se
envió, y un espacio si el concurso no tenía ese problema. Los límites
son 1 segundo y 64 MB.

## Entrada

n, y para cada concurso la línea del nombre, la de la fecha, la línea
"p s" y s líneas "letra veredicto". Un veredicto es uno de `Accepted`,
`Wrong Answer`, `Runtime Error`, `Time Limit Exceeded`,
`Memory Limit Exceeded`, `Compilation Error`.

## Salida

La tabla, con el formato del ejemplo, con una línea de borde antes del
encabezado, después de él y después de cada concurso.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
Codeforces Gamma Round 512
29.02.16
5 4
A Accepted
B Accepted
C Accepted
E Accepted
URKOP
17.10.15
12 11
A Accepted
B Wrong Answer
B Time Limit Exceeded
J Accepted
B Accepted
J Time Limit Exceeded
J Accepted
F Accepted
E Runtime Error
H Accepted
E Runtime Error
```

Salida:

```
+------------------------------+--------+-------------+
|Contest name                  |Date    |ABCDEFGHIJKLM|
+------------------------------+--------+-------------+
|Codeforces Gamma Round 512    |29.02.16|ooo.o        |
+------------------------------+--------+-------------+
|URKOP                         |17.10.15|oo..xo.o.o.. |
+------------------------------+--------+-------------+
```

## Solución

Cada concurso empieza con p puntos seguidos de 13 − p espacios. Un envío
pone `o` en su marca si el veredicto es `Accepted`; cualquier otro pone
`x` salvo que la marca ya sea `o`. Después se imprimen las filas con el
nombre rellenado con espacios hasta 30 caracteres. La complejidad temporal es
O(input).

Los nombres pueden tener espacios, así que la entrada se lee línea a
línea, quitando los espacios y retornos de carro finales (un nombre
nunca termina en espacio). Las marcas conservan sus espacios finales: en
el ejemplo la segunda fila termina en `.. ` antes del borde.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2073_implementation.cpp](2073_implementation.cpp) | G++ 13.2 x64 | implementation | O(input) | AC | 0.015 s | 380 KB |
| [2073_implementation.go](2073_implementation.go) | Go 1.14 x64 | implementation | O(input) | AC | 0.015 s | 1832 KB |
| [2073_implementation.java](2073_implementation.java) | Java 1.8 | implementation | O(input) | AC | 0.078 s | 2308 KB |
| [2073_implementation.py](2073_implementation.py) | Python 3.12 x64 | implementation | O(input) | AC | 0.062 s | 1324 KB |
| [2073_implementation.rs](2073_implementation.rs) | Rust 1.75 x64 | implementation | O(input) | AC | 0.015 s | 748 KB |
