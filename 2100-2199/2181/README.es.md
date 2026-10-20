# 2181. Contar viajes de ida y vuelta en una cuadrícula sin repetir cruces

[Timus 2181](https://acm.timus.ru/problem.aspx?space=1&num=2181) · dificultad 1267 · dp, math

Problema original de Semyon Trifochkin, del Concurso Escolar de Programación de los Urales 2023.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La ciudad es una cuadrícula N × M de cruces a la que le faltan K calles
entre vecinos. La ruta de un día va de (1, 1) a (N, M) avanzando solo
hacia coordenadas mayores, luego vuelve avanzando solo hacia menores, y
ningún cruce salvo los dos extremos se visita dos veces. Contar las
rutas distintas módulo 10⁹ + 7. Los límites son 3 segundos y 256 MB.

## Entrada

N y M, 2 ≤ N, M ≤ 300, luego K, 0 ≤ K ≤ 10⁵, y K calles que faltan,
cada una como los dos cruces vecinos que unía.

## Salida

El número de rutas módulo 10⁹ + 7, o 0.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3
2
1 2 1 3
1 3 2 3
```

Salida:

```
2
```

## Solución

La vuelta, leída al revés, es otro camino monótono de (1, 1) a (N, M),
así que una ruta es un par ordenado de caminos monótonos que solo
comparten los extremos. Deben salir de (1, 1) en direcciones distintas y
entrar en (N, M) por lados distintos. El camino por (1, 2) queda por
encima del otro, así que termina por (N − 1, M), y el camino por (2, 1)
termina por (N, M − 1); las cuatro aristas de las esquinas deben
existir.

Contar pares de caminos disjuntos en vértices de A₁ = (1, 2),
A₂ = (2, 1) a B₁ = (N − 1, M), B₂ = (N, M − 1) es el lema de
Lindström–Gessel–Viennot:

det = P(A₁, B₁) · P(A₂, B₂) − P(A₁, B₂) · P(A₂, B₁),

donde P cuenta caminos monótonos. Todo par que se corta se cancela
intercambiando las colas tras el primer cruce común, lo que lo empareja
con un par que se corta del otro emparejamiento, y el emparejamiento
cruzado no puede ser disjunto en una cuadrícula plana. Dos DP sobre la
cuadrícula, una desde cada inicio, dan las cuatro cantidades.
Cualquiera de los caminos puede ser la ida, así que la respuesta es
2 · det.

En el ejemplo (1, 3) no tiene calles, así que el camino superior es
(1, 2) → (2, 2) → (2, 3), el inferior debe esquivar (2, 2) por (3, 1),
y el único par da 2 rutas.

Esto cuesta O(NM + K).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2181_dp_math.cpp](2181_dp_math.cpp) | G++ 13.2 x64 | dp, math | O(NM + K) | AC | 0.062 s | 372 KB |
| [2181_dp_math.go](2181_dp_math.go) | Go 1.14 x64 | dp, math | O(NM + K) | AC | 0.031 s | 5724 KB |
| [2181_dp_math.java](2181_dp_math.java) | Java 1.8 | dp, math | O(NM + K) | AC | 0.109 s | 608 KB |
| [2181_dp_math.py](2181_dp_math.py) | Python 3.12 x64 | dp, math | O(NM + K) | AC | 0.171 s | 25224 KB |
| [2181_dp_math.rs](2181_dp_math.rs) | Rust 1.75 x64 | dp, math | O(NM + K) | AC | 0.015 s | 2936 KB |
