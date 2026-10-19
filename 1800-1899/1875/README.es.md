# 1875. Angry Birds

[Timus 1875](https://acm.timus.ru/problem.aspx?space=1&num=1875) · dificultad 965 · geometry

Problema original de Fedor Fominykh, del Concurso Regional de Programación por Equipos de los Urales 2011.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Un tirachinas en el origen lanza pájaros a cualquier velocidad y con
cualquier ángulo; solo actúa la gravedad, así que cada uno vuela por
una parábola abierta hacia abajo. Los pájaros atraviesan los monos que
golpean. Cinco monos cuelgan en puntos de coordenadas positivas, sin
dos en una misma recta con el tirachinas. ¿Cuál es el menor número de
disparos que los alcanza a todos?

## Entrada

Cinco líneas con las coordenadas de los monos, enteros positivos hasta
10 000.

## Salida

El menor número de disparos.

## Ejemplos

### Ejemplo 1

Entrada:

```
1 5
2 8
3 9
4 8
5 5
```

Salida:

```
1
```

## Solución

Un disparo sigue y = bx − cx² con c > 0, y cualquier curva así se
puede volar. Dividiendo entre x, la pendiente y/x = b − cx decrece
linealmente en x. Así que un disparo alcanza varios monos exactamente
cuando sus pendientes y/x, como función de x, están en una misma recta
decreciente. Dos monos pueden compartir disparo solo si tienen x
distintas y el de más a la derecha tiene menor pendiente. Esa pareja
fija el disparo, y los demás monos sobre él se hallan con la prueba de
la recta, todo en enteros tras quitar denominadores. Con cada mono
suelto y el disparo de cada pareja como conjuntos candidatos, una
programación dinámica sobre los 2⁵ subconjuntos halla el menor número
de conjuntos que cubre a los cinco. `O(1)`.

En el ejemplo las pendientes son 5, 4, 3, 2, 1 en x = 1 … 5: una recta
decreciente, así que la parábola y = x(6 − x) alcanza a todos los monos
de un disparo.

Trampas:

- los monos uno encima de otro (misma x) nunca comparten disparo;
- una pareja cuya pendiente crece con x necesitaría una parábola
  abierta hacia arriba, que la gravedad no permite;
- los productos llegan a unos 10¹⁶, así que hacen falta enteros de 64
  bits.

Las respuestas coinciden con una implementación aceptada independiente
en 300 niveles aleatorios, muchos con tres a cinco monos en una misma
parábola.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1875_geometry.cpp](1875_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 196 KB |
| [1875_geometry.go](1875_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1072 KB |
| [1875_geometry.java](1875_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.156 s | 1700 KB |
| [1875_geometry.py](1875_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.125 s | 588 KB |
| [1875_geometry.rs](1875_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.062 s | 236 KB |
