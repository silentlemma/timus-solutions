# 1763. La pulga erudita

[Timus 1763](https://acm.timus.ru/problem.aspx?space=1&num=1763) · dificultad 5379 · math

Problema original de Igor Chevdar, del XIV Campeonato de los Urales de Programación Competitiva, 10 de abril de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una mesa redonda está dividida en n sectores numerados en sentido
horario. Empezando en el sector 1, un caminante pasa a un sector vecino
o salta por encima de dos sectores, es decir, del sector i a i ± 1 o
i ± 3 alrededor del círculo. Contar los recorridos que visitan cada
sector exactamente una vez y vuelven al sector 1, módulo 10⁹ + 9.

## Entrada

n (6 ≤ n ≤ 10⁹).

## Salida

El número de recorridos módulo 10⁹ + 9.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
```

Salida:

```
12
```

## Solución

Los recorridos son los ciclos hamiltonianos del círculo con cuerdas de
longitud 3, cada uno contado en ambos sentidos. Se pueden contar sector
a sector: al decidir las aristas de cada sector hacia delante, a i + 1
e i + 3, solo siguen abiertos los últimos sectores y los tres primeros,
que reciben sus aristas de vuelta al final. Un estado guarda el grado
de cada sector abierto y qué extremos abiertos pertenecen al mismo
camino, y el ciclo solo puede cerrarse con la última arista. Así hay un
conjunto finito de estados con transiciones fijas, de modo que los
recuentos cumplen una recurrencia lineal.

La recurrencia se halló con el método de Berlekamp–Massey a partir de
los recuentos para 7 a 200 sectores hechos con esa búsqueda: tiene
orden 19, es la misma con 40 o con 195 términos y reproduce todos los
recuentos hasta 200. La búsqueda misma coincide con una búsqueda simple
de todos los recorridos hasta 33 sectores. Con seis sectores los saltos
de +3 y −3 caen en el mismo sector, así que 6 se responde aparte.

Para n grande se reduce x^(n − 7) módulo el polinomio característico de
la recurrencia por cuadrados sucesivos, y los coeficientes resultantes
combinan los 19 primeros recuentos. `O(k² log n)` con k = 19.

Con seis sectores hay 12 recorridos: 6 ciclos sin orientación, cada uno
en ambos sentidos.

Trampas:

- con seis sectores los movimientos +3 y −3 coinciden, lo que rompe el
  patrón de las demás mesas;
- algunos coeficientes son negativos y hay que devolverlos al rango;
- el recuento no es monótono: 9 sectores dan 110 recorridos, menos que
  8.

Las respuestas coinciden con los recuentos de la búsqueda para todas
las mesas de hasta 200 sectores y con una implementación aceptada
independiente en 80 mesas aleatorias de hasta 10⁹ sectores.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1763_math.cpp](1763_math.cpp) | G++ 13.2 x64 | math | O(k^2 log n), k = 19 | AC | 0.015 s | 380 KB |
| [1763_math.go](1763_math.go) | Go 1.14 x64 | math | O(k^2 log n), k = 19 | AC | 0.031 s | 1092 KB |
| [1763_math.java](1763_math.java) | Java 1.8 | math | O(k^2 log n), k = 19 | AC | 0.125 s | 1652 KB |
| [1763_math.py](1763_math.py) | Python 3.12 x64 | math | O(k^2 log n), k = 19 | AC | 0.093 s | 560 KB |
| [1763_math.rs](1763_math.rs) | Rust 1.75 x64 | math | O(k^2 log n), k = 19 | AC | 0.031 s | 244 KB |
