# 1430. Crimen y castigo

[Timus 1430](https://acm.timus.ru/problem.aspx?space=1&num=1430) · dificultad 461 · number_theory

Problema original de Nikita Rybak, Ilya Grebnov y Dmitry Kovalioff, de Timus Top Coders: First Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los artículos cuestan A o B cada uno, se puede comprar cualquier
cantidad de cada uno y hay N para gastar (1 ≤ A, B, N ≤ 2·10⁹). Hay que
hallar cantidades x e y con x·A + y·B ≤ N lo mayor posible; vale
cualquier par óptimo.

Límite de tiempo: 0.5 segundos. Límite de memoria: 64 MB.

## Entrada

A, B y N.

## Salida

x e y.

## Ejemplos

### Ejemplo 1

Entrada:

```
8 5 22
```

Salida:

```
2 1
```

## Solución

Sea A ≥ B (si no, se intercambian y luego se intercambia la respuesta).
Si x ≥ B, entonces B artículos de precio A pueden cambiarse por A de
precio B con el mismo total, así que alguna respuesta óptima tiene
x < B; y x·A ≤ N da x ≤ N / A. Así que x va de 0 a min(N / A, B − 1), y
para cada x el resto compra y = (N − x·A) / B artículos de precio B.
Como A ≥ B, o bien B ≤ √N o bien N / A < √N, así que hay como mucho unos
44 722 valores de x; además el bucle para en cuanto se gasta justo N.
`O(√N)`.

Detalles a tener en cuenta:

- productos como x·A caben en 32 bits con signo (pruebas 03, 06);
- si ambos precios superan N, no se compra nada (prueba 12);
- la respuesta no es única, así que las pruebas usan un verificador
  (prueba 02).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1430_number_theory.cpp](1430_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(sqrt N) | AC | 0.031 s | 128 KB |
| [1430_number_theory.go](1430_number_theory.go) | Go 1.14 x64 | number_theory | O(sqrt N) | AC | 0.031 s | 1068 KB |
| [1430_number_theory.java](1430_number_theory.java) | Java 1.8 | number_theory | O(sqrt N) | AC | 0.109 s | 1684 KB |
| [1430_number_theory.py](1430_number_theory.py) | Python 3.12 x64 | number_theory | O(sqrt N) | AC | 0.109 s | 468 KB |
| [1430_number_theory.rs](1430_number_theory.rs) | Rust 1.75 x64 | number_theory | O(sqrt N) | AC | 0.062 s | 220 KB |
