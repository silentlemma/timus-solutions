# 1753. Estantería

[Timus 1753](https://acm.timus.ru/problem.aspx?space=1&num=1753) · dificultad 335 · geometry

Problema original de Dmitry Ivankov, del XI Concurso Individual Abierto de la Universidad Estatal de los Urales, 13 de marzo de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una estantería de longitud L tiene bordes de altura h en ambos
extremos. Un libro de altura H está de pie junto al borde izquierdo. Su
canto inferior se arrastra hacia la derecha por la estantería mientras
su lado sigue apoyado en lo alto del borde izquierdo, hasta que el
libro queda tumbado. Todo tiene grosor cero. Hallar cuánto se aleja a
la izquierda del borde izquierdo el centro del libro.

## Entrada

Enteros h, H y L (1 ≤ h < H < L ≤ 1000).

## Salida

El mayor desplazamiento del centro del libro a la izquierda del borde,
con un error de a lo sumo 10⁻⁵.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 120 200
```

Salida:

```
39.850361
```

## Solución

Se pone lo alto del borde izquierdo en (0, h) y el pie del libro en
(x, 0). El libro sigue la recta del pie a lo alto del borde, un tramo
de longitud r = √(x² + h²), así que su centro, a distancia H/2 del pie,
está en la posición horizontal x(1 − H / 2r). El desplazamiento a la
izquierda es f(x) = x(H / 2r − 1).

Su derivada es H·h² / 2r³ − 1, así que f crece mientras r³ < H·h²/2 y
decrece después, y el mejor momento es r = ∛(H·h²/2). Ese r nunca pasa
de H, así que el libro aún se apoya en el borde. Si ese r no supera h,
lo que ocurre justo cuando H ≤ 2h, el centro nunca pasa el borde y la
respuesta es 0; si no, x = √(r² − h²) y la respuesta es f(x). L no
influye, pues el libro siempre cabe en la estantería. `O(1)`.

En el ejemplo r = ∛2940 ≈ 14,33, x ≈ 12,50 y el desplazamiento es de
unos 39,85.

Trampas:

- un libro de a lo sumo el doble del borde da 0, no un desplazamiento
  negativo;
- el borde está a la izquierda, así que mover el pie a la derecha
  empuja el centro a la izquierda solo mientras el libro está empinado.

La fórmula coincide con un barrido de 200001 posiciones del pie en 100
entradas aleatorias y con una implementación aceptada independiente en
otras 300.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1753_geometry.cpp](1753_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 152 KB |
| [1753_geometry.go](1753_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1088 KB |
| [1753_geometry.java](1753_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1816 KB |
| [1753_geometry.py](1753_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 400 KB |
| [1753_geometry.rs](1753_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 244 KB |
