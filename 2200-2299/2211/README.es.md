# 2211. Contar triángulos de lados enteros con un área entera dada

[Timus 2211](https://acm.timus.ru/problem.aspx?space=1&num=2211) · dificultad 1875 · number_theory

Problema original de Vadim Barinov, de la Olimpiada Académica Universitaria Escolar de Informática 2023.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Contar los triángulos con lados de longitud entera y área exactamente S,
donde triángulos con el mismo multiconjunto de lados son el mismo. Los
límites son 0.5 segundos y 256 MB.

## Entrada

S, 1 ≤ S ≤ 10⁹.

## Salida

El número de triángulos.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
```

Salida:

```
1
```

## Solución

La fórmula de Herón da S² = p(p − a)(p − b)(p − c) para el semiperímetro
p. Un triángulo con lados y área enteros siempre tiene perímetro par y
área divisible por 6, así que si S no es divisible por 6 la respuesta es
0. Si no, x = p − a, y = p − b y z = p − c son enteros positivos, los
lados son y + z, x + z y x + y, y

xyz(x + y + z) = S².

A triángulos distintos corresponden soluciones con x ≤ y ≤ z. Tanto x
como y dividen a S², así que la solución lista los divisores de S² a
partir de la factorización de S. Para cada x con 3x⁴ ≤ S², los
candidatos y ≥ x llegan hasta el mayor con y²(x + 2y) ≤ S² / x, lo que
mantiene z ≥ y y se halla con búsqueda binaria. Cuando xy divide a S², z
es la raíz positiva de z² + (x + y)z − S² / (xy) = 0, que debe ser
entera: el discriminante (x + y)² + 4S² / (xy) tiene que ser un cuadrado
perfecto con la paridad correcta.

En el ejemplo S² = 36 = 1 · 2 · 3 · 6, así que x, y, z = 1, 2, 3 y los
lados son 5, 4 y 3.

El trabajo está acotado por pares de divisores de S² con x e y pequeños,
lo bastante rápido para todo S hasta 10⁹.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2211_number_theory.cpp](2211_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(d(S²) log d(S²)) | AC | 0.031 s | 852 KB |
| [2211_number_theory.go](2211_number_theory.go) | Go 1.14 x64 | number_theory | O(d(S²) log d(S²)) | AC | 0.046 s | 2740 KB |
| [2211_number_theory.java](2211_number_theory.java) | Java 1.8 | number_theory | O(d(S²) log d(S²)) | AC | 0.250 s | 3296 KB |
| [2211_number_theory.py](2211_number_theory.py) | PyPy 3.10 x64 | number_theory | O(d(S²) log d(S²)) | AC | 0.500 s | 7688 KB |
| [2211_number_theory.rs](2211_number_theory.rs) | Rust 1.75 x64 | number_theory | O(d(S²) log d(S²)) | AC | 0.046 s | 892 KB |
