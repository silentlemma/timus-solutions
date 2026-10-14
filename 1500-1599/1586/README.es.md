# 1586. Números triprimos

[Timus 1586](https://acm.timus.ru/problem.aspx?space=1&num=1586) · dificultad 144 · dp

Problema original de Denis Musin, de la subregión oriental del NEERC del ACM ICPC 2007–2008, Ekaterimburgo, 27 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un número es triprimo cuando cada tres cifras vecinas forman un primo de
tres cifras. Hay que contar los números triprimos de n cifras
(3 ≤ n ≤ 10000) módulo 10⁹ + 9.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

n.

## Salida

La cuenta módulo 10⁹ + 9.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
```

Salida:

```
204
```

## Solución

Que una cifra pueda seguir depende solo de las dos últimas cifras, así
que los números se cuentan por ellas. Para n = 3 cada primo de tres
cifras cuenta una vez, bajo sus dos últimas cifras. Cada cifra c
siguiente se añade a un número que acaba en ab exactamente cuando abc es
un primo de tres cifras, y el número nuevo acaba en bc. Los 143 primos
de tres cifras dan 143 transiciones por cifra: `O(143·n)`. Los
resultados se contrastaron con comprobar todos los números de hasta seis
cifras.

Detalles a tener en cuenta:

- un primo de tres cifras no puede empezar por 0, así que ninguna
  ventana puede empezar por una cifra cero; contar por los propios
  primos ya lo tiene en cuenta;
- la cuenta crece deprisa y se toma módulo 10⁹ + 9, no 10⁹ + 7.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1586_dp.cpp](1586_dp.cpp) | G++ 13.2 x64 | dp | O(n) | AC | 0.015 s | 204 KB |
| [1586_dp.go](1586_dp.go) | Go 1.14 x64 | dp | O(n) | AC | 0.031 s | 6456 KB |
| [1586_dp.java](1586_dp.java) | Java 1.8 | dp | O(n) | AC | 0.171 s | 6072 KB |
| [1586_dp.py](1586_dp.py) | Python 3.12 x64 | dp | O(n) | AC | 0.390 s | 488 KB |
| [1586_dp.rs](1586_dp.rs) | Rust 1.75 x64 | dp | O(n) | AC | 0.015 s | 240 KB |
