# 1437. Gasolinera

[Timus 1437](https://acm.timus.ru/problem.aspx?space=1&num=1437) · dificultad 493 · bfs

Problema original de Alexey Lakhtin, del Séptimo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 25 de febrero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Tres bidones caben de 0 a 255 litros cada uno. El surtidor solo puede
llenar un bidón hasta el borde, la gasolina puede pasarse de un bidón a
otro hasta que el primero se vacíe o el segundo se llene, y no se puede
derramar nada. Solo después de todos los trasvases, algunos bidones se
vacían en el depósito. ¿Cuántos volúmenes positivos distintos puede
recibir el depósito?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Las tres capacidades, una por línea.

## Salida

El número de volúmenes.

## Ejemplos

### Ejemplo 1

Entrada:

```
0
3
4
```

Salida:

```
6
```

## Solución

Se recorren todos los estados (x, y, z) de los bidones desde todos
vacíos, con tres movimientos de llenar un bidón y seis de verter uno en
otro. Tras cualquier movimiento algún bidón está vacío o lleno, así que
como mucho unos 3·2·256² de los 256³ estados son alcanzables. Cada
estado alcanzado da las sumas de sus subconjuntos no vacíos de bidones
como volúmenes para el depósito; se cuentan los positivos distintos.
Para capacidades a, b, c, sean P=(a+1)(b+1)(c+1), V=a+b+c+1 y S el número
de estados alcanzados. Incluida la inicialización de marcas, el tiempo
medio es `O(P)`, o `O(P + S log V)` en C++ con su conjunto ordenado.

Detalles a tener en cuenta:

- cero litros no cuentan (pruebas 01, 03);
- un bidón ya lleno no admite más, así que en el ejemplo no se pueden
  obtener 5 litros (prueba 01);
- tres bidones iguales siempre están vacíos o llenos (prueba 05).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1437_bfs.cpp](1437_bfs.cpp) | G++ 13.2 x64 | bfs | O(P + S log V) | AC | 0.031 s | 16164 KB |
| [1437_bfs.go](1437_bfs.go) | Go 1.14 x64 | bfs | O(P) | AC | 0.046 s | 10572 KB |
| [1437_bfs.java](1437_bfs.java) | Java 1.8 | bfs | O(P) | AC | 0.156 s | 20420 KB |
| [1437_bfs.py](1437_bfs.py) | Python 3.12 x64 | bfs | O(P) | AC | 0.406 s | 17212 KB |
| [1437_bfs.rs](1437_bfs.rs) | Rust 1.75 x64 | bfs | O(P) | AC | 0.062 s | 3104 KB |
