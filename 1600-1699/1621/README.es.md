# 1621. Integral definida

[Timus 1621](https://acm.timus.ru/problem.aspx?space=1&num=1621) · dificultad 4445 · math

Problema original del SPbSU ITMO Contest en el campus de Petrozavodsk, invierno de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

P(x) = a4·x⁴ + a3·x³ + a2·x² + a1·x + a0 tiene coeficientes enteros de
valor absoluto a lo sumo 10⁶, a4 ≠ 0, sin raíces reales ni raíces
repetidas. Calcula la integral de 1 / P(x) sobre toda la recta real, con
un error absoluto o relativo de a lo sumo 10⁻⁹.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

a0, a1, a2, a3 y a4.

## Salida

El valor de la integral.

## Ejemplos

### Ejemplo 1

Entrada:

```
16 0 0 0 1
```

Salida:

```
0.2776801836
```

## Solución

La sustitución x = sinh t, dx = cosh t dt convierte la recta infinita en
t ∈ (−∞, ∞) con un integrando que decae como e⁻³ᵗ; cortar en |t| = 20
(x ≈ 2,4·10⁸) pierde menos de 10⁻²⁰. El resto es cuadratura adaptativa
de Gauss–Legendre de tres puntos: un intervalo se divide en dos mientras
las dos mitades juntas difieran del total en más de
10⁻¹³ · (1 + |valor|), hasta 50 niveles, de modo que los picos agudos de
raíces cercanas al eje real reciben intervalos finos y los tramos planos
quedan gruesos. `O(S)` para S intervalos.

El análisis complejo da una comprobación: la integral es 2πi por la suma
de 1 / P′(z) sobre las raíces z del semiplano superior. Las raíces
halladas numéricamente dan los mismos valores en todas las pruebas de
aquí.

Detalles a tener en cuenta:

- un coeficiente principal negativo hace a P negativo en todas partes y
  a la integral negativa (prueba 03);
- raíces como 999 ± i dan un pico estrecho lejos del origen (prueba 04);
- 10⁶ x⁴ + 1 y x⁴ + 10⁶ ponen la masa en escalas muy distintas
  (pruebas 05, 06).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1621_math.cpp](1621_math.cpp) | G++ 13.2 x64 | math | O(S) | AC | 0.031 s | 464 KB |
| [1621_math.go](1621_math.go) | Go 1.14 x64 | math | O(S) | AC | 0.046 s | 1088 KB |
| [1621_math.java](1621_math.java) | Java 1.8 | math | O(S) | AC | 0.234 s | 1960 KB |
| [1621_math.py](1621_math.py) | Python 3.12 x64 | math | O(S) | AC | 0.265 s | 552 KB |
| [1621_math.rs](1621_math.rs) | Rust 1.75 x64 | math | O(S) | AC | 0.015 s | 280 KB |
