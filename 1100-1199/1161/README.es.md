# 1161. El resultado más ligero de fusionar criaturas con el doble de la media geométrica

[Timus 1161](https://acm.timus.ru/problem.aspx?space=1&num=1161) · dificultad 92 · greedy

Problema original de Nick Durov, de la subregión norte del concurso regional ACM ICPC del noreste de Europa 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

`N ≤ 100` criaturas tienen pesos enteros hasta 10000. Dos de ellas pueden
fusionarse en una de peso `2·√(m₁·m₂)`, y las fusiones siguen hasta que
queda una. Halla el menor peso final posible, con dos cifras decimales.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego los `N` pesos.

## Salida

El menor peso final.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
72
50
```

Salida:

```
120.00
```

### Ejemplo 2

Entrada:

```
3
72
30
50
```

Salida:

```
120.00
```

## Solución

Se fusionan primero las dos más pesadas, luego el resultado con la
siguiente más pesada, y así hasta la más ligera. En cualquier orden de
fusiones, cada peso acaba dentro de varias raíces cuadradas anidadas: un
peso fusionado `k` veces entra en el resultado como su raíz de orden
`2^k`, por constantes que solo dependen de la forma de las fusiones. El
peso final es mínimo cuando los pesos mayores pasan por más raíces, y la
cadena desde el más pesado hacia abajo hace justo eso, dando a los pesos
mayores las posiciones más profundas. Ordenar y una pasada:
`O(N log N)`.

Detalles a tener en cuenta:

- con una sola criatura, su peso es la respuesta;
- el orden importa: fusionar primero las ligeras da un resultado más
  pesado;
- el peso nunca pasa de 40000, muy dentro de la precisión de double.

Las respuestas se compararon con probar todos los órdenes de fusión en 150
colonias aleatorias de hasta siete criaturas.

## Notas por lenguaje

- Todos los lenguajes ordenan y acumulan de la misma manera.
- Java redondea el resultado mediante `BigDecimal` con empates al par,
  como `printf` en C.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1161_greedy.cpp](1161_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.015 s | 216 KB |
| [1161_greedy.go](1161_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.031 s | 1096 KB |
| [1161_greedy.java](1161_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.140 s | 1912 KB |
| [1161_greedy.py](1161_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.078 s | 364 KB |
| [1161_greedy.rs](1161_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.015 s | 248 KB |
