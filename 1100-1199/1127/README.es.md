# 1127. La torre de cubos más alta con cada uno de sus cuatro lados de un solo color

[Timus 1127](https://acm.timus.ru/problem.aspx?space=1&num=1127) · dificultad 323 · bruteforce

Problema original de Ekaterina Vasilyeva, del sexto concurso universitario de programación de la Universidad Estatal de los Urales, 21 de octubre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay `N` cubos (`1 < N ≤ 1000`); cada cara de un cubo tiene un color (una
de 10 letras), y las seis caras de un cubo son todas distintas. Las caras
se dan como delantera, derecha, izquierda, trasera, superior e inferior.
Apila tantos cubos como sea posible, girando cada uno como se quiera, de
modo que cada una de las cuatro caras laterales de la torre sea de un solo
color. Imprime la altura.

Límite de tiempo: 0,4 segundos. Límite de memoria: 64 MB.

## Entrada

`N` y luego `N` líneas de seis letras de color.

## Salida

La mayor altura.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
GYVABW
AOCGYV
CABVGO
OVYWGA
```

Salida:

```
3
```

## Solución

Una torre queda determinada por el anillo de colores de sus lados:
delantero, derecho, trasero, izquierdo. Un cubo encaja en un anillo si
una de sus 24 orientaciones muestra exactamente ese anillo. Como sus seis
colores son distintos, un cubo muestra cada anillo en como mucho una
orientación, así que contar para cada anillo los cubos que pueden
mostrarlo da la altura de la torre más alta con ese anillo. Las 24
orientaciones se generan una vez a partir de dos cuartos de vuelta, uno
alrededor del eje vertical y otro alrededor del eje izquierda-derecha,
como permutaciones de las seis posiciones de las caras. `O(24·N)`.

Detalles a tener en cuenta:

- los giros deben ser rotaciones, no reflexiones: un cuarto de vuelta
  lleva la cara delantera a la derecha, la derecha atrás, y así
  sucesivamente, conservando la orientación;
- la imagen especular de un cubo también encaja: volteada alrededor del
  eje delante-detrás muestra el mismo anillo de lados, solo con arriba y
  abajo intercambiados, y esos no importan;
- en una orientación fija, los colores superior e inferior no importan.

Las respuestas se comprobaron con una construcción aparte de las 24
rotaciones como matrices de permutación con signo y determinante +1 que
actúan sobre las normales de las caras, en todas las pruebas.

## Soluciones optimizadas

Go y Rust cuentan los tres anillos laterales obtenidos al elegir cada pareja de caras opuestas como arriba y abajo. Los seis colores de cada cubo son distintos, por lo que el mínimo del anillo es único. Se gira hasta ese color y se elige el sentido menor para identificar anillos equivalentes. Los cuatro colores se codifican en base C = 10 y se cuentan en un vector plano de contadores de 16 bits.

El envío aceptado en Go 1.14 x64 tarda 0.046 s frente a 0.031 s de la base y usa 896 KB frente a 1344 KB.

Las implementaciones base aceptadas [1127_bruteforce.cpp](1127_bruteforce.cpp), [1127_bruteforce.java](1127_bruteforce.java), [1127_bruteforce.py](1127_bruteforce.py) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes generan las orientaciones con una pequeña búsqueda
  sobre los dos giros; C++ cuenta los anillos en un mapa ordenado y los demás en una tabla hash.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1127_bruteforce.cpp](1127_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(24·N) | AC | 0.015 s | 300 KB | 11279333 |
| [1127_bruteforce.go](1127_bruteforce.go) | Go 1.14 x64 | bruteforce | O(24·N) | AC | 0.031 s | 1344 KB | 11279335 |
| [1127_bruteforce.java](1127_bruteforce.java) \* | Java 1.8 | bruteforce | O(24·N) | AC | 0.171 s | 6664 KB | 11279344 |
| [1127_bruteforce.py](1127_bruteforce.py) \* | Python 3.12 x64 | bruteforce | O(24·N) | AC | 0.093 s | 768 KB | 11279338 |
| [1127_bruteforce.rs](1127_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(24·N) | AC | 0.031 s | 440 KB | 11279345 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1127_bruteforce_optimized.go](1127_bruteforce_optimized.go) \* | Go 1.14 x64 | bruteforce | O(N + C⁴) | AC | 0.046 s | 896 KB | 11311096 |
| [1127_bruteforce_optimized.rs](1127_bruteforce_optimized.rs) \* | Rust 1.75 x64 | bruteforce | O(N + C⁴) | AC | 0.015 s | 220 KB | 11311098 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
