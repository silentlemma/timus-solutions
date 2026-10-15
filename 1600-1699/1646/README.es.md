# 1646. ¡Godzilla contraataca!

[Timus 1646](https://acm.timus.ru/problem.aspx?space=1&num=1646) · dificultad 886 · strings

Problema original de Ivan Burmistrov, del USU Junior Contest, octubre de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan dos muestras de ADN. Cada uno de los m días se obtiene una muestra
nueva pegando dos anteriores (la segunda tras la primera). Hay que contar
las apariciones de un patrón dado en la última muestra, módulo 10⁹ + 7.

## Entrada

El patrón (hasta 100 letras `ACGT`), las dos primeras muestras (hasta 10
letras cada una), m (1 ≤ m ≤ 100) y luego m pares: el día k, los números
de las dos muestras que se pegan, cada uno de 1 a k + 1.

## Salida

El número de apariciones módulo 10⁹ + 7.

## Ejemplos

### Ejemplo 1

Entrada:

```
AGA
A
G
4
1 2
2 1
3 1
5 4
```

Salida:

```
2
```

### Ejemplo 2

Entrada:

```
A
CT
AG
2
1 1
3 3
```

Salida:

```
0
```

## Solución

La longitud puede duplicarse cada día, así que la última muestra puede
tener unas 2¹⁰⁰ letras; nunca se construye. De cada muestra se guarda solo
su número de apariciones módulo 10⁹ + 7 y sus primeras y últimas L − 1
letras, donde L es la longitud del patrón (o la muestra entera si es más
corta).

Pegar A y B conserva todas las apariciones dentro de A y dentro de B y
añade las que cruzan la unión. Una de esas empieza en las últimas L − 1
letras de A y acaba en las primeras L − 1 de B, así que son exactamente
las apariciones en la cadena corta tail(A) + head(B): ninguna parte sola
basta para contener el patrón. El nuevo comienzo son las primeras L − 1
letras de head(A) + head(B), y el nuevo final las últimas L − 1 de
tail(A) + tail(B), lo que sigue siendo correcto cuando una muestra es más
corta que L − 1. `O(m · L²)`.

Detalles a tener en cuenta:

- la cuenta puede desbordar enteros de 64 bits: 2¹⁰⁰ copias de `A` contienen
  2¹⁰⁰ apariciones de `A` (prueba 04);
- una muestra más corta que L − 1 debe guardarse entera; un corte desde
  `len(s) - (L - 1)` en Python puede recortarla (prueba 06);
- con un patrón de una letra los extremos guardados quedan vacíos y nada
  cruza una unión.

Las respuestas coinciden con una implementación aceptada independiente
en 400 pruebas aleatorias y con un conteo directo en las pequeñas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1646_strings.cpp](1646_strings.cpp) | G++ 13.2 x64 | strings | O(m · L²) | AC | 0.015 s | 436 KB |
| [1646_strings.go](1646_strings.go) | Go 1.14 x64 | strings | O(m · L²) | AC | 0.031 s | 1168 KB |
| [1646_strings.java](1646_strings.java) | Java 1.8 | strings | O(m · L²) | AC | 0.140 s | 2144 KB |
| [1646_strings.py](1646_strings.py) | Python 3.12 x64 | strings | O(m · L²) | AC | 0.109 s | 532 KB |
| [1646_strings.rs](1646_strings.rs) | Rust 1.75 x64 | strings | O(m · L²) | AC | 0.015 s | 280 KB |
