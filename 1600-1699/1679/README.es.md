# 1679. La torre de Scrooge

[Timus 1679](https://acm.timus.ru/problem.aspx?space=1&num=1679) · dificultad 1009 · geometry

Problema original del folclore, del Ural SU Contest en el campus de verano de Petrozavodsk, agosto de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una isla redonda de radio R tiene el centro en el origen. Decidir si
algún cuadrado inscrito en su circunferencia tiene los dos puntos dados
en su borde.

## Entrada

T (1 ≤ T ≤ 1000) y luego T líneas de enteros R, x1, y1, x2, y2
(1 ≤ R ≤ 10000); ambos puntos están en el círculo.

## Salida

YES o NO para cada línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
2 1 1 1 -1
2 1 1 0 0
1 1 0 -1 0
```

Salida:

```
YES
NO
YES
```

## Solución

Cada lado de un cuadrado inscrito es una cuerda a distancia s = R / √2
del centro, y el círculo recorta de su recta exactamente ese lado. Así,
un punto del círculo está en un lado si y solo si está en su recta.

Sea u la normal unitaria del lado que pasa por el primer punto P, es
decir, u · P = s. Los demás lados tienen normales −u y u girada ±90°, y
para ellos u · Q = s equivale a u · Q′ = s, donde Q′ es el segundo
punto Q girado 0°, 180° o ±90°. Por tanto la respuesta es YES si y solo
si para uno de los cuatro giros Q′ los puntos P y Q′ están en una recta
común a distancia s del centro:

- si Q′ = P, vale cualquier recta por P a distancia s, que existe si y
  solo si |P| ≥ s, es decir, 2|P|² ≥ R²;
- si no, es la recta por P y Q′, a distancia |P × Q′| / |P − Q′|, y la
  prueba es 2 (P × Q′)² = R² |P − Q′|².

Todo son comprobaciones enteras exactas, por debajo de 10¹⁷. `O(T)`.

Trampa: los ángulos en coma flotante son frágiles aquí. Un punto a
distancia exactamente s, el punto medio de un lado (R = 12, (6, 6), por
ejemplo), da un arcocoseno de 1 que el redondeo puede sacar de rango;
el test 02 contiene tales puntos.

Las respuestas coinciden con una búsqueda en coma flotante sobre las
orientaciones para todos los pares de puntos con R ≤ 3 y en 21000 casos
aleatorios con R ≤ 30.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1679_geometry.cpp](1679_geometry.cpp) | G++ 13.2 x64 | geometry | O(T) | AC | 0.015 s | 128 KB |
| [1679_geometry.go](1679_geometry.go) | Go 1.14 x64 | geometry | O(T) | AC | 0.031 s | 1196 KB |
| [1679_geometry.java](1679_geometry.java) | Java 1.8 | geometry | O(T) | AC | 0.109 s | 504 KB |
| [1679_geometry.py](1679_geometry.py) | Python 3.12 x64 | geometry | O(T) | AC | 0.062 s | 892 KB |
| [1679_geometry.rs](1679_geometry.rs) | Rust 1.75 x64 | geometry | O(T) | AC | 0.046 s | 268 KB |
