# 1348. La cabra en el huerto 2

[Timus 1348](https://acm.timus.ru/problem.aspx?space=1&num=1348) · dificultad 177 · geometry

Problema original de Pavel Egorov, del Campeonato Escolar, marzo de 2005.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cabra está atada al punto C con una cuerda de longitud L, así que
alcanza todo lo que está a L o menos de C. Un bancal de piñas es el
segmento AB. Hay que hallar cuánto hay que alargar la cuerda para que la
cabra alcance al menos una piña, y cuánto para alcanzarlas todas, con
dos cifras tras el punto. Todos los números son enteros, L ≥ 0, y las
coordenadas valen como mucho 10 000 en valor absoluto.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Las coordenadas de A, B y C y la longitud L.

## Salida

Los dos alargamientos, uno por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
8 -6 8 6
0 0 7
```

Salida:

```
1.00
3.00
```

## Solución

El punto más cercano del bancal es la proyección de C sobre la recta
AB, llevada a A o a B si cae fuera del segmento. El punto de un segmento
más lejano de cualquier punto es uno de sus extremos. Así que las
respuestas son max(0, d_cerca − L) y max(0, max(|CA|, |CB|) − L). La
proyección usa t = (C − A) · (B − A) / |B − A|², limitado entre 0 y 1, y
un bancal de un solo punto, A = B, toma t = 0.

L no tiene cota superior. Se leen sus dígitos decimales acumulando
min(30000, 10 * rope + digit), y se deja de acumular al llegar a 30000.
Toda distancia es como mucho 20000√2 < 30000, así que este límite conserva
ambas respuestas y evita desbordar un entero o una conversión a coma
flotante. La geometría tarda `O(1)`; contando la entrada, el tiempo y el
espacio son `O(k)`, donde k es el número de caracteres de entrada.

Detalles a tener en cuenta:

- el bancal puede ser un solo punto (pruebas 02 y 08);
- con C en la recta del bancal más allá de un extremo, el punto más
  cercano es ese extremo, no la proyección (prueba 04);
- una cuerda que ya basta necesita 0, no un número negativo (prueba 05);
- L puede superar los rangos enteros y de coma flotante: hay que limitarlo
  al leer sus dígitos, sin convertir el token completo (pruebas 09–11).

## Notas por lenguaje

- Las cinco soluciones usan las mismas fórmulas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1348_geometry.cpp](1348_geometry.cpp) | G++ 13.2 x64 | geometry | O(k) | AC | 0.015 s | 412 KB |
| [1348_geometry.go](1348_geometry.go) | Go 1.14 x64 | geometry | O(k) | AC | 0.031 s | 1088 KB |
| [1348_geometry.java](1348_geometry.java) | Java 1.8 | geometry | O(k) | AC | 0.125 s | 1856 KB |
| [1348_geometry.py](1348_geometry.py) | Python 3.12 x64 | geometry | O(k) | AC | 0.078 s | 552 KB |
| [1348_geometry.rs](1348_geometry.rs) | Rust 1.75 x64 | geometry | O(k) | AC | 0.031 s | 272 KB |
