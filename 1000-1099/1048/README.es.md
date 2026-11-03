# 1048. Sumar dos números de un millón de cifras

[Timus 1048](https://acm.timus.ru/problem.aspx?space=1&num=1048) · dificultad 201 · implementation

Problema original de Stanislav Vasiliev y Alexander Klepinin, del concurso universitario de programación de la Universidad Estatal de los Urales, 25 de marzo de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos enteros positivos tienen `N` cifras cada uno (`1 ≤ N ≤ 10^6`, se
permiten ceros a la izquierda), y su suma también cabe en `N` cifras. Se
dan en columnas: la línea `i` contiene la `i`-ésima cifra de cada número.
Imprime la suma con exactamente `N` cifras.

Límite de tiempo: 2 segundos. Límite de memoria: 16 MB.

## Entrada

`N` y luego `N` líneas con dos cifras separadas por un espacio.

## Salida

Las `N` cifras de la suma en una línea.

## Evaluación

La salida se compara por tokens y contiene exactamente `N` cifras.
El candidato Python real pasó 610 sumas: 600 operandos positivos aleatorios
de hasta 300 cifras frente a suma entera de precisión arbitraria, y diez
casos analíticos de acarreo/ceros iniciales en longitudes 2, 3, 31, 1000
y 1000000. Un acarreo recorre todo el número; el otro extremo conserva
muchos ceros iniciales. Las entradas respetan la ausencia de desbordamiento;
los esperados de un millón de cifras no convierten los operandos a enteros.
Los candidatos reales Python y Rust pasaron además 14 entradas del
repositorio cada uno en Docker y obtuvieron sus propios Accepted exactos.
Las 610 comprobaciones del oráculo fueron ejecuciones Python, no 610
ejecuciones de cada lenguaje compilado.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 4
4 2
6 8
3 7
```

Salida:

```
4750
```

### Ejemplo 2

Entrada:

```
3
0 0
4 5
5 5
```

Salida:

```
100
```

## Solución

Sumamos columnas de derecha a izquierda. Con suma de cifras `s`
y acarreo entrante `c`, escribimos `(s + c) mod 10` y pasamos
`(s + c) div 10` a la izquierda. El acarreo inicial es cero; como
`0 ≤ s ≤ 18`, siempre es 0 o 1 y el valor temporal no supera 19.
Por inducción, el sufijo procesado contiene las cifras bajas exactas
de su suma y el resto se transmite por acarreo. La garantía de que
la suma cabe en `N` cifras hace que el acarreo final sea cero.
Conservamos las `N` cifras, incluidos ceros iniciales, sin añadir otra cifra.

Las bases nativas guardan sumas de columnas en bytes y reutilizan el
arreglo para salida. El último byte del búfer `N + 1` es el salto de
línea, no otra cifra inicial. La base Python legible lee toda la entrada,
quita espacios y separa dos cadenas de operandos antes del mismo recorrido
inverso. Rust base retiene toda la entrada además del arreglo de sumas/salida.
Todas usan tiempo y espacio `O(N)`; se conservan las cinco bases Accepted.

## Soluciones optimizadas

Los nuevos Python y Rust descartan la entrada al leerla y conservan
solo sumas de columnas `0..18` en un búfer de `N + 1` bytes. El recorrido
inverso las sustituye por cifras ASCII; el último byte sigue siendo un
salto de línea. No hacen falta operandos separados ni entrada completa:
de cada pareja solo importa su suma. El búfer ocupa `N + 1` bytes,
sin entorno de ejecución ni búferes de E/S. Tiempo y espacio siguen
en `O(N)`: optimización de almacenamiento y E/S de la misma suma escolar,
de ahí `_optimized`.

Python lee las líneas de parejas indicadas; Rust filtra dígitos ASCII
del flujo bloqueado después de `N`. Ambos escriben el búfer terminado
directamente, sin convertir cada millón de cifras en un gran entero.

Python exacto Accepted: 0,593 s / 1392 KB frente a 0,406 s / 10360 KB,
86,6% menos memoria pero 46,1% más tiempo registrado. Rust: 0,046 s /
1144 KB frente a 0,015 s / 10248 KB, 88,8% menos memoria y también
mayor tiempo registrado. Se admiten por memoria, no por velocidad.
Las bases legibles con menor tiempo registrado se mantienen.

## Notas por lenguaje

Instantánea del 2 de noviembre de 2026: C++ original tiene puestos
1 en tiempo y 5 en memoria frente a 234 registros filtrados de otros
autores; Java es primero en ambas frente a seis. La muestra Go está
vacía: su cobertura formal no demuestra superioridad competitiva.
Rust optimizado es primero en ambas frente a un registro. Python
optimizado tiene puestos 7 y 1 frente a ocho y conserva asterisco:
el perfil acordado exige C++ entre el 15% superior o los primeros 10
puestos en ambas métricas, y primero en ambas para las demás familias.
El ahorro de memoria Python satisface la admisión al margen de la clasificación.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1048_implementation.cpp](1048_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 1184 KB | 11278646 |
| [1048_implementation.go](1048_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.062 s | 1976 KB | 11278650 |
| [1048_implementation.java](1048_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.140 s | 2080 KB | 11278656 |
| [1048_implementation.py](1048_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.406 s | 10360 KB | 11278662 |
| [1048_implementation.rs](1048_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 10248 KB | 11278658 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1048_implementation_optimized.py](1048_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(N) | AC | 0.593 s | 1392 KB | 11308404 |
| [1048_implementation_optimized.rs](1048_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.046 s | 1144 KB | 11308405 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
