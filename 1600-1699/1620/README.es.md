# 1620. Casa inteligente

[Timus 1620](https://acm.timus.ru/problem.aspx?space=1&num=1620) · dificultad 1551 · probability

Problema original del SPbSU ITMO Contest en el campus de Petrozavodsk, invierno de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N bombillas (1 ≤ N ≤ 10⁹), M de ellas encendidas. K veces (K ≤ 1000) un
virus elige una bombilla al azar uniformemente y cambia su estado.
Imprime el número esperado de bombillas encendidas al final como fracción
irreducible p/q.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

N, M y K.

## Salida

La esperanza como `p/q`.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 1 9
```

Salida:

```
0/1
```

### Ejemplo 2

Entrada:

```
5 4 3
```

Salida:

```
353/125
```

## Solución

Si en promedio hay E bombillas encendidas, un cambio apaga una con
probabilidad E / N y enciende una con probabilidad (N − E) / N, así que
la siguiente esperanza es E · (1 − 2/N) + 1. Su punto fijo es N/2, y la
distancia a él se multiplica cada vez por (N − 2)/N:

E_K = N/2 + (M − N/2) · ((N − 2)/N)^K = (N^(K+1) + (2M − N)(N − 2)^K) / (2 N^K).

Los números llegan a unas 9 000 cifras. Python, Go y Java usan sus
enteros grandes. Un mcd de dos números así es lento en Java, y C++ y
Rust no tienen enteros grandes, así que estas soluciones guardan el
numerador en dígitos de base 10⁹ y cancelan solo los primos de 2N
—ningún otro primo divide al denominador 2N^K—, dividiendo por cada uno
mientras se pueda. `O(K²)` operaciones con dígitos.

Detalles a tener en cuenta:

- el resultado puede ser 0, impreso como `0/1` (el primer ejemplo);
- N = 1 hace negativo a N − 2, y N = 2 lo hace cero (pruebas 03, 05);
- con K = 0 la respuesta es M/1 (prueba 04);
- Python 3.12 limita la impresión de enteros a 4 300 cifras si no se
  levanta el límite.

Las respuestas coinciden con una implementación aceptada independiente
en 300 entradas aleatorias, muchas con N potencia de dos o con muchos
factores primos pequeños.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1620_math.cpp](1620_math.cpp) | G++ 13.2 x64 | math | O(K²) | AC | 0.031 s | 324 KB |
| [1620_math.go](1620_math.go) | Go 1.14 x64 | math | O(K²) | AC | 0.031 s | 1432 KB |
| [1620_math.java](1620_math.java) | Java 1.8 | math | O(K²) | AC | 0.156 s | 5720 KB |
| [1620_math.py](1620_math.py) | Python 3.12 x64 | math | O(K²) | AC | 0.062 s | 472 KB |
| [1620_math.rs](1620_math.rs) | Rust 1.75 x64 | math | O(K²) | AC | 0.031 s | 344 KB |
