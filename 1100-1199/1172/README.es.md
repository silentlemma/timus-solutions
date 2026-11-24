# 1172. Contar viajes circulares por tres islas solo en barco

[Timus 1172](https://acm.timus.ru/problem.aspx?space=1&num=1172) · dificultad 548 · combinatorics

Problema original de Mugurel Ionut Andreica, del Romanian Open Contest de diciembre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Tres islas tienen `N ≤ 30` ciudades cada una. Hay barcos entre cualquier
par de ciudades de islas distintas y no se puede viajar dentro de una
isla. Empezando en una ciudad dada, hay que contar los viajes circulares
que visitan cada otra ciudad exactamente una vez y vuelven; un viaje y el
mismo leído al revés cuentan como uno.

Límite de tiempo: 1 segundo. Límite de memoria: 16 MB.

## Entrada

`N`.

## Salida

El número de viajes, con hasta 121 dígitos.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
```

Salida:

```
16
```

## Solución

Se separa un viaje en su patrón de islas y la elección de ciudades. El
patrón es una secuencia cíclica de `3N` etiquetas de isla, que empieza en
la isla del turista, con `N` de cada etiqueta y sin dos vecinas iguales,
incluidas la última y la primera. Para un patrón fijo, las otras `N − 1`
ciudades de la isla de origen llenan sus huecos de `(N − 1)!` maneras y
cada una de las otras islas de `N!` maneras. Leer un viaje al revés da
otra secuencia desde el mismo inicio (el viaje tiene al menos tres
ciudades), así que el total se divide entre dos.

Los patrones se cuentan con `ways[a][b][c][i]`: secuencias que empiezan en
la isla 0, usan `a`, `b` y `c` huecos de las tres islas y terminan en la
isla `i`. Cada valor es la suma de dos valores con un hueco menos de la
isla `i` que terminan en otra isla. La respuesta cuenta las secuencias
completas que no terminan en la isla 0. Solo se guardan dos planos de `a`
fijo, así que hay pocos números grandes a la vez. `O(N³)`
sumas de números grandes.

Detalles a tener en cuenta:

- el ciclo también prohíbe que la última ciudad esté en la isla de
  origen;
- la ciudad inicial está fija, así que la isla de origen aporta
  `(N − 1)!`, no `N!`;
- la tabla completa para `N = 30` tendría unos 90 000 números grandes,
  y dos planos solo necesitan unos 6 000.

Las respuestas se compararon con una fuerza bruta sobre todos los órdenes
para `N ≤ 3` y con una solución escrita aparte para todo `N` hasta 30.

La versión didáctica en Python construye los patrones una posición a la vez. Un diccionario cuenta los prefijos según las tres cantidades usadas y la última isla. Para extender un prefijo se elige otra isla con un hueco libre y se suma su cuenta a la siguiente capa. Solo se guardan la longitud actual y la siguiente. Al completar el patrón se descartan los finales en la isla inicial, se asignan las ciudades y se divide por dos. Las tres cantidades suman la longitud, así que hay O(N²) estados por capa, O(N³) sumas de enteros grandes y O(N²) contadores.

## Soluciones optimizadas

Go mantiene la DP de dos planos, pero guarda cada conteo en tres dígitos de base 10⁹ en vez de asignar objetos math/big por celda. Fijada la isla inicial, como máximo 90 posiciones producen a lo sumo 2⁸⁹ palabras de islas, menos de 10²⁷; tres dígitos bastan también para los valores intermedios. Los dos planos fijos ocupan 69192 bytes de dígitos. Las multiplicaciones factoriales finales usan catorce dígitos: 126 cifras cubren las hasta 122 anteriores a dividir entre dos. El multiplicador máximo es 30²·29, por lo que bastan productos y acarreos de 64 bits. Todo se calcula, sin tabla de respuestas. El tiempo sigue siendo O(N³) sumas de longitud fija. Se usan manejadores estándar en lugar de fmt y se conservan la base math/big y las otras cuatro versiones aceptadas.

Las implementaciones base aceptadas [1172_combinatorics.cpp](1172_combinatorics.cpp), [1172_combinatorics.java](1172_combinatorics.java), [1172_combinatorics.py](1172_combinatorics.py), [1172_combinatorics.rs](1172_combinatorics.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Python, Go y Java usan sus enteros grandes; C++ y Rust guardan los
  números como arreglos de dígitos en base 10⁹ con suma, multiplicación
  por un número pequeño y división entre dos.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1172_combinatorics.cpp](1172_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N³) big additions | AC | 0.015 s | 376 KB | 11283141 |
| [1172_combinatorics.go](1172_combinatorics.go) | Go 1.14 x64 | combinatorics | O(N³) big additions | AC | 0.015 s | 6024 KB | 11283143 |
| [1172_combinatorics.java](1172_combinatorics.java) | Java 1.8 | combinatorics | O(N³) big additions | AC | 0.125 s | 4580 KB | 11283148 |
| [1172_combinatorics.py](1172_combinatorics.py) \* | Python 3.12 x64 | combinatorics | O(N³) big additions | AC | 0.093 s | 884 KB | 11283145 |
| [1172_combinatorics.rs](1172_combinatorics.rs) | Rust 1.75 x64 | combinatorics | O(N³) big additions | AC | 0.031 s | 568 KB | 11283151 |
| [1172_dp.py](1172_dp.py) | Python 3.12 x64 | dp | O(N³) big additions | AC | 0.14 s | 920 KB | 11315936 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1172_combinatorics_optimized.go](1172_combinatorics_optimized.go) | Go 1.14 x64 | combinatorics | O(N³) big additions | AC | 0.015 s | 404 KB | 11314877 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
