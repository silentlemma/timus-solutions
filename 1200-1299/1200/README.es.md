# 1200. Cuántos cuernos y pezuñas fabricar

[Timus 1200](https://acm.timus.ru/problem.aspx?space=1&num=1200) · dificultad 256 · math

Problema original de Magaz Asanov, del Concurso por Equipos de la Universidad Estatal de los Urales, marzo de 2002.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada cuerno da `A` rublos y cada pezuña `B` rublos, con
`-10000 ≤ A, B ≤ 10000` dados con dos decimales. Se pueden vender como
mucho `K ≤ 10000` artículos en total, y los extorsionadores cobran el
cuadrado del número de artículos de cada tipo. Hay que elegir `x` cuernos
e `y` pezuñas con `x + y ≤ K` que maximicen `A·x + B·y − x² − y²`; entre
los mejores planes, el de menos cuernos y luego el de menos pezuñas.

Límite de tiempo: 0.25 segundos. Límite de memoria: 64 MB.

## Entrada

`A` y `B`, y luego `K`.

## Salida

El mayor beneficio con dos decimales y luego `x` e `y`.

## Ejemplos

### Ejemplo 1

Entrada:

```
34.20 61.70
45
```

Salida:

```
1239.50
16 29
```

## Solución

Se trabaja en kopeks para que cada beneficio sea un entero exacto:
`a·x − 100·x² + b·y − 100·y²`, con `a` y `b` los precios por 100. Se
prueba cada `x` de 0 a `K`. Con `x` fijo, la parte de las pezuñas es una
parábola cóncava en `y`, así que su mejor valor en `0..K−x` está en el
entero justo por debajo o justo por encima del vértice `b/200`, llevado al
rango; se prueban ambos y en un empate se queda el `y` menor. Recorrer `x`
hacia arriba y sustituir el mejor solo con un beneficio estrictamente
mayor da el desempate pedido. `O(K)`.

Detalles a tener en cuenta:

- con beneficios en coma flotante, dos planes iguales pueden compararse
  como distintos y desempatar mal;
- el beneficio puede llegar a `5·10⁷` rublos, `5·10⁹` kopeks, más de lo
  que cabe en enteros de 32 bits;
- si ambos precios son negativos, la respuesta es no fabricar nada, y el
  beneficio debe imprimirse como `0.00`, no `-0.00`.

Las respuestas se compararon con una búsqueda exhaustiva escrita aparte
sobre todos los planes en 400 entradas aleatorias con `K` pequeño.

## Notas por lenguaje

- Todos los lenguajes leen los precios como números en coma flotante y
  los redondean a kopeks, lo que es exacto con dos decimales en este
  rango.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1200_math.cpp](1200_math.cpp) | G++ 13.2 x64 | math | O(K) | AC | 0.015 s | 156 KB |
| [1200_math.go](1200_math.go) | Go 1.14 x64 | math | O(K) | AC | 0.031 s | 1096 KB |
| [1200_math.java](1200_math.java) | Java 1.8 | math | O(K) | AC | 0.140 s | 2096 KB |
| [1200_math.py](1200_math.py) | Python 3.12 x64 | math | O(K) | AC | 0.093 s | 488 KB |
| [1200_math.rs](1200_math.rs) | Rust 1.75 x64 | math | O(K) | AC | 0.046 s | 260 KB |
