# 1749. Suma periódica

[Timus 1749](https://acm.timus.ru/problem.aspx?space=1&num=1749) · dificultad 2053 · matrix

Problema original de Petr Lezhankin, del concurso de la USATU de Ufá en el campus de entrenamiento de verano de Petrozavodsk, agosto de 2009.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

S(t) es la suma de todas las subcadenas de la escritura decimal de t,
leídas como números con ceros iniciales permitidos, y F(t, k) es t
escrito k veces seguidas. Dados p, k y m, hallar S(F(p, k)) módulo m.

## Entrada

p (1 ≤ p < 10¹⁰⁰⁰⁰⁰) y luego k y m (1 ≤ k, m ≤ 10⁹).

## Salida

S(F(p, k)) módulo m.

## Ejemplos

### Ejemplo 1

Entrada:

```
1205
3 999999999
```

Salida:

```
847123538
```

## Solución

Se leen las cifras de izquierda a derecha y sea E la suma de las
subcadenas que terminan en la cifra actual. Una cifra nueva d en la
posición j alarga cada una de ellas en una cifra y empieza una nueva,
así que E pasa a 10·E + d·j, y S acumula E tras cada cifra.

Sobre una copia de p esto es lineal en el estado (S, E, J, 1), donde J
es el número de cifras antes de la copia: la posición de su i-ésima
cifra es J + i. Una pasada por p da la matriz 4 × 4 de una copia: E pasa
a 10ⁿ·E + v·J + w, con v el valor de p y w la suma de sus cifras
ponderadas por sus posiciones y potencias de diez; S gana las sumas
acumuladas de esas tres cantidades; J crece en la longitud n de p. La
potencia k-ésima de esta matriz, por cuadrados repetidos módulo m,
aplicada al estado inicial S = E = J = 0 da la respuesta.
`O(n + log k)`.

En el ejemplo, S(1205) solo vale 1575, y las tres copias dan 847123538
módulo 999999999.

Trampas:

- p tiene hasta 100 000 cifras, así que se lee como cadena;
- las subcadenas con ceros iniciales cuentan con su valor, así que una
  cifra cero también avanza las posiciones;
- con m = 1 toda respuesta es 0.

Las respuestas coinciden con una suma directa sobre todas las
subcadenas con enteros exactos en 300 casos aleatorios, y con una
implementación aceptada independiente en las pruebas grandes.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1749_matrix.cpp](1749_matrix.cpp) | G++ 13.2 x64 | matrix | O(n + log k) | AC | 0.015 s | 640 KB |
| [1749_matrix.go](1749_matrix.go) | Go 1.14 x64 | matrix | O(n + log k) | AC | 0.031 s | 1764 KB |
| [1749_matrix.java](1749_matrix.java) | Java 1.8 | matrix | O(n + log k) | AC | 0.125 s | 1196 KB |
| [1749_matrix.py](1749_matrix.py) | Python 3.12 x64 | matrix | O(n + log k) | AC | 0.156 s | 936 KB |
| [1749_matrix.rs](1749_matrix.rs) | Rust 1.75 x64 | matrix | O(n + log k) | AC | 0.015 s | 480 KB |
