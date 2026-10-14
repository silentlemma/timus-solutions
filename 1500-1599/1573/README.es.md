# 1573. Alquimia

[Timus 1573](https://acm.timus.ru/problem.aspx?space=1&num=1573) · dificultad 108 · math

Problema original de Alexander Ipatov, del USU Junior Contest (XIV Campeonato Abierto por Equipos de Programación para Escolares de la Región de Sverdlovsk), octubre de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Sandro tiene tres bolsas de reactivos distintos: B azules, R rojos y Y
amarillos (de 1 a 100 cada una). Una poción necesita un reactivo de cada
color de su receta, todos de colores distintos. Hay que contar los
conjuntos de reactivos con los que se hace la poción.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

B, R e Y, y luego K y los K colores de la receta (Blue, Red o Yellow).

## Salida

El número de maneras.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3 5
3
Red
Yellow
Blue
```

Salida:

```
30
```

## Solución

Cada color de la receta toma un reactivo de su propia bolsa, y las
elecciones son independientes, así que la respuesta es el producto de
los tamaños de las bolsas que nombra la receta. Es como mucho
100³ = 10⁶. `O(K)`.

Detalles a tener en cuenta:

- la entrada da las bolsas en el orden azul, rojo, amarillo, mientras
  que la receta del ejemplo empieza por el rojo;
- solo cuentan los colores de la receta (pruebas 02, 03).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1573_math.cpp](1573_math.cpp) | G++ 13.2 x64 | math | O(K) | AC | 0.015 s | 416 KB |
| [1573_math.go](1573_math.go) | Go 1.14 x64 | math | O(K) | AC | 0.015 s | 1084 KB |
| [1573_math.java](1573_math.java) | Java 1.8 | math | O(K) | AC | 0.125 s | 1628 KB |
| [1573_math.py](1573_math.py) | Python 3.12 x64 | math | O(K) | AC | 0.078 s | 452 KB |
| [1573_math.rs](1573_math.rs) | Rust 1.75 x64 | math | O(K) | AC | 0.015 s | 408 KB |
