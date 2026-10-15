# 1723. El libro de Sandro

[Timus 1723](https://acm.timus.ru/problem.aspx?space=1&num=1723) · dificultad 62 · strings

Problema original de Ivan Burmistrov (preparado por Olga Soboleva), del Concurso Regional de Programación por Equipos de los Urales 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Cada subcadena de una palabra dada es un hechizo, y su fuerza es el
número de veces que aparece en la palabra, contando las apariciones
solapadas. Imprimir un hechizo de fuerza máxima.

## Entrada

Una palabra no vacía de a lo sumo 50 letras latinas minúsculas.

## Salida

Cualquier hechizo de fuerza máxima.

## Ejemplos

### Ejemplo 1

Entrada:

```
tebidohtebidoh
```

Salida:

```
tebidoh
```

## Solución

Cada aparición de un hechizo empieza con una aparición de su primera
letra, y apariciones distintas empiezan en lugares distintos. Así que
ningún hechizo es más fuerte que su primera letra sola, y una letra más
frecuente es un hechizo de fuerza máxima. `O(n)`.

En el ejemplo cada letra aparece dos veces, así que `t` es tan fuerte
como `tebidoh`.

Trampas:

- las apariciones pueden solaparse: `aba` aparece tres veces en
  `abababa`, pero `a` aparece cuatro;
- se acepta cualquier hechizo de fuerza máxima, así que las pruebas usan
  un comprobador.

El comprobador cuenta las apariciones de la respuesta, con solapamientos,
y las compara con las de la respuesta esperada. Una letra más frecuente
coincide con una búsqueda exhaustiva de todas las subcadenas en 300
palabras aleatorias.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1723_strings.cpp](1723_strings.cpp) | G++ 13.2 x64 | strings | O(n) | AC | 0.015 s | 356 KB |
| [1723_strings.go](1723_strings.go) | Go 1.14 x64 | strings | O(n) | AC | 0.031 s | 1068 KB |
| [1723_strings.java](1723_strings.java) | Java 1.8 | strings | O(n) | AC | 0.125 s | 1572 KB |
| [1723_strings.py](1723_strings.py) | Python 3.12 x64 | strings | O(n) | AC | 0.078 s | 404 KB |
| [1723_strings.rs](1723_strings.rs) | Rust 1.75 x64 | strings | O(n) | AC | 0.031 s | 228 KB |
