# 1267. El metro de Ekaterimburgo

[Timus 1267](https://acm.timus.ru/problem.aspx?space=1&num=1267) · dificultad 1729 · dp

Problema original de Leonid Volkov (preparado por Leonid Volkov y Alexander Somov), del Campeonato de la Universidad Estatal de los Urales, 25 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una línea de metro tiene N estaciones (1 ≤ N ≤ 16) con tiempos de viaje
entre vecinas en minutos enteros (cada uno hasta 10⁵, quizá 0). Los
trenes salen de la estación 1 hacia la N cada P minutos desde el minuto
A, y de la N hacia la 1 cada P minutos desde el minuto B (1 ≤ P ≤ 10⁵,
0 ≤ A, B ≤ P); cada tren llega al otro extremo y deja la línea. Las
paradas son instantáneas. Quien hace turismo empieza en la estación S,
sube a cualquier tren y debe bajar en cada otra estación para verla, lo
que con la subida lleva 59 segundos, así que el siguiente tren tomado en
una estación sale al menos un minuto después de la llegada. Al final se
vuelve a S. Hay que hallar el menor tiempo desde la primera subida hasta
la llegada final a S.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, luego los N − 1 tiempos de viaje, luego S, y luego P, A y B.

## Salida

La duración mínima en minutos.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
5 7
2
4 0 1
```

Salida:

```
28
```

## Solución

Tres observaciones simplifican el problema.

- La hora de inicio es libre, y cuando los primeros trenes llegan a los
  extremos el horario se repite con periodo P. Empezar un número entero
  de periodos más tarde usa los mismos trenes en los mismos momentos
  relativos, así que se puede suponer que los trenes circulan siempre:
  hacia N pasan por la estación i en los momentos A + pos(i) mod P, hacia
  1 en B + pos(N) − pos(i) mod P.
- Estar antes en una estación nunca es peor: se puede esperar cualquier
  tren posterior. Así que para cada conjunto de estaciones vistas y
  estación actual solo importa la llegada más temprana.
- Bajar en una estación ya vista nunca ayuda. Seguir desde ella en el
  mismo sentido no es mejor que quedarse en el tren, y el tren de vuelta
  pasa por la estación anterior después de que se saliera de ella, así
  que esperando allí se habría tomado.

Para cada sentido del primer tren, una DP sobre (conjunto visto,
estación) guarda la llegada más temprana. Desde cada estado se toma el
primer tren en cada sentido que sale al menos un minuto después de la
llegada y se viaja a cualquier estación no vista en su camino. Con todo
visto, se suma el viaje directo de vuelta a S. Con n = N es
`O(2ⁿ · n²)`.

Detalles a tener en cuenta:

- no se puede salir en el mismo tren en que se llegó: la siguiente
  salida es al menos un minuto después;
- los tiempos de viaje pueden ser 0, con varias estaciones en el mismo
  sitio (pruebas 05, 09);
- un viaje puede pasar por estaciones no vistas sin parar;
- con N = 1 la respuesta es 0 (prueba 02).

La DP se comparó en 400 casos pequeños (N ≤ 6, tramos y periodos
cortos) con una búsqueda sobre el horario real, con los primeros trenes,
cualquier tren inicial y bajadas en estaciones ya vistas.

## Notas por lenguaje

- Todos los lenguajes hacen la misma DP sobre un arreglo plano de
  2ⁿ · n llegadas.
- CPython necesita unos 1,3 s en las pruebas más grandes, más que el
  límite, así que la solución en Python se envía con PyPy 3.10.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1267_dp.cpp](1267_dp.cpp) | G++ 13.2 x64 | dp | O(2ⁿ · n²) | AC | 0.093 s | 7948 KB |
| [1267_dp.go](1267_dp.go) | Go 1.14 x64 | dp | O(2ⁿ · n²) | AC | 0.109 s | 10036 KB |
| [1267_dp.java](1267_dp.java) | Java 1.8 | dp | O(2ⁿ · n²) | AC | 0.218 s | 8768 KB |
| [1267_dp.py](1267_dp.py) | PyPy 3.10 x64 | dp | O(2ⁿ · n²) | AC | 0.312 s | 27088 KB |
| [1267_dp.rs](1267_dp.rs) | Rust 1.75 x64 | dp | O(2ⁿ · n²) | AC | 0.062 s | 8284 KB |
