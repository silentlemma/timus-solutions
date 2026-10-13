# 1432. Doble suerte

[Timus 1432](https://acm.timus.ru/problem.aspx?space=1&num=1432) · dificultad 6926 · greedy

Problema original de Evgeny Krokhalev, del Séptimo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 25 de febrero de 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Los billetes tienen 2N cifras (4 ≤ 2N ≤ 1500, con ceros a la izquierda
permitidos) y llegan hasta el de todo nueves. Un billete es de la suerte
si las sumas de cifras de sus dos mitades son iguales, o si son iguales
las sumas de las cifras en posiciones impares y pares. Empezando por el
billete dado, hay que hallar el primer par de billetes consecutivos t,
t + 1 que sean ambos de la suerte (el billete dado puede ser t), o
imprimir «No solution».

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

El billete actual.

## Salida

Los dos billetes, o «No solution».

## Ejemplos

### Ejemplo 1

Entrada:

```
293087
```

Salida:

```
293149 293150
```

## Solución

Se escribe el balance de un billete como suma de cifras con signo: la
regla de las mitades cuenta la primera mitad con + y la segunda con −,
la de las posiciones alterna + y −; un billete es de la suerte cuando
uno de los dos balances es 0. Se elige qué regla hace de la suerte a t y
cuál a t + 1: cuatro combinaciones, cada una resuelta por separado, y
gana la respuesta menor.

Si t acaba en nueves tras una cifra en la posición p que es como mucho
8, entonces t + 1 tiene esa cifra uno mayor y ceros detrás. Así que,
fijado p, las condiciones son dos ecuaciones lineales en las cifras
hasta p, y los nueves tras p solo suman constantes. Además t ≥ s justo
cuando las cifras de t hasta p no son menores que las de s, así que para
cada p hay que hallar la menor cadena de cifras x ≥ s[0..p] con x_p ≤ 8
que cumpla dos ecuaciones con pesos ±1.

Si unas cifras aún pueden cumplir las ecuaciones es una prueba de
intervalos. Las posiciones se reparten en cuatro clases por los signos
de sus dos pesos, la suma de cada clase puede ser cualquier entero entre
sus cotas, y las dos ecuaciones pasan a ser condiciones sobre la
diferencia de las sumas de las clases «ambos +» y «ambos −» y de las dos
mixtas, más una comprobación de paridad. Con conteos prefijos por clase
la prueba cuesta O(1). Para cada p, primero se comprueba x = s[0..p];
si no sirve, se conserva el prefijo más largo posible de s, se toma la
menor cifra mayor que sea viable y se rellena el resto de forma voraz
con las menores cifras que encajen.
Los candidatos de distintos p y combinaciones se comparan por dónde
superan primero a s y la cifra allí, y la cadena entera solo en caso de
empate. `O(L²)` con L = 2N.

Detalles a tener en cuenta:

- el billete dado y el siguiente pueden ser ya la respuesta (prueba 08);
- el billete de todo nueves no tiene siguiente, y algunos billetes no
  tienen ningún par (pruebas 04, 05, 07, gen3);
- los dos billetes pueden usar reglas distintas (prueba 01);
- un acarreo a través de muchos nueves cambia ambos balances a la vez
  (pruebas 10, 15, 18, gen2).

## Notas por lenguaje

- Python se ejecuta con PyPy: las pruebas más grandes tardan unos 2 s
  con CPython y unos 0,4 s con PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1432_greedy.cpp](1432_greedy.cpp) | G++ 13.2 x64 | greedy | O(L^2) | AC | 0.078 s | 3680 KB |
| [1432_greedy.go](1432_greedy.go) | Go 1.14 x64 | greedy | O(L^2) | AC | 0.140 s | 6868 KB |
| [1432_greedy.java](1432_greedy.java) | Java 1.8 | greedy | O(L^2) | AC | 0.468 s | 5536 KB |
| [1432_greedy.py](1432_greedy.py) | PyPy 3.10 x64 | greedy | O(L^2) | AC | 0.984 s | 12228 KB |
| [1432_greedy.rs](1432_greedy.rs) | Rust 1.75 x64 | greedy | O(L^2) | AC | 0.078 s | 416 KB |
