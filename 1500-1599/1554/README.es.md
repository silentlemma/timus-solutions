# 1554. Funciones multiplicativas

[Timus 1554](https://acm.timus.ru/problem.aspx?space=1&num=1554) · dificultad 639 · number_theory

Problema original del Novosibirsk SU Contest en el campus de Petrozavodsk, septiembre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados los N primeros valores (N ≤ 10⁴) de una función multiplicativa F
con valores módulo 2007, hay que hallar los N primeros valores de su
inversa G para la convolución de Dirichlet,
(F * G)(n) = Σ F(n/d)·G(d) sobre los divisores d de n, que debe valer 1
en n = 1 y 0 en el resto.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

N y luego F(1), …, F(N).

## Salida

G(1), …, G(N) en una línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
16
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
```

Salida:

```
1 2006 2006 0 2006 1 2006 0 0 1 2006 0 2006 1 1 0
```

## Solución

En n = 1 la condición dice F(1)·G(1) = 1. Para n > 1 da
F(1)·G(n) = −Σ F(n/d)·G(d) sobre los divisores propios d de n, todos
menores que n. Una F multiplicativa tiene F(1) = 1; aun así las
soluciones dividen por F(1) mediante su inverso módulo 2007, lo que no
cuesta nada.

Así que G se rellena en orden creciente, como una criba: en cuanto se
conoce G(d), se suma F(k)·G(d) al acumulador de cada múltiplo d·k ≤ N
con k ≥ 2; cuando el bucle llega a n, su acumulador ya tiene la suma
completa sobre los divisores propios. Son O(N log N) pasos,
unos 10⁵. Los resultados se comprobaron directamente con la definición.

Detalles a tener en cuenta:

- 2007 = 9·223 no es primo, así que −1 es 2006 y los inversos requieren
  el algoritmo de Euclides extendido o una función de biblioteca;
- la inversa de 1 en todas partes es la función de Möbius (prueba 01),
  la de la identidad n·μ(n) (prueba 03) y la de la función de Liouville
  |μ| (prueba 04).

## Soluciones optimizadas

Cada actualización se reduce módulo 2007, así que los arreglos solo contienen valores de 0 a 2006 y bastan 16 bits. La multiplicación usa un tipo entero más ancho antes de reducir. Un coeficiente nulo no aporta nada a los múltiplos siguientes, por lo que se omiten esas actualizaciones.

El envío de Go 11317288 tardó 0.031 s y usó 968 KB frente a 0.031 s y 1676 KB en la base.

El envío de Rust 11317290 tardó 0.015 s y usó 240 KB frente a 0.015 s y 940 KB en la base.

El envío de Java 11317291 tardó 0.109 s y usó 528 KB frente a 0.109 s y 1152 KB en la base.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321745 · Go 1.14 x64 №11322093 · Java 1.8 №11322412 · Python 3.12 x64 №11321746 · Rust 1.75 x64 №11322455.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1554_number_theory.cpp](1554_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(N log N) | AC | 0.015 s | 264 KB | 11321745 |
| [1554_number_theory.go](1554_number_theory.go) | Go 1.14 x64 | number_theory | O(N log N) | AC | 0.031 s | 1676 KB | 11322093 |
| [1554_number_theory.java](1554_number_theory.java) | Java 1.8 | number_theory | O(N log N) | AC | 0.109 s | 1152 KB | 11322412 |
| [1554_number_theory.py](1554_number_theory.py) | Python 3.12 x64 | number_theory | O(N log N) | AC | 0.109 s | 2636 KB | 11321746 |
| [1554_number_theory.rs](1554_number_theory.rs) | Rust 1.75 x64 | number_theory | O(N log N) | AC | 0.015 s | 940 KB | 11322455 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1554_number_theory_optimized.go](1554_number_theory_optimized.go) \* | Go 1.14 x64 | number_theory | O(N log N) | AC | 0.031 s | 968 KB | 11317288 |
| [1554_number_theory_optimized.rs](1554_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(N log N) | AC | 0.015 s | 240 KB | 11317290 |
| [1554_number_theory_optimized.java](1554_number_theory_optimized.java) | Java 1.8 | number_theory | O(N log N) | AC | 0.109 s | 528 KB | 11317291 |

\* El objetivo de clasificación de Go sigue pendiente. El objetivo de clasificación de Rust sigue pendiente. El objetivo de clasificación de Java sigue pendiente.
