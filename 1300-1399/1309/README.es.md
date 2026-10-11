# 1309. El arte de discutir

[Timus 1309](https://acm.timus.ru/problem.aspx?space=1&num=1309) · dificultad 602 · math

Problema original con idea de Alexander Klepinin, preparado por Alexander Klepinin y Stanislav Vasiliev, del Octavo Campeonato Estudiantil por Equipos de Programación de los Urales, Ekaterimburgo, 11–16 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

f(0) = 0 y f(n) = g(n, f(n − 1)), donde

g(x, y) = ((y − 1)x⁵ + x³ − xy + 3x + 7y) mod 9973.

Hay que calcular f(n) para 0 ≤ n ≤ 10⁸ en medio segundo.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

El número n.

## Salida

f(n).

## Ejemplos

### Ejemplo 1

Entrada:

```
50
```

Salida:

```
6300
```

## Solución

Agrupando los términos en y:

g(x, y) = y · (x⁵ − x + 7) + (x³ + 3x − x⁵) mod 9973,

así que cada paso es una aplicación afín y → a(x) · y + b(x) módulo
9973, cuyos coeficientes solo dependen de x mod 9973. Por tanto los
pasos x = 1, …, 9973 se repiten, en el mismo orden, en cada bloque de
9973 valores consecutivos de x.

- Se componen las 9973 aplicaciones de un bloque en una sola
  y → A · y + B.
- Se escribe n = q · 9973 + r. Se aplica y → A · y + B q veces
  (q ≤ 10 028) y después los pasos sueltos x = 1, …, r.

Tres bucles cortos de unos 10 000 pasos en lugar de 10⁸.
`O(9973 + n / 9973)`.

Detalles a tener en cuenta:

- con y = 0 la expresión es negativa para x ≥ 2, así que el resto debe
  tomarse a la manera matemática, de 0 a 9972. Un `%` que trunca, como
  el de C, daría una respuesta distinta por primera vez en n = 1893
  (prueba 04);
- x⁵ no cabe en 64 bits ni siquiera con x cerca de 9973, así que las
  potencias se reducen módulo 9973 tras cada multiplicación;
- n = 0 da 0 (prueba 02), y n justo por debajo, en y justo por encima
  de un múltiplo de 9973 comprueba las uniones (pruebas 05–07).

Los resultados se compararon con la recurrencia directa para todos los
n hasta 60 000 y, para n grandes, con un segundo método que eleva la
aplicación del bloque a la potencia q por cuadrados sucesivos.

## Notas por lenguaje

- Java usa `Math.floorMod` y Rust `rem_euclid` para el resto no
  negativo; C++ y Go suman 9973 antes del último `%`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1309_math.cpp](1309_math.cpp) | G++ 13.2 x64 | math | O(9973 + n / 9973) | AC | 0.015 s | 128 KB |
| [1309_math.go](1309_math.go) | Go 1.14 x64 | math | O(9973 + n / 9973) | AC | 0.031 s | 1092 KB |
| [1309_math.java](1309_math.java) | Java 1.8 | math | O(9973 + n / 9973) | AC | 0.125 s | 2148 KB |
| [1309_math.py](1309_math.py) | Python 3.12 x64 | math | O(9973 + n / 9973) | AC | 0.078 s | 464 KB |
| [1309_math.rs](1309_math.rs) | Rust 1.75 x64 | math | O(9973 + n / 9973) | AC | 0.046 s | 224 KB |
