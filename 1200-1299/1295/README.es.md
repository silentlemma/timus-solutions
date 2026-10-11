# 1295. Delirio

[Timus 1295](https://acm.timus.ru/problem.aspx?space=1&num=1295) · dificultad 151 · number_theory

Problema original de Den Raskovalov, de la Novena Competición Abierta por Equipos de Programación para Escolares, 13 de marzo de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

¿En cuántos ceros termina el número decimal 1ⁿ + 2ⁿ + 3ⁿ + 4ⁿ, para
1 ≤ n ≤ 300 000?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

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

## Notas por lenguaje

- Python usa el `pow` de tres argumentos incorporado; los demás
  lenguajes elevan a la potencia módulo 100 a mano.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1295_number_theory.cpp](1295_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log n) | AC | 0.015 s | 128 KB |
| [1295_number_theory.go](1295_number_theory.go) | Go 1.14 x64 | number_theory | O(log n) | AC | 0.031 s | 1080 KB |
| [1295_number_theory.java](1295_number_theory.java) | Java 1.8 | number_theory | O(log n) | AC | 0.125 s | 1600 KB |
| [1295_number_theory.py](1295_number_theory.py) | Python 3.12 x64 | number_theory | O(log n) | AC | 0.093 s | 464 KB |
| [1295_number_theory.rs](1295_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log n) | AC | 0.046 s | 240 KB |
