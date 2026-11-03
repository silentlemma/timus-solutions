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

## Evaluación

Se compara la salida completa, incluidos espacios y saltos de línea.

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

## Soluciones optimizadas

Se conserva la DP de dos extremos tras ordenar por humedad y posición. Las cotas permiten empaquetar ambos campos en una clave entera cuyo orden coincide exactamente con el lexicográfico, recuperando la posición sin colisiones. Las claves primitivas sustituyen tuplas y comparadores de objetos; no cambian transiciones ni grupos de humedad igual.

- `2072_sorting_dp_optimized.cpp`: 0.031 s / 924 KB; base `2072_sorting_dp.cpp`: 0.093 s / 956 KB; cambio respecto a la base: tiempo -66.7%, memoria -3.3%.
- `2072_sorting_dp_optimized.py`: 0.328 s / 12940 KB; base `2072_sorting_dp.py`: 0.343 s / 21636 KB; cambio respecto a la base: tiempo -4.4%, memoria -40.2%.

## Notas por lenguaje

Se usa la instantánea guardada del 1–2 de noviembre de 2026. C++ exige el 15% superior o los primeros 10 puestos en tiempo y memoria; las demás familias exigen el primer puesto en ambas métricas. Los empates comparten puesto. Las muestras vacías solo acreditan cobertura formal.

- C++: base didáctica preferida `2072_sorting_dp.cpp`; versión que cubre `2072_sorting_dp_optimized.cpp`; puestos tiempo/memoria 4/2, registros de otros autores 114/114.

- Go: base didáctica preferida `2072_sorting_dp.go`; versión que cubre `2072_sorting_dp.go`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

- Java: base didáctica preferida `2072_sorting_dp.java`; versión que cubre `2072_sorting_dp.java`; puestos tiempo/memoria 1/1, registros de otros autores 6/6.

- Python/PyPy: base didáctica preferida `2072_sorting_dp.py`; versión que cubre `2072_sorting_dp_optimized.py`; puestos tiempo/memoria 3/1, registros de otros autores 11/11.

- Rust: base didáctica preferida `2072_sorting_dp.rs`; versión que cubre `2072_sorting_dp.rs`; puestos tiempo/memoria 1/1, registros de otros autores 1/1.

## Soluciones

La tabla sencilla incluye las fuentes didácticas preferidas y las alternativas Accepted conservadas. Las notas identifican la base preferida de cada familia.

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2072_sorting_dp.cpp](2072_sorting_dp.cpp) | G++ 13.2 x64 | sorting, dp | O(n log n) | AC | 0.093 s | 956 KB | 11309226 |
| [2072_sorting_dp.go](2072_sorting_dp.go) | Go 1.14 x64 | sorting, dp | O(n log n) | AC | 0.078 s | 4292 KB | 11294463 |
| [2072_sorting_dp.java](2072_sorting_dp.java) | Java 1.8 | sorting, dp | O(n log n) | AC | 0.140 s | 2072 KB | 11309227 |
| [2072_sorting_dp.py](2072_sorting_dp.py) | Python 3.12 x64 | sorting, dp | O(n log n) | AC | 0.343 s | 21636 KB | 11309228 |
| [2072_sorting_dp.rs](2072_sorting_dp.rs) | Rust 1.75 x64 | sorting, dp | O(n log n) | AC | 0.015 s | 3420 KB | 11309229 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2072_sorting_dp_optimized.cpp](2072_sorting_dp_optimized.cpp) | G++ 13.2 x64 | sorting, dp | O(N log N) | AC | 0.031 s | 924 KB | 11308423 |
| [2072_sorting_dp_optimized.py](2072_sorting_dp_optimized.py) \* | Python 3.12 x64 | sorting, dp | O(N log N) | AC | 0.328 s | 12940 KB | 11308422 |

\* Accepted; todavía no se alcanza el objetivo de clasificación. Esta versión admite mejoras.
