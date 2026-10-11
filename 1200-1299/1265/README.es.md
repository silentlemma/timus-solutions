# 1265. Espejo

[Timus 1265](https://acm.timus.ru/problem.aspx?space=1&num=1265) · dificultad 1539 · geometry

Problema original de Alexander Klepinin (preparado por Ivan Dashkevich), del Campeonato de la Universidad Estatal de los Urales, 25 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados el ojo (x1, y1), el objetivo (x2, y2) y un espejo plano, el
segmento entre (xm1, ym1) y (xm2, ym2), hay que decidir si el objetivo
se ve en el espejo desde el ojo. El espejo refleja por ambas caras, con
el ángulo de incidencia igual al de reflexión. Los ocho números están en
[−1000, 1000] con como mucho seis cifras tras el punto; ninguno de los
dos puntos está en la recta del espejo y los extremos del espejo son
distintos.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Los ocho números, separados por espacios y saltos de línea.

## Salida

`VISIBLE` o `INVISIBLE`.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 0 0 -1 0 0 1 1
```

Salida:

```
VISIBLE
```

### Ejemplo 2

Entrada:

```
0.000001   0
0   0.000001
-0.000001   -0.000001
0.000001   0.000001
```

Salida:

```
INVISIBLE
```

## Solución

El objetivo se ve cuando ambos puntos están del mismo lado de la recta
del espejo y la línea de visión del ojo a la imagen especular del
objetivo cruza el segmento del espejo, extremos incluidos.

Se pone el origen en un extremo A del espejo, s a lo largo del espejo,
y e y t como el ojo y el objetivo respecto de A. Los productos
vectoriales he = s × e y ht = s × t son las alturas de los dos puntos
sobre la recta, multiplicadas por |s|; deben tener el mismo signo. Los
productos escalares pe = s · e y pt = s · t son sus posiciones a lo
largo de la recta, multiplicadas por |s|. La línea de visión corta la
recta del espejo donde divide el tramo entre los dos pies en la razón
de las alturas, es decir, a

```text
u = (pe · ht + pt · he) / ((he + ht) · |s|²)
```

de la longitud del espejo desde A, y el objetivo se ve justo cuando
0 ≤ u ≤ 1.

La coma flotante no basta: el cruce puede quedar a unas
millonésimas de un extremo de un espejo de dos mil de largo y decidir
la respuesta. Por eso
cada número se lee como un entero exacto en millonésimas, hasta 10⁹.
Alturas y posiciones llegan entonces a 8 · 10¹⁸, y los productos de la
comprobación a unos 1,3 · 10³⁸, que aún caben en un entero de 128 bits
con signo. `O(1)`.

Detalles a tener en cuenta:

- un objetivo delante del espejo no siempre se ve: la línea reflejada
  puede no tocar el segmento (prueba 04);
- una línea de visión por un extremo del espejo cuenta como vista
  (prueba 05), y mover el ojo 10⁻⁶ cambia la respuesta (pruebas 06, 07);
- los puntos en lados opuestos nunca se ven, aunque el espejo tenga dos
  caras (pruebas 02, 03);
- ya la suma he + ht puede desbordar 64 bits.

Las respuestas se compararon en 1500 casos aleatorios (enteros pequeños
y puntos con seis decimales) con una reflexión exacta del objetivo en
fracciones y una prueba de intersección de segmentos.

## Notas por lenguaje

- C++ y Rust calculan en `__int128` e `i128`; Go y Java toman alturas y
  posiciones en 64 bits y los productos finales en `big.Int` y
  `BigInteger`; Python usa sus propios enteros.
- Todos los lenguajes analizan los números a mano, completando la parte
  fraccionaria a seis cifras, de modo que ningún valor pasa por un
  double.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1265_geometry.cpp](1265_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 368 KB |
| [1265_geometry.go](1265_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1188 KB |
| [1265_geometry.java](1265_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 564 KB |
| [1265_geometry.py](1265_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 516 KB |
| [1265_geometry.rs](1265_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 228 KB |
