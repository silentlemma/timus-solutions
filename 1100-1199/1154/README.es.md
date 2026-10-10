# 1154. El mejor momento del día para una batalla de magos elementales

[Timus 1154](https://acm.timus.ru/problem.aspx?space=1&num=1154) · dificultad 885 · math

Problema original de Evgeny Bryzgalov, del campeonato de programación por equipos de los Urales, Perm, abril de 2001, ronda en inglés.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Magos de cuatro elementos, Aire, Tierra, Fuego y Agua, luchan por la Luz
y por la Oscuridad. Cada elemento tiene durante el día un momento de
fuerza y uno de debilidad, con su poder en cada uno; entre ellos el poder
cambia linealmente, y el día se repite. La fuerza de un bando es la suma
de los poderes de sus magos. Elige el segundo del día, de `00:00:00` a
`23:59:59`, en que la ventaja de la Luz sobre la Oscuridad es mayor, el
más temprano si hay varios iguales, e imprímelo con la ventaja con dos
decimales. Si la Luz no puede ser más fuerte en ningún momento, imprime
`We can't win!`.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Cuatro líneas `código hora-fuerza poder-fuerza hora-debilidad
poder-debilidad`, y luego los magos de la Luz y de la Oscuridad como
cadenas de las letras `A`, `E`, `F`, `W`, con 1 a 1000 magos cada una.

## Salida

La hora y la ventaja, o `We can't win!`.

## Ejemplos

### Ejemplo 1

Entrada:

```
A 10:00:00 130 18:00:00 40
E 14:00:00 150 21:30:00 25
F 06:00:00 105 18:00:00 70
W 23:00:00 140 02:00:00 20
A
WWW
```

Salida:

```
02:00:00
25.00
```

### Ejemplo 2

Entrada:

```
A 10:00:00 130 18:00:00 40
E 14:00:00 150 21:30:00 25
F 06:00:00 105 18:00:00 70
W 23:00:00 140 02:00:00 20
A
WWWF
```

Salida:

```
We can't win!
```

## Solución

Solo importa la diferencia: para cada elemento sea `c` el número de sus
magos en el bando de la Luz menos los del bando de la Oscuridad. La
ventaja en el instante `t` es `Σ c·power(t)`. Cada poder baja linealmente
del momento de fuerza al de debilidad, avanzando por el día, y vuelve a
subir linealmente; así que la ventaja es lineal a trozos, con quiebros
solo en los ocho momentos. Un trozo lineal alcanza su máximo en un
extremo, y el día mismo está cortado a medianoche, así que el mejor
segundo es uno de los ocho momentos, `00:00:00` o `23:59:59`. Se evalúa la
ventaja en ellos, se toma el mayor valor y, entre iguales, la hora más
temprana. La Luz gana solo si ese valor es positivo.

Detalles a tener en cuenta:

- el tiempo de la fuerza a la debilidad pasa por medianoche cuando la
  debilidad llega antes en el día, así que las diferencias se toman
  módulo 86400;
- si la ventaja se mantiene en su máximo durante un intervalo, su primer
  segundo es un momento o la medianoche, que están entre las candidatas;
- una ventaja exactamente cero no es una victoria;
- la ventaja es fraccionaria y se imprime con dos decimales.

Las respuestas se compararon en todas las pruebas y en 40 entradas
aleatorias con un cálculo exacto, en fracciones, en los 86400 segundos del
día.

## Notas por lenguaje

- Python evalúa las candidatas en fracciones exactas.
- C++, Go, Java y Rust usan doubles y toman como iguales los valores a
  menos de `10⁻⁹` al elegir el momento óptimo más temprano.
- Java redondea la ventaja mediante `BigDecimal` con empates al par, como
  `printf` en C, porque su propio `%.2f` redondea la cadena decimal hacia
  arriba en las mitades y podría diferir en mitades exactas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1154_math.cpp](1154_math.cpp) | G++ 13.2 x64 | math | O(L + D) | AC | 0.015 s | 440 KB |
| [1154_math.go](1154_math.go) | Go 1.14 x64 | math | O(L + D) | AC | 0.015 s | 1152 KB |
| [1154_math.java](1154_math.java) | Java 1.8 | math | O(L + D) | AC | 0.140 s | 4336 KB |
| [1154_math.py](1154_math.py) | Python 3.12 x64 | math | O(L + D) | AC | 0.078 s | 1012 KB |
| [1154_math.rs](1154_math.rs) | Rust 1.75 x64 | math | O(L + D) | AC | 0.031 s | 468 KB |
