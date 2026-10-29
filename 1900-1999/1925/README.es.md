# 1925. El último valor para igualar una suma total

[Timus 1925](https://acm.timus.ru/problem.aspx?space=1&num=1925) · difficulty 70 · math

Problema original de Pavel Ageev, del concurso escolar regional de los Urales de 2012.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se conocen n rondas anteriores. En la ronda i se mostró bᵢ, la entrada
prevista era bᵢ−2 y la real fue gᵢ. Ahora se muestra k. Solo se comprueba
el total de las n+1 rondas: la suma real debe igualar la prevista.
Encontrar un entero no negativo para la ronda actual, o declarar que no
existe. Las rondas pasadas no necesitan ser correctas individualmente.
Límites: 1 segundo, 64 MB.

## Entrada

n,k con 1≤n,k≤100, seguidos de n pares bᵢ,gᵢ, cada valor entre 0 y 100.

## Salida

El entero no negativo necesario, incluido cero. La salida no está
limitada a 100. Si es imposible, escribir exactamente `Big Bang!`,
respetando espacio, mayúsculas y signo de exclamación.

## Evaluación

Comparación exacta de tokens: un entero o los tokens `Big` y `Bang!`.

## Ejemplos

```
6 5
3 1
3 1
5 3
6 5
5 5
7 2
```

```
3
```

```
1 3
4 6
```

```
Big Bang!
```

## Solución

Sea x la entrada de hoy. La comprobación compara las sumas de las n + 1
rondas: g₁ + … + gₙ + x = (b₁ − 2) + … + (bₙ − 2) + (k − 2). Por tanto
x = k − 2 + Σ(bᵢ − gᵢ − 2); si es negativo, ninguna entrada sirve y la
respuesta es `Big Bang!`. `O(n)`.

Detalles a tener en cuenta:

- la suma parcial puede volverse negativa a mitad de camino y acabar
  siendo no negativa, así que se decide solo al final;
- cero es una respuesta válida;
- cada ronda, la de hoy incluida, resta 2.

## Soluciones optimizadas

La solución optimizada en C++ lee los pares con `scanf` en lugar de
`iostream` y los suma al momento en lugar de guardar el historial:
124 KB en lugar de 428 KB.

La solución optimizada en Java lee la entrada en bloques de 1 KB y la
analiza a mano en lugar de usar `Scanner`, y suma las lecturas a medida
que las lee en lugar de guardarlas: 0.078 s en lugar de 0.140 s y 364 KB
en lugar de 1796 KB.

## Notas por lenguaje

Ningún lenguaje necesita nada especial.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1925_math.cpp](1925_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 428 KB | 11291544 |
| [1925_math.go](1925_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1088 KB | 11291551 |
| [1925_math.java](1925_math.java) | Java 1.8 | math | O(n) | AC | 0.140 s | 1796 KB | 11291560 |
| [1925_math.py](1925_math.py) | Python 3.12 x64 | math | O(n) | AC | 0.093 s | 504 KB | 11291556 |
| [1925_math.rs](1925_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 236 KB | 11291566 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1925_math_optimized.cpp](1925_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 124 KB | 11303650 |
| [1925_math_optimized.java](1925_math_optimized.java) | Java 1.8 | math | O(n) | AC | 0.078 s | 364 KB | 11303789 |
