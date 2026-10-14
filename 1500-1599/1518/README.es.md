# 1518. Acertijo Jedi 3

[Timus 1518](https://acm.timus.ru/problem.aspx?space=1&num=1518) · dificultad 1049 · math

Problema original de Ilya Grebnov, Nikita Rybak y Dmitry Kovalioff, de Timus Top Coders: Third Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan las claves K1 … KN (1 ≤ N ≤ 100, cada una de 0 a 100), y cada
clave posterior cumple
Ki = (Ki−1·CN + Ki−2·CN−1 + … + Ki−N·C1) mod Y, con desplazamientos Ci
iguales a 0 o 1 y 2 ≤ Y < 2²⁸. Hay que hallar KX para N < X < 2²⁸.

Límite de tiempo: 1.5 segundos. Límite de memoria: 64 MB.

## Entrada

N, X e Y, luego las N claves y luego los N desplazamientos.

## Salida

KX.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 6 73
12 91 65
1 1 0
```

Salida:

```
22
```

## Solución

Contando desde K1, la clave KX es el término X − 1 de una recurrencia
lineal. Su polinomio característico es P(x) = x^N − Σ x^(N−j) sobre los
j con C(N+1−j) = 1. Se calcula x^(X−1) módulo P(x) e Y por cuadrados
sucesivos: se multiplican dos polinomios de grado menor que N y luego
se pliega cada término x^d con d ≥ N sustituyendo x^N por la suma de
arriba. Si x^(X−1) ≡ r0 + r1·x + … + r(N−1)·x^(N−1), entonces
KX = r0·K1 + r1·K2 + … + r(N−1)·KN mod Y. Cada producto cuesta
`O(N²)`, y unos 2·28 productos dan `O(N² log X)`, unas 10⁶
operaciones; elevar una matriz de 100 × 100 necesitaría unos 6·10⁷
multiplicaciones.

Detalles a tener en cuenta:

- X llega a 2²⁸, así que recorrer las claves una a una es demasiado
  lento (gen5);
- los productos de dos restos llegan a 2⁵⁶, así que se reduce tras cada
  uno (prueba 05, gen5);
- las claves dadas pueden alcanzar Y y también hay que reducirlas
  (prueba 07);
- con N = 1 el polinomio es constante: x se sustituye por C1
  (pruebas 02, 03);
- con todos los desplazamientos a 0, las claves posteriores son 0
  (prueba 04).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1518_math.cpp](1518_math.cpp) | G++ 13.2 x64 | math | O(N^2 log X) | AC | 0.015 s | 204 KB |
| [1518_math.go](1518_math.go) | Go 1.14 x64 | math | O(N^2 log X) | AC | 0.031 s | 1200 KB |
| [1518_math.java](1518_math.java) | Java 1.8 | math | O(N^2 log X) | AC | 0.140 s | 3120 KB |
| [1518_math.py](1518_math.py) | Python 3.12 x64 | math | O(N^2 log X) | AC | 0.109 s | 544 KB |
| [1518_math.rs](1518_math.rs) | Rust 1.75 x64 | math | O(N^2 log X) | AC | 0.046 s | 244 KB |
