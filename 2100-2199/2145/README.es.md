# 2145. Contar repartos de problemas que cada estudiante puede resolver

[Timus 2145](https://acm.timus.ru/problem.aspx?space=1&num=2145) · dificultad 375 · combinatorics, sorting

Problema original de Valentin Zuev, del Concurso Escolar de Programación de los Urales 2019.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

n estudiantes tienen conocimiento aᵢ y n problemas tienen dificultad bⱼ;
un estudiante resuelve un problema cuando aᵢ ≥ bⱼ. Contar, módulo p, las
formas de dar a cada estudiante exactamente un problema, todos
distintos, de modo que cada uno pueda resolver el suyo. Los límites son
3 segundos y 256 MB.

## Entrada

n, 1 ≤ n ≤ 10⁵, los valores aᵢ, los valores bⱼ, todos entre 0 y 10⁹, y
p, 1 ≤ p ≤ 10⁹.

## Salida

El número de formas módulo p.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
1 2 3
1 2 3
100
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
3
3 3 3
1 1 1
100
```

Salida:

```
6
```

## Solución

Se ordenan los estudiantes por conocimiento y se reparten los problemas
desde el más débil. Sea cᵢ el número de problemas que resuelve el
estudiante i-ésimo (contando desde 0). Todo problema que resuelve un
estudiante más débil lo resuelve también el i-ésimo, y los i más débiles
ya se llevaron i problemas distintos de los cᵢ del i-ésimo. Se lleven lo
que se lleven, el i-ésimo tiene exactamente cᵢ − i opciones, así que la
respuesta es el producto de los cᵢ − i. En cuanto un factor vale 0, el
producto queda en 0.

Tras ordenar ambos arreglos, cᵢ crece con i y un único puntero sobre los
problemas los da todos. El producto se toma módulo p en cada paso, y
1 % p cubre p = 1. El trabajo es O(n log n).

En el segundo ejemplo cada estudiante resuelve cada problema, y el
producto es 3 · 2 · 1 = 6.

## Soluciones optimizadas

C++ y Go codifican problemas y estudiantes en un solo vector de eventos de 32 bits. El bit inferior identifica el tipo y coloca el problema antes que un estudiante de igual valor. Tras ordenar, un problema aumenta las opciones libres. Un estudiante multiplica la respuesta por ese número y consume una opción. El producto es el mismo que al recorrer dos vectores.

Las implementaciones base aceptadas [2145_combinatorics_sorting.java](2145_combinatorics_sorting.java), [2145_combinatorics_sorting.py](2145_combinatorics_sorting.py), [2145_combinatorics_sorting.rs](2145_combinatorics_sorting.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2145_combinatorics_sorting.cpp](2145_combinatorics_sorting.cpp) | G++ 13.2 x64 | combinatorics, sorting | O(n log n) | AC | 0.171 s | 1768 KB | 11294961 |
| [2145_combinatorics_sorting.go](2145_combinatorics_sorting.go) | Go 1.14 x64 | combinatorics, sorting | O(n log n) | AC | 0.203 s | 5672 KB | 11294962 |
| [2145_combinatorics_sorting.java](2145_combinatorics_sorting.java) | Java 1.8 | combinatorics, sorting | O(n log n) | AC | 0.156 s | 2156 KB | 11294964 |
| [2145_combinatorics_sorting.py](2145_combinatorics_sorting.py) \* | Python 3.12 x64 | combinatorics, sorting | O(n log n) | AC | 0.187 s | 21384 KB | 11294963 |
| [2145_combinatorics_sorting.rs](2145_combinatorics_sorting.rs) \* | Rust 1.75 x64 | combinatorics, sorting | O(n log n) | AC | 0.031 s | 6320 KB | 11294965 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [2145_combinatorics_sorting_optimized.cpp](2145_combinatorics_sorting_optimized.cpp) | G++ 13.2 x64 | combinatorics, sorting | O(n log n) | AC | 0.031 s | 924 KB | 11310444 |
| [2145_combinatorics_sorting_optimized.go](2145_combinatorics_sorting_optimized.go) \* | Go 1.14 x64 | combinatorics, sorting | O(n log n) | AC | 0.078 s | 1740 KB | 11310447 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
