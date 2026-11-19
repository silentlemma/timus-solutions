# 1525. Camino

[Timus 1525](https://acm.timus.ru/problem.aspx?space=1&num=1525) · dificultad 376 · implementation

Problema original de Dmitry Gozman, del Dmitry Gozman Contest 1 en el campus de invierno de Petrozavodsk, enero de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un robot está en una casilla desconocida de una caja de n × m × k
(1 ≤ n, m, k ≤ 10⁵) y ejecuta un programa de como mucho 10⁵ pasos: 'l'
y 'r' a lo ancho, 'd' y 'u' a lo alto, 'b' y 'f' a lo largo. Un paso
que saldría de la caja se ignora. Hay que contar las casillas en las
que el robot puede terminar.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

n, m y k, y luego el programa en una línea.

## Salida

El número de casillas finales posibles.

## Evaluación

Las pruebas del repositorio comparan todo el texto de salida, ignorando solo el espacio en blanco final. Conserva los espacios significativos, los saltos de línea, las mayúsculas y la puntuación.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 1 1
uuuur
```

Salida:

```
1
```

### Ejemplo 2

Entrada:

```
2 2 2
ulf
```

Salida:

```
1
```

### Ejemplo 3

Entrada:

```
13 14 15
uudlbdrruffbr
```

Salida:

```
1560
```

## Solución

Los tres ejes no se influyen, así que la respuesta es el producto de
las cuentas de cada eje. En un eje, cada paso desplaza cada inicio una
unidad o lo deja contra la pared, de modo que dos inicios vecinos
siguen en orden y a distancia de como mucho uno. Por tanto, los finales
de todos los inicios llenan todo el tramo entre los finales de los
inicios extremos 1 y L, y el eje aporta f(L) − f(1) + 1. Basta simular
esos dos inicios. `O(len)`.

Detalles a tener en cuenta:

- la cuenta llega a unos 10¹⁵ y necesita 64 bits (prueba 04, gen1);
- el programa puede estar vacío, y entonces vale cualquier casilla
  (prueba 05);
- una racha suficientemente larga de pasos iguales empuja todos los inicios
  contra una pared (pruebas 01, 06).

## Soluciones optimizadas

`1525_implementation_optimized.java`. Conserva la imagen de intervalo monótona por eje, actualizando las tres parejas al leer los bytes una sola vez. Un movimiento limita ambos extremos de su eje; los demás no cambian. El programa vacío deja intervalos intactos. Multiplica sus tres longitudes; el máximo 10^15 cabe en long. Tiempo O(L) por L bytes y solo nueve long más búfer fijo; elimina String completo y tres recorridos repetidos. El único número final aún usa println.

Frente a `1525_implementation.java`: tiempo 0.140 s → 0.093 s; memoria 2212 KB → 496 KB.

En cada eje se guarda el desplazamiento sin paredes s y sus extremos de prefijo lo y hi, incluido cero. Con coordenadas de 0 a L − 1, los extremos alcanzables son s − lo y L − 1 + s − hi hasta encontrarse. Un nuevo mínimo fija el primero en cero y un nuevo máximo fija el segundo en L − 1. Una vez juntos no vuelven a separarse. El recuento es max(1, L − (hi − lo)) y los tres recuentos se multiplican tras una sola pasada.

Las implementaciones base aceptadas [1525_implementation.java](1525_implementation.java) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Las nuevas fuentes se comparan con la instantánea del 18 de noviembre de 2026 de otros autores en compiladores actuales del juez. No hay corte por ID ni fecha. Los empates comparten puesto y los tiempos inferiores a 0.015 s se comparan como 0.015 s. Los puestos siguientes corresponden a las nuevas versiones; las fuentes existentes conservan sus propias métricas Accepted históricas.

`1525_implementation_optimized.java`: puesto de tiempo 1/15 y de memoria 1/15 en esta muestra comparable.

Un asterisco indica una meta de clasificación pendiente: C++ exige los diez primeros o el 15% superior en ambas métricas; las demás familias, el primer puesto en ambas. Una fuente aún puede admitirse por el criterio independiente de clasificación o mejora, incluida una reducción de al menos el 30% en tiempo o memoria.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1525_implementation.cpp](1525_implementation.cpp) | G++ 13.2 x64 | implementation | O(len) | AC | 0.015 s | 528 KB | 11287395 |
| [1525_implementation.go](1525_implementation.go) | Go 1.14 x64 | implementation | O(len) | AC | 0.015 s | 1748 KB | 11287396 |
| [1525_implementation.java](1525_implementation.java) \* | Java 1.8 | implementation | O(len) | AC | 0.140 s | 2212 KB | 11287401 |
| [1525_implementation.py](1525_implementation.py) | Python 3.12 x64 | implementation | O(len) | AC | 0.109 s | 692 KB | 11287398 |
| [1525_implementation.rs](1525_implementation.rs) | Rust 1.75 x64 | implementation | O(len) | AC | 0.046 s | 468 KB | 11287405 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1525_math.cpp](1525_math.cpp) | G++ 13.2 x64 | math | O(len) | AC | 0.015 s | 112 KB | 11310466 |
| [1525_math.go](1525_math.go) \* | Go 1.14 x64 | math | O(len) | AC | 0.015 s | 932 KB | 11310467 |
| [1525_math.py](1525_math.py) | Python 3.12 x64 | math | O(len) | AC | 0.078 s | 520 KB | 11310470 |
| [1525_math.rs](1525_math.rs) \* | Rust 1.75 x64 | math | O(len) | AC | 0.031 s | 216 KB | 11310469 |
| [1525_implementation_optimized.java](1525_implementation_optimized.java) | Java 1.8 | implementation | O(L) | AC | 0.093 s | 496 KB | 11325017 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
