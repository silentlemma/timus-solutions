# 1484. Puntuación de la película

[Timus 1484](https://acm.timus.ru/problem.aspx?space=1&num=1484) · dificultad 629 · math

Problema original de Vladimir Yakovlev, del Campeonato de la Universidad Estatal de los Urales, 7 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La puntuación de una película es la media de votos enteros de 1 a 10,
redondeada a un decimal con las mitades hacia arriba (7.55 se muestra
como 7.6). Ahora muestra X tras N votos (1 ≤ X, Y ≤ 10 con un decimal,
1 ≤ N ≤ 10⁶). Hay que hallar el menor número de votos nuevos que hacen
que la puntuación muestre como mucho Y sean cuales sean los votos
anteriores, o escribir «Impossible».

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

X, Y y N.

## Salida

El número de votos o «Impossible».

## Ejemplos

### Ejemplo 1

Entrada:

```
9.5 2.0 12
```

Salida:

```
86
```

## Solución

Se trabaja en décimas: x = 10X e y = 10Y. Una suma S de N votos muestra
x justo cuando (2x − 1)N ≤ 20S < (2x + 1)N, y los votos permiten
N ≤ S ≤ 10N. Si ningún entero S cumple ambas cosas, ningún conjunto de
votos muestra X y la respuesta es «Impossible»: un solo voto, por
ejemplo, nunca muestra 7.1.

Los votos nuevos deben ser todos 1, y el peor caso es el mayor S
posible. Tras k de esos votos la puntuación muestra como mucho y cuando
20(S + k) < (2y + 1)(N + k), es decir, (2y − 19)·k > 20S − (2y + 1)N.
Como Y ≥ 1, 2y − 19 es positivo, así que el menor k es 0 si el lado
derecho ya es negativo y (20S − (2y + 1)N) div (2y − 19) + 1 si no.
`O(1)`.

Detalles a tener en cuenta:

- una puntuación que N votos no pueden mostrar es «Impossible», aunque
  el objetivo fuera fácil (pruebas 02, 09);
- 7.55 se redondea a 7.6, así que los límites son semiabiertos y mejor
  llevarlos en enteros (prueba 07);
- la respuesta llega a 179 000 001 al bajar a 1.0 un millón de dieces
  (prueba 04).

## Soluciones optimizadas

Python representa las medias mostradas como décimas enteras. Calcula la suma original máxima compatible con el redondeo y usa el límite superior estricto para obtener el número de votos nuevos.

El envío 11321720 en Python tardó 0.062 s y usó 420 KB. La versión sencilla tardó 0.078 s y usó 464 KB.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11322393 · Java 1.8 №11321717 · Go 1.14 x64 №11322437 · Python 3.12 x64 №11322438 · Rust 1.75 x64 №11322436.

El envío 11322439 en Go tardó 0.015 s y usó 320 KB. La versión sencilla tardó 0.031 s y usó 1072 KB.

Go lee los tres números en un pequeño búfer de bytes y escribe directamente los dígitos decimales del resultado, sin usar formato genérico de entrada y salida.

### Nuevas versiones aceptadas

Estas versiones usan los [criterios compartidos](../../RATING_CRITERIA.md) y Accepted del código exacto. Las discusiones anteriores describen ejecuciones y comparaciones históricas, no otra regla vigente. Se conservan las versiones sencillas y las implementaciones anteriores distintas.

`1484_math_optimized.java`. Se conserva el algoritmo y se sustituye Scanner por entrada de bytes con búfer. Cuando basta la conversión numérica normal, la salida evita Formatter. El fin de archivo funciona también sin salto de línea final; se conserva la versión sencilla.

Accepted #11328557 (Java 1.8): **0.093 s / 444 KB**. Comparación archivada: `1484_math.java` (Java 1.8) — 0.093 s / 1624 KB (#11321717).

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1484_math.cpp](1484_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 116 KB | 11322393 |
| [1484_math.go](1484_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1072 KB | 11322437 |
| [1484_math.java](1484_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1624 KB | 11321717 |
| [1484_math.py](1484_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 464 KB | 11322438 |
| [1484_math.rs](1484_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 232 KB | 11322436 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1484_math_optimized.py](1484_math_optimized.py) | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 420 KB | 11321720 |
| [1484_math_optimized.go](1484_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 320 KB | 11322439 |
| [1484_math_optimized.java](1484_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 444 KB | 11328557 |
