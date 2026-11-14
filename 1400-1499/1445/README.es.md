# 1445. Regalos de Navidad

[Timus 1445](https://acm.timus.ru/problem.aspx?space=1&num=1445) · dificultad 593 · math

Problema original de Stanislav Vasiliev, del Décimo Campeonato Universitario de Programación por Equipos de los Urales, 24–25 de marzo de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Las amistades de Harry forman N grupos (1 ≤ N ≤ 500) de 1 a 500
personas. Harry se reúne con cada persona por separado, le entrega un
regalo y recibe otro a cambio. A una persona se le puede dar un regalo
preparado de antemano o uno recibido de alguien de otro grupo, nunca uno
de su propio grupo. Hay que hallar el menor número de regalos que Harry
debe preparar cuando elige el orden de las reuniones y cuando el orden
es el peor posible.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

N y luego los tamaños de los grupos.

## Salida

El mejor y el peor número de regalos preparados.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
3 7 3 2
```

Salida:

```
1 7
```

## Solución

Sea m el tamaño del grupo mayor y S el número total de personas. Cada
intercambio devuelve un regalo, así que Harry tiene siempre tantos
regalos como preparó. Las m personas del grupo mayor necesitan regalos
de fuera de él, y de fuera solo llegan S − m regalos en total, así que
hay que preparar al menos 2m − S, y al menos uno en cualquier caso. Con
eso basta: si 2m > S, las primeras 2m − S personas del grupo mayor
reciben los regalos preparados; después se alterna ese grupo con los
demás. En otro caso, se ordenan las personas sin vecinos del mismo grupo;
un regalo basta.

En el peor orden el grupo mayor llega primero; sus regalos no sirven
dentro de él, así que hacen falta m regalos. También bastan: Harry tiene
m regalos, y de cada grupo como mucho tantos como personas suyas ya
vistas, así que para cada persona que aún espera queda un regalo de
fuera. `O(N)`.

Detalles a tener en cuenta:

- con un solo grupo, en ambos casos todos los regalos se preparan
  (pruebas 02, 03);
- un regalo basta cuando el grupo mayor no supera al resto más uno
  (pruebas 05, 06, 08).

## Soluciones optimizadas

Go y Java leen una vez el tamaño de cada grupo y solo guardan la suma y el máximo. Escriben las dos respuestas sin formato genérico.

Go lee una vez los tamaños de los grupos y calcula ambos límites con su suma y su máximo. Go 1.14 x64, envío 11322860. Tiempo 0,031 → 0,015 s, memoria 1080 → 424 KB.

El envío de Java 11317352 tardó 0,125 s y usó 376 KB, frente a 0,14 s y 1960 KB de la versión sencilla.

El envío de Python 11317966 tardó 0,093 s y usó 344 KB, frente a 0,078 s y 480 KB de la versión sencilla.

Python convierte cada tamaño y actualiza la suma y el máximo en el momento, sin construir una lista de enteros aparte.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321765 · Go 1.14 x64 №11322086 · Rust 1.75 x64 №11321769 · Java 1.8 №11322087 · Python 3.12 x64 №11322088.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1445_math.cpp](1445_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 112 KB | 11321765 |
| [1445_math.go](1445_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 1080 KB | 11322086 |
| [1445_math.java](1445_math.java) | Java 1.8 | math | O(N) | AC | 0.14 s | 1960 KB | 11322087 |
| [1445_math.py](1445_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.078 s | 480 KB | 11322088 |
| [1445_math.rs](1445_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.031 s | 224 KB | 11321769 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1445_math_optimized.go](1445_math_optimized.go) \* | Go 1.14 x64 | math | O(N) | AC | 0.015 s | 424 KB | 11322860 |
| [1445_math_optimized.java](1445_math_optimized.java) | Java 1.8 | math | O(N) | AC | 0.125 s | 376 KB | 11317352 |
| [1445_math_optimized.py](1445_math_optimized.py) \* | Python 3.12 x64 | math | O(N) | AC | 0.093 s | 344 KB | 11317966 |

\* Las soluciones marcadas aún pueden mejorar en la clasificación objetivo.
