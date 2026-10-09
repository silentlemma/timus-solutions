# 1051. Un solitario de saltos en una cuadrícula infinita

[Timus 1051](https://acm.timus.ru/problem.aspx?space=1&num=1051) · dificultad 534 · games, math

Problema original de Stanislav Vasiliev, del concurso universitario de programación de la Universidad Estatal de los Urales, 25 de marzo de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un rectángulo de `M × N` piedras (`1 ≤ M, N ≤ 10000`) está sobre los nodos
de una cuadrícula infinita. Un movimiento: una piedra salta sobre una
vecina horizontal o vertical hasta el nodo vacío de detrás, y la piedra
saltada se retira. Halla el menor número de piedras que pueden quedar.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`M` y `N`.

## Salida

El menor número de piedras restantes.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 4
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
1 7
```

Salida:

```
4
```

## Solución

La respuesta solo depende de la forma:

```text
min(M, N) = 1                           ->  ceil(max(M, N) / 2)
si no, M o N divisible entre 3          ->  2
si no                                   ->  1
```

**Por qué no 1 cuando un lado es divisible entre 3.** Se colorea el nodo
`(x, y)` con `(x + y) mod 3`. Tres nodos consecutivos de una fila o
columna tienen tres colores distintos, y un salto vacía dos de ellos y
ocupa el tercero: cada recuento cambia en uno, así que las paridades de
los tres recuentos cambian a la vez, y si son iguales o no nunca cambia.
Un rectángulo con un lado divisible entre 3 tiene recuentos iguales de los
tres colores (todos con la misma paridad); una sola piedra tiene recuentos
`1, 0, 0`, que no lo son. Así que quedan al menos dos piedras, y dos se
pueden alcanzar.

**El resto de casos en dos dimensiones.** Las piedras se pueden quitar de
tres en tres en fila con ayuda de una piedra vecina, lo que reduce el
rectángulo lado a lado hasta unos pocos casos pequeños; todos terminan con
una piedra.

**Una fila.** Un salto toma dos vecinas y deja una piedra dos casillas más
allá en la línea, y en una sola línea las piedras no se pueden volver a
juntar, así que cada piedra participa en como mucho un salto: quedan al
menos `ceil(n / 2)` piedras, y saltando por parejas desde los extremos se
consigue.

La fórmula también se comprobó con una búsqueda exhaustiva de todas las
posiciones (salvo traslación) para todos los tableros hasta `3 × 4`,
`2 × 7` y `4 × 4`. `O(1)`.

Detalles a tener en cuenta:

- una fila es distinta: `1 × 7` deja 4, no 1;
- `2 × 3` deja 2, mientras que `2 × 4` deja 1;
- `M` y `N` pueden venir en cualquier orden.

## Notas por lenguaje

- Todos los lenguajes evalúan la misma fórmula.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1051_games_math.cpp](1051_games_math.cpp) | G++ 13.2 x64 | games, math | O(1) | AC | 0.015 s | 128 KB |
| [1051_games_math.go](1051_games_math.go) | Go 1.14 x64 | games, math | O(1) | AC | 0.015 s | 1068 KB |
| [1051_games_math.java](1051_games_math.java) | Java 1.8 | games, math | O(1) | AC | 0.125 s | 1632 KB |
| [1051_games_math.py](1051_games_math.py) | Python 3.12 x64 | games, math | O(1) | AC | 0.078 s | 328 KB |
| [1051_games_math.rs](1051_games_math.rs) | Rust 1.75 x64 | games, math | O(1) | AC | 0.031 s | 224 KB |
