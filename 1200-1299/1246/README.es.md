# 1246. En qué sentido se recorre un polígono

[Timus 1246](https://acm.timus.ru/problem.aspx?space=1&num=1246) · dificultad 334 · geometry

Problema original de Evgeny Kobzev, del Concurso Individual de la Universidad Estatal de los Urales, 1 de marzo de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un perro está atado a un poste dentro de una parcela vallada, un polígono
simple de N vértices (3 ≤ N ≤ 200 000, coordenadas enteras de valor
absoluto hasta 50 000). Un corredor da vueltas y vueltas junto a la
valla, pasando por los vértices en el orden dado, y el perro persigue al
corredor por dentro. ¿Hacia dónde se enrolla la cuerda en el poste: en el sentido
de las agujas del reloj (`cw`) o en el contrario (`ccw`)?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego los N vértices en el orden del corredor.

## Salida

`cw` o `ccw`.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
0 0
0 1
1 1
1 0
```

Salida:

```
cw
```

## Solución

El perro sigue al corredor por el interior de la parcela, así que la
cuerda se enrolla en el sentido en que el corredor recorre el polígono.
Ese es el signo del área con signo del polígono por la fórmula del
zapatero, `Σ (x_i·y_{i+1} − x_{i+1}·y_i)`: positivo en sentido contrario a
las agujas del reloj y negativo en el de las agujas. El polígono es
simple y no degenerado, así que la suma nunca es cero. `O(N)`.

Detalles a tener en cuenta:

- el polígono no tiene por qué ser convexo, así que el giro en un vértice
  no dice nada; solo decide el área total (pruebas 04 y 05);
- cada término llega a 5·10⁹, más de 32 bits, así que la suma se guarda
  en 64 bits.

## Notas por lenguaje

- Python multiplica las listas de coordenadas por una copia rotada con
  `map`; los demás lenguajes usan un solo bucle.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1246_geometry.cpp](1246_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.265 s | 128 KB |
| [1246_geometry.go](1246_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.062 s | 4120 KB |
| [1246_geometry.java](1246_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.156 s | 3584 KB |
| [1246_geometry.py](1246_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.218 s | 41236 KB |
| [1246_geometry.rs](1246_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.062 s | 10468 KB |
