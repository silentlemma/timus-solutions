# 1537. Ents

[Timus 1537](https://acm.timus.ru/problem.aspx?space=1&num=1537) · dificultad 284 · dp

Problema original de Sergey Pupyrev, del Octavo Campeonato Personal Abierto de la Universidad Estatal de los Urales, 3 de marzo de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El primer ent aprende dos palabras. Cada ent que ha aprendido w
palabras se las enseña a un ent viejo y a uno joven que aún no hablan;
después los elfos enseñan al viejo una palabra más, con lo que termina
con w + 1, y al joven w más, con lo que termina con 2w. Esto sigue sin
fin. Hay que contar los ents que saben exactamente K palabras, módulo P
(K ≤ 10⁷, P ≤ 10⁹).

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

K y P.

## Salida

El número de ents que saben exactamente K palabras, módulo P.

## Ejemplos

### Ejemplo 1

Entrada:

```
4 10
```

Salida:

```
2
```

## Solución

Sea f(w) el número de ents que saben w palabras. Cada ent salvo el
primero tuvo un único maestro, como alumno viejo (w − 1 palabras) o
joven (w / 2 palabras, solo para w par), así que f(2) = 1 y
f(w) = f(w − 1) + f(w / 2) para w par, f(w) = f(w − 1) para w impar. Un
w impar no añade nada, de modo que g(m) = f(2m) = f(2m + 1) cumple
g(1) = 1 y g(m) = g(m − 1) + g(⌊m / 2⌋), y la respuesta es g(⌊K / 2⌋),
o 0 para K = 1. Son los números de particiones binarias, demasiado
grandes para guardarlos exactos, así que todo se reduce módulo P.

Basta una pasada por m hasta K / 2 = 5·10⁶; solo se vuelven a consultar
los valores hasta K / 4, así que solo se guardan esos (un arreglo de
2,5·10⁶ números). La suma de dos restos puede pasar de 2³¹,
así que las sumas usan enteros de 64 bits. `O(K)`.

Detalles a tener en cuenta:

- K = 1: nadie sabe una sola palabra (prueba 02);
- P = 1 hace que toda respuesta sea 0 (prueba 04);
- la suma de dos restos menores que 10⁹ desborda un entero de 32 bits
  con signo (pruebas 06, 07);
- Python se ejecuta con PyPy: K = 10⁷ tarda unos 0,8 s con CPython y
  unos 0,17 s con PyPy.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1537_dp.cpp](1537_dp.cpp) | G++ 13.2 x64 | dp | O(K) | AC | 0.046 s | 9684 KB |
| [1537_dp.go](1537_dp.go) | Go 1.14 x64 | dp | O(K) | AC | 0.109 s | 11700 KB |
| [1537_dp.java](1537_dp.java) | Java 1.8 | dp | O(K) | AC | 0.140 s | 11368 KB |
| [1537_dp.py](1537_dp.py) | PyPy 3.10 x64 | dp | O(K) | AC | 0.203 s | 20812 KB |
| [1537_dp.rs](1537_dp.rs) | Rust 1.75 x64 | dp | O(K) | AC | 0.046 s | 9836 KB |
