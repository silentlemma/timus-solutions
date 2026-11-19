# 1353. La función milmillonaria de Vasya

[Timus 1353](https://acm.timus.ru/problem.aspx?space=1&num=1353) · dificultad 103 · dp

Problema original de Denis Musin, del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dado S, 1 ≤ S ≤ 81, hay que contar los enteros de 1 a 10⁹ cuya suma de
cifras es S.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El número S.

## Salida

La cantidad.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
1
```

Salida:

```
10
```

## Solución

Todo número menor que 10⁹ es una cadena de nueve cifras si se le añaden
ceros a la izquierda, y esos ceros no cambian la suma de cifras. Así que
se cuentan cadenas de cifras: ways[s] tras k cifras es la cantidad de
cadenas de k cifras con suma s, y cada cifra nueva d de 0 a 9 lleva
ways[s] a s + d. Tras nueve cifras, ways[S] cuenta los números de 0 a
999 999 999 con suma S. El cero tiene suma 0 y nunca se cuenta, y el
propio 10⁹, con suma de cifras 1, suma uno cuando S = 1.
`O(9 · 81 · 10)`.

Detalles a tener en cuenta:

- 10⁹ está en el rango: S = 1 da 10, no 9 (prueba 01);
- desde S = 10 una sola cifra ya no puede llevar toda la suma, y el
  conteo simple de barras y estrellas cuenta de más (prueba 07);
- los valores son simétricos, ways[s] = ways[81 − s], y el mayor es
  45 433 800 en S = 40 y 41, que cabe en 32 bits.

La misma tabla para 10⁶ en lugar de 10⁹ se comparó con contar las sumas
de cifras de todos los números hasta 10⁶.

## Soluciones optimizadas

`1353_dp_optimized.java`. Conserva el DP de nueve dígitos y añade 10^9 si S=1. Sustituye diez transiciones por suma por una ventana de diez estados previos, reutilizando dos arreglos long de S+1 celdas. Lee el único entero con un búfer de 1024 bytes en vez de Scanner. Tiempo O(9S), espacio auxiliar O(S); conserva intacto el DP sencillo. Se admite por la memoria medida de su propio Accepted, sin afirmar primer puesto.

Frente a `1353_dp.java`: tiempo 0.125 s → 0.093 s; memoria 1 576 KB → 476 KB.

`1353_dp_optimized.py`. Mantiene DP por dígitos, con suma deslizante en vez de diez adiciones por estado. Tras k dígitos guarda solo sumas hasta min(S,9k), en dos filas: O(9S) tiempo y O(S) espacio auxiliar. Hay un entero acotado de entrada. Vacía toda la salida antes de os._exit(0), que omite el cierre del intérprete; esto no garantiza aceleración algorítmica. El juez usó PyPy 3.10 y volvió a aceptar la fuente sencilla con CPython 3.12: cada medida pertenece a su fuente y runtime. Memoria 496 a 228 KB, tiempo 0.093 a 0.125 s. Conserva la sencilla y marca con asterisco la meta de clasificación pendiente.

Frente a `1353_dp.py`: tiempo 0.093 s → 0.125 s; memoria 496 KB → 228 KB.

`1353_dp_optimized.rs`. El mismo DP sustituye diez transiciones por una suma deslizante de diez estados. Dos arreglos fijos de 82 u32 cubren sumas hasta 81; visita solo sumas alcanzables por longitud. Para D=9 y M=9D, O(DM) tiempo y O(M) espacio auxiliar, constantes acotadas en esta tarea. Las cuentas no superan 10^9 cadenas y caben en u32. Entrada/salida por bytes del runtime C evita asignaciones de texto y formato de Rust. Conserva la sencilla y el extra 10^9 si S=1. La mejora medida es memoria; no deduce aceleración de otra ejecución histórica.

Frente a `1353_dp.rs`: tiempo 0.062 s → 0.062 s; memoria 216 KB → 60 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Las cinco fuentes sencillas permanecen intactas. Sus filas usan los nuevos Accepted de la fuente exacta, con ambas medidas y el ID de una misma entrega; las tablas README originales se guardan en la copia de integración. Estas comprobaciones no cuentan como optimizaciones.

`1353_dp_optimized.java`: puesto de tiempo 4/94 y de memoria 10/94 en esta muestra comparable.

`1353_dp_optimized.py`: puesto de tiempo 71/97 y de memoria 1/97 en esta muestra comparable.

`1353_dp_optimized.rs`: no hay suficientes resultados rivales comparables para acreditar un puesto; se admite por la mejora medida respecto de la fuente sencilla.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|----------|
| [1353_dp.cpp](1353_dp.cpp) | G++ 13.2 x64 | dp | O(9·81·10) | AC | 0.015 s | 184 KB | 11325593 |
| [1353_dp.go](1353_dp.go) | Go 1.14 x64 | dp | O(9·81·10) | AC | 0.031 s | 1096 KB | 11325576 |
| [1353_dp.java](1353_dp.java) | Java 1.8 | dp | O(9·81·10) | AC | 0.125 s | 1576 KB | 11325572 |
| [1353_dp.py](1353_dp.py) | Python 3.12 x64 | dp | O(9·81·10) | AC | 0.093 s | 496 KB | 11325599 |
| [1353_dp.rs](1353_dp.rs) | Rust 1.75 x64 | dp | O(9·81·10) | AC | 0.062 s | 216 KB | 11325616 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|----------|
| [1353_dp_optimized.java](1353_dp_optimized.java) \* | Java 1.8 | dp | O(9S) time; O(S) space | AC | 0.093 s | 476 KB | 11324972 |
| [1353_dp_optimized.py](1353_dp_optimized.py) \* | PyPy 3.10 x64 | dp | O(9S) time; O(S) space | AC | 0.125 s | 228 KB | 11325475 |
| [1353_dp_optimized.rs](1353_dp_optimized.rs) \* | Rust 1.75 x64 | dp | O(DM) time; O(M) space | AC | 0.062 s | 60 KB | 11325096 |


\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
