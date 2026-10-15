# 1734. Base de finales

[Timus 1734](https://acm.timus.ru/problem.aspx?space=1&num=1734) · dificultad 2169 · combinatorics

Problema original de Igor Chevdar, del XIV Campeonato Abierto por Equipos de Programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Contar las posiciones de damas en un tablero n × n con exactamente k
piezas. Una pieza es un peón o una dama blanca o negra y está en una
casilla oscura; deben estar los dos colores, y ningún peón está en la
fila donde se coronaría (los peones blancos no en la última fila, los
negros no en la primera). Imprimir la cantidad módulo 10⁹ + 7.

## Entrada

n y k (4 ≤ n ≤ 1000, n par, 2 ≤ k ≤ n²/4).

## Salida

La cantidad de posiciones módulo 10⁹ + 7.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 2
```

Salida:

```
172
```

## Solución

Hay n²/2 casillas oscuras: n/2 en la primera fila, n/2 en la última y
m = n²/2 − n en medio. Una casilla oscura de la primera o la última
fila admite tres clases de pieza y cualquier otra cuatro, así que las
posiciones con k piezas, sin mirar los colores, son

Σ C(n, a)·3^a·C(m, k − a)·4^(k − a)

sobre a, las piezas en las dos filas del borde.

A eso se le restan las posiciones de un solo color, dos veces por
simetría. Para las blancas, una casilla de la última fila admite solo
la dama y cualquier otra el peón o la dama, lo que da

Σ C(n/2, a)·C(m + n/2, k − a)·2^(k − a).

Como k ≥ 2, el tablero nunca está vacío. Los factoriales hasta n²/2 y
sus inversos dan los coeficientes binomiales. `O(n²)` para los
factoriales, `O(n log k)` para las sumas.

Para n = 4 y k = 2 la primera suma es 96 + 192 + 54 = 342 y la segunda
60 + 24 + 1 = 85, así que la respuesta es 342 − 2·85 = 172.

Trampas:

- las dos filas del borde pierden una clase de pieza, no solo la fila
  de coronación del rival;
- para un solo color las filas del borde difieren: en su primera fila
  valen las dos clases, en su última solo la dama;
- la diferencia debe volver al rango 0 … 10⁹ + 6.

Las cantidades coinciden con un listado de todas las posiciones para
todo k en tableros 4 × 4 y para k hasta 4 en tableros 6 × 6, y con una
implementación aceptada independiente en las pruebas grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1734_combinatorics.cpp](1734_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(n²) | AC | 0.031 s | 7736 KB |
| [1734_combinatorics.go](1734_combinatorics.go) | Go 1.14 x64 | combinatorics | O(n²) | AC | 0.046 s | 9672 KB |
| [1734_combinatorics.java](1734_combinatorics.java) | Java 1.8 | combinatorics | O(n²) | AC | 0.171 s | 9468 KB |
| [1734_combinatorics.py](1734_combinatorics.py) | Python 3.12 x64 | combinatorics | O(n²) | AC | 0.281 s | 39668 KB |
| [1734_combinatorics.rs](1734_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(n²) | AC | 0.046 s | 7896 KB |
