# 1116. Recortar una función constante a trozos con el dominio de otra

[Timus 1116](https://acm.timus.ru/problem.aspx?space=1&num=1116) · dificultad 333 · two_pointers

Problema original de Oleg Kats, del USU Open Collegiate Programming Contest, octubre de 2001, Junior Session.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una función constante a trozos es una lista de intervalos semiabiertos
disjuntos `[A, B)` con un valor `Y` en cada uno, ordenada por `A`; dos
intervalos que se tocan nunca tienen el mismo valor. Dadas dos funciones
así, `F1` y `F2` (cada una con `1 ≤ N ≤ 15000` intervalos,
`|A|, |B| < 32000`, `A < B`, `|Y| ≤ 100`), construye `F`: vale `F1` donde
`F1` está definida y `F2` no, y no está definida en ningún otro sitio.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

Dos líneas, una por función: `N` y luego `N` ternas `A B Y`.

## Salida

Una línea en el mismo formato que describe `F`; un `0` solo si `F` no
está definida en ningún punto.

## Evaluación

La salida se compara token a token; los espacios en blanco de más no
importan.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 -1 1 2 1 3 4 4 6 3
2 -2 2 1 5 7 5
```

Salida:

```
2 2 3 4 4 5 3
```

## Solución

Ambas listas están ordenadas, así que basta un recorrido con dos
punteros. Para cada intervalo `[A, B)` de `F1` se avanza un cursor de `A`
a `B`: se saltan los intervalos de `F2` que terminan en el cursor o antes;
si el siguiente ya cubre el cursor, el cursor salta a su final; si no, se
emite el trozo desde el cursor hasta el inicio de ese intervalo (o hasta
`B`) con el valor `Y`. El puntero en `F2` nunca retrocede, así que todo el
recorrido es `O(N1 + N2)`.

Los trozos no necesitan unirse: los trozos de un mismo intervalo están
separados por huecos, y los de dos intervalos distintos solo pueden
tocarse donde se tocaban los intervalos, que tienen valores distintos.

Detalles a tener en cuenta:

- los intervalos son semiabiertos: `[0, 2)` y `[2, 4)` se tocan pero no se
  solapan, así que un intervalo de `F2` que termina en `x` no cubre `x`;
- un intervalo de `F2` puede abarcar varios intervalos de `F1`, así que su
  puntero no debe avanzar solo porque un intervalo de `F1` haya terminado;
- cuando no queda nada, la respuesta es solo el número `0`.

Las respuestas se comprobaron con una fuerza bruta que evalúa ambas
funciones en cada celda unitaria del rango de coordenadas y vuelve a unir
las rachas de valores iguales en intervalos, en todas las pruebas y en 100
pares aleatorios.

## Soluciones optimizadas

Las versiones en C++ y Go guardan cada intervalo como tres enteros de 16 bits con signo. Conservan la primera lista y leen la segunda según se necesita, manteniendo solo el intervalo de recorte actual. Cada intervalo de recorte se lee como máximo una vez. Los intervalos de salida se guardan en un vector compacto porque su cantidad se imprime primero. El tiempo es O(N1 + N2).

El envío aceptado en G++ 13.2 x64 tarda 0.062 s frente a 0.046 s de la base y usa 444 KB frente a 1880 KB.

Las implementaciones base aceptadas [1116_two_pointers.java](1116_two_pointers.java), [1116_two_pointers.py](1116_two_pointers.py), [1116_two_pointers.rs](1116_two_pointers.rs) también cubren el conjunto rápido: en la instantánea de comparación guardada ya cumplen la regla de inclusión por estar en el 15% superior o en los diez primeros puestos, tanto en tiempo como en memoria. Se reutilizan los mismos fuentes sin copias idénticas. Un asterisco señala una versión que todavía no alcanza el objetivo de clasificación de su lenguaje.

## Notas por lenguaje

Estas notas describen las implementaciones sencillas.

- Todos los lenguajes hacen el mismo recorrido; Go usa escritura con búfer,
  los demás arman una cadena de salida.

## Soluciones

### Sencillas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1116_two_pointers.cpp](1116_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N1 + N2) | AC | 0.046 s | 1880 KB | 11279235 |
| [1116_two_pointers.go](1116_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N1 + N2) | AC | 0.062 s | 6832 KB | 11279236 |
| [1116_two_pointers.java](1116_two_pointers.java) \* | Java 1.8 | two_pointers | O(N1 + N2) | AC | 0.125 s | 5400 KB | 11279239 |
| [1116_two_pointers.py](1116_two_pointers.py) \* | Python 3.12 x64 | two_pointers | O(N1 + N2) | AC | 0.140 s | 13144 KB | 11279238 |
| [1116_two_pointers.rs](1116_two_pointers.rs) \* | Rust 1.75 x64 | two_pointers | O(N1 + N2) | AC | 0.015 s | 2112 KB | 11279241 |

### Optimizadas

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria | Envío |
|---|---|---|---|---|---|---|---|
| [1116_two_pointers_optimized.cpp](1116_two_pointers_optimized.cpp) \* | G++ 13.2 x64 | two_pointers | O(N1 + N2) | AC | 0.062 s | 444 KB | 11310386 |
| [1116_two_pointers_optimized.go](1116_two_pointers_optimized.go) \* | Go 1.14 x64 | two_pointers | O(N1 + N2) | AC | 0.031 s | 1712 KB | 11310385 |

\* Accepted; aún no se alcanza la meta de clasificación. Esta versión admite más optimización.
