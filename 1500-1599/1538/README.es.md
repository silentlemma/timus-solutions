# 1538. Torres de guardia

[Timus 1538](https://acm.timus.ru/problem.aspx?space=1&num=1538) · dificultad 1273 · geometry

Problema original de Alexander Ipatov, del Octavo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 3 de marzo de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Dadas N colinas (5 ≤ N ≤ 5000) con coordenadas enteras de valor
absoluto hasta 10⁸, sin tres en una recta, hay que elegir cinco que sean
los vértices de un pentágono convexo, o indicar que no las hay.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y luego las coordenadas de las colinas, una por línea.

## Salida

`No`, o `Yes` y los números de cinco colinas en sentido antihorario
alrededor del pentágono. Se acepta cualquier pentágono así.

## Ejemplos

### Ejemplo 1

Entrada:

```
6
1 0
0 1
1 2
2 0
2 2
3 1
```

Salida:

```
Yes
2 1 4 5 3
```

## Solución

Por el teorema de Erdős–Szekeres, nueve puntos cualesquiera del plano
sin tres en una recta contienen cinco en posición convexa (ocho no
bastan). Así que bastan las primeras min(N, 9) colinas: se prueba cada
uno de sus a lo sumo C(9, 5) = 126 subconjuntos de cinco, se construye
su envolvente convexa con la cadena monótona de Andrew y se escribe el
primer subconjunto cuya envolvente tiene los cinco puntos. La cadena
recorre la envolvente en sentido antihorario. La respuesta solo puede
ser `No` cuando N ≤ 8. El resto de la entrada ni siquiera hace falta
leerlo. Los productos vectoriales llegan a unos 8·10¹⁶, así que hacen
falta 64 bits. `O(1)` aparte de leer nueve puntos.

Detalles a tener en cuenta:

- ocho colinas pueden no tener pentágono convexo (prueba 04), pero una
  novena siempre crea uno (prueba 05);
- las colinas deben ir en sentido antihorario, sea cual sea su orden en
  la entrada (prueba 06);
- con coordenadas de 10⁸ los productos vectoriales no caben en 32 bits
  (prueba 07);
- hay varias respuestas, así que las pruebas usan un verificador (todas
  las pruebas).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1538_geometry.cpp](1538_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 196 KB |
| [1538_geometry.go](1538_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.046 s | 1160 KB |
| [1538_geometry.java](1538_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.156 s | 2812 KB |
| [1538_geometry.py](1538_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 1176 KB |
| [1538_geometry.rs](1538_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.031 s | 472 KB |
