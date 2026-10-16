# 1759. Longevos

[Timus 1759](https://acm.timus.ru/problem.aspx?space=1&num=1759) · dificultad 462 · implementation

Problema original de Alexander Ipatov, del XI Concurso Individual Abierto de la Universidad Estatal de los Urales, 13 de marzo de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una lista de n personas da para cada una la fecha de nacimiento, la
fecha en que pasó a ser la persona viva más anciana y la fecha de
muerte; la segunda fecha de cada persona es la fecha de muerte de la
anterior. Hallar quién vivió más días, contando el día de nacimiento y
el de muerte. En caso de empate, nombrar a quien murió antes.

## Entrada

n (1 ≤ n ≤ 100) y luego n líneas de tres fechas `dd.mm.yyyy` entre
01.01.1800 y 31.12.2009 del calendario gregoriano, cada una posterior a
la anterior. Todos los nacimientos son distintos, y también todas las
muertes.

## Salida

El número de esa persona en la lista.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
10.10.1873 27.12.1987 11.01.1988
18.11.1874 11.01.1988 14.02.1991
21.02.1875 14.02.1991 04.08.1997
29.08.1880 04.08.1997 16.04.1998
```

Salida:

```
3
```

## Solución

Cada fecha se convierte en un número de día, y una vida dura
muerte − nacimiento + 1 días. El número de día cuenta el año desde
marzo, para que el 29 de febrero, cuando lo hay, sea el último día del
año: así los años anteriores al año y suman 365·y días más
⌊y/4⌋ − ⌊y/100⌋ + ⌊y/400⌋ días bisiestos, y los días antes del mes m
(marzo es 0) son ⌊(153·m + 2) / 5⌋, ya que de marzo a julio y de agosto
a diciembre hay 153 días con el mismo patrón. La lista va en orden de
muerte, así que la respuesta es la primera persona que alcanza la vida
más larga. `O(n)`.

En el ejemplo las vidas duran 41731, 42457, 44725 y 42964 días, así que
la tercera persona, nacida en 1875 y muerta en 1997, vivió más.

Trampas:

- 1800 y 1900 no son bisiestos, y 2000 sí;
- cuentan el día de nacimiento y el de muerte, lo que no cambia al
  ganador pero sí las longitudes;
- un empate lo gana la muerte más temprana, que es la línea anterior.

Las respuestas coinciden con un recuento basado en una biblioteca
estándar de fechas y con una implementación aceptada independiente en
160 listas aleatorias, con empates y fechas cerca del final de febrero
de 1800, 1900 y 2000.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1759_implementation.cpp](1759_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB |
| [1759_implementation.go](1759_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.031 s | 1128 KB |
| [1759_implementation.java](1759_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 1804 KB |
| [1759_implementation.py](1759_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 520 KB |
| [1759_implementation.rs](1759_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 232 KB |
