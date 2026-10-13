# 1482. Juego del triángulo

[Timus 1482](https://acm.timus.ru/problem.aspx?space=1&num=1482) · dificultad 2928 · geometry

Problema original de Alexander Ipatov, del Campeonato de la Universidad Estatal de los Urales, 7 de octubre de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

En un mapa hay un triángulo no degenerado dibujado y una ficha
triangular (todas las coordenadas son enteros de hasta 2000 en valor
absoluto). En un movimiento la ficha puede trasladarse o girarse, pero
nunca darse la vuelta. ¿Puede un solo movimiento poner los vértices de
la ficha exactamente sobre los dibujados? Se escribe 0 si no; 1 dx dy
para una traslación; si no, 2 x0 y0 A para un giro alrededor de
(x0, y0) de A grados en sentido antihorario, 0 ≤ A < 360, con al menos
diez cifras tras el punto.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

Los vértices del triángulo dibujado y luego los de la ficha, en pares
x y.

## Salida

0, 1 dx dy o 2 x0 y0 A.

## Ejemplos

### Ejemplo 1

Entrada:

```
0 0 10 0 0 -10
0 0 10 0 0 10
```

Salida:

```
2 0.0000000000 0.0000000000 270.0000000000
```

## Solución

Los vértices solo tienen que coincidir como conjuntos, así que se
prueban las seis formas de emparejar los vértices de la ficha con los
dibujados. Un emparejamiento se logra con un movimiento justo cuando
los tres lados coinciden y ambos triángulos giran en el mismo sentido,
ya que un movimiento no refleja. Ambas comprobaciones usan cuadrados
de longitudes y productos vectoriales enteros, así que son exactas.

Si algún emparejamiento válido desplaza los tres vértices con el mismo
vector, esa traslación es la respuesta. Si no, se toma un emparejamiento
válido. El ángulo es el que forman un lado de la ficha y su imagen,
con atan2 de sus productos vectorial y escalar, llevado a [0, 360). El
centro es un vértice que no se mueve, si lo hay. Si no, está en la
mediatriz de cada vértice y su imagen: 2(t − s)·c = |t|² − |s|². Dos de
esas rectas con direcciones distintas se cortan en él, y la regla de
Cramer da el centro como fracción exacta, que se escribe con diez
cifras. `O(1)`.

Detalles a tener en cuenta:

- los vértices pueden venir en cualquier orden (pruebas 08, gen1);
- un escaleno reflejado tiene los mismos lados pero no se alcanza
  (prueba 03);
- la ficha ya colocada es una traslación de (0, 0) (prueba 02);
- un giro pequeño puede tener centro lejano, a unos 2·10⁴ en la prueba 05,
  así que conviene calcularlo exactamente y no con (I − R)⁻¹ en coma
  flotante.

## Notas por lenguaje

- C++ y Rust escriben la fracción exacta con aritmética entera: la
  parte entera y luego el resto por 10¹⁰ entre el denominador,
  redondeado. Go usa `big.Rat`, Java `BigDecimal` y Python `Fraction`.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1482_geometry.cpp](1482_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 216 KB |
| [1482_geometry.go](1482_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 1220 KB |
| [1482_geometry.java](1482_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.125 s | 2172 KB |
| [1482_geometry.py](1482_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 1092 KB |
| [1482_geometry.rs](1482_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 276 KB |
