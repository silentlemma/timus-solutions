# 2121. Área entre dos parábolas reflejadas

[Timus 2121](https://acm.timus.ru/problem.aspx?space=1&num=2121) · dificultad 723 · geometry, math

Problema original de Alexey Danilyuk, del concurso t.me/umnik_team, campamento de Petrozavodsk, verano de 2018.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hallar el área de la región limitada por las parábolas y = (x − a)² y
x = (y − a)², impresa con exactamente 10 cifras tras el punto decimal.
Los límites son 1 segundo y 64 MB.

## Entrada

Un entero a, 1 ≤ a ≤ 10¹⁸.

## Salida

El área.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
7.6666666667
```

## Solución

Se traslada el origen a (a, a): con x = a + p e y = a + q la región es
q ≥ p² − a y p ≥ q² − a. Las dos parábolas se cortan en cuatro puntos.
Dos están sobre q = p, donde p² = p + a, así que p = (1 ± s)/2 con
s = √(4a + 1). Restar las ecuaciones da (p − q)(p + q + 1) = 0, así que
los otros dos están sobre p + q = −1 en p = (−1 ± t)/2 con t = √(4a − 3).

Se integra en p: el borde superior es q = √(p + a), y el inferior es
q = p² − a cerca de ambos extremos y q = −√(p + a) en el medio. En cada
esquina √(p + a) vale |q|, así que cada primitiva se convierte en un
polinomio en las coordenadas de las esquinas. Después las sumas y los
productos de las dos raíces de cada par eliminan s y t: el área es
exactamente 4a − 1/3.

Así que la respuesta es 4a − 1 seguido de ".6666666667". Para a = 10¹⁸
la parte entera queda justo por debajo de 4 · 10¹⁸ y cabe en un entero de
64 bits, mientras que la coma flotante perdería las últimas cifras.

En el ejemplo 4 · 2 − 1/3 = 7.6666666667.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2121_geometry_math.cpp](2121_geometry_math.cpp) | G++ 13.2 x64 | geometry, math | O(1) | AC | 0.015 s | 132 KB |
| [2121_geometry_math.go](2121_geometry_math.go) | Go 1.14 x64 | geometry, math | O(1) | AC | 0.015 s | 1076 KB |
| [2121_geometry_math.java](2121_geometry_math.java) | Java 1.8 | geometry, math | O(1) | AC | 0.125 s | 1628 KB |
| [2121_geometry_math.py](2121_geometry_math.py) | Python 3.12 x64 | geometry, math | O(1) | AC | 0.078 s | 376 KB |
| [2121_geometry_math.rs](2121_geometry_math.rs) | Rust 1.75 x64 | geometry, math | O(1) | AC | 0.015 s | 240 KB |
