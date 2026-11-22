# 1025. Los menos partidarios para ganar una votación por mayoría en dos niveles

[Timus 1025](https://acm.timus.ru/problem.aspx?space=1&num=1025) · dificultad 67 · greedy, sorting

Problema original de la Segunda Competición por Equipos de Programación para Escolares de la Región de Sverdlovsk, 7 de octubre de 2000.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los votantes están repartidos en `K` grupos (`K` impar, `1 ≤ K ≤ 101`),
cada uno de tamaño impar; en total como mucho 9999. Un grupo dice «sí»
cuando más de la mitad de sus miembros vota sí, y una decisión se aprueba
cuando más de la mitad de los grupos dice «sí». Encuentra el menor número de
partidarios que, colocados en los grupos adecuados, aprueban cualquier
decisión.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`K` y luego los `K` tamaños de los grupos.

## Salida

El menor número de partidarios.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
9 3 11 1 7
```

Salida:

```
7
```

### Ejemplo 2

Entrada:

```
1
9999
```

Salida:

```
5000
```

## Solución

Para aprobar una decisión los partidarios deben ganar `K / 2 + 1` grupos
(división entera, `K` es impar), y ganar un grupo de `s` votantes (`s`
impar) requiere `s / 2 + 1` partidarios; los que sobren en ese grupo se
desperdician, igual que los partidarios en grupos perdidos.

Así que hay que elegir `K / 2 + 1` grupos con el menor coste total
`s / 2 + 1`. El coste crece con el tamaño, así que los mejores grupos son
simplemente los más pequeños: se ordenan los tamaños y se suman los costes
de los primeros `K / 2 + 1`. `O(K log K)`.

Detalles a tener en cuenta:

- la mayoría de grupos es `K / 2 + 1`, y la mayoría en un grupo de `s` es
  `s / 2 + 1`, no `s / 2`;
- los tamaños no vienen ordenados en la entrada.

## Soluciones optimizadas

`1025_greedy_sorting_optimized.py`. Python sigue ordenando los tamaños y eligiendo los floor(K/2)+1 menores. Como todos son impares, los partidarios son (sum(selected_sizes)+needed)//2: una suma en C y una división sustituyen el generador Python con división por grupo. Lee tokens binarios, escribe una vez y sale dentro de main antes de destruir los datos locales. Tiempo O(K log K), datos ordenados O(K), además de la entrada leída durante el proceso. Conserva la misma elección voraz y la base clara de costes por grupo.

Accepted exacto Python 3.12 x64 #11327542: 0.062 s / 648 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 66/551, memoria 502/551. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11324842 (PyPy 3.10 x64) era 0.109 s / 212 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1025_greedy_sorting_optimized.py`: 0.062 s / 648 KB; base didáctica conservada `1025_greedy_sorting.py`: 0.093 s / 372 KB.

`1025_greedy_sorting_optimized.java`. Java conserva la elección voraz de la mayoría más pequeña: gana los floor(K/2)+1 grupos menores con floor(size/2)+1 partidarios en cada uno. Para K<=101 inserta cada tamaño leído en su posición de un arreglo int ordenado, sin cargar Arrays.sort. Cambia deliberadamente la ordenación O(K log K) por O(K^2) comparaciones acotadas para reducir el arranque de biblioteca; no es una mejora asintótica. Un búfer de entrada de 1024 bytes y salida decimal directa evitan Scanner y cadenas numéricas. Espacio auxiliar O(K); conserva la base más sencilla con ordenación de biblioteca.

Accepted exacto Java 1.8 #11327343: 0.093 s / 320 KB. Comparación guardada del grupo de compiladores del 2026-11-20: tiempo 108/770, memoria 4/770. Bajo 1024 KB la admisión estricta solo usa tiempo: diez primeros o 15% superior, con empates compartidos y corte porcentual redondeado hacia arriba. Conserva el asterisco por la meta propia del lenguaje: primer puesto en ambas métricas. El registro optimizado documentado antes #11303704 era 0.125 s / 384 KB; es un par histórico distinto, no la medición actual de este fuente. Las bases didácticas permanecen intactas.

- `1025_greedy_sorting_optimized.java`: 0.093 s / 320 KB; base didáctica conservada `1025_greedy_sorting.java`: 0.109 s / 1724 KB.

`1025_greedy_sorting_optimized.go`. Go conserva la elección voraz de una mayoría de los grupos más pequeños. El código optimizado lee bytes directamente e inserta cada grupo en un único arreglo fijo de hasta 101 entradas. Usa deliberadamente ordenación por inserción: O(K²), frente a O(K log K) de la base, pero evita sus contenedores dinámicos y el coste de fmt con este límite pequeño. Suma floor(size/2)+1 para los primeros floor(K/2)+1 grupos. Se mantiene el código original con ordenación de biblioteca.

Frente a `1025_greedy_sorting.go`: tiempo 0.031 s → 0.015 s; memoria 1076 KB → 796 KB.

## Notas por lenguaje

La misma ordenación y suma en todos los lenguajes.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1025_greedy_sorting.cpp](1025_greedy_sorting.cpp) | G++ 13.2 x64 | greedy, sorting | O(K log K) | AC | 0.001 s | 188 KB | 11303273 |
| [1025_greedy_sorting.go](1025_greedy_sorting.go) | Go 1.14 x64 | greedy, sorting | O(K log K) | AC | 0.031 s | 1076 KB | 11278301 |
| [1025_greedy_sorting.java](1025_greedy_sorting.java) | Java 1.8 | greedy, sorting | O(K log K) | AC | 0.109 s | 1724 KB | 11278306 |
| [1025_greedy_sorting.py](1025_greedy_sorting.py) | Python 3.12 x64 | greedy, sorting | O(K log K) | AC | 0.093 s | 372 KB | 11278304 |
| [1025_greedy_sorting.rs](1025_greedy_sorting.rs) | Rust 1.75 x64 | greedy, sorting | O(K log K) | AC | 0.031 s | 220 KB | 11278307 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1025_greedy_sorting_optimized.java](1025_greedy_sorting_optimized.java) \* | Java 1.8 | greedy, sorting | O(K²) time; O(K) auxiliary space | AC | 0.093 s | 320 KB | 11327343 |
| [1025_greedy_sorting_optimized.go](1025_greedy_sorting_optimized.go) | Go 1.14 x64 | greedy, sorting | O(K²) | AC | 0.015 s | 796 KB | 11328361 |
| [1025_greedy_sorting_optimized.py](1025_greedy_sorting_optimized.py) \* | Python 3.12 x64 | greedy, sorting | O(K log K) time; O(K + I) storage | AC | 0.062 s | 648 KB | 11327542 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
