# 1647. ¡Divide la isla!

[Timus 1647](https://acm.timus.ru/problem.aspx?space=1&num=1647) · dificultad 833 · geometry

Problema original de Vladislav Isenbaev (preparado por Alexander Ipatov), del USU Junior Contest, octubre de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una isla es un triángulo no degenerado. Hay que hallar dos puntos S y T
de su costa tales que el segmento ST divida la isla en dos partes de
igual área e igual longitud de costa, o decir que no existen.

## Entrada

Seis enteros x₁ y₁ x₂ y₂ x₃ y₃, de valor absoluto hasta 2000.

## Salida

`YES` y las coordenadas de S y T con precisión 10⁻⁹, o `NO`. Se acepta
cualquier segmento válido.

## Ejemplos

### Ejemplo 1

Entrada:

```
0 0 10 0 0 10
```

Salida:

```
YES
0 0
5 5
```

### Ejemplo 2

Entrada:

```
0 3 4 0 3 4
```

Salida:

```
YES
1.741248277008306 3.580416092336102
3.445803840397070 0.415647119702198
```

## Solución

Se recorre la costa por longitud de arco. S va en la posición s y T
medio perímetro más allá, así que la costa siempre queda partida por la
mitad; sea f(s) el área del lado de S a T menos la mitad del triángulo.
Mover S medio perímetro intercambia las partes, así que
f(s + P/2) = −f(s), y f es continua: tiene una raíz en [0, P/2]. Por
tanto la respuesta es siempre `YES` (esas rectas
pasan por el incentro), y la bisección encuentra una raíz.

El área de una parte sale de la fórmula del lazo sobre S, los vértices
que se cruzan camino de T y T, con los vértices anotados en sus
posiciones de arco dos vueltas seguidas, para que pasar por el primer
vértice no requiera un caso especial. Doscientos pasos de bisección
bastan para alcanzar la precisión de double. `O(1)` con una
constante de unos miles de operaciones.

Detalles a tener en cuenta:

- `NO` nunca es la respuesta, aunque el enunciado lo permita;
- la cuerda puede empezar o acabar en un vértice, como en el primer
  ejemplo; la parametrización por arco lo cubre sin casos especiales;
- un verificador acepta cualquier cuerda válida, ya que puede haber
  hasta tres.

Las cuerdas del programa pasan el verificador en todas las pruebas, igual
que las de una implementación aceptada independiente en 180 triángulos
aleatorios.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1647_geometry.cpp](1647_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 216 KB |
| [1647_geometry.go](1647_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1116 KB |
| [1647_geometry.java](1647_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1988 KB |
| [1647_geometry.py](1647_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.093 s | 848 KB |
| [1647_geometry.rs](1647_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 276 KB |
