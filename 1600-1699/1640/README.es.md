# 1640. Anillo de frío

[Timus 1640](https://acm.timus.ru/problem.aspx?space=1&num=1640) · dificultad 177 · geometry

Problema original de Dmitry Ivankov (preparado por Alexander Ipatov), del USU Junior Contest, octubre de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay demonios en n puntos de la red. Sandro puede teletransportarse a
cualquier punto sin demonio y lanzar ahí un anillo de hielo de radio a
lo sumo 10000 centrado en él. El anillo debe matar al menos a un demonio
(uno sobre la circunferencia), y todos los demonios que sigan vivos deben
quedar dentro. Hay que dar un centro y un radio.

## Entrada

n (1 ≤ n ≤ 100) y luego las coordenadas de los demonios, enteros de
valor absoluto hasta 1000, medidas desde la posición actual de Sandro.
Todos los demonios están en puntos distintos y ninguno en el de Sandro.

## Salida

El centro y el radio con precisión 10⁻⁹. Se acepta cualquier respuesta
válida.

## Ejemplos

### Ejemplo 1

Entrada:

```
7
1 1
1 5
3 6
5 3
8 0
9 5
5 9
```

Salida:

```
5 4 5
```

### Ejemplo 2

Entrada:

```
2
0 2
2 0
```

Salida:

```
1 1 1.41421356237309
```

## Solución

No hace falta teletransportarse. La posición de Sandro no tiene demonio,
y la circunferencia a su alrededor que pasa por el demonio más lejano lo
mata y encierra a todos los demás. Su radio es a lo sumo 1000 · √2, muy
por debajo de 10000. `O(n)`.

Detalles a tener en cuenta:

- el centro no puede ser el punto de un demonio, así que el centro del
  menor círculo envolvente no siempre vale; el punto de partida siempre;
- hay muchas respuestas válidas, así que un verificador acepta cualquier
  circunferencia que cumpla las reglas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1640_geometry.cpp](1640_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.015 s | 148 KB |
| [1640_geometry.go](1640_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.015 s | 1112 KB |
| [1640_geometry.java](1640_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.140 s | 2032 KB |
| [1640_geometry.py](1640_geometry.py) | Python 3.12 x64 | geometry | O(n) | AC | 0.078 s | 488 KB |
| [1640_geometry.rs](1640_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.015 s | 256 KB |
