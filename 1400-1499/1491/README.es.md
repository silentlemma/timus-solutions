# 1491. Historia irreal

[Timus 1491](https://acm.timus.ru/problem.aspx?space=1&num=1491) · dificultad 205 · prefix_sums

Problema original de Alexander Toropov, del Decimotercer Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 14 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N caballeros (2 ≤ N ≤ 100000) están numerados de 1 a N. El rey nombra a,
b y c, y cada caballero de a a b recibe c monedas; después cada
caballero nombra otra terna a_i, b_i, c_i con el mismo efecto
(1 ≤ a ≤ b ≤ N, 1 ≤ c ≤ 10000). Hay que escribir cuántas monedas
recibe cada caballero.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, la terna del rey y luego las N ternas de los caballeros.

## Salida

N totales separados por espacios.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
2 3 2
2 4 1
3 4 1
1 2 1
1 1 1
```

Salida:

```
2 4 4 2
```

### Ejemplo 2

Entrada:

```
7
1 7 1
2 3 4
3 5 3
1 2 1
5 7 4
2 4 10
3 4 2
1 6 3
```

Salida:

```
5 19 23 19 11 8 5
```

## Solución

N + 1 sumas sobre tramos de hasta 10⁵ de largo, una a una, son demasiado
lentas. Un array de diferencias anota un regalo de c a los caballeros
a..b como +c en la posición a y −c en la posición b + 1; luego una suma
acumulada sobre el array da el total de cada caballero. `O(N)`.

Detalles a tener en cuenta:

- la terna del rey es un regalo más, así que hay N + 1 (pruebas 01, 02);
- un total puede llegar a 100001 · 10000 ≈ 10⁹, cerca del límite de 32
  bits, así que las sumas se guardan en 64 bits (gen2);
- las condiciones sobre los asientos de los caballeros no cambian nada
  en las cuentas (todas las pruebas).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1491_prefix_sums.cpp](1491_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N) | AC | 0.187 s | 980 KB |
| [1491_prefix_sums.go](1491_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N) | AC | 0.031 s | 4540 KB |
| [1491_prefix_sums.java](1491_prefix_sums.java) | Java 1.8 | prefix_sums | O(N) | AC | 0.109 s | 8872 KB |
| [1491_prefix_sums.py](1491_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N) | AC | 0.328 s | 35944 KB |
| [1491_prefix_sums.rs](1491_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N) | AC | 0.046 s | 9428 KB |
