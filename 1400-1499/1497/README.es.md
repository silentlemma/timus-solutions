# 1497. Cortar un cuadrado

[Timus 1497](https://acm.timus.ru/problem.aspx?space=1&num=1497) · dificultad 304 · implementation

Problema original de Alexander Toropov, del Decimotercer Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 14 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una hoja cuadriculada de N × N (3 ≤ N ≤ 1000) se corta en una pieza
negra (casillas 1) y una blanca (casillas 0), ambas conexas por los
lados. Las piezas están juntas sobre una mesa. ¿Se puede alejar una de
la otra sin levantar ninguna de la mesa? Hay que escribir «Yes» o
«No».

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego N filas de N caracteres 0 y 1.

## Salida

«Yes» o «No».

## Ejemplos

### Ejemplo 1

Entrada:

```
5
10001
10001
10001
11111
11111
```

Salida:

```
Yes
```

### Ejemplo 2

Entrada:

```
5
11011
11011
10001
11111
11111
```

Salida:

```
No
```

## Solución

Alejar una pieza es lo mismo que mover la otra en sentido contrario,
así que solo hay que mover la pieza negra. Puede salir hacia arriba
cuando ninguna columna tiene una casilla blanca encima de una negra, y
lo mismo hacia abajo, la izquierda y la derecha. Un deslizamiento en
diagonal no añade nada: cada arista entre las piezas debe mirar en
contra del movimiento, y entonces los dos deslizamientos por los ejes
que forman la diagonal también están libres. Así que basta comprobar
las cuatro direcciones, con una pasada por la hoja para cada una.
`O(N²)`.

Detalles a tener en cuenta:

- una pieza rodeada por la otra nunca puede salir (prueba 03, gen2);
- un solo gancho, aunque mida una casilla, traba las piezas (pruebas
  05, 07, gen4);
- un corte en escalera se separa a lo largo de un eje, aunque sus
  aristas miren en dos sentidos (prueba 04, gen1).

## Soluciones optimizadas

C++ y Go comprueban los cuatro sentidos en una sola pasada. En una pareja horizontal de colores distintos solo queda permitido el sentido que aleja la pieza negra de la blanca. Las parejas verticales hacen lo mismo en el otro eje. Se guardan cuatro indicadores y se termina si todos se desactivan. Bastan la fila anterior y la actual, de modo que el espacio es O(N).

Las implementaciones base aceptadas [1497_implementation.java](1497_implementation.java), [1497_implementation.py](1497_implementation.py), [1497_implementation.rs](1497_implementation.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1497_implementation.cpp](1497_implementation.cpp) | G++ 13.2 x64 | implementation | O(N^2) | AC | 0.031 s | 868 KB | 11287233 |
| [1497_implementation.go](1497_implementation.go) | Go 1.14 x64 | implementation | O(N^2) | AC | 0.046 s | 2192 KB | 11287234 |
| [1497_implementation.java](1497_implementation.java) \* | Java 1.8 | implementation | O(N^2) | AC | 0.109 s | 2952 KB | 11287236 |
| [1497_implementation.py](1497_implementation.py) \* | Python 3.12 x64 | implementation | O(N^2) | AC | 0.109 s | 4276 KB | 11287235 |
| [1497_implementation.rs](1497_implementation.rs) | Rust 1.75 x64 | implementation | O(N^2) | AC | 0.031 s | 2116 KB | 11287237 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1497_implementation_optimized.cpp](1497_implementation_optimized.cpp) \* | G++ 13.2 x64 | implementation | O(N²) | AC | 0.031 s | 112 KB | 11310458 |
| [1497_implementation_optimized.go](1497_implementation_optimized.go) \* | Go 1.14 x64 | implementation | O(N²) | AC | 0.031 s | 904 KB | 11310460 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
