# 1836. Pez de Babel

[Timus 1836](https://acm.timus.ru/problem.aspx?space=1&num=1836) · dificultad 1170 · geometry

Problema original de Denis Dublennykh, del XV Campeonato Abierto de los Urales de Programación Competitiva, abril de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un acuario abierto tiene base cuadrada de lado a. Un sensor en cada
arista vertical marca el nivel del agua en esa arista; el coche se
inclina, así que la superficie puede no ser paralela al fondo. Para cada
prueba, hallar el volumen de agua, o decir "error" si las lecturas son
imposibles, o "ambiguous" si no fijan el volumen.

## Entrada

t (1 ≤ t ≤ 10⁴), luego t líneas: a y los cuatro niveles, aristas en
orden alrededor de la base, todos enteros de 0 a 10⁶ con a > 0.

## Salida

Para cada prueba, el volumen con error absoluto o relativo de como
mucho 10⁻⁶, o "error", o "ambiguous".

## Ejemplos

### Ejemplo 1

Entrada:

```
2
10 2 3 4 3
10 2 3 3 3
```

Salida:

```
300.000
error
```

## Solución

La superficie es un plano, así que sus alturas f₁, …, f₄ sobre las
esquinas cumplen f₁ + f₃ = f₂ + f₄, y un sensor marca max(0, fᵢ): una
lectura 0 solo dice que fᵢ ≤ 0.

- Sin lecturas nulas: el plano se conoce. Es coherente exactamente
  cuando las sumas de las diagonales coinciden, y el volumen es
  a²·(h₁ + h₂ + h₃ + h₄)/4.
- Todas las lecturas nulas: el plano no queda por encima del fondo en
  ningún punto, volumen 0.
- Un cero, en la esquina i: el plano da fᵢ = (left + right) − far, que
  debe ser como mucho 0. El plano cae bajo el fondo en un tetraedro de la
  esquina: baja a fᵢ en la esquina y cruza el cero en las dos
  aristas a fracciones −fᵢ/(left − fᵢ) y −fᵢ/(right − fᵢ). Su volumen,
  un sexto del producto de sus aristas, se divide entre a² y se suma
  a la altura media.
- Dos ceros o más: las alturas ocultas solo deben ser como mucho 0 y
  equilibrar las diagonales. Si ambas diagonales tienen una esquina
  oculta, siempre pueden hacerlo, y de muchas maneras; si solo una la
  tiene, falla exactamente cuando la suma conocida de esa diagonal es
  menor que la de la otra. En los demás casos el volumen no queda fijado.

`O(1)` por prueba; Python corrige con fracciones exactas, los demás
usan coma flotante.

En el primer ejemplo 2 + 4 = 3 + 3 y el volumen es 100·12/4 = 300; en
el segundo 2 + 3 ≠ 3 + 3.

Trampas:

- una lectura cero no es una altura cero, solo una cota;
- con una esquina seca, la fórmula sin el tetraedro se queda corta:
  para lado 4 y niveles 0 1 5 1 la altura oculta es −3 y el volumen es
  16·(1 + 27/96) = 20.5, no 16;
- los volúmenes llegan a 10¹⁸.

Las respuestas coinciden con una implementación aceptada independiente
en diez mil pruebas aleatorias, la mitad de ellas planos reales
cortados por el fondo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1836_geometry.cpp](1836_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) per test | AC | 0.046 s | 460 KB |
| [1836_geometry.go](1836_geometry.go) | Go 1.14 x64 | geometry | O(1) per test | AC | 0.062 s | 2444 KB |
| [1836_geometry.java](1836_geometry.java) | Java 1.8 | geometry | O(1) per test | AC | 0.171 s | 6924 KB |
| [1836_geometry.py](1836_geometry.py) | Python 3.12 x64 | geometry | O(1) per test | AC | 0.156 s | 4868 KB |
| [1836_geometry.rs](1836_geometry.rs) | Rust 1.75 x64 | geometry | O(1) per test | AC | 0.015 s | 1292 KB |
