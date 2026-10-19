# 2110. Mayor OR tras borrar exactamente k números

[Timus 2110](https://acm.timus.ru/problem.aspx?space=1&num=2110) · dificultad 1024 · bitmask, dp, backtracking

Problema original de Alexey Danilyuk, del Campeonato Juvenil de la UrFU 2016.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Borrar exactamente k de n enteros no negativos de modo que el OR bit a
bit de los que quedan sea lo mayor posible. Cada prueba cumple k ≤ 7 o
que todos los números son a lo sumo 10⁵. Los límites son 2 segundos y
64 MB.

## Entrada

n y k, 0 ≤ k ≤ 100, k + 1 ≤ n ≤ 10⁵, y luego los n números, cada uno a
lo sumo 10⁹.

## Salida

El mayor OR.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 1
32 16 8 7
```

Salida:

```
56
```

### Ejemplo 2

Entrada:

```
4 1
98765432 98765432 98765432 1
```

Salida:

```
98765433
```

## Solución

Sea F el OR de todos los números y r = n − k cuántos se conservan. Cada
bit activo de F tiene un testigo, un número que lo contiene, así que a lo
sumo popcount(F) números ya dan F, y los demás puestos pueden llenarse
con cualquier cosa. Por tanto, si r ≥ popcount(F), la respuesta es F.

Si no, r < popcount(F) ≤ 30, y quedan dos casos pequeños.

- k ≤ 7: entonces n = r + k ≤ 36. Una búsqueda en profundidad, con los
  números ordenados de mayor a menor, elige cuáles conservar. Corta una
  rama cuando el OR actual junto con todos los números posteriores no
  puede superar el mejor resultado, y toma esa cota de inmediato cuando
  los puestos restantes bastan para elegir un testigo por cada bit que
  aún falta.
- Números a lo sumo 10⁵: entonces F < 2¹⁷, r ≤ 16 y n ≤ 116. Una mochila
  sobre máscaras OR guarda, para cada máscara, el menor número de valores
  distintos que la producen; una máscara alcanzada con a lo sumo r
  números es posible, porque los duplicados y otros números llenan los
  demás puestos sin bajar el OR. Las máscaras se recorren en orden
  decreciente para usar cada número una vez, y el bucle se detiene en
  cuanto se alcanza F.

En el segundo ejemplo todas las copias de 98765432 dan los mismos bits,
así que borrar una copia conserva el 1 y la respuesta es 98765433.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2110_bitmask_dp_backtracking.cpp](2110_bitmask_dp_backtracking.cpp) | G++ 13.2 x64 | bitmask, dp, backtracking | O(n + 2^17 n) in the worst branch | AC | 0.031 s | 936 KB |
| [2110_bitmask_dp_backtracking.go](2110_bitmask_dp_backtracking.go) | Go 1.14 x64 | bitmask, dp, backtracking | O(n + 2^17 n) in the worst branch | AC | 0.031 s | 2168 KB |
| [2110_bitmask_dp_backtracking.java](2110_bitmask_dp_backtracking.java) | Java 1.8 | bitmask, dp, backtracking | O(n + 2^17 n) in the worst branch | AC | 0.125 s | 1036 KB |
| [2110_bitmask_dp_backtracking.py](2110_bitmask_dp_backtracking.py) | Python 3.12 x64 | bitmask, dp, backtracking | O(n + 2^17 n) in the worst branch | AC | 0.781 s | 11344 KB |
| [2110_bitmask_dp_backtracking.rs](2110_bitmask_dp_backtracking.rs) | Rust 1.75 x64 | bitmask, dp, backtracking | O(n + 2^17 n) in the worst branch | AC | 0.031 s | 2148 KB |
