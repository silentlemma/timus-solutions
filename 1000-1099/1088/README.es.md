# 1088. La distancia entre dos bifurcaciones de un árbol binario de caminos

[Timus 1088](https://acm.timus.ru/problem.aspx?space=1&num=1088) · dificultad 751 · trees

Problema original de Oleg Kats, de la Tercera Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 4 de marzo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Desde la primera piedra el camino se bifurca a izquierda y derecha cada
hora, y tras `F` horas cada rama llega a un muelle en el mar. Los muelles
se numeran de modo que girando siempre a la derecha se llega al muelle 1,
girando a la izquierda solo en la última bifurcación al muelle 2,
girando a la izquierda solo en la penúltima al muelle 3, y así
sucesivamente. Iliá está en la bifurcación a `E` horas del mar camino del
muelle `Ep`; la piedra mágica es la bifurcación a `D` horas del mar camino
del muelle `Dp`. Su caballo puede cabalgar como mucho `H` horas, una hora
por tramo. ¿Puede Iliá llegar a la piedra mágica?
(`0 ≤ D, E, F, H ≤ 30`, `1 ≤ Dp, Ep ≤ 2^30`.)

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`D`, `E`, `F`, `Dp`, `Ep` y `H`.

## Salida

`YES` o `NO`.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 2 3 2 6 4
```

Salida:

```
YES
```

## Solución

Los caminos forman un árbol binario completo de profundidad `F`. La
numeración dice que `p − 1`, escrito con `F` cifras binarias, es el
camino al muelle `p`: la cifra más alta es la primera bifurcación, y 1
significa girar a la izquierda. Una bifurcación a `k` horas del mar camino
del muelle `p` es el mismo camino sin sus últimos `k` giros: el número
`(p − 1) >> k` a profundidad `F − k`.

Así que Iliá es el nodo `a = (Ep − 1) >> E` a profundidad `F − E`, y la
piedra es `b = (Dp − 1) >> D` a profundidad `F − D`. Se sube el más
profundo hasta la profundidad del otro con desplazamientos a la derecha,
una hora cada uno, y luego se suben los dos juntos, dos horas por paso,
hasta que los números coinciden: esa es su bifurcación común más baja. Se
comparan las horas con `H`. `O(F)`.

Detalles a tener en cuenta:

- los muelles se cuentan desde 1, así que el camino es `p − 1`, no `p`;
- las dos bifurcaciones pueden estar a profundidades distintas, y una
  puede ser antepasada de la otra;
- los números llegan a `2^30`, que cabe en enteros con signo de 32 bits,
  pero las soluciones usan 64 bits para que `p − 1` y los desplazamientos
  sean sencillos.

Las respuestas se comprobaron escribiendo ambos caminos como cadenas de
giros y contando los tramos a través de su prefijo común más largo.

## Notas por lenguaje

- Rust desestructura los seis números con un patrón de corte y
  `let else`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1088_trees.cpp](1088_trees.cpp) | G++ 13.2 x64 | trees | O(F) | AC | 0.015 s | 376 KB |
| [1088_trees.go](1088_trees.go) | Go 1.14 x64 | trees | O(F) | AC | 0.031 s | 1076 KB |
| [1088_trees.java](1088_trees.java) | Java 1.8 | trees | O(F) | AC | 0.109 s | 1604 KB |
| [1088_trees.py](1088_trees.py) | Python 3.12 x64 | trees | O(F) | AC | 0.093 s | 388 KB |
| [1088_trees.rs](1088_trees.rs) | Rust 1.75 x64 | trees | O(F) | AC | 0.031 s | 220 KB |
