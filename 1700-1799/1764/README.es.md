# 1764. Transiberiano

[Timus 1764](https://acm.timus.ru/problem.aspx?space=1&num=1764) · dificultad 1810 · math

Problema original de Alexander Ipatov, del XIV Campeonato de los Urales de Programación Competitiva, 10 de abril de 2010.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

La carga va de una ciudad a otra por cuatro rutas, y seis puentes la
limitan. Con los puentes numerados en el orden de la entrada, la ruta 1
cruza los puentes 1, 2 y 6, la ruta 2 cruza 4, 5 y 6, la ruta 3 cruza
4, 2 y 3, y la ruta 4 cruza 1, 5 y 3; cada puente lleva como mucho su
capacidad diaria en total. Elegir las cargas de las rutas, no
necesariamente enteras, para que el total sea lo mayor posible.

## Entrada

Las seis capacidades, números enteros de 1 a 10⁹.

## Salida

Las cuatro cargas, con un error de a lo sumo 10⁻³. Se acepta cualquier
plan óptimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
70 30 60 100 20 50
```

Salida:

```
20.000 10.000 10.000 10.000
```

## Solución

Cada puente está en exactamente dos rutas, y los seis puentes dan los
seis pares de las cuatro rutas. Así que la tarea es un programa lineal:
maximizar x₁ + x₂ + x₃ + x₄ con xᵢ + xⱼ ≤ c para cada puente y xᵢ ≥ 0.
Las cargas posibles forman un politopo acotado, y el mejor plan está en
uno de sus vértices, donde cuatro de las diez restricciones se cumplen
con igualdad.

Se prueban las 210 formas de elegir cuatro restricciones. Cada una da
un sistema 4 × 4 con coeficientes 0, 1 y −1, que se resuelve
exactamente por la regla de Cramer: las cargas son numeradores enteros
sobre un mismo denominador entero, así que comprobar las demás
restricciones y comparar totales no requiere redondeo alguno. Se
imprime el mejor vértice factible. `O(1)`.

En el ejemplo los puentes de Kotelnich (30) y Vyatskiye Polyany (20)
juntos están en cada ruta una vez, así que ningún plan lleva más de 50.
El programa imprime 30, 20, 0 y 0, otro plan con el mismo total que el
del ejemplo.

Trampas:

- las mejores cargas pueden ser medias, como cuando todas las
  capacidades son 1 y cada ruta lleva 0,5;
- el plan no es único, así que el verificador compara totales;
- con capacidades de hasta 10⁹, buscar vértices en coma flotante puede
  aceptar o rechazar por error uno que está en el borde.

Los totales coinciden con una búsqueda sobre todas las cargas
semienteras en 120 casos aleatorios con capacidades pequeñas y con una
implementación aceptada independiente en 90 casos aleatorios, todos
comprobados contra las capacidades.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1764_math.cpp](1764_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 224 KB |
| [1764_math.go](1764_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 2404 KB |
| [1764_math.java](1764_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 2712 KB |
| [1764_math.py](1764_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 824 KB |
| [1764_math.rs](1764_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 284 KB |
