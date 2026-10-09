# 1081. La K-ésima cadena binaria sin dos unos seguidos

[Timus 1081](https://acm.timus.ru/problem.aspx?space=1&num=1081) · dificultad 269 · dp

Problema original de Emil Kelevedzhiev, del Torneo de Informática del Festival Matemático de Invierno, Varna 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Considera todas las cadenas de longitud `N` (`0 < N < 44`) formadas por 0
y 1 sin dos unos seguidos, ordenadas lexicográficamente. Imprime la
`K`-ésima (`0 < K < 10^9`), o `-1` si hay menos de `K`.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y `K`.

## Salida

La cadena, o `-1`.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 1
```

Salida:

```
000
```

## Solución

Sea `count[r]` el número de cadenas válidas de longitud `r`: una cadena
empieza o bien con 0 y cualquier resto válido, o bien con `10` y
cualquier resto válido, así que `count[r] = count[r − 1] + count[r − 2]`
con `count[0] = 1` y `count[1] = 2`, los números de Fibonacci.

La respuesta se construye de izquierda a derecha. Si el carácter anterior
es 1, este debe ser 0. Si no, las cadenas con 0 aquí van primero en el
orden, y hay `count[rest]` de ellas, donde `rest` es el número de
posiciones después de esta (el 0 no restringe el siguiente carácter). Si
`K ≤ count[rest]`, se escribe 0; si no, se resta `count[rest]` a `K` y se
escribe 1. Si desde el principio `K > count[N]`, se imprime `-1`. `O(N)`.

Detalles a tener en cuenta:

- `count[43] = 1 134 903 170` es mayor que cualquier `K`, así que para
  `N = 43` siempre hay respuesta; aun así los conteos se guardan en
  enteros de 64 bits;
- tras un 1 el siguiente carácter es forzoso y `K` no cambia;
- las cadenas se cuentan desde `K = 1`, la cadena de solo ceros.

Las respuestas se comprobaron con la lista ordenada de todas las cadenas
válidas para `N ≤ 20`, y para cadenas más largas calculando de vuelta la
posición de la respuesta con un conteo memorizado.

## Notas por lenguaje

- Python hace crecer la lista `count` con `append` hasta llegar a `N`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1081_dp.cpp](1081_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 200 KB |
| [1081_dp.go](1081_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.015 s | 1084 KB |
| [1081_dp.java](1081_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 1640 KB |
| [1081_dp.py](1081_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.093 s | 476 KB |
| [1081_dp.rs](1081_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.046 s | 216 KB |
