# 1218. Qué jedi puede ganar el torneo

[Timus 1218](https://acm.timus.ru/problem.aspx?space=1&num=1218) · dificultad 323 · graphs

Problema original de Leonid Volkov, del séptimo concurso universitario de programación de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada uno de los `N ≤ 200` jedi tiene tres parámetros, y en cada
parámetro todos los valores son distintos. De dos jedi gana el combate el
que es más fuerte en al menos dos parámetros, y el perdedor deja el
torneo. Hay que listar, en el orden de la entrada, a cada jedi para el
que algún calendario de combates deja a ese jedi como el último en pie.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y luego, para cada jedi, un nombre de hasta 30 letras y tres enteros
de valor absoluto hasta `10⁵`.

## Salida

Los posibles ganadores, uno por línea, en el orden de la entrada.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
Solo 0 0 0
Anakin 20 18 30
Luke 40 12 25
Kenobi 15 3 2
Yoda 35 9 125
```

Salida:

```
Anakin
Luke
Yoda
```

## Solución

Cada pareja tiene exactamente un ganador, así que la relación «vence a»
es un grafo de torneo. Un jedi puede ganar el torneo exactamente cuando
desde ese jedi se llega a todos los demás por cadenas de victorias.

Si se llega a todos, se toma un árbol de esas cadenas con raíz en el
candidato y se juegan los combates desde las hojas hacia arriba: cada jedi
se enfrenta al que está justo encima en el árbol, que gana ese combate, hasta que
solo queda el candidato. Si a algunos no se llega, nadie alcanzable puede
vencer a ninguno de ellos, así que el último de ellos nunca puede ser
eliminado por el lado del candidato.

Por eso se calcula el cierre transitivo de «vence a» con el algoritmo de
Warshall y se imprime cada jedi que alcanza a todos los demás. `O(N³)`.

Detalles a tener en cuenta:

- un único jedi gana por defecto;
- en un anillo de tres, cualquiera de ellos puede ganar, como muestra el
  ejemplo;
- la salida conserva el orden de la entrada, no un orden de fuerza.

Las respuestas se compararon con una solución escrita aparte en 200
torneos aleatorios y en todas las pruebas.

## Notas por lenguaje

- Python guarda cada fila del cierre como un entero grande, así que una
  fila se combina en una sola operación; los demás lenguajes usan
  matrices booleanas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1218_graphs.cpp](1218_graphs.cpp) | G++ 13.2 x64 | graphs | O(N³) | AC | 0.031 s | 424 KB |
| [1218_graphs.go](1218_graphs.go) | Go 1.14 x64 | graphs | O(N³) | AC | 0.031 s | 1188 KB |
| [1218_graphs.java](1218_graphs.java) | Java 1.8 | graphs | O(N³) | AC | 0.171 s | 2196 KB |
| [1218_graphs.py](1218_graphs.py) | Python 3.12 x64 | graphs | O(N³) | AC | 0.109 s | 520 KB |
| [1218_graphs.rs](1218_graphs.rs) | Rust 1.75 x64 | graphs | O(N³) | AC | 0.046 s | 288 KB |
