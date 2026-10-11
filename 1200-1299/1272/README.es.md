# 1272. Un metro que no es el de Ekaterimburgo

[Timus 1272](https://acm.timus.ru/problem.aspx?space=1&num=1272) · dificultad 147 · dsu

Problema original de Magaz Asanov (preparado por Igor Goldberg), del Campeonato de la Universidad Estatal de los Urales, 25 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una ciudad está sobre N ≤ 10 000 islas unidas por K ≤ 12 000 túneles y
M ≤ 12 000 puentes, y entre todos conectan todas las islas. Un metro
debe conectar todas las islas usando algunos de estos enlaces, con el
menor número posible de puentes. ¿Cuántos puentes necesita?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N, K y M, luego K túneles y M puentes, cada uno como dos números de
isla.

## Salida

El menor número de puentes.

## Ejemplos

### Ejemplo 1

Entrada:

```
6 3 4
1 2
2 3
4 5
1 3
3 4
4 6
5 6
```

Salida:

```
2
```

## Solución

Los túneles no cuestan nada, así que se toman todos: dividen las islas
en grupos ya conectados. Cada puente puede unir como mucho dos grupos en
uno y, como toda la red es conexa, siempre se pueden elegir puentes que
unan los grupos de uno en uno. La respuesta es el número de grupos por
túneles menos uno, contado con una estructura de unión-búsqueda sobre
los túneles; los puentes ni siquiera hace falta leerlos.
`O((N + K) α(N))`.

Detalles a tener en cuenta:

- los puentes no importan, solo que conectan los grupos, cosa que el
  enunciado garantiza;
- los túneles pueden repetirse o unir una isla consigo misma
  (prueba 05);
- con una sola isla, o si los túneles ya lo conectan todo, la respuesta
  es 0 (pruebas 02, 04).

## Notas por lenguaje

- Todos los lenguajes usan la misma unión-búsqueda con reducción de
  caminos a la mitad.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1272_dsu.cpp](1272_dsu.cpp) | G++ 13.2 x64 | dsu | O((N + K) α(N)) | AC | 0.031 s | 228 KB |
| [1272_dsu.go](1272_dsu.go) | Go 1.14 x64 | dsu | O((N + K) α(N)) | AC | 0.015 s | 1428 KB |
| [1272_dsu.java](1272_dsu.java) | Java 1.8 | dsu | O((N + K) α(N)) | AC | 0.140 s | 488 KB |
| [1272_dsu.py](1272_dsu.py) | Python 3.12 x64 | dsu | O((N + K) α(N)) | AC | 0.093 s | 3328 KB |
| [1272_dsu.rs](1272_dsu.rs) | Rust 1.75 x64 | dsu | O((N + K) α(N)) | AC | 0.046 s | 732 KB |
