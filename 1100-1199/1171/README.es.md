# 1171. El descenso por una estación espacial con más comida por día

[Timus 1171](https://acm.timus.ru/problem.aspx?space=1&num=1171) · dificultad 1265 · dp

Problema original de Mugurel Ionut Andreica, del Romanian Open Contest de diciembre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una estación tiene `N ≤ 16` niveles, cada uno una cuadrícula de `4×4`
salas con comida de 1 a 255, y algunas salas tienen una puerta a la misma
sala un nivel más abajo. Empezando en una sala dada del nivel superior, un
astronauta da un paso al día (norte, este, sur, oeste, o abajo por una
puerta), nunca entra dos veces en una sala ni sube, y debe terminar en el
nivel 1. Cada sala visitada le da su comida. Hay que maximizar la comida
reunida dividida por el número de días, que es el número de salas
visitadas, e imprimir ese recorrido.

Límite de tiempo: 1 segundo. Límite de memoria: 4 MB.

## Entrada

`N`, luego para cada nivel desde arriba cuatro filas de comida y cuatro
filas de puertas, y luego la fila y la columna de la sala inicial.

## Salida

La mejor razón con cuatro decimales, el número de movimientos y, si los
hay, los movimientos con las letras `N`, `E`, `S`, `W` y `D`.

## Evaluación

Se acepta cualquier recorrido válido que termine en el nivel 1 y alcance
la mejor razón; el comprobador reproduce los movimientos.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
1 20 1 1
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
0 0 0 0
0 0 0 0
0 0 0 0
1 1 1 1
20 1 1 1
1 1 1 1
1 1 1 1
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1 1
```

Salida:

```
8.6000
4
EDSW
```

## Solución

Dentro de un nivel el recorrido es un camino simple de la cuadrícula
`4×4`, y solo hay 28 512. Para cada nivel, un recorrido en profundidad
por todos ellos anota `best[s][e][k]`, la mayor comida en un camino de `k`
salas de `s` a `e`.

La razón se maximiza con el método de Dinkelbach. Para la razón actual
`num/den`, se busca el recorrido con el mayor `den·comida − num·salas`.
Es una programación dinámica sencilla desde el nivel inferior: el valor de
entrar en un nivel por la sala `s` es el mejor, sobre sus salidas `e`
(puertas, o cualquier sala en el nivel 1) y longitudes `k`, de
`den·best[s][e][k] − num·k` más el valor de entrar en el siguiente nivel
por `e`. Si el mejor recorrido puntúa por encima de cero, su propia razón
es mayor y pasa a ser el nuevo `num/den`; cuando nada puntúa por encima
de cero, la razón es óptima. Todo es aritmética entera, así que la parada
es exacta. Cada ronda cuesta `O(N·16³)`, y las rondas son pocas.

Al final se reconstruye el recorrido: en cada nivel, un segundo recorrido
busca un camino de su inicio a su final con la longitud y la comida
anotadas.

Detalles a tener en cuenta:

- el recorrido debe llegar al nivel 1, así que en los niveles superiores
  el camino de un nivel solo puede acabar en salas con puerta, y en el
  nivel 1 en cualquiera;
- los días son las salas visitadas, uno más que los movimientos, y con un
  solo nivel y una sala inicial rica puede no haber ningún movimiento;
- el límite de memoria es de 4 MB, así que no se guardan los caminos, solo
  la mayor comida por inicio, final y longitud.

Las razones se compararon con una solución escrita aparte en 300
estaciones aleatorias de 1 a 16 niveles, y cada recorrido impreso pasó el
comprobador.

## Notas por lenguaje

- Todos los lenguajes hacen los mismos recorridos y las mismas rondas de
  Dinkelbach.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1171_dp.cpp](1171_dp.cpp) | G++ 13.2 x64 | dp | O(N·16³) per round | AC | 0.031 s | 492 KB |
| [1171_dp.go](1171_dp.go) | Go 1.14 x64 | dp | O(N·16³) per round | AC | 0.046 s | 1732 KB |
| [1171_dp.java](1171_dp.java) | Java 1.8 | dp | O(N·16³) per round | AC | 0.140 s | 1612 KB |
| [1171_dp.py](1171_dp.py) | Python 3.12 x64 | dp | O(N·16³) per round | AC | 0.453 s | 2420 KB |
| [1171_dp.rs](1171_dp.rs) | Rust 1.75 x64 | dp | O(N·16³) per round | AC | 0.031 s | 648 KB |
