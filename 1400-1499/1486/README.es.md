# 1486. Cuadrados iguales

[Timus 1486](https://acm.timus.ru/problem.aspx?space=1&num=1486) · dificultad 621 · hashing

Problema original de Vladimir Yakovlev, del Campeonato de la Universidad Estatal de los Urales, 7 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En una matriz N × M de letras minúsculas (1 ≤ N, M ≤ 500) hay que hallar
el mayor K tal que dos cuadrados K × K distintos (pueden solaparse, pero
no coincidir) sean iguales, y escribir K y sus esquinas superiores
izquierdas, o 0 si no hay dos casillas iguales.

Límite de tiempo: 2 segundos. Límite de memoria: 128 MB.

## Entrada

N y M, y luego N filas de M letras.

## Salida

K y luego las dos esquinas como fila y columna, o solo 0. Se acepta
cualquier pareja.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 10
ljkfghdfas
isdfjksiye
pgljkijlgp
eyisdafdsi
lnpglkfkjl
```

Salida:

```
3
1 1
3 3
```

## Solución

Dos cuadrados K × K distintos e iguales contienen dos cuadrados
(K − 1) × (K − 1) distintos e iguales, sus partes superiores
izquierdas. Así que la existencia de una pareja de tamaño K es monótona
en K, y la búsqueda binaria halla el mayor K en unas nueve
comprobaciones.

Una comprobación calcula el hash de todos los cuadrados K × K en
`O(NM)`: un hash rodante sobre cada fila da el hash de cada ventana de K
letras, y un segundo hash rodante, con otra base, recorre cada columna
de esos hashes de fila. Cuadrados iguales dan hashes iguales. Un hash
repetido se confirma comparando los dos cuadrados letra a letra, así
que una colisión solo puede costar tiempo, nunca dar una respuesta
errónea. `O(NM log min(N, M))`.

Detalles a tener en cuenta:

- los dos cuadrados pueden solaparse, como en un tablero de ajedrez,
  donde los mejores cuadrados están a un paso (prueba 07);
- si ninguna letra se repite, la respuesta es solo 0 (pruebas 02, 03,
  05);
- una matriz cuadrada de una sola letra solo admite K = N − 1, porque dos
  cuadrados N × N coincidirían; una alargada admite min(N, M) (gen4,
  prueba 06).

## Notas por lenguaje

- Python se ejecuta con PyPy: las pruebas más grandes tardan unos 1,2 s
  con CPython y unos 0,35 s con PyPy. Hace el hash módulo 2⁶¹ − 1; los
  demás lenguajes juntan dos hashes módulo 10⁹ + 7 y 998244353 en una
  clave de 64 bits.
- Con PyPy aun así excede el límite de 2 s en la prueba 10 del juez; se
  mantiene marcada TLE: pasa todas las pruebas de aquí, pero no se
  afirma que sea lo bastante rápida en cada prueba del juez.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1486_hashing.cpp](1486_hashing.cpp) | G++ 13.2 x64 | hashing | O(NM log min(N, M)) | AC | 0.234 s | 7924 KB |
| [1486_hashing.go](1486_hashing.go) | Go 1.14 x64 | hashing | O(NM log min(N, M)) | AC | 0.718 s | 25556 KB |
| [1486_hashing.java](1486_hashing.java) | Java 1.8 | hashing | O(NM log min(N, M)) | AC | 0.671 s | 17900 KB |
| [1486_hashing.py](1486_hashing.py) | PyPy 3.10 x64 | hashing | O(NM log min(N, M)) | TLE (test 10) | 2.031 s | 37456 KB |
| [1486_hashing.rs](1486_hashing.rs) | Rust 1.75 x64 | hashing | O(NM log min(N, M)) | AC | 0.125 s | 7980 KB |
