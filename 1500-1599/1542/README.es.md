# 1542. Autocompletado

[Timus 1542](https://acm.timus.ru/problem.aspx?space=1&num=1542) · dificultad 624 · sorting

Problema original de Den Raskovalov, del XI Campeonato Universitario por Equipos de Programación de los Urales, Ekaterimburgo, 21 de abril de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un diccionario contiene N palabras distintas (N ≤ 10⁵, de hasta 15
letras minúsculas) con sus frecuencias (hasta 10⁶). Para cada uno de
M ≤ 15000 prefijos tecleados hay que listar como mucho diez palabras que
empiecen por él, primero las más frecuentes y, a igual frecuencia, por
orden alfabético.

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

N, luego N líneas con una palabra y su frecuencia, y luego M y los M
prefijos, uno por línea.

## Salida

Para cada prefijo, sus sugerencias, una por línea; las listas de
prefijos consecutivos se separan con una línea vacía.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
kare 10
kanojo 20
karetachi 1
korosu 7
sakura 3
3
k
ka
kar
```

Salida:

```
kanojo
kare
korosu
karetachi

kanojo
kare
karetachi

kare
karetachi
```

## Solución

Se ordenan las palabras una vez por frecuencia decreciente y luego
alfabéticamente. Cada consulta distinta va a una tabla hash con una
lista vacía. Después se recorren las palabras ordenadas: para cada uno
de los a lo sumo 15 prefijos de una palabra que sea una consulta, se
añade la palabra a su lista si aún no tiene diez. Como las palabras
llegan en el orden pedido, cada lista termina siendo exactamente la
respuesta. El tiempo total es `O(N log N + 15·N + M)`; las consultas
repetidas reutilizan la misma lista.

Detalles a tener en cuenta:

- un prefijo sin palabras ocupa igualmente su sitio en la salida: un
  bloque vacío, también al principio o al final (prueba 02);
- las frecuencias iguales van por orden alfabético, así que a va antes
  que ab (prueba 03);
- una consulta puede coincidir con una palabra entera o ser más larga
  que todas (prueba 05).

## Soluciones optimizadas

Python guarda la frecuencia invertida en tres bytes de mayor a menor peso antes de cada palabra. Ordena esas cadenas de bytes sin tuplas y comprueba solo las longitudes de prefijo que aparecen en las consultas. El envío 11317220 tardó 0,562 s y usó 17632 KB frente a 0,656 s y 33184 KB en la base.

Rust empaqueta la frecuencia y las letras en una clave de ordenación de 128 bits, examina solo las longitudes de prefijo consultadas y guarda las sugerencias como bytes. El envío 11317222 tardó 0,062 s y usó 9652 KB frente a 0,109 s y 15020 KB en la base.

**Envíos de las versiones sencillas en Timus**

G++ 13.2 x64 №11321809 · Go 1.14 x64 №11321811 · Java 1.8 №11321814 · Python 3.12 x64 №11322065 · Rust 1.75 x64 №11322067.

C++ guarda las palabras en registros de tamaño fijo, consulta solo las longitudes pedidas mediante vistas de cadena y escribe las sugerencias directamente. G++ 13.2 x64, envío 11322388. Tiempo 0,171 → 0,093 s, memoria 11168 → 4104 KB.

Go guarda las palabras en registros de tamaño fijo, consulta solo las longitudes pedidas mediante vistas de cadena y escribe las sugerencias directamente. Go 1.14 x64, envío 11322389. Tiempo 0,187 → 0,109 s, memoria 11308 → 10108 KB.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1542_sorting.cpp](1542_sorting.cpp) | G++ 13.2 x64 | sorting | O(N log N + 15 N + M) | AC | 0.171 s | 11168 KB | 11321809 |
| [1542_sorting.go](1542_sorting.go) | Go 1.14 x64 | sorting | O(N log N + 15 N + M) | AC | 0.187 s | 11308 KB | 11321811 |
| [1542_sorting.java](1542_sorting.java) | Java 1.8 | sorting | O(N log N + 15 N + M) | AC | 0.484 s | 36648 KB | 11321814 |
| [1542_sorting.py](1542_sorting.py) | Python 3.12 x64 | sorting | O(N log N + 15 N + M) | AC | 0.656 s | 33184 KB | 11322065 |
| [1542_sorting.rs](1542_sorting.rs) | Rust 1.75 x64 | sorting | O(N log N + 15 N + M) | AC | 0.109 s | 15020 KB | 11322067 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|----------|----------|---------|-------------|-----------|--------|---------|---|
| [1542_sorting_optimized.py](1542_sorting_optimized.py) \* | Python 3.12 x64 | sorting | O(N log N + 15 N + M) | AC | 0.562 s | 17632 KB | 11317220 |
| [1542_sorting_optimized.rs](1542_sorting_optimized.rs) | Rust 1.75 x64 | sorting | O(N log N + 15 N + M) | AC | 0.062 s | 9652 KB | 11317222 |
| [1542_sorting_optimized.cpp](1542_sorting_optimized.cpp) | G++ 13.2 x64 | sorting | O(N log N + 15 N + M) | AC | 0.093 s | 4104 KB | 11322388 |
| [1542_sorting_optimized.go](1542_sorting_optimized.go) | Go 1.14 x64 | sorting | O(N log N + 15 N + M) | AC | 0.109 s | 10108 KB | 11322389 |

\* En el corte de clasificación, Python ocupa el sexto lugar en tiempo y el primero en memoria. La versión cumple el criterio de ahorro de memoria.
