# 1654. Mensaje cifrado

[Timus 1654](https://acm.timus.ru/problem.aspx?space=1&num=1654) · dificultad 60 · implementation

Problema original de Vladimir Yakovlev (idea de Alexander Klepinin), del cuarto de final de la subregión oriental del NEERC 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un texto sin dos letras vecinas iguales se cifró insertando, muchas
veces, un par de letras iguales en cualquier lugar. Hay que quitar todos
los pares insertados e imprimir el texto original.

## Entrada

Una línea de hasta 200000 letras latinas minúsculas.

## Salida

El texto restaurado (posiblemente vacío).

## Ejemplos

### Ejemplo 1

Entrada:

```
wwstdaadierfflitzzz
```

Salida:

```
stierlitz
```

## Solución

Quitar un par de vecinas iguales es como cancelar x · x = 1 en un grupo
donde cada letra es su propia inversa, y esas reducciones siempre acaban
en el mismo texto, en cualquier orden. El texto original no tiene vecinas
iguales, así que es exactamente esa forma reducida.

Una pila la calcula en una pasada: una letra igual a la cima de la pila
la cancela y cualquier otra se apila. `O(n)`.

Detalles a tener en cuenta:

- quitar pares puede juntar nuevas letras iguales (`abba` desaparece por
  completo, prueba 04), así que una sola pasada de izquierda a derecha sin
  pila no basta;
- tres letras iguales dejan una (prueba 06);
- la respuesta puede ser una línea vacía (pruebas 02, 04).

Las respuestas coinciden con una implementación aceptada independiente
en 60 pruebas aleatorias.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1654_implementation.cpp](1654_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.031 s | 988 KB |
| [1654_implementation.go](1654_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 3072 KB |
| [1654_implementation.java](1654_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.093 s | 3828 KB |
| [1654_implementation.py](1654_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.109 s | 1424 KB |
| [1654_implementation.rs](1654_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 936 KB |
