# 1528. Sucesión

[Timus 1528](https://acm.timus.ru/problem.aspx?space=1&num=1528) · dificultad 272 · math

Problema original de Dmitry Gozman, del Dmitry Gozman Contest 1 en el campus de invierno de Petrozavodsk, enero de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Con f(1) = g(1) = 1, f(n) = 1 + f(1)g(1) + … + f(n − 1)g(n − 1) y
g(n) = 1 + 2g(1) + … + 2g(n − 1) − g(n − 1)². Para hasta 5000 casos
(1 ≤ n ≤ 10000, 2 ≤ p ≤ 2·10⁹) hay que escribir f(n) mod p.

Límite de tiempo: 3 segundos. Límite de memoria: 64 MB.

## Entrada

Pares n y p, uno por línea, terminados en 0 0.

## Salida

f(n) mod p para cada caso.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 2
2 11
0 0
```

Salida:

```
1
2
```

## Solución

Ambas sucesiones tienen forma cerrada. Si g(i) = i para i < n,
entonces g(n) = 1 + (n − 1)n − (n − 1)² = n. Así
f(n) − f(n − 1) = f(n − 1)·(n − 1), de modo que f(n) = n·f(n − 1) = n!.
Cada caso pide n! mod p. Si n ≥ p, el propio p es uno de los factores y
la respuesta es 0. Si no, se multiplica hasta n reduciendo módulo p;
los productos quedan por debajo de 2·10¹³, dentro de 64 bits. Son hasta
5·10⁷ multiplicaciones en total, rápido en lenguajes compilados. En
Python el bucle simple tarda unos 6 segundos, así que la solución en
Python guarda los factoriales exactos de cada múltiplo de 100 como
enteros grandes, reduce uno de ellos y multiplica como mucho 99
factores más.

Detalles a tener en cuenta:

- las fórmulas parecen pesadas, pero g(n) = n y f(n) = n! (todas las
  pruebas);
- n ≥ p da 0 directamente (prueba 02, gen3);
- p llega a 2·10⁹, así que los productos necesitan 64 bits (prueba 03,
  gen1);
- un primo p justo por encima de n es una buena prueba: el teorema de
  Wilson da (p − 1)! ≡ −1 (prueba 05).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1528_math.cpp](1528_math.cpp) | G++ 13.2 x64 | math | O(n) per case | AC | 0.328 s | 132 KB |
| [1528_math.go](1528_math.go) | Go 1.14 x64 | math | O(n) per case | AC | 0.343 s | 1224 KB |
| [1528_math.java](1528_math.java) | Java 1.8 | math | O(n) per case | AC | 0.609 s | 904 KB |
| [1528_math.py](1528_math.py) | Python 3.12 x64 | math | O(n) per case | AC | 0.359 s | 17900 KB |
| [1528_math.rs](1528_math.rs) | Rust 1.75 x64 | math | O(n) per case | AC | 0.250 s | 520 KB |
