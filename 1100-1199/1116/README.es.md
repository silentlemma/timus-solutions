# 1116. Recortar una función constante a trozos con el dominio de otra

[Timus 1116](https://acm.timus.ru/problem.aspx?space=1&num=1116) · dificultad 332 · two_pointers

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

## Notas por lenguaje

- Todos los lenguajes hacen el mismo recorrido; la salida se arma en un
  solo búfer.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1116_two_pointers.cpp](1116_two_pointers.cpp) | G++ 13.2 x64 | two_pointers | O(N1 + N2) | AC | 0.046 s | 1880 KB |
| [1116_two_pointers.go](1116_two_pointers.go) | Go 1.14 x64 | two_pointers | O(N1 + N2) | AC | 0.062 s | 6832 KB |
| [1116_two_pointers.java](1116_two_pointers.java) | Java 1.8 | two_pointers | O(N1 + N2) | AC | 0.125 s | 5400 KB |
| [1116_two_pointers.py](1116_two_pointers.py) | Python 3.12 x64 | two_pointers | O(N1 + N2) | AC | 0.140 s | 13144 KB |
| [1116_two_pointers.rs](1116_two_pointers.rs) | Rust 1.75 x64 | two_pointers | O(N1 + N2) | AC | 0.015 s | 2112 KB |
