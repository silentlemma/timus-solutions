# 1636. Tiempo de penalización

[Timus 1636](https://acm.timus.ru/problem.aspx?space=1&num=1636) · dificultad 61 · implementation

Problema original de Alex Samsonov, del XIII Campeonato Abierto de Programación por Equipos de la Universidad Estatal de los Urales.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los equipos QXX y ZZZ resolvieron los diez problemas; QXX ganó con un
tiempo de penalización T1 frente al T2 de ZZZ. Cada intento rechazado
suma 20 minutos. Dado cuántos intentos rechazados hizo ZZZ en cada
problema, hay que decidir si ZZZ habría ganado sin ellos. A igualdad de
tiempo los equipos se ordenan por nombre, así que ZZZ seguiría segundo.

## Entrada

T1 y T2 (250 ≤ T1 ≤ T2 ≤ 2400) en la primera línea y luego diez números
de intentos rechazados de ZZZ.

## Salida

`Dirty debug :(` si los intentos le costaron el primer puesto a ZZZ, y
`No chance.` en otro caso.

## Evaluación

Las pruebas del repositorio comparan exactamente los tokens de salida; los espacios entre tokens no son significativos.

## Ejemplos

### Ejemplo 1

Entrada:

```
290 420
0 0 0 2 1 0 2 0 1 0
```

Salida:

```
No chance.
```

### Ejemplo 2

Entrada:

```
300 719
0 0 0 0 0 0 21 0 0 0
```

Salida:

```
Dirty debug :(
```

## Solución

Restar a T2 20 minutos por cada intento rechazado. ZZZ habría ganado
solo con un tiempo estrictamente menor que T1, ya que un empate es para
QXX por orden alfabético. `O(1)`.

Detalles a tener en cuenta:

- el mismo tiempo limpio sigue siendo derrota (prueba 03), un minuto
  menos es victoria (prueba 04);
- las respuestas terminan en un punto y en una cara triste, ambos parte
  del texto esperado.

Las respuestas coinciden con una implementación aceptada independiente
en 100 pruebas aleatorias.

## Soluciones optimizadas

La solución optimizada en Java analiza los números byte a byte desde
`System.in` en lugar de usar `Scanner`: 368 KB en lugar de 1600 KB, con
el mismo tiempo.

`1636_implementation_optimized.py`. Conserva T2-20*sum(rejections)<T1 estrictamente: igualdad aún da No chance. Lee tokens enteros por map y consume los diez contadores restantes con sum, sin lista entera separada de intentos ni entrada decodificada. Trabajo O(P), P=10 contadores; sigue existiendo almacenamiento de tokens. El programa independiente para el juez vacía stdout antes de os._exit(0), omitiendo la finalización normal del intérprete. Su propio Accepted acredita la mejora de memoria. El cambio de salida por sí solo no mejora la complejidad asintótica y su beneficio de ejecución no se garantiza en otras plataformas. La versión sencilla no cambia.

Frente a `1636_implementation.py`: tiempo 0.078 s → 0.109 s; memoria 428 KB → 216 KB.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1636_implementation_optimized.py`: puesto de tiempo 62/80 y de memoria 1/80 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1636_implementation.cpp](1636_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 116 KB | 11303772 |
| [1636_implementation.go](1636_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1064 KB | 11288447 |
| [1636_implementation.java](1636_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 1600 KB | 11288449 |
| [1636_implementation.py](1636_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 428 KB | 11288448 |
| [1636_implementation.rs](1636_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 244 KB | 11303773 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|-------|
| [1636_implementation_optimized.java](1636_implementation_optimized.java) | Java 1.8 | implementation | O(1) | AC | 0.093 s | 368 KB | 11303765 |
| [1636_implementation_optimized.py](1636_implementation_optimized.py) \* | PyPy 3.10 x64 | implementation | O(P), P=10 | AC | 0.109 s | 216 KB | 11325073 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
