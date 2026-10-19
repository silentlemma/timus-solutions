# 1984. Una circunferencia que toca todos los discos unitarios

[Timus 1984](https://acm.timus.ru/problem.aspx?space=1&num=1984) · dificultad 214 · geometry

Problema popular, del Campeonato Abierto de la UrFU 2013.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Colocar `n` discos de radio 1 dentro de una circunferencia, con
interiores disjuntos, de modo que cada disco sea tangente interiormente
a la frontera exterior. Hallar el mínimo radio exterior. La entrada es
un entero con `1≤n≤10`. Límites: 0,5 segundos y 64 MB.

## Entrada

Un entero `n`.

## Salida

Un número real: el radio mínimo.

## Evaluación

Los números se comparan con error absoluto o relativo 10⁻⁶.

## Ejemplos

Entrada:

```
2
```

Salida:

```
2
```

## Solución

Con un disco, la respuesta es 1. Para `n≥2`, sean `R` el radio exterior
y `r=R−1>0`. La tangencia interior obliga a que todos los centros estén
en la circunferencia concéntrica de radio `r`. Dos centros cualesquiera
deben estar separados al menos por 2.

Ordenar los centros por ángulo polar. Los `n` intervalos angulares
cíclicos suman `2π`, así que alguno tiene tamaño `α≤2π/n≤π`. La
distancia de esa pareja es `2r sin(α/2)≤2r sin(π/n)`. Como debe ser al
menos 2, resulta `R≥1+1/sin(π/n)`.

La cota se alcanza colocando los centros en los vértices de un polígono
regular de `n` lados sobre una circunferencia de radio `1/sin(π/n)`. Los
centros vecinos distan exactamente 2 y las demás parejas no están más
cerca. Cada disco unitario llega al radio exterior `R=r+1`, cumpliendo
todas las tangencias. Por tanto, para `n≥2` el mínimo es `1+1/sin(π/n)`.

En el ejemplo `n=2`, los centros son opuestos en una circunferencia de
radio 1. Los discos unitarios se tocan y caben en una circunferencia de
radio 2, por lo que la respuesta es 2.

La fórmula requiere un número constante de operaciones: tiempo y memoria
`O(1)`. La doble precisión y diez cifras decimales bastan para la
tolerancia en todo el rango permitido.

Trampas:

- Cada disco debe tocar la frontera exterior; el empaquetamiento sin esa
  condición es otro problema.
- Los centros están a distancia `R−1`, no `R`.
- Resolver primero el caso de un disco para evitar dividir entre `sin(π)`.
- Usar `π/n` en radianes.
- Los interiores no pueden solaparse, pero los discos sí pueden tocarse.

## Notas por lenguaje

Los cinco programas evalúan la misma fórmula en doble precisión. C++
obtiene π mediante `acos(-1)`; Python, Go, Java y Rust usan las
constantes estándar de π. Java fija la configuración regional para
imprimir el punto decimal.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1984_geometry.cpp](1984_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 444 KB |
| [1984_geometry.go](1984_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 1100 KB |
| [1984_geometry.java](1984_geometry.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1820 KB |
| [1984_geometry.py](1984_geometry.py) | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 396 KB |
| [1984_geometry.rs](1984_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 256 KB |
