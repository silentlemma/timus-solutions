# 1809. Chapáev y las patatas

[Timus 1809](https://acm.timus.ru/problem.aspx?space=1&num=1809) · dificultad 598 · implementation

Problema original de Dmitry Ivankov, de la subregión oriental del NEERC 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cuatro patatas están en celdas distintas de un tablero de 20 × 20. Una
patata puede disparar a otra si comparten fila o columna sin ninguna
patata entre ellas. Mover el menor número de patatas a celdas libres
para que cada patata pueda disparar exactamente a otra.

## Entrada

Cuatro líneas con las coordenadas x e y de las patatas, de 1 a 20.

## Salida

Las nuevas coordenadas en el mismo orden. Se acepta cualquier
respuesta óptima.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 1
2 2
4 4
4 3
```

Salida:

```
1 2
2 2
4 4
4 3
```

## Solución

Se busca una disposición donde la relación «puede disparar» divida las
cuatro patatas en dos parejas. Se comprueba la disposición tal cual. Si
no, se prueba a mover una patata a cada una de las 400 celdas. Si no,
dos movimientos siempre bastan. Si las dos patatas que se quedan se
ven entre sí, las otras dos pueden formar su propia pareja en una fila
y columnas que las fijas no usan. Si no, cada patata movida puede ir
junto a una de las fijas. Así que, para cada elección de las dos que se
mueven, basta probar las celdas junto a las fijas y esa pareja aparte.
Una prueba de estrés con 20000 disposiciones aleatorias nunca dejó
vacío este paso. `O(1)`.

En el ejemplo la segunda pareja, (4, 4) y (4, 3), ya está bien, y mover
la primera patata a (1, 2) la empareja con (2, 2).

Trampas:

- una patata entre otras dos bloquea el disparo, así que cuatro en una
  línea no forman parejas;
- una patata no puede ver a más de una, así que una pareja no debe
  compartir línea con la otra;
- las patatas movidas deben caer en celdas libres del tablero.

El verificador comprueba la disposición y compara el número de patatas
movidas con el de la respuesta esperada. Todas las soluciones lo
superan en disposiciones aleatorias, esquinas abarrotadas, una sola
línea y disposiciones casi válidas, frente a una implementación
aceptada independiente que prueba todos los pares de celdas.

## Soluciones optimizadas

Java reutiliza los arreglos de coordenadas y de vecinos al probar casillas para un solo movimiento. Cada prueba cuenta los vecinos visibles y rechaza las posiciones superpuestas. El envío 11317164 tardó 0,109 s y usó 384 KB frente a 0,156 s y 1780 KB en la base.

**Envíos de las versiones sencillas en Timus**

Go 1.14 x64 №11321831 · G++ 13.2 x64 №11321917 · Java 1.8 №11321915 · Python 3.12 x64 №11328309 · Rust 1.75 x64 №11321919.

Rust prueba una coordenada por cada intervalo entre posiciones fijas. En una disposición válida ninguna línea puede contener tres patatas, así que basta con contar las otras patatas de la misma fila o columna. Rust 1.75 x64, envío 11322514. Tiempo 0,062 → 0,046 s, memoria 236 → 228 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1809_implementation.cpp](1809_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 188 KB | 11321917 |
| [1809_implementation.go](1809_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1124 KB | 11321831 |
| [1809_implementation.java](1809_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.156 s | 1780 KB | 11321915 |
| [1809_implementation.py](1809_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.109 s | 848 KB | 11328309 |
| [1809_implementation.rs](1809_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.062 s | 236 KB | 11321919 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1809_implementation_optimized.java](1809_implementation_optimized.java) \* | Java 1.8 | implementation | O(1) | AC | 0.109 s | 384 KB | 11317164 |
| [1809_implementation_optimized.rs](1809_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 228 KB | 11322514 |

\* El corte de clasificación no contiene envíos comparables en Java de otros autores.
