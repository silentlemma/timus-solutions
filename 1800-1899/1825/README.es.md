# 1825. Bombardeo de ifrits 2

[Timus 1825](https://acm.timus.ru/problem.aspx?space=1&num=1825) · dificultad 927 · geometry

Problema original de Alexander Belits, del XII Concurso Individual Abierto de la Universidad Estatal de los Urales, 19 de marzo de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada una de dos botellas destruye un anillo: todo lo que está a una
distancia entre r y R de su punto de impacto. Los puntos distan d.
Hallar el área total destruida por ambas botellas.

## Entrada

d, r₁, R₁, r₂, R₂ (0 ≤ d ≤ 15000, 1 ≤ rᵢ < Rᵢ ≤ 15000).

## Salida

El área de la unión de los dos anillos, con error absoluto o relativo
de como mucho 10⁻⁶.

## Ejemplos

### Ejemplo 1

Entrada:

```
200 100 300 200 300
```

Salida:

```
353992.933435
```

## Solución

La unión es la suma de las áreas de los anillos π(R² − r²) menos su
intersección. Un anillo es un disco menos un disco menor dentro de él,
así que, con L(a, b) el área común a discos de radios a y b alrededor
de los dos puntos, por inclusión y exclusión

intersección = L(R₁, R₂) − L(r₁, R₂) − L(R₁, r₂) + L(r₁, r₂).

L es la lente de siempre: 0 si d ≥ a + b, π·min(a, b)² si d ≤ |a − b|,
y si no a²α + b²β menos el área de la cometa que pasa por ambos
centros y ambos puntos de corte, donde α y β son los semiángulos de la
lente vistos desde los centros, por el teorema del coseno, y la cometa
vale la mitad de √((−d+a+b)(d+a−b)(d−a+b)(d+a+b)). Las comprobaciones
de caso usan enteros exactos, y estrictamente dentro del caso de lente
los cosenos quedan lejos de ±1. `O(1)`.

En el ejemplo L(r₁, R₂) es todo el primer disco interior: un disco de
radio 100 a distancia 200 cabe dentro de uno de radio 300; los otros
tres pares son lentes de verdad.

Trampas:

- con d = 0 ambas fórmulas de la lente dividen por cero; el caso de
  contención lo atrapa antes;
- un anillo puede caer entero en el hueco del otro, y entonces la
  intersección es 0 aunque los discos exteriores se corten;
- distinguir cruce y tangencia: en la prueba 06 el anillo pequeño cruza
  la circunferencia exterior del grande (distancias de 8 a 12 frente a
  un radio de 10); en la prueba 07 son tangentes exteriores (7 = 5 + 2)
  y el área de intersección es 0;
- las áreas llegan a unos 10⁹, así que lo que cuenta es el error
  relativo.

El ejemplo coincide con un conteo sobre una malla fina, y todas las
respuestas coinciden con una implementación aceptada independiente en
unos 400 casos aleatorios y tangentes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1825_geometry.cpp](1825_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 160 KB |
| [1825_geometry.go](1825_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 1076 KB |
| [1825_geometry.java](1825_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 1852 KB |
| [1825_geometry.py](1825_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 508 KB |
| [1825_geometry.rs](1825_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 248 KB |
