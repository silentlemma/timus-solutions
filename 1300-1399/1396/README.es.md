# 1396. Máximo. Versión 2

[Timus 1396](https://acm.timus.ru/problem.aspx?space=1&num=1396) · dificultad 1955 · math

Problema original preparado por Vladimir Yakovlev.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La misma sucesión que en el [problema 1079](../../1000-1099/1079/README.es.md):
a₀ = 0, a₁ = 1, a₂ᵢ = aᵢ, a₂ᵢ₊₁ = aᵢ + aᵢ₊₁. Para hasta 10 000 números
1 ≤ n < 10¹⁸ hay que imprimir el mayor aᵢ con 0 ≤ i ≤ n.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Un n por línea, terminando con 0.

## Salida

El mayor término hasta cada n.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
10
0
```

Salida:

```
3
4
```

## Solución

Un término se lee de las cifras binarias de su índice. Para un prefijo
m de cifras se guarda el par (aₘ, aₘ₊₁): una cifra 0 lo convierte en
(aₘ, aₘ + aₘ₊₁) y una cifra 1 en (aₘ + aₘ₊₁, aₘ₊₁). Ambas aplicaciones
son lineales, así que tras r cifras más la primera componente es
p·aₘ + q·aₘ₊₁ con p y q fijos.

Todo i ≤ n es o bien el propio n o coincide con n hasta alguna cifra 1
que baja a 0, con r cifras cualesquiera debajo. Así que se recorren las
cifras de n desde arriba y en cada cifra 1 se toma el mejor de todos los
finales de r cifras tras el prefijo bajado. El mejor final está entre
un máximo de ocho candidatos: cifras alternas empezando por 0 o por 1,
tal cual o con la
última cifra puesta a 1 o las dos últimas a 11 o 01. Sus (p, q) se
calculan una vez para cada r hasta 60, así que cada consulta cuesta
`O(log n)`. Los términos con índice menor que 2⁶⁰ quedan por debajo de
3·10¹², dentro de 64 bits.

Detalles a tener en cuenta:

- no bastan las cifras alternas: desde a₀, a₁ dos cifras libres dan el
  máximo con 11, no con 01 ni con 10;
- los récords crecen como números de Fibonacci y pasan de 32 bits para n
  grandes (prueba 04).

Los ocho finales se compararon con el máximo real de cada bloque de 2ʳ
índices por debajo de 2²² para r de 12 a 20, y todos los casos pequeños
probando todos los finales; las respuestas se compararon con un
recorrido directo para cada n hasta 65 536.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1396_math.cpp](1396_math.cpp) | G++ 13.2 x64 | math | O(log n) | AC | 0.001 s | 216 KB |
| [1396_math.go](1396_math.go) | Go 1.14 x64 | math | O(log n) | AC | 0.015 s | 1360 KB |
| [1396_math.java](1396_math.java) | Java 1.8 | math | O(log n) | AC | 0.109 s | 2340 KB |
| [1396_math.py](1396_math.py) | Python 3.12 x64 | math | O(log n) | AC | 0.562 s | 2252 KB |
| [1396_math.rs](1396_math.rs) | Rust 1.75 x64 | math | O(log n) | AC | 0.001 s | 764 KB |
