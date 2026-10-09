# 1029. El recorrido más barato hacia arriba en un edificio de oficinas

[Timus 1029](https://acm.timus.ru/problem.aspx?space=1&num=1029) · dificultad 354 · dp, dijkstra

Problema original del III Campeonato Universitario por Equipos de Programación de los Urales, 1999.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un edificio tiene `M` plantas (`1 ≤ M ≤ 100`) con `N` despachos cada una
(`1 ≤ N ≤ 500`); cada despacho cobra una tarifa positiva. Un recorrido
empieza en cualquier despacho de la primera planta; cada paso sube una
planta por el mismo número de despacho o va a un despacho vecino de la misma
planta. Encuentra un recorrido que termine en la planta superior y pague el
menor total de las tarifas de los despachos visitados. Cualquier despacho se
alcanza por como mucho `10^9` en total.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`M` y `N`, y luego `M` líneas de `N` tarifas: la línea `i` es la planta `i`.

## Salida

Los números de despacho en el orden del recorrido. Se acepta cualquier
recorrido de coste mínimo.

## Evaluación

El verificador reconstruye las plantas a partir de los números de despacho
—el mismo número otra vez significa subir una planta, un número que difiere
en uno es un paso por la planta— y comprueba que el recorrido empieza en la
primera planta, termina en la superior y cuesta exactamente el mínimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 3
5 1 9
9 1 1
1 9 1
```

Salida:

```
2 2 3 3
```

### Ejemplo 2

Entrada:

```
1 1
7
```

Salida:

```
1
```

## Solución

**Programación dinámica por plantas.** Sea `best[i][j]` el recorrido más
barato que termina en el despacho `j` de la planta `i`. En una planta, el
camino más barato a un despacho viene de abajo, del vecino izquierdo o del
derecho, y en una misma planta un recorrido óptimo nunca da la vuelta,
porque las tarifas son positivas. Así que cada planta lleva tres pasadas:

1. desde abajo: `best[i][j] = fee[i][j] + best[i - 1][j]` (en la primera
   planta solo `fee[0][j]`);
2. de izquierda a derecha:
   `best[i][j] = min(best[i][j], best[i][j - 1] + fee[i][j])`;
3. de derecha a izquierda:
   `best[i][j] = min(best[i][j], best[i][j + 1] + fee[i][j])`.

Se recuerda para cada despacho cuál de las tres dio su valor; desde el
despacho más barato de la planta superior se siguen esas elecciones hacia
atrás hasta la primera planta y se imprimen los despachos al revés.
`O(M·N)`.

**Camino mínimo.** Los despachos con los movimientos arriba, izquierda y
derecha forman un grafo con pesos positivos en los vértices: Dijkstra desde
todos los despachos de la primera planta a la vez da la misma respuesta en
`O(M·N log(M·N))`.

Detalles a tener en cuenta:

- el recorrido puede ir primero al despacho más barato de la primera planta,
  así que las pasadas horizontales también hacen falta en ella;
- la salida enumera todos los despachos visitados, incluidos los pasos por
  la planta;
- las sumas de tarifas pueden pasar de 32 bits en las comparaciones: usa
  enteros de 64 bits.

## Notas por lenguaje

- **C++**, **Go**, **Python**, **Java**, **Rust**: la programación dinámica.
- **C++** tiene además Dijkstra sobre la cuadrícula.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1029_dijkstra.cpp](1029_dijkstra.cpp) | G++ 13.2 x64 | dijkstra | O(M·N log(M·N)) | AC | 0.046 s | 1156 KB |
| [1029_dp.cpp](1029_dp.cpp) | G++ 13.2 x64 | dp | O(M·N) | AC | 0.046 s | 1160 KB |
| [1029_dp.go](1029_dp.go) | Go 1.14 x64 | dp | O(M·N) | AC | 0.046 s | 4596 KB |
| [1029_dp.java](1029_dp.java) | Java 1.8 | dp | O(M·N) | AC | 0.125 s | 3564 KB |
| [1029_dp.py](1029_dp.py) | Python 3.12 x64 | dp | O(M·N) | AC | 0.140 s | 6036 KB |
| [1029_dp.rs](1029_dp.rs) | Rust 1.75 x64 | dp | O(M·N) | AC | 0.046 s | 2628 KB |
