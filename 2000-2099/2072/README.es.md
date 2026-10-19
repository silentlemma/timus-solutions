# 2072. Regar por humedad, terminando cada grupo en un extremo

[Timus 2072](https://acm.timus.ru/problem.aspx?space=1&num=2072) · dificultad 206 · sorting, dp

Problema original de Ilya Kuchumov, del Concurso Regional por Equipos de Programación de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n flores están en fila, a un paso unas de otras, cada una con su
humedad. Un jardinero empieza junto a la flor de más a la izquierda y
debe regarlas todas en orden de humedad no decreciente; las flores de
igual humedad pueden ir en cualquier orden. Regar una flor y dar un
paso hasta una vecina cuestan un minuto cada uno. Hallar el menor tiempo
total. Los límites son 2 segundos y 64 MB.

## Entrada

n, 1 ≤ n ≤ 10⁵, y después las n humedades de izquierda a derecha, cada
una de 1 a 10⁹.

## Salida

El menor tiempo total en minutos.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
3 2 5 6 2 5
```

Salida:

```
21
```

## Solución

Regar siempre cuesta n minutos, así que solo importa caminar. Se ordenan
las flores por humedad y se dividen en grupos de igual humedad; los
grupos se hacen uno tras otro. Dentro de un grupo el jardinero debe
pasar por cada flor entre su posición más a la izquierda l y la más a la
derecha r, así que el camino cubre todo el segmento [l; r], y lo mejor
es ir a un extremo y barrer hasta el otro. Termina en l o en r, y nada
más del pasado importa para el grupo siguiente.

Por eso se guardan dos valores por grupo: el menor tiempo para
terminarlo en l y en r. Desde la posición p, terminar en l cuesta
|p − r| + (r − l) (primero se va a r), y terminar en r cuesta
|p − l| + (r − l). Cada uno se minimiza sobre los dos extremos posibles
del grupo anterior; antes del primer grupo el jardinero está en la
posición 1. La respuesta es el menor valor final más n. Domina la
ordenación: O(n log n).

En el ejemplo los grupos son {2, 5}, {1}, {3, 6} y {4} (humedad 2, 3,
5 y 6), y el mejor camino da 15 pasos, más 6 riegos: 21.

## Notas por lenguaje

El total puede superar 2³¹ (hasta unos 10¹⁰), así que C++, Go, Java y Rust
usan enteros de 64 bits. Java ordena la humedad y la posición empaquetadas en un long.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2072_sorting_dp.cpp](2072_sorting_dp.cpp) | G++ 13.2 x64 | sorting, dp | O(n log n) | AC | 0.078 s | 980 KB |
| [2072_sorting_dp.go](2072_sorting_dp.go) | Go 1.14 x64 | sorting, dp | O(n log n) | AC | 0.078 s | 4292 KB |
| [2072_sorting_dp.java](2072_sorting_dp.java) | Java 1.8 | sorting, dp | O(n log n) | AC | 0.125 s | 2132 KB |
| [2072_sorting_dp.py](2072_sorting_dp.py) | Python 3.12 x64 | sorting, dp | O(n log n) | AC | 0.312 s | 22588 KB |
| [2072_sorting_dp.rs](2072_sorting_dp.rs) | Rust 1.75 x64 | sorting, dp | O(n log n) | AC | 0.031 s | 3424 KB |
