# 1517. La subcadena común más larga

[Timus 1517](https://acm.timus.ru/problem.aspx?space=1&num=1517) · dificultad 240 · suffix_structures

Problema original de Ilya Grebnov, Nikita Rybak y Dmitry Kovalioff, de Timus Top Coders: Third Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan dos cadenas de letras latinas mayúsculas, cada una de longitud `N`, `1 ≤ N ≤ 100000`. Imprime cualquier subcadena contigua de longitud máxima presente en ambas; si no comparten ninguna letra, imprime una línea vacía. Tiempo: 2 segundos. Memoria: 64 MB.

## Entrada

El entero `N`, seguido de las dos cadenas en líneas separadas.

## Salida

Una subcadena común más larga, o una línea vacía si su longitud es cero.

## Evaluación

Se acepta cualquier respuesta óptima. Se verifica que aparezca en ambas cadenas y que su longitud sea máxima; los empates no tienen que coincidir con el ejemplo.

## Ejemplos

### Ejemplo 1

Entrada:

```
28
VOTEFORTHEGREATALBANIAFORYOU
CHOOSETHEGREATALBANIANFUTURE
```

Salida:

```
THEGREATALBANIA
```

## Solución

Construye el autómata de sufijos de la primera cadena. Un estado agrupa
subcadenas con las mismas posiciones finales y guarda longitud máxima,
enlace de sufijo y transiciones. Cada extensión crea un estado nuevo;
si un destino tiene longitud excesiva, se divide su clase mediante un
clon y se redirigen las transiciones correspondientes.

Recorre la segunda cadena manteniendo el sufijo más largo del prefijo
leído que aparece en la primera. Si falta la transición, sigue enlaces
de sufijo acortando la coincidencia hasta encontrarla o alcanzar la raíz.
La mayor longitud y su posición final reconstruyen la respuesta. Toda
subcadena común es sufijo de algún prefijo leído, así que el máximo es
óptimo. Los enlaces reducen la longitud y cada carácter la aumenta a lo
sumo en uno: el recorrido total es lineal.

Hay `O(N)` estados y transiciones. Con el alfabeto fijo de 26 letras,
tiempo y espacio son `O(N)`. Las versiones nativas sencillas guardan filas
completas de transiciones; Python usa diccionarios. Las cinco fuentes
legibles se conservan sin cambios.

## Soluciones optimizadas

Las versiones optimizadas guardan solo transiciones existentes en arrays
planos: una cabeza por estado y letra, destino e índice siguiente por
arista. Cada búsqueda examina como máximo 26 aristas. Un clon recibe su
propia copia de la lista para que las redirecciones no alteren el estado
original. Con `N ≤ 100000`, índices y longitudes caben en 32 bits; Python
usa arrays enteros compactos y un bytearray para las letras.

Se eliminan las filas de 26 columnas y los objetos diccionario sin
cambiar el invariante del autómata. El tiempo sigue siendo `O(N)` para
el alfabeto fijo, con una constante de búsqueda mayor, y el espacio sigue
siendo `O(N)` con una constante mucho menor. La mejora principal es de memoria.

Reducción medida de memoria frente a las fuentes Accepted inalteradas: C++ 82.9%, Go 70.6%, Java 81.1%, Python 82.7%, Rust 81.0%. Las cinco cumplen el umbral por memoria. Python tarda más: 1,312 s frente a 0,500 s, pero baja de 56240 a 9736 KB. Go también tarda más: 0,078 s frente a 0,046 s. Son compromisos de tiempo y espacio aceptados, no una aceleración universal. Instantánea: 2 de noviembre de 2026; los asteriscos señalan objetivos de clasificación pendientes.

## Notas por lenguaje

Python se comparó en 5.760 pares con una DP cuadrática independiente de
subcadena común más larga. También se comprobaron los grafos de cadenas
de 100.000 caracteres sobre alfabetos de 1, 2 y 26 letras. Cada uno de los
cinco programas reales superó 13 entradas del repositorio en Docker antes
del envío. Estas comprobaciones complementan sus propios registros Accepted.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1517_suffix_structures.cpp](1517_suffix_structures.cpp) | G++ 13.2 x64 | suffix_structures | O(N) | AC | 0.093 s | 29044 KB | 11287349 |
| [1517_suffix_structures.go](1517_suffix_structures.go) | Go 1.14 x64 | suffix_structures | O(N) | AC | 0.046 s | 25012 KB | 11287350 |
| [1517_suffix_structures.java](1517_suffix_structures.java) | Java 1.8 | suffix_structures | O(N) | AC | 0.203 s | 35156 KB | 11287352 |
| [1517_suffix_structures.py](1517_suffix_structures.py) | Python 3.12 x64 | suffix_structures | O(N) | AC | 0.500 s | 56240 KB | 11287351 |
| [1517_suffix_structures.rs](1517_suffix_structures.rs) | Rust 1.75 x64 | suffix_structures | O(N) | AC | 0.062 s | 28496 KB | 11287353 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1517_suffix_structures_optimized.cpp](1517_suffix_structures_optimized.cpp) | G++ 13.2 x64 | suffix_structures | O(N) | AC | 0.062 s | 4968 KB | 11308174 |
| [1517_suffix_structures_optimized.go](1517_suffix_structures_optimized.go) | Go 1.14 x64 | suffix_structures | O(N) | AC | 0.078 s | 7356 KB | 11308176 |
| [1517_suffix_structures_optimized.java](1517_suffix_structures_optimized.java) | Java 1.8 | suffix_structures | O(N) | AC | 0.156 s | 6652 KB | 11308178 |
| [1517_suffix_structures_optimized.py](1517_suffix_structures_optimized.py) \* | Python 3.12 x64 | suffix_structures | O(N) | AC | 1.312 s | 9736 KB | 11308173 |
| [1517_suffix_structures_optimized.rs](1517_suffix_structures_optimized.rs) | Rust 1.75 x64 | suffix_structures | O(N) | AC | 0.062 s | 5408 KB | 11308179 |

\* Aceptada; aún no cumple el objetivo de clasificación. Puede optimizarse más.
