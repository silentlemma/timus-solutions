# 2179. El mayor número de carreteras rectas sin cruces entre ciudades

[Timus 2179](https://acm.timus.ru/problem.aspx?space=1&num=2179) · dificultad 2099 · geometry

Problema original de Vadim Barinov, del Concurso Escolar de Programación de los Urales 2023.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ciudades distintas son puntos del plano. Una carretera es un segmento
recto entre dos ciudades sin otra ciudad encima, y las carreteras solo
pueden tocarse en extremos comunes. Hallar el mayor número de
carreteras. Los límites son 1 segundo y 256 MB.

## Entrada

N, 2 ≤ N ≤ 10⁵, y luego N puntos con coordenadas de valor absoluto
hasta 10⁹.

## Salida

El mayor número de carreteras.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
3 1
-2 -3
1 0
0 6
```

Salida:

```
6
```

## Solución

Un conjunto de carreteras al que no se puede añadir otra es una
triangulación de los puntos: cada cara acotada es un triángulo y el
borde exterior es la envolvente convexa. Si h ciudades están en el borde
de la envolvente, contando las colineales, la fórmula de Euler da a toda
triangulación las mismas 3N − 3 − h aristas, así que la respuesta solo
necesita h.

La cadena monótona construye la envolvente inferior y la superior de los
puntos ordenados y quita un punto solo en un giro estricto a la derecha,
así que las ciudades sobre una arista de la envolvente se quedan en la
cadena. Las dos cadenas comparten sus dos extremos, así que
h = inferior + superior − 2. Si todas las ciudades están en una recta,
ambas cadenas tienen las N, h sale 2N − 2 y la fórmula da las N − 1
carreteras entre vecinas, que es lo correcto.

En el ejemplo (1, 0) está dentro del triángulo de las otras tres, así
que h = 3 y la respuesta es 12 − 3 − 3 = 6: los tres lados y tres
carreteras a la ciudad interior.

La ordenación da O(N log N).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2179_geometry.cpp](2179_geometry.cpp) | G++ 13.2 x64 | geometry | O(N log N) | AC | 0.062 s | 4392 KB |
| [2179_geometry.go](2179_geometry.go) | Go 1.14 x64 | geometry | O(N log N) | AC | 0.078 s | 13208 KB |
| [2179_geometry.java](2179_geometry.java) | Java 1.8 | geometry | O(N log N) | AC | 0.187 s | 7228 KB |
| [2179_geometry.py](2179_geometry.py) | Python 3.12 x64 | geometry | O(N log N) | AC | 0.484 s | 25840 KB |
| [2179_geometry.rs](2179_geometry.rs) | Rust 1.75 x64 | geometry | O(N log N) | AC | 0.062 s | 8148 KB |
