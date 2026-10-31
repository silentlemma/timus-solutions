# 1295. Delirio

[Timus 1295](https://acm.timus.ru/problem.aspx?space=1&num=1295) · dificultad 151 · number_theory

Problema original de Den Raskovalov, de la Novena Competición Abierta por Equipos de Programación para Escolares, 13 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

¿En cuántos ceros termina el número decimal 1ⁿ + 2ⁿ + 3ⁿ + 4ⁿ, para
1 ≤ n ≤ 300 000?

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

El número n.

## Salida

La cantidad de ceros finales.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
3
```

Salida:

```
2
```

## Solución

Para el mayor n la suma tiene más de 180 000 cifras, pero sus ceros
finales están limitados por la potencia de 2 que contiene. Sea
S = 1ⁿ + 2ⁿ + 3ⁿ + 4ⁿ.

- n = 1: S = 10, un cero.
- n par: 1ⁿ + 3ⁿ ≡ 1 + 1 = 2 (mod 4), y 2ⁿ, 4ⁿ son múltiplos de 4, así
  que S es divisible por 2 pero no por 4.
- n impar, n ≥ 3: 3ⁿ ≡ 3 (mod 8), luego 1ⁿ + 3ⁿ ≡ 4 (mod 8), mientras
  que 2ⁿ y 4ⁿ son múltiplos de 8; S es divisible por 4 pero no por 8.

Así que S nunca termina en tres ceros, y S mod 100 lo decide todo: dos
ceros si vale 0, un cero si termina en 0 y ninguno en otro caso. Las
cuatro potencias módulo 100 salen de la exponenciación rápida.
`O(log n)`.

De hecho la respuesta solo depende de n mod 20: 0 cuando 4 divide a n,
2 cuando n deja resto 3 módulo 4 o 5 módulo 20, y 1 en los demás
casos. Las soluciones la calculan directamente sin apoyarse en esta
tabla.

Detalles a tener en cuenta:

- un n con resto 1 módulo 4 suele dar un cero, pero n = 5, 25, … dan
  dos (pruebas 05 y 06);
- la suma completa se puede construir con enteros grandes, pero nunca
  hace falta: solo importan sus dos últimas cifras.

Los resultados se compararon con la suma exacta en enteros grandes para
todos los n hasta 3000.

## Soluciones optimizadas

La solución optimizada en Java analiza `n` a mano desde un búfer de 4 KB
que se llena desde `System.in`, en lugar de crear un `Scanner`, así que
la JVM no carga el escáner ni sus expresiones regulares; las potencias
módulo 100 son las mismas: {1295_number_theory_optimized.java}.

### Mejora medida

Cada versión optimizada tiene Accepted y reduce el tiempo o la memoria
al menos un 30% frente a la versión básica del mismo lenguaje. Se
conservan los fuentes básicos. Una reducción negativa indica mayor
coste. El asterisco solo se refiere al objetivo de clasificación.

- `1295_number_theory_optimized.java`: reducción de tiempo +12.80%;
  reducción de memoria +79.75%; base: `1295_number_theory.java`.

## Notas por lenguaje

En la clasificación del 2026-10-31, las siguientes implementaciones
básicas ya alcanzan los objetivos de tiempo y memoria. Se conservan sus
archivos en el conjunto básico; estos lenguajes no necesitan otra
implementación para alcanzar el objetivo.

- [1295_number_theory.cpp](1295_number_theory.cpp).
- [1295_number_theory.go](1295_number_theory.go).
- [1295_number_theory.rs](1295_number_theory.rs).

- Python usa el `pow` de tres argumentos incorporado; los demás
  lenguajes elevan a la potencia módulo 100 a mano.

## Soluciones

### Sencillas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1295_number_theory.cpp](1295_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log n) | AC | 0.015 s | 128 KB | 11284634 |
| [1295_number_theory.go](1295_number_theory.go) | Go 1.14 x64 | number_theory | O(log n) | AC | 0.031 s | 1080 KB | 11284638 |
| [1295_number_theory.java](1295_number_theory.java) | Java 1.8 | number_theory | O(log n) | AC | 0.125 s | 1600 KB | 11284648 |
| [1295_number_theory.py](1295_number_theory.py) | Python 3.12 x64 | number_theory | O(log n) | AC | 0.093 s | 464 KB | 11284644 |
| [1295_number_theory.rs](1295_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log n) | AC | 0.046 s | 240 KB | 11284651 |

### Optimizadas

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1295_number_theory_optimized.java](1295_number_theory_optimized.java) | Java 1.8 | number_theory | O(log n) | AC | 0.109 s | 324 KB | 11305839 |
