# 1521. Maniobras militares 2

[Timus 1521](https://acm.timus.ru/problem.aspx?space=1&num=1521) · dificultad 121 · fenwick

Problema original de Ilya Grebnov, Nikita Rybak y Dmitry Kovalioff, de Timus Top Coders: Third Challenge.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N soldados (1 ≤ N ≤ 100000), numerados de 1 a N, marchan en círculo. En
cada ronda sale un soldado: primero el soldado K (1 ≤ K ≤ N), y luego
cada vez el que está K puestos por delante del último en salir,
contando solo los que siguen marchando. Hay que escribir los soldados
en el orden en que salen.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y K.

## Salida

Los números de los soldados en el orden en que salen.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 3
```

Salida:

```
3 1 5 2 4
```

## Solución

Se numeran los soldados que siguen marchando 0, 1, … en el orden del
círculo. Si el último en salir tenía el rango r entre ellos, el
siguiente tiene el rango (r + K − 1) mod (soldados restantes), porque
el puesto del que sale lo ocupa el soldado de detrás. Un árbol de
Fenwick guarda 1 por cada soldado que sigue marchando; descender por
potencias de dos encuentra el soldado de un rango dado en `O(log N)`,
y quitar un soldado es una actualización puntual. `O(N log N)` en
total.

Detalles a tener en cuenta:

- borrar de una lista simple cuesta `O(N)` por ronda, `O(N²)` en total,
  demasiado lento para 100000 soldados (gen1);
- con K = 1 los soldados salen en orden (prueba 03, gen5);
- con K = N empieza el último soldado (prueba 04, gen4).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1521_fenwick.cpp](1521_fenwick.cpp) | G++ 13.2 x64 | fenwick | O(N log N) | AC | 0.031 s | 2136 KB |
| [1521_fenwick.go](1521_fenwick.go) | Go 1.14 x64 | fenwick | O(N log N) | AC | 0.062 s | 2460 KB |
| [1521_fenwick.java](1521_fenwick.java) | Java 1.8 | fenwick | O(N log N) | AC | 0.171 s | 5016 KB |
| [1521_fenwick.py](1521_fenwick.py) | Python 3.12 x64 | fenwick | O(N log N) | AC | 0.640 s | 12028 KB |
| [1521_fenwick.rs](1521_fenwick.rs) | Rust 1.75 x64 | fenwick | O(N log N) | AC | 0.031 s | 2512 KB |
