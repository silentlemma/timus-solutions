# 2187. Cortar un camino de grado creciente en viajes pagados

[Timus 2187](https://acm.timus.ru/problem.aspx?space=1&num=2187) · dificultad 1357 · dp, graphs

Problema original de Artyom Abaturov, del Concurso Escolar de Programación de los Urales 2024.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un grafo simple tiene n islas con aᵢ monedas y m aristas. Un viaje es un
camino por aristas donde cada isla siguiente tiene grado estrictamente
mayor; un viaje de longitud i cuesta bᵢ, y solo la isla donde termina da
sus monedas. Empezando en la isla 1 con a₁ monedas, se puede hacer
cualquier número de viajes seguidos, cada uno desde donde terminó el
anterior. Hallar cuántas monedas se pueden conservar como máximo. Los
límites son 1 segundo y 256 MB.

## Entrada

n y m, 2 ≤ n ≤ 10⁵, 1 ≤ m ≤ 10⁵, luego a₁ … a_n y b₁ … b_{n−1}, todos
entre 1 y 10⁹, y luego las m aristas.

## Salida

El mayor total.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 10
5 6 8 2 5 7
3 5 2 4 6
1 2
1 3
1 4
2 3
2 4
2 5
3 4
3 6
4 5
4 6
```

Salida:

```
10
```

## Solución

Los grados siguen creciendo de un viaje al siguiente, así que todos los
viajes juntos forman un único camino de grado creciente desde la isla
1, cortado en las islas donde se toman las monedas. Orientar cada arista
hacia el grado mayor da un DAG, y los grados en un camino de longitud L
son números distintos de suma a lo sumo 2m, así que L es O(√m).

Sea f(v) el mejor total cuando el último viaje termina en v. Recorriendo
las islas por grado, cada isla v guarda una fila cuya entrada L es el
mejor f(u) entre las islas u con un camino de exactamente L aristas
hasta v; la fila se forma con las filas de sus predecesores desplazadas
en uno. Entonces

f(v) = aᵥ + máx sobre L ≥ 1 de (row[L] − b_L),

f(1) = a₁, y la respuesta es el mayor f. Solo participan las islas
alcanzables desde 1.

Las soluciones compiladas empujan cada fila por las aristas salientes.
La versión en Python ahorra tiempo dos veces: cada isla empieza con una
copia de su fila entrante más larga y solo mezcla en ella las demás, y
la misma DP también puede correr hacia atrás desde los finales de los
caminos con las aristas invertidas, así que se elige la dirección cuyas
filas suman menos trabajo.

En el ejemplo un viaje de longitud 1 a la isla 3 da 5 + 8 − 3 = 10.

Cada arista mezcla una fila de longitud O(√m), así que la DP tarda
O(m √m). Leer e inicializar la entrada requiere O(n + m), y las soluciones
compiladas ordenan los vértices por conteo, para un tiempo total de
O(n + m √m). Python usa ordenación por comparaciones, para un total de
O(n log n + m √m). Una trampa ilustrada por el test 03: las islas aisladas
o inalcanzables también deben leerse e inicializarse; n no tiene por qué
ser O(m).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2187_dp_graphs.cpp](2187_dp_graphs.cpp) | G++ 13.2 x64 | dp, graphs | O(n + m √m) | AC | 0.078 s | 6724 KB |
| [2187_dp_graphs.go](2187_dp_graphs.go) | Go 1.14 x64 | dp, graphs | O(n + m √m) | AC | 0.078 s | 17156 KB |
| [2187_dp_graphs.java](2187_dp_graphs.java) | Java 1.8 | dp, graphs | O(n + m √m) | AC | 0.234 s | 9912 KB |
| [2187_dp_graphs.py](2187_dp_graphs.py) | PyPy 3.10 x64 | dp, graphs | O(n log n + m √m) | AC | 0.343 s | 55364 KB |
| [2187_dp_graphs.rs](2187_dp_graphs.rs) | Rust 1.75 x64 | dp, graphs | O(n + m √m) | AC | 0.062 s | 15008 KB |
