# 1513. La fábula del limón

[Timus 1513](https://acm.timus.ru/problem.aspx?space=1&num=1513) · dificultad 381 · dp

Problema original de Nikita Rybak, Ilya Grebnov y Dmitry Kovalioff, de Timus Top Coders: Third Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un texto usa la palabra «limón» N veces (1 ≤ N ≤ 10000). Algunas pueden
cambiarse por «plátano» para que no haya más de K limones seguidos
(0 ≤ K ≤ N). Hay que contar exactamente las maneras de hacerlo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y K.

## Salida

El número de maneras.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 2
```

Salida:

```
24
```

## Solución

Sea a[i] el número de líneas de i palabras sin rachas de más de K
limones. Una línea válida de i palabras es una línea válida de i − 1
palabras más una palabra, limón o plátano, lo que da 2·a[i − 1], salvo
las líneas en que el nuevo limón forma una racha de exactamente K + 1:
esas son una línea válida de i − K − 2 palabras, un plátano y K + 1
limones, así que a[i] = 2·a[i − 1] − a[i − K − 2] para i > K, con
a[−1] = 1 para la línea de solo limones, y a[i] = 2^i para i ≤ K. No
hay módulo, así que los números son enteros grandes; Python, Go y Java
los tienen, y C++ y Rust usan cifras en base 10⁹. `O(N²)` operaciones
con cifras en el peor caso.

Detalles a tener en cuenta:

- la respuesta es exacta y llega a 2^10000, unas 3000 cifras (pruebas
  04, 07);
- con K = 0 queda una sola línea de plátanos (prueba 05);
- con K = 1 salen números de Fibonacci (prueba 06);
- la resta necesita la línea de i − K − 2 palabras aunque sea de −1
  palabras, el caso de K + 1 limones seguidos (prueba 01, gen3).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1513_dp.cpp](1513_dp.cpp) | G++ 13.2 x64 | dp | O(N^2) | AC | 0.046 s | 14844 KB |
| [1513_dp.go](1513_dp.go) | Go 1.14 x64 | dp | O(N^2) | AC | 0.062 s | 9884 KB |
| [1513_dp.java](1513_dp.java) | Java 1.8 | dp | O(N^2) | AC | 0.156 s | 12788 KB |
| [1513_dp.py](1513_dp.py) | Python 3.12 x64 | dp | O(N^2) | AC | 0.093 s | 8152 KB |
| [1513_dp.rs](1513_dp.rs) | Rust 1.75 x64 | dp | O(N^2) | AC | 0.031 s | 15176 KB |
