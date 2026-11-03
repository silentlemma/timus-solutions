# 1028. Contar los puntos por debajo y a la izquierda de cada punto

[Timus 1028](https://acm.timus.ru/problem.aspx?space=1&num=1028) · dificultad 265 · fenwick, segment_tree

Problema original del III Campeonato Universitario por Equipos de Programación de los Urales, 1999.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan `N` puntos distintos, `1 ≤ N ≤ 15000`, con coordenadas enteras `0 ≤ x, y ≤ 32000`, ordenados por `y` creciente y por `x` creciente al empatar `y`. El nivel de un punto es el número de otros puntos con `x' ≤ x` e `y' ≤ y`. Cuenta los puntos de cada nivel desde 0 hasta `N − 1`. Tiempo: 0,25 segundos. Memoria: 64 MB.

## Entrada

`N`, seguido de `N` líneas `x y` en el orden indicado, sin puntos coincidentes.

## Salida

`N` líneas con los recuentos de los niveles 0, 1, …, `N − 1`.

## Evaluación

La salida se compara token a token; los espacios en blanco extra no importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
2 0
6 0
0 2
4 2
4 4
1 6
```

Salida:

```
2
2
1
1
0
0
```

### Ejemplo 2

Entrada:

```
1
32000 32000
```

Salida:

```
1
```

## Solución

Al llegar un punto, todos los anteriores ya cumplen `y′ ≤ y`. Uno
posterior tiene mayor `y`, o la misma `y` con mayor `x`, así que no puede
contribuir. El nivel es el número de puntos anteriores con `x′ ≤ x`.

Mantén frecuencias en un Fenwick sobre `x = 0..32000`. Desplaza `x` en
uno para indexar desde 1: consulta el prefijo hasta `x + 1`, incrementa
la casilla del nivel e inserta después el punto. Cada celda Fenwick
guarda un sufijo de su prefijo de índices; borrar sucesivamente el bit
activo más bajo divide la consulta en intervalos disjuntos. La inserción
actualiza exactamente los intervalos que contienen ese índice. La
consulta cuenta así los puntos requeridos; consultar antes de insertar
excluye el propio punto. Los de igual `y` también se insertan de inmediato,
sin esperar al final del grupo: los anteriores de esa fila deben contar.

Tiempo `O(N log C)`, `C = 32001`, y `O(C + N)` celdas para árbol e
histograma. Se conserva el árbol de segmentos C++ original: consulta
`[0, x + 1)` e inserta `x` con el mismo argumento de orden. Tiene la misma
cota asintótica, pero un árbol mayor. Las seis fuentes Accepted originales
se conservan sin cambiar sus bytes.

## Soluciones optimizadas

Cada contador del árbol o histograma es como máximo `N ≤ 15000`, por
lo que bastan celdas sin signo de 16 bits; las sumas usan aritmética más
amplia. Los Fenwick compactos sustituyen enteros nativos completos o
listas de objetos Python por arrays de 16 bits. En el máximo, los dos
arrays de contadores ocupan `2 × (32002 + 15000) = 94004` bytes, sin
entrada, salida ni entorno de ejecución.

C++ usa un lector con búfer pequeño y salida estándar amortiguada.
Python procesa los tokens en flujo y elimina el generador al terminar,
pero aún construye la cadena final de salida. Rust retiene el texto
de entrada, lo analiza de manera diferida sin vector de todos los números
y escribe con búfer. Tiempo `O(N log C)` y contadores `O(C + N)` se mantienen:
es una optimización de implementación y memoria.

Memoria medida frente al Fenwick original del mismo lenguaje: C++ 348 →
224 KB (35,6% menos), Python 3644 → 1576 KB (56,8%), Rust 1076 → 580 KB
(46,1%). Las tres fuentes tienen su propio Accepted y cumplen por memoria.
Python tarda más: 0,156 s frente a 0,109 s; Rust sigue en 0,031 s. C++
registra 0,015 s frente a 0,031 s, pero un solo tick no demuestra una
aceleración fiable. Su base de comparación es el Fenwick original,
no el árbol de segmentos de mayor memoria.

## Notas por lenguaje

Python se comprobó en 811 conjuntos pequeños con recuentos directos de dominancia
bidimensional: todos los subconjuntos no vacíos de la cuadrícula 3 × 3,
coordenadas límite aleatorias. Otros dos extremos de 15000 puntos usan
histogramas esperados derivados por fórmula, cubriendo un contador de 15000 y contadores Fenwick máximos.
Los tres programas reales también superaron 14 entradas del repositorio en Docker.

Instantánea del 2 de noviembre de 2026: C++ tiene puestos 1 en tiempo y
2 en memoria entre 235 registros filtrados de otros autores, cumpliendo
el objetivo. Rust es primero en ambas métricas frente a dos. Python tiene
puestos 5 y 3 frente a 19 y conserva el asterisco. Java original es primero
en ambas frente a cinco. La muestra Go está vacía; su cobertura formal
no demuestra superioridad competitiva.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1028_fenwick.cpp](1028_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(N log C), C = 32001 | AC | 0.031 s | 348 KB | 11278320 |
| [1028_fenwick.go](1028_fenwick.go) | Go 1.14 x64 | fenwick | O(N log C), C = 32001 | AC | 0.046 s | 1512 KB | 11278322 |
| [1028_fenwick.java](1028_fenwick.java) | Java 1.8 | fenwick | O(N log C), C = 32001 | AC | 0.093 s | 888 KB | 11278326 |
| [1028_fenwick.py](1028_fenwick.py) | Python 3.12 x64 | fenwick | O(N log C), C = 32001 | AC | 0.109 s | 3644 KB | 11278325 |
| [1028_fenwick.rs](1028_fenwick.rs) | Rust 1.75 x64 | fenwick | O(N log C), C = 32001 | AC | 0.031 s | 1076 KB | 11278327 |
| [1028_segment_tree.cpp](1028_segment_tree.cpp) | G++ 13.2 x64 | segment_tree | O(N log C), C = 32001 | AC | 0.031 s | 472 KB | 11278321 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1028_fenwick_optimized.cpp](1028_fenwick_optimized.cpp) | G++ 13.2 x64 | fenwick | O(N log C), C = 32001 | AC | 0.015 s | 224 KB | 11308209 |
| [1028_fenwick_optimized.py](1028_fenwick_optimized.py) \* | Python 3.12 x64 | fenwick | O(N log C), C = 32001 | AC | 0.156 s | 1576 KB | 11308208 |
| [1028_fenwick_optimized.rs](1028_fenwick_optimized.rs) | Rust 1.75 x64 | fenwick | O(N log C), C = 32001 | AC | 0.031 s | 580 KB | 11308211 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
