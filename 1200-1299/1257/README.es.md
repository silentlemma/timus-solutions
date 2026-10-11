# 1257. Guiones de división

[Timus 1257](https://acm.timus.ru/problem.aspx?space=1&num=1257) · dificultad 1722 · implementation

Problema original de Den Raskovalov, de la Competición Abierta por Equipos de Programación para Escolares de la Región de Sverdlovsk, 11 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Maquetar un texto en una página de 40 caracteres de ancho con reglas de
división de palabras. Una palabra es una secuencia de letras latinas;
cualquier otro carácter separa palabras. Una regla `s1-s2` (hasta 100
reglas, |s1| + |s2| ≤ 40) indica que una palabra que termina en s1s2,
sin distinguir mayúsculas, puede cortarse antes de s2: el principio
queda en la línea actual seguido de `-` y s2 empieza la siguiente línea.
Ninguna línea de salida puede superar 40 caracteres, contando el `-`.
Si una palabra no cabe, se elige la regla que quepa y pase menos letras;
si no cabe ninguna, la palabra entera pasa a la línea siguiente. Se conservan
los espacios, la puntuación y los saltos de línea que ya tiene el texto.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, luego N reglas, una por línea, y después el texto: como mucho 450
líneas de hasta 250 caracteres, con palabras de hasta 40 letras.

## Salida

El texto maquetado.

## Ejemplos

### Ejemplo 1

Entrada:

```
12
un-usual
for-ced
re-al
sum-mer
N-ED
home-work
sec-ret
ho-lidays
Wi-zard
th-Er
L-so
Holi-days
Harry Potter was a highly unusual boy in many ways. 
For one thing, he hated the summer holidays more than any 
other time of year. For another, he really 
 wanted to do his homework but was forced to do it in 
secret, in the dead of night. And he also happened 
to be a wizard.
```

Salida:

```
Harry Potter was a highly unusual boy in
 many ways. 
For one thing, he hated the summer holi-
days more than any 
other time of year. For another, he 
really 
 wanted to do his homework but was for-
ced to do it in 
secret, in the dead of night. And he al-
so happened 
to be a wizard.
```

## Solución

Se recorre el texto llevando la columna actual:

- un salto de línea se copia y pone la columna a cero;
- cualquier otro separador se copia, pero si la línea ya tiene 40
  caracteres, antes se escribe un salto de línea;
- una palabra que cabe se copia;
- si no, entre las reglas cuyo s1s2 termina la palabra (comparando en
  minúsculas) y cuyo principio con el `-` aún cabe, se toma la de s2
  más corto: se escribe el principio, `-`, un salto de línea y s2; si no
  hay tal regla, un salto de línea y la palabra.

Ninguna palabra pasa de 40 letras, así que siempre cabe en una línea
nueva. `O(N · 40 + L · (1 + N · 40))` para un texto de L caracteres.

Detalles a tener en cuenta:

- los separadores también pasan de línea: un espacio tras una línea
  llena empieza la siguiente (en el ejemplo, ` many ways.`), y lo mismo
  los puntos (prueba 02);
- un salto de línea de la entrada justo después de una línea llena es el
  único corte en ese lugar, no un segundo (pruebas 03, 10);
- el texto puede acabar sin salto de línea (prueba 04);
- la regla debe coincidir con el final de la palabra, no con el primer
  lugar donde aparecen sus letras (prueba 05);
- las reglas no distinguen mayúsculas (prueba 06), y la parte pasada más
  corta solo se busca entre las reglas cuyo principio cabe (pruebas 07,
  12);
- una regla que pasa una sola letra nunca se aplica: el principio con el
  `-` mide lo mismo que la palabra entera, que habría cabido.

Las soluciones se compararon con una implementación independiente en
450 textos aleatorios.

## Notas por lenguaje

- Todos los lenguajes leen la entrada como bytes, quitan `\r` y recorren
  el texto una vez.
- Java decodifica e imprime los bytes como ISO-8859-1, para que cada
  byte siga siendo un carácter.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1257_implementation.cpp](1257_implementation.cpp) | G++ 13.2 x64 | implementation | O(N · 40 + L · (1 + N · 40)) | AC | 0.046 s | 768 KB |
| [1257_implementation.go](1257_implementation.go) | Go 1.14 x64 | implementation | O(N · 40 + L · (1 + N · 40)) | AC | 0.031 s | 1876 KB |
| [1257_implementation.java](1257_implementation.java) | Java 1.8 | implementation | O(N · 40 + L · (1 + N · 40)) | AC | 0.156 s | 5152 KB |
| [1257_implementation.py](1257_implementation.py) | Python 3.12 x64 | implementation | O(N · 40 + L · (1 + N · 40)) | AC | 0.140 s | 1740 KB |
| [1257_implementation.rs](1257_implementation.rs) | Rust 1.75 x64 | implementation | O(N · 40 + L · (1 + N · 40)) | AC | 0.015 s | 600 KB |
