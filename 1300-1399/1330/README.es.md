# 1330. Intervalos

[Timus 1330](https://acm.timus.ru/problem.aspx?space=1&num=1330) · dificultad 95 · prefix_sums

Problema original de Den Raskovalov, del Décimo Campeonato por Equipos de Programación para Escolares de la Región de Sverdlovsk, 16 de octubre de 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N ≤ 10 000 sensores dan lecturas enteras de −10 000 a 10 000. Hay que
responder hasta 100 000 preguntas: la suma de las lecturas de los
sensores i a j, con i ≤ j.

Límite de tiempo: 0,5 segundos. Límite de memoria: 64 MB.

## Entrada

N, luego N lecturas, luego Q y Q pares i, j.

## Salida

Una suma por línea.

## Ejemplos

### Ejemplo 1

Entrada:

```
5
1
2
3
-1
4
3
1 5
4 4
1 4
```

Salida:

```
9
-1
5
```

## Solución

Se guarda before[i], la suma de las primeras i lecturas, con
before[0] = 0. La suma de i a j es before[j] − before[i − 1], una resta
por pregunta. `O(N + Q)`.

Detalles a tener en cuenta:

- las sumas están entre −10⁸ y 10⁸, lo que cabe en un entero de 32
  bits;
- puede no haber ninguna pregunta (prueba 03);
- con 100 000 preguntas, la entrada y la salida se leen y escriben en
  bloques grandes para no pasar de 0,5 segundos.

## Notas por lenguaje

- Java lee la entrada con su propio búfer de bytes y reúne las
  respuestas en una sola cadena.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1330_prefix_sums.cpp](1330_prefix_sums.cpp) | G++ 13.2 x64 | prefix_sums | O(N + Q) | AC | 0.125 s | 2784 KB |
| [1330_prefix_sums.go](1330_prefix_sums.go) | Go 1.14 x64 | prefix_sums | O(N + Q) | AC | 0.046 s | 2828 KB |
| [1330_prefix_sums.java](1330_prefix_sums.java) | Java 1.8 | prefix_sums | O(N + Q) | AC | 0.109 s | 7492 KB |
| [1330_prefix_sums.py](1330_prefix_sums.py) | Python 3.12 x64 | prefix_sums | O(N + Q) | AC | 0.125 s | 27608 KB |
| [1330_prefix_sums.rs](1330_prefix_sums.rs) | Rust 1.75 x64 | prefix_sums | O(N + Q) | AC | 0.046 s | 3736 KB |
