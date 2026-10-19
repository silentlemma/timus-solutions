# 1844. Caudillo del ejército de magos

[Timus 1844](https://acm.timus.ru/problem.aspx?space=1&num=1844) · dificultad 1558 · dp

Problema original de Evgeny Kurpilyansky, del Ural SU Contest en la sesión de verano de Petrozavodsk, agosto de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dos mentores, Sandro y Zagamius, entrevistan magos en despachos
distintos. Cada uno sigue un plan fijo de pasos "llamar al mago a" y
"despedir al mago a". Un mago solo puede estar en un despacho, así que
una llamada espera mientras el mago está con el otro mentor; si ambos
pueden actuar, cualquiera puede ir primero. Decir si los mentores pueden
quedarse esperándose el uno al otro para siempre.

## Entrada

t (1 ≤ t ≤ 10) pruebas. Cada una empieza con n, m y k
(1 ≤ n, m, k ≤ 1000): las longitudes de los planes de Sandro y Zagamius
y el número de magos. Luego los n pasos de Sandro y los m de Zagamius,
cada uno "+ a" o "- a" (1 ≤ a ≤ k). Nadie llama a un mago que ya está
en su despacho ni despide a uno que no está, y al final ambos despachos
quedan vacíos.

## Salida

Para cada prueba ":-)" si ambos planes terminan con seguridad, y ":-("
si los mentores pueden atascarse.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
4 4 2
+ 1
+ 2
- 2
- 1
+ 1
+ 2
- 2
- 1
4 4 2
+ 1
+ 2
- 1
- 2
+ 2
+ 1
- 2
- 1
```

Salida:

```
:-)
:-(
```

## Solución

Un momento es una celda (i, j): Sandro ha hecho i pasos y Zagamius j.
Una celda está ocupada si ambos despachos tienen a un mismo mago. Un
paso queda bloqueado exactamente cuando llevaría a una celda ocupada:
solo una llamada puede hacer que dos despachos compartan un mago, y
ocurre justo cuando el otro mentor tiene a ese mago. Así, los momentos
posibles son las celdas alcanzables desde (0, 0) con pasos hacia abajo
y a la derecha por celdas libres, y los mentores pueden atascarse si una
de ellas, distinta de (n, m), tiene ambas vecinas ocupadas o fuera de la
rejilla. La última fila y la última columna nunca se atascan, porque el
mentor que terminó no tiene a nadie.

Qué celdas están ocupadas. En una fila fija el conjunto de magos de
Sandro es fijo; recorriendo la fila se cuentan los magos que están en
ambos despachos, sumando o restando uno cuando Zagamius llama o despide
a un mago que tiene Sandro. Con las celdas ocupadas conocidas, una
pasada por la rejilla marca las alcanzables y comprueba si alguna es un
callejón sin salida. `O(t·(n·m + k))`.

La solución en Python hace lo mismo con las filas como máscaras de bits
sobre j. Cada mago recibe la máscara de las columnas donde lo tiene
Zagamius; las celdas ocupadas de una fila son la unión de esas máscaras
sobre los magos de Sandro, repartida por los tramos de filas en que
Sandro tiene a cada mago con un árbol de segmentos sobre las filas.
Dentro de una fila, Zagamius avanza a la derecha desde cada celda a la
que se llegó desde arriba hasta la siguiente celda ocupada; el XOR de la
máscara ocupada con esa máscara menos las semillas, restaurando luego
los bits semilla, llena cada tramo libre desde su primera semilla con
unas pocas operaciones de enteros grandes.
En total: `O(t·(k + (m + n·log n)·⌈m/w⌉))`, con w bits por dígito del entero grande.

En la segunda prueba del ejemplo Sandro llama al mago 1 mientras
Zagamius llama al mago 2. Ahora Sandro espera al mago 2 y Zagamius al
mago 1.

Trampas:

- solo una llamada puede esperar, así que un callejón sin salida exige
  que ambos mentores vayan a llamar a un mago que tiene el otro;
- un mismo mago puede ser llamado muchas veces, así que importan los
  tramos en que se le tiene, no los magos.

Las respuestas coinciden con una implementación aceptada independiente
en ciento cincuenta archivos aleatorios de diez pruebas cada uno.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1844_dp.cpp](1844_dp.cpp) | G++ 13.2 x64 | dp | O(t·(n·m + k)) | AC | 0.078 s | 2048 KB |
| [1844_dp.go](1844_dp.go) | Go 1.14 x64 | dp | O(t·(n·m + k)) | AC | 0.093 s | 7304 KB |
| [1844_dp.java](1844_dp.java) | Java 1.8 | dp | O(t·(n·m + k)) | AC | 0.171 s | 6816 KB |
| [1844_dp.py](1844_dp.py) | Python 3.12 x64 | dp | O(t·(k + (m + n·log n)·⌈m/w⌉)) | AC | 0.140 s | 3536 KB |
| [1844_dp.rs](1844_dp.rs) | Rust 1.75 x64 | dp | O(t·(n·m + k)) | AC | 0.078 s | 2644 KB |
