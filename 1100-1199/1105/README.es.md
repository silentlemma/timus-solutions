# 1105. Elegir intervalos de modo que exactamente uno cubra dos tercios del tiempo

[Timus 1105](https://acm.timus.ru/problem.aspx?space=1&num=1105) · dificultad 824 · greedy

Problema original de Dmitry Filimonenkov con Igor Goldberg, del Tetrahedron Team Contest, mayo de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un lapso de tiempo `[T0, T1]` está cubierto por `N < 10 000` intervalos
`[a_i, b_i]` con `T0 ≤ a_i < b_i ≤ T1`: cada instante del lapso está en
al menos uno de ellos. Elige un conjunto de intervalos tal que el tiempo
total cubierto por exactamente un intervalo elegido sea al menos
`2/3 · (T1 − T0)`. Imprime `0` si no existe tal conjunto. Todos los
tiempos son números reales.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

`T0 T1`, luego `N` y luego `N` líneas `a_i b_i`.

## Salida

El número de intervalos elegidos y luego sus números (desde 1), uno por
línea, en cualquier orden; o un único `0`.

## Evaluación

Se acepta cualquier conjunto válido. El comprobador recorre los extremos
de los intervalos elegidos, mide el tiempo cubierto por exactamente uno
de ellos y lo compara con `2/3 · (T1 − T0)` con una tolerancia de
`10^-6`.

## Ejemplos

### Ejemplo 1

Entrada:

```
0.0 20.0
7
1.0 1.5
0.0 10.0
9.0 10.0
18.0 20.0
9.0 18.0
2.72 3.14
19.0 20.0
```

Salida:

```
2
2
5
```

## Solución

La respuesta siempre existe, así que nunca se imprime `0`. Primero se
reducen los intervalos a una cadena con el recubrimiento voraz clásico:
se ordenan por inicio y, desde el punto actual, se toma siempre el
intervalo que empieza no más tarde y llega más lejos. En la cadena
resultante `I_1, …, I_m` solo se solapan los vecinos: si `I_{k+2}`
empezara antes de que acabe `I_k`, el voraz lo habría tomado en lugar de
`I_{k+1}`.

Así, cada instante del lapso está en un solo intervalo de la cadena o en
el solape de dos vecinos. Se quita uno de cada tres intervalos de la
cadena, empezando en el desplazamiento 0, 1 o 2. Un instante cubierto
por un intervalo sigue cubierto una vez en los dos desplazamientos que
conservan ese intervalo; un instante del solape de `I_k` e `I_{k+1}` queda
cubierto una vez en los dos desplazamientos que quitan uno de ellos, ya
que nunca se quitan ambos. Sumando los tres desplazamientos, cada instante
cuenta dos veces, así que el mejor conserva al menos `2/3` del lapso. Su
tiempo en solitario es `Σ |I_k| − 2 Σ solapes` sobre los intervalos
conservados y los pares de vecinos conservados. `O(N log N)`.

Detalles a tener en cuenta:

- elegir todos los intervalos puede no dar nada: dos intervalos
  idénticos que cubren todo el lapso nunca están solos;
- los vecinos de la cadena pueden solo tocarse, con un solape de longitud
  cero, que la fórmula trata con `max(0, ·)`.

Las respuestas se comprobaron con una fuerza bruta sobre todos los
subconjuntos con fracciones exactas en cientos de recubrimientos
pequeños aleatorios, que además confirmó que 2/3 siempre se alcanza, y
con el comprobador en todas las pruebas.

## Notas por lenguaje

- Las cinco soluciones leen los tiempos como double; cadenas iguales en
  la entrada dan valores iguales, así que los extremos que se tocan se
  comparan como iguales en todas partes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1105_greedy.cpp](1105_greedy.cpp) | G++ 13.2 x64 | greedy | O(N log N) | AC | 0.031 s | 424 KB |
| [1105_greedy.go](1105_greedy.go) | Go 1.14 x64 | greedy | O(N log N) | AC | 0.031 s | 1636 KB |
| [1105_greedy.java](1105_greedy.java) | Java 1.8 | greedy | O(N log N) | AC | 0.187 s | 6656 KB |
| [1105_greedy.py](1105_greedy.py) | Python 3.12 x64 | greedy | O(N log N) | AC | 0.078 s | 3296 KB |
| [1105_greedy.rs](1105_greedy.rs) | Rust 1.75 x64 | greedy | O(N log N) | AC | 0.031 s | 628 KB |
