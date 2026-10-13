# 1417. Póquer espacial

[Timus 1417](https://acm.timus.ru/problem.aspx?space=1&num=1417) · dificultad 1884 · math

Problema original de Stanislav Vasiliev, del Campeonato de la Universidad Estatal de los Urales, 29 de octubre de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un jugador y un crupier muestran cada uno de 1 a N dedos (1 < N ≤ 100).
Una tabla N × N da el premio del jugador para cada par: 1000 en la
diagonal, donde coinciden, y un entero de 0 a 10 en lo demás. El jugador
paga 20 por ronda; el casino busca maximizar su beneficio esperado ante
un jugador que actúa de forma óptima. Hay que hallar las probabilidades
con que el crupier debe mostrar cada número
para que el premio esperado del jugador no dependa del número que el
jugador muestre, e imprimirlas con 5 cifras tras el punto.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

N, luego la tabla: la fila i para el número i del jugador, la columna j
para el número j del crupier.

## Salida

N probabilidades, una por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
1000 10 10
0 1000 1
5 3 1000
```

Salida:

```
0.32986
0.33623
0.33391
```

## Solución

Con probabilidades p, el jugador que muestra i espera Σⱼ A[i][j]·pⱼ, y
todos esos valores deben ser un mismo v. Se resuelve A·x = (1, …, 1)
por eliminación gaussiana con pivoteo parcial; entonces p = x / Σx y
v = 1 / Σx.

La diagonal de 1000 pesa más que el resto de su fila (como mucho
99 · 10 = 990), así que A no es singular. La aplicación
Fᵢ(x) = (1 − Σⱼ≠ᵢ A[i][j]·xⱼ) / 1000 preserva [10⁻⁵, 10⁻³]ᴺ y contrae
con un factor de como mucho 0.99, así que su punto fijo x es positivo.
Por tanto la respuesta siempre existe con probabilidades positivas.
`O(N³)`.

Detalles a tener en cuenta:

- las filas son del jugador y las columnas del crupier, así que el
  sistema es A·p = v·1 y no su traspuesto (pruebas 03, 05);
- premios de consolación iguales en todas partes dan probabilidades
  iguales (pruebas 02, 04).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1417_math.cpp](1417_math.cpp) | G++ 13.2 x64 | math | O(N^3) | AC | 0.015 s | 308 KB |
| [1417_math.go](1417_math.go) | Go 1.14 x64 | math | O(N^3) | AC | 0.031 s | 1240 KB |
| [1417_math.java](1417_math.java) | Java 1.8 | math | O(N^3) | AC | 0.125 s | 1208 KB |
| [1417_math.py](1417_math.py) | Python 3.12 x64 | math | O(N^3) | AC | 0.140 s | 1732 KB |
| [1417_math.rs](1417_math.rs) | Rust 1.75 x64 | math | O(N^3) | AC | 0.031 s | 420 KB |
