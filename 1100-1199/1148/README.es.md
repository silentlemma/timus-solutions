# 1148. La K-ésima torre en orden lexicográfico con niveles que difieren en un ladrillo

[Timus 1148](https://acm.timus.ru/problem.aspx?space=1&num=1148) · dificultad 1730 · dp

Problema original de Timus; no se indican autor ni fuente.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una torre tiene `H ≤ 60` niveles; el más bajo tiene `M ≤ 10` ladrillos y
cada nivel siguiente tiene exactamente un ladrillo más o uno menos que el
de abajo, nunca cero. Considera todas esas torres que usan como mucho
`N ≤ 32767` ladrillos, escritas como la lista de anchos de los niveles de
abajo arriba y ordenadas lexicográficamente. Imprime cuántas hay y luego
la torre con cada número `K` dado, contando desde 1.

Límite de tiempo: 1 segundo. Límite de memoria: 4 MB.

## Entrada

`N`, `H` y `M`, y luego números `K`, uno por línea, terminando con `-1`.

## Salida

El número de torres y luego los anchos de cada torre pedida.

## Ejemplos

### Ejemplo 1

Entrada:

```
22 5 4
1
10
-1
```

Salida:

```
10
4 3 2 1 2
4 5 4 5 4
```

## Solución

Sea `count(n, h, m)` el número de torres de `h` niveles cuyo nivel más
bajo tiene `m` ladrillos y que usan como mucho `n` ladrillos. Vale `0`
cuando `m = 0` o `m > n`, `1` cuando `h = 1`, y en otro caso

`count(n, h, m) = count(n − m, h − 1, m − 1) + count(n − m, h − 1, m + 1)`.

La respuesta a la primera pregunta es `count(N, H, M)`, como mucho
`2^59`, que cabe en 64 bits. La `K`-ésima torre se lee nivel a nivel: la
continuación más estrecha va primero en orden lexicográfico, así que si
`K` es como mucho el número de torres que siguen con `m − 1`, se toma
esa; si no, se resta ese número y se sigue con `m + 1`.

La dificultad es la memoria. Una torre de `h` niveles que empieza con `m`
nunca necesita más de `m·h + h(h − 1)/2` ladrillos, así que `n` se puede
recortar ahí, y a una altura dada solo aparecen anchos de una paridad,
dentro de `M ± (H − h)`. Aun así, una tabla completa sobre `(n, h, m)`
ocuparía decenas de megabytes. Por eso los valores se guardan solo para
una de cada cuatro alturas, unos 245 mil valores de 64 bits o 2 MB, y las
tres alturas intermedias se recalculan por recursión simple, lo que cuesta
como mucho `2⁴ = 16` consultas a la siguiente altura guardada por valor
guardado. Un valor guardado se calcula una vez, la primera vez que hace
falta.

Detalles a tener en cuenta:

- el número de torres llega a unos `4,7·10¹⁷`, así que hacen falta enteros
  de 64 bits;
- un nivel de un ladrillo no puede encogerse a cero;
- un `n` mayor que lo que podría usar cualquier torre se recorta, lo que
  mantiene la tabla pequeña y comparte los valores guardados;
- `M > N` no deja ninguna torre.

Las respuestas se compararon con un listado de todas las torres en orden
en 200 entradas aleatorias de hasta 14 niveles, y las pruebas grandes con
una reconstrucción por número que memoriza todos los estados.

## Notas por lenguaje

- Todos los lenguajes guardan la misma tabla dispersa y recurren entre
  sus capas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1148_dp.cpp](1148_dp.cpp) | G++ 13.2 x64 | dp | O(H·(M + H)·min(N, M·H + H²)) | AC | 0.015 s | 1664 KB |
| [1148_dp.go](1148_dp.go) | Go 1.14 x64 | dp | O(H·(M + H)·min(N, M·H + H²)) | AC | 0.015 s | 3020 KB |
| [1148_dp.java](1148_dp.java) | Java 1.8 | dp | O(H·(M + H)·min(N, M·H + H²)) | AC | 0.093 s | 2432 KB |
| [1148_dp.py](1148_dp.py) | Python 3.12 x64 | dp | O(H·(M + H)·min(N, M·H + H²)) | AC | 0.625 s | 2480 KB |
| [1148_dp.rs](1148_dp.rs) | Rust 1.75 x64 | dp | O(H·(M + H)·min(N, M·H + H²)) | AC | 0.015 s | 2028 KB |
