# 1201. Un calendario mensual con una fecha entre corchetes

[Timus 1201](https://acm.timus.ru/problem.aspx?space=1&num=1201) · dificultad 364 · implementation

Problema original de Alexander Klepinin, del Concurso por Equipos de la Universidad Estatal de los Urales, marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dada una fecha entre los años 1600 y 2400, hay que imprimir el
calendario de su mes: siete filas, de lunes a domingo, una columna por
semana y la fecha dada entre corchetes. Los años bisiestos siguen la
regla gregoriana.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El día, el mes y el año.

## Salida

Exactamente siete líneas con el formato de los ejemplos. Cada fila
empieza con `mon` … `sun`; cada semana ocupa cinco caracteres, la última
cuatro, y el día va alineado a la derecha en dos caracteres tras dos
espacios. En la fecha dada, el espacio anterior y el posterior se
sustituyen por `[` y `]`.

## Ejemplos

### Ejemplo 1

Entrada:

```
16 3 2002
```

Salida:

```
mon        4   11   18   25
tue        5   12   19   26
wed        6   13   20   27
thu        7   14   21   28
fri   1    8   15   22   29
sat   2    9  [16]  23   30
sun   3   10   17   24   31
```

### Ejemplo 2

Entrada:

```
1 3 2002
```

Salida:

```
mon        4   11   18   25
tue        5   12   19   26
wed        6   13   20   27
thu        7   14   21   28
fri [ 1]   8   15   22   29
sat   2    9   16   23   30
sun   3   10   17   24   31
```

## Solución

Se cuentan los días desde el 1 de enero del año 1, lunes en el
calendario gregoriano, hasta el primer día del mes: `365·(y−1)` más los
días bisiestos `⌊(y−1)/4⌋ − ⌊(y−1)/100⌋ + ⌊(y−1)/400⌋` más la duración
de los meses anteriores del año. El resto módulo 7 es la fila del primer
día, y el mes necesita `⌈(first + days)/7⌉` columnas. Después cada
casilla es simplemente el día `7·column + row − first + 1` cuando cae
dentro del mes. `O(1)`.

Detalles a tener en cuenta:

- 1900 no es bisiesto pero 2000 sí;
- un mes puede necesitar cuatro, cinco o seis columnas;
- los anchos son fijos incluso donde la casilla está vacía, así que las
  filas que terminan antes de la última semana conservan sus espacios
  finales; las salidas esperadas de estas pruebas se comparan carácter a
  carácter;
- una fecha de una cifra entre corchetes conserva su relleno: `[ 1]`.

Los calendarios se compararon con una solución escrita aparte en 605
fechas, entre ellas los extremos del rango y varios febreros.

## Notas por lenguaje

- Todos los lenguajes construyen cada fila casilla a casilla con los
  mismos anchos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1201_implementation.cpp](1201_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.031 s | 196 KB |
| [1201_implementation.go](1201_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1124 KB |
| [1201_implementation.java](1201_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.125 s | 1752 KB |
| [1201_implementation.py](1201_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 560 KB |
| [1201_implementation.rs](1201_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 252 KB |
