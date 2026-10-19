# 1833. Esperanzas del piragüismo

[Timus 1833](https://acm.timus.ru/problem.aspx?space=1&num=1833) · dificultad 2007 · matching

Problema original de Alexander Ipatov (preparado por Evgeny Kurpilyansky), del XV Campeonato Abierto de los Urales de Programación Competitiva, abril de 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n piragüistas formaron m tripulaciones de dos que ganaron premios.
Pagar a cada piragüista una prima no negativa para que los dos miembros
de cada tripulación premiada reciban juntos al menos k, gastando en
total lo menos posible.

## Entrada

n, k, m (2 ≤ n ≤ 500, 1 ≤ k ≤ 10000, 0 ≤ m ≤ 100000), luego m
tripulaciones como pares de piragüistas distintos, cada una una vez.

## Salida

La prima de cada piragüista, con error absoluto de como mucho 10⁻⁶. Se
acepta cualquier pago óptimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 1000 4
1 2
1 3
2 4
3 4
```

Salida:

```
146.5
853.5
853.5
146.5
```

## Solución

Es la relajación lineal de la cobertura de vértices: minimizar Σxᵥ con
xᵤ + xᵥ ≥ k en cada tripulación. Siempre tiene un óptimo
semientero, y se halla con el grafo duplicado: una copia izquierda y
otra derecha de cada piragüista, y por cada tripulación se une u a la
izquierda con v a la derecha, y v a la izquierda con u a la derecha.
Una cobertura de vértices mínima C de este grafo bipartito da
xᵥ = k/2 por cada copia de v en C. Cada tripulación queda cubierta dos
veces en el grafo duplicado, así que recibe al menos k, y el total
k·|C|/2 es óptimo porque cualquier solución fraccionaria, dividida por
k y copiada a ambos lados, es una cobertura fraccionaria del grafo
bipartito, cuyo óptimo es el entero |C|.

Por el teorema de König, C sale de un emparejamiento máximo: se buscan
caminos alternantes desde las copias izquierdas libres; las copias
izquierdas no alcanzadas y las derechas alcanzadas forman C. El
emparejamiento cuesta `O(n·m)` con los caminos de aumento de Kuhn, y
Python usa Hopcroft–Karp.

En el ejemplo las tripulaciones forman el ciclo 1–2–4–3–1, un ciclo
par, y la cobertura da 500 a cada piragüista: 2000 en total, lo mismo
que la respuesta del ejemplo 146.5 + 853.5 + 853.5 + 146.5.

Trampas:

- pagar solo 0 o k sale más caro: en un triángulo tres mitades, 1.5k
  en total, superan a dos k enteros;
- los piragüistas sin tripulación reciben 0;
- hay muchos pagos óptimos, así que la respuesta se comprueba por su
  total y por las tripulaciones.

Todas las respuestas tienen el menor total hallado probando todos los
pagos con valores 0, k/2 y k para hasta 9 piragüistas, y coinciden en
total con una implementación aceptada independiente en las pruebas
grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1833_matching.cpp](1833_matching.cpp) | G++ 13.2 x64 | matching | O(n m) | AC | 0.093 s | 1364 KB |
| [1833_matching.go](1833_matching.go) | Go 1.14 x64 | matching | O(n m) | AC | 0.140 s | 6008 KB |
| [1833_matching.java](1833_matching.java) | Java 1.8 | matching | O(n m) | AC | 0.218 s | 7396 KB |
| [1833_matching.py](1833_matching.py) | Python 3.12 x64 | matching | O(n m) | AC | 0.218 s | 17380 KB |
| [1833_matching.rs](1833_matching.rs) | Rust 1.75 x64 | matching | O(n m) | AC | 0.046 s | 4260 KB |
