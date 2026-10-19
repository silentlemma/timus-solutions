# 2067. Parejas a las que no se suma un tercero

[Timus 2067](https://acm.timus.ru/problem.aspx?space=1&num=2067) · dificultad 326 · geometry

Problema original de Alexey Danilyuk, preparado por Alexey Danilyuk y Alexander Borzunov, del Concurso Regional por Equipos de Programación de los Urales 2015.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Se dan n puntos distintos (sᵢ, rᵢ). Para dos puntos v, u sea p(v, u) la
distancia entre ellos, y para tres puntos sea p(v, u, w) la mitad de la
suma de las tres distancias entre pares. Dos puntos distintos v, u
forman una pareja óptima si p(v, u) ≥ p(v, u, w) para todo punto w.
Hallar todas las parejas óptimas. Los límites son 2 segundos y 64 MB.

## Entrada

El número de puntos n, 2 ≤ n ≤ 2·10⁵, y después n líneas con los
enteros sᵢ y rᵢ, −10⁸ ≤ sᵢ, rᵢ ≤ 10⁸. No hay puntos repetidos.

## Salida

El número de parejas óptimas y después las parejas, una por línea, con
los números de sus puntos en el orden de entrada. Las parejas y los dos
números de cada pareja pueden ir en cualquier orden.

## Evaluación

Un comprobador compara el número de parejas y el conjunto de parejas,
con los dos números de cada una en cualquier orden.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
2 3
7 6
```

Salida:

```
1
1 2
```

### Ejemplo 2

Entrada:

```
3
5 5
2 -4
-4 2
```

Salida:

```
0
```

## Solución

Multiplicando la condición por 2: p(v, u) ≥ p(v, u, w) significa
p(v, u) ≥ p(v, w) + p(w, u). La desigualdad triangular dice lo
contrario, así que debe darse la igualdad, y eso ocurre exactamente
cuando w está en el segmento vu (para w = v o w = u se cumple sola).
Por tanto v y u son una pareja óptima exactamente cuando todos los
puntos están en el segmento entre ellos.

Si los puntos no están todos en una recta, no hay parejas óptimas. Si lo
están, los únicos candidatos son los dos extremos de la recta, y sirven:
todos los demás puntos quedan entre ellos. Dos puntos siempre están
alineados, así que n = 2 da la única pareja 1 2.

La alineación se comprueba de forma exacta con el producto vectorial
(p₂ − p₁) × (pᵢ − p₁) = 0, cuyos términos llegan a 4·10¹⁶ y caben en
enteros de 64 bits. Los extremos son el menor y el mayor punto en el
orden por s y luego por r. Todo cuesta O(n), salvo la ordenación en Python: O(n log n).

En el segundo ejemplo los tres puntos forman un triángulo, así que la
respuesta es 0.

## Notas por lenguaje

Los productos necesitan enteros de 64 bits.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2067_geometry.cpp](2067_geometry.cpp) | G++ 13.2 x64 | geometry | O(n) | AC | 0.296 s | 2888 KB |
| [2067_geometry.go](2067_geometry.go) | Go 1.14 x64 | geometry | O(n) | AC | 0.281 s | 8768 KB |
| [2067_geometry.java](2067_geometry.java) | Java 1.8 | geometry | O(n) | AC | 0.109 s | 3708 KB |
| [2067_geometry.py](2067_geometry.py) | Python 3.12 x64 | geometry | O(n log n) | AC | 0.531 s | 62832 KB |
| [2067_geometry.rs](2067_geometry.rs) | Rust 1.75 x64 | geometry | O(n) | AC | 0.062 s | 10476 KB |
