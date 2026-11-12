# 1019. El intervalo blanco más largo tras repintar una recta

[Timus 1019](https://acm.timus.ru/problem.aspx?space=1&num=1019) · dificultad 465 · sorting, dsu

Problema original del Ural State University Internal Contest '99 #2.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El segmento `[0, 10^9]` de la recta numérica es blanco. Luego se aplican en
orden `N` repintados (`1 ≤ N ≤ 5000`): el `i`-ésimo pinta el segmento de
`a_i` a `b_i` (`0 < a_i < b_i < 10^9`, enteros) de blanco o de negro.
Encuentra el intervalo blanco más largo del resultado; entre intervalos de
igual longitud, el de más a la izquierda.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas `a b c`, donde `c` es `w` (blanco) o `b` (negro).

## Salida

Los extremos `x y` (`x < y`) del intervalo blanco más largo.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
2 999999998 b
100 500 w
500 900 w
300 310 b
```

Salida:

```
310 900
```

### Ejemplo 2

Entrada:

```
1
1 999999999 w
```

Salida:

```
0 1000000000
```

## Solución

Se reúnen 0, 10⁹ y todos los extremos, se ordenan y eliminan duplicados. Cada tramo entre coordenadas consecutivas tiene color uniforme. Se pintan los tramos en orden y después se unen los blancos contiguos al recorrerlos de izquierda a derecha. Se comparan longitudes reales, no cantidades de tramos, y solo se actualiza ante una mejora estricta para mantener el empate más a la izquierda. Hay hasta 2N+1 tramos: ordenar cuesta O(N log N), pintar O(N²), y el espacio es O(N). Con N ≤ 5000 son como máximo 50005000 asignaciones. Python usa rebanadas bytearray cuya copia interna es nativa; así el algoritmo sencillo pasa en los cinco lenguajes. Se unen los blancos que se tocan y se incluyen 0 y 10⁹. El prefijo intacto [0,min a) garantiza una respuesta blanca.

## Soluciones optimizadas

Las variantes DSU procesan los repintados al revés. Una estructura de sucesores encuentra el primer tramo aún no asignado por una operación posterior; tras pintarlo lo enlaza al siguiente. Cada tramo se pinta una sola vez. Ordenar y buscar extremos cuesta O(N log N), con O(N) de espacio. Go Accepted usa 592 KB y 0.031 s, frente a 1784 KB y 0.031 s de la versión directa: 66.8% menos memoria. Se conservan los DSU aceptados de C++ y Python. Python DSU usa 3560 KB y 0.078 s; el nuevo sencillo, 5 464 KB y 0.093 s. Se conserva para enseñar aunque ambas métricas empeoren. C++ DSU usa 212 KB frente a 208 KB del directo; 0.031 frente a 0.015 s es un solo salto del temporizador, así que su admisión rápida se basa en la clasificación guardada y no en un supuesto 30% de mejora temporal. Java y Rust reutilizan los archivos directos de Sencillas para su cobertura rápida, sin copias idénticas.

## Notas por lenguaje

El pintado directo sencillo ya tiene Accepted en los cinco lenguajes. DSU es otro algoritmo con nombres propios. El nuevo DSU Go usa manejadores estándar y arreglos primitivos compactos. Se conservan todos los archivos anteriores y sus métricas Accepted históricas. Los asteriscos señalan fuentes del conjunto rápido que aún no alcanzan la meta de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1019_sorting.cpp](1019_sorting.cpp) | G++ 13.2 x64 | sorting | O(N^2) after sorting | AC | 0.031 s | 208 KB | 11278218 |
| [1019_sorting.go](1019_sorting.go) | Go 1.14 x64 | sorting | O(N^2) after sorting | AC | 0.031 s | 1784 KB | 11278227 |
| [1019_sorting.java](1019_sorting.java) \* | Java 1.8 | sorting | O(N^2) after sorting | AC | 0.203 s | 3960 KB | 11278235 |
| [1019_sorting.py](1019_sorting.py) | Python 3.12 x64 | sorting | O(N²) after sorting | AC | 0.093 s | 5 464 KB | 11314812 |
| [1019_sorting.rs](1019_sorting.rs) \* | Rust 1.75 x64 | sorting | O(N^2) after sorting | AC | 0.046 s | 692 KB | 11278240 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1019_dsu_sorting.cpp](1019_dsu_sorting.cpp) | G++ 13.2 x64 | dsu, sorting | O(N log N) | AC | 0.015 s | 212 KB | 11278221 |
| [1019_dsu_sorting.go](1019_dsu_sorting.go) \* | Go 1.14 x64 | dsu, sorting | O(N log N) | AC | 0.031 s | 592 KB | 11314801 |
| [1019_dsu_sorting.py](1019_dsu_sorting.py) \* | Python 3.12 x64 | dsu, sorting | O(N log N) | AC | 0.078 s | 3560 KB | 11278231 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
