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
respuesta. Son `O(N log N + 15·N)` búsquedas en la tabla hash, y las
consultas repetidas no cuestan nada.

Detalles a tener en cuenta:

- un prefijo sin palabras ocupa igualmente su sitio en la salida: un
  bloque vacío, también al principio o al final (prueba 02);
- las frecuencias iguales van por orden alfabético, así que a va antes
  que ab (prueba 03);
- una consulta puede coincidir con una palabra entera o ser más larga
  que todas (prueba 05).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1542_sorting.cpp](1542_sorting.cpp) | G++ 13.2 x64 | sorting | O(N log N + 15 N) | AC | 0.187 s | 11212 KB |
| [1542_sorting.go](1542_sorting.go) | Go 1.14 x64 | sorting | O(N log N + 15 N) | AC | 0.203 s | 11304 KB |
| [1542_sorting.java](1542_sorting.java) | Java 1.8 | sorting | O(N log N + 15 N) | AC | 0.468 s | 36636 KB |
| [1542_sorting.py](1542_sorting.py) | Python 3.12 x64 | sorting | O(N log N + 15 N) | AC | 0.593 s | 32604 KB |
| [1542_sorting.rs](1542_sorting.rs) | Rust 1.75 x64 | sorting | O(N log N + 15 N) | AC | 0.093 s | 15136 KB |
