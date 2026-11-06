# 1201. Un calendario mensual con una fecha entre corchetes

[Timus 1201](https://acm.timus.ru/problem.aspx?space=1&num=1201) · dificultad 365 · implementation

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
cuatro, salvo la casilla con la fecha entre corchetes. El día va alineado
a la derecha en dos caracteres tras dos espacios. En la fecha dada,
el espacio anterior y el posterior se
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
dentro del mes. Se imprimen casillas de cinco caracteres, omitiendo el
espacio final de la última columna, pero conservando el corchete de
cierre de la fecha seleccionada. `O(1)`.

Detalles a tener en cuenta:

- 1900 no es bisiesto pero 2000 sí;
- un mes puede necesitar cuatro, cinco o seis columnas;
- los anchos son fijos incluso donde la casilla está vacía, así que las
  filas que terminan antes de la última semana conservan sus espacios
  finales; las salidas esperadas de estas pruebas se comparan carácter a
  carácter después de aplicar `rstrip()` al final de toda la salida,
  no de cada línea;
- una fecha entre corchetes en la última columna sigue ocupando cinco
  caracteres, incluido el `]` de cierre (pruebas 04 y 08);
- una fecha de una cifra entre corchetes conserva su relleno: `[ 1]`.

Los calendarios se compararon con una solución escrita aparte en 605
fechas, entre ellas los extremos del rango y varios febreros.

## Soluciones optimizadas

C++ y Go calculan el primer día de la semana con la fórmula gregoriana de años bisiestos y generan las celdas directamente en búferes de bytes de tamaño fijo. Conservan los espacios y los corchetes del día elegido. C++ escribe una fila por vez. Go prepara las siete filas en un búfer y lee la fecha en un búfer fijo de bytes. Usa los descriptores estándar directamente y completa las escrituras parciales.

Las implementaciones base aceptadas [1201_implementation.java](1201_implementation.java), [1201_implementation.py](1201_implementation.py), [1201_implementation.rs](1201_implementation.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes construyen cada fila casilla a casilla con los
  mismos anchos.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1201_implementation.cpp](1201_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.031 s | 196 KB | 11283545 |
| [1201_implementation.go](1201_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1124 KB | 11283546 |
| [1201_implementation.java](1201_implementation.java) \* | Java 1.8 | implementation | O(1) | AC | 0.125 s | 1752 KB | 11283552 |
| [1201_implementation.py](1201_implementation.py) \* | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 560 KB | 11283551 |
| [1201_implementation.rs](1201_implementation.rs) \* | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 252 KB | 11283556 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1201_implementation_optimized.cpp](1201_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 104 KB | 11311038 |
| [1201_implementation_optimized.go](1201_implementation_optimized.go) \* | Go 1.14 x64 | implementation | O(1) | AC | 0.015 s | 284 KB | 11311222 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
