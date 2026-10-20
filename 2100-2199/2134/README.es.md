# 2134. Sellar un documento hasta que k casillas se pinten dos veces

[Timus 2134](https://acm.timus.ru/problem.aspx?space=1&num=2134) · dificultad 1714 · simulation

Problema original de Kirill Borozdin, del concurso «Más vale tarde que nunca».

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un sello con un patrón a × b de casillas negras se presiona q veces
sobre un documento n × m en posiciones dadas. Una casilla pintada más de
una vez queda repintada. Hallar el primer sello tras el que hay al menos
k casillas repintadas, o imprimir el documento final si eso nunca
ocurre. Los límites son 1 segundo y 256 MB.

## Entrada

n, m y k, 1 ≤ n, m ≤ 1000, 1 ≤ k ≤ 100, luego a y b, el patrón, luego q,
1 ≤ q ≤ 10⁵, y las q posiciones.

## Salida

"Wasted after stamp #s", o el documento como n líneas de "." y "#".

## Ejemplos

### Ejemplo 1

Entrada:

```
4 3 2
3 2
#.
.#
..
2
1 1
2 2
```

Salida:

```
#..
.#.
..#
...
```

### Ejemplo 2

Entrada:

```
4 3 1
3 2
#.
.#
..
2
1 1
2 2
```

Salida:

```
Wasted after stamp #2
```

## Solución

Basta con pintar cada casilla negra de cada sello, guardando para cada
casilla del documento si se pintó 0, 1 o al menos 2 veces y el número de
casillas repintadas; se para en cuanto ese número llega a k. Es lo
bastante rápido por un argumento de conteo.

Mientras el documento es legible, hay menos de k casillas en el estado
"al menos 2". Así que cada sello toca a lo sumo k − 1 de esas casillas,
y cada una de sus otras casillas pasa de 0 a 1, lo que ocurre a lo sumo
nm veces en total, o de 1 a 2, lo que ocurre menos de k veces. Por tanto
todos los sellos juntos tocan a lo sumo q(k − 1) + nm + k casillas. Una
posición usada por tercera vez puede saltarse entera: todas sus casillas
ya están repintadas. El trabajo es O(ab + nm + qk), unos 10⁷ pasos.

En los ejemplos ambos sellos pintan la casilla (2, 2). Con k = 2 se
admite una casilla repintada y se imprime el documento; con k = 1 queda
inservible tras el segundo sello.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2134_simulation.cpp](2134_simulation.cpp) | G++ 13.2 x64 | simulation | O(ab + nm + qk) | AC | 0.046 s | 6728 KB |
| [2134_simulation.go](2134_simulation.go) | Go 1.14 x64 | simulation | O(ab + nm + qk) | AC | 0.078 s | 34136 KB |
| [2134_simulation.java](2134_simulation.java) | Java 1.8 | simulation | O(ab + nm + qk) | AC | 0.125 s | 9176 KB |
| [2134_simulation.py](2134_simulation.py) | Python 3.12 x64 | simulation | O(ab + nm + qk) | AC | 0.421 s | 49268 KB |
| [2134_simulation.rs](2134_simulation.rs) | Rust 1.75 x64 | simulation | O(ab + nm + qk) | AC | 0.031 s | 11968 KB |
