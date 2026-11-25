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

## Soluciones optimizadas

Rust eleva por cuadrados sucesivos la transformación afín de un período y luego evalúa los pasos restantes. El envío 11317191 tardó 0,015 s y usó 204 KB frente a 0,046 s y 216 KB en la base.

Go eleva la transformación afín de un período completo mediante exponenciación binaria y calcula directamente los pasos restantes. Go 1.14 x64, envío 11322858. Tiempo 0,031 → 0,031 s, memoria 1120 → 312 KB.

Go lee y escribe los dígitos directamente. Eleva por cuadrados sucesivos la transformación afín de un período completo y calcula los pasos restantes.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321826 · Java 1.8 №11321828 · Python 3.12 x64 №11321829 · Go 1.14 x64 №11322062 · Rust 1.75 x64 №11322063.

Python compone la transformación afín de los períodos completos por cuadrados sucesivos y luego procesa directamente los términos restantes. Python 3.12 x64, envío 11322405. Tiempo 0,109 → 0,093 s, memoria 448 → 396 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1309_math.cpp](1309_math.cpp) | G++ 13.2 x64 | math | O(9973 + n / 9973) | AC | 0.015 s | 112 KB | 11321826 |
| [1309_math.go](1309_math.go) | Go 1.14 x64 | math | O(9973 + n / 9973) | AC | 0.031 s | 1120 KB | 11322062 |
| [1309_math.java](1309_math.java) | Java 1.8 | math | O(9973 + n / 9973) | AC | 0.093 s | 2180 KB | 11321828 |
| [1309_math.py](1309_math.py) | Python 3.12 x64 | math | O(9973 + n / 9973) | AC | 0.109 s | 448 KB | 11321829 |
| [1309_math.rs](1309_math.rs) | Rust 1.75 x64 | math | O(9973 + n / 9973) | AC | 0.046 s | 216 KB | 11322063 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1309_math_optimized.rs](1309_math_optimized.rs) | Rust 1.75 x64 | math | O(n mod 9973 + log(n / 9973 + 1)) | AC | 0.015 s | 204 KB | 11317191 |
| [1309_math_optimized.go](1309_math_optimized.go) \* | Go 1.14 x64 | math | O(n mod 9973 + log(n / 9973 + 1)) | AC | 0.031 s | 312 KB | 11322858 |
| [1309_math_optimized.py](1309_math_optimized.py) | Python 3.12 x64 | math | O(n mod 9973 + log(n / 9973 + 1)) | AC | 0.093 s | 396 KB | 11322405 |

\* Las soluciones marcadas aún pueden mejorar en la clasificación objetivo.
