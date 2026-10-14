# 1566. Postales triangulares

[Timus 1566](https://acm.timus.ru/problem.aspx?space=1&num=1566) · dificultad 3034 · geometry

Problema original de Vladimir Yakovlev, del XII Campeonato de Programación de la Universidad Estatal de los Urales, 6 de octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dados los lados enteros de un sobre triangular y de una postal
triangular, todos de como mucho 1000 milímetros, hay que decidir si la
postal cabe en el sobre. La postal se puede mover, girar y dar la
vuelta, y puede tocar los bordes del sobre.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Los lados del sobre en la primera línea y los de la postal en la
segunda.

## Salida

`YES` o `NO`.

## Ejemplos

### Ejemplo 1

Entrada:

```
30 40 50
50 36 27
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
200 200 200
210 110 110
```

Salida:

```
NO
```

## Solución

Un triángulo cabe en otro exactamente cuando cabe con uno de sus lados
apoyado en un lado del otro. Es un hecho conocido sobre dos triángulos,
y aquí además se comprobó: una búsqueda fina sobre los giros de la
postal, que prueba cada giro de forma exacta (existe una traslación
cuando la suma sobre los lados del sobre de la longitud por lo que la
postal sobresale más allá de la dirección de ese lado no pasa del doble
del área), coincidió con esta regla en unos 600 pares aleatorios, igual
que un programa independiente.

Así que hay que probar 3 · 3 · 2 colocaciones: un lado de la postal
sobre un lado del sobre, con la postal volteada o no. Con el lado del
sobre de (0, 0) a (m, 0), su vértice en (w, H), y el vértice de la
postal en (u, h) sobre el inicio de su lado de longitud ℓ, la postal se
desliza t a lo largo del lado. Cabe cuando ℓ ≤ m, h ≤ H y algún t de
[0, m − ℓ] deja su vértice entre los otros dos lados del sobre:

h·w / H ≤ t + u ≤ m − h·(m − w) / H.

Ambos extremos son lineales en t, así que es una intersección de
intervalos. Tocar cuenta, así que cada comparación admite 10⁻⁹. Un sobre
plano, si aparece, solo admite una postal plana que no sea más larga.
Todo tarda tiempo constante.

Detalles a tener en cuenta:

- la postal puede ser el propio sobre, tocándolo en todas partes
  (prueba 03);
- no basta un lado largo: una aguja de longitud 999 con un extremo de
  2 mm es demasiado ancha en ese extremo para entrar en una esquina de
  60° de un sobre equilátero de 1000 mm (prueba 05);
- el vértice de la postal puede quedar más allá de los extremos de su
  propio lado si tiene ahí un ángulo obtuso, y lo mismo el del sobre
  (prueba 07).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1566_geometry.cpp](1566_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 128 KB |
| [1566_geometry.go](1566_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1064 KB |
| [1566_geometry.java](1566_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.140 s | 1716 KB |
| [1566_geometry.py](1566_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.109 s | 656 KB |
| [1566_geometry.rs](1566_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.062 s | 232 KB |
