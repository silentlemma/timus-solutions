# 1280. Ordenación topológica

[Timus 1280](https://acm.timus.ru/problem.aspx?space=1&num=1280) · dificultad 141 · graphs

Problema original de Sergey Volchenkov, Vladimir Pinaev y Michael Kopachev, del cuarto de final de la región central de Rusia del ACM ICPC 2003–2004, Rybinsk, 15–16 de octubre de 2003.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay N ≤ 1000 asignaturas y M ≤ 100 000 reglas "s u": la asignatura s
debe estudiarse antes que la u. ¿Es el orden dado de las N asignaturas
compatible con todas las reglas?

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

N y M, las M reglas y luego el orden de las N asignaturas.

## Salida

`YES` o `NO`.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 6
1 3
1 4
3 5
5 2
4 2
1 2
1 3 4 5 2
```

Salida:

```
YES
```

### Ejemplo 2

Entrada:

```
5 6
1 3
1 4
3 5
5 2
4 2
1 2
1 2 4 5 3
```

Salida:

```
NO
```

## Solución

No hace falta ordenar nada: se guarda el lugar de cada asignatura en el
orden dado y se comprueba que cada regla va hacia delante, es decir, que
s está antes que u. Si las reglas tienen un ciclo, alguna regla del
ciclo va hacia atrás en cualquier orden, así que la comprobación ya
dice `NO`, como pide el enunciado. `O(N + M)`.

Detalles a tener en cuenta:

- una regla puede ir de una asignatura a sí misma, y ningún orden la
  cumple (prueba 04);
- las reglas pueden repetirse (prueba 07);
- sin reglas cualquier orden vale (prueba 06).

## Notas por lenguaje

- Todos los lenguajes guardan los lugares en un arreglo y recorren las
  reglas una vez.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1280_graphs.cpp](1280_graphs.cpp) | G++ 13.2 x64 | graphs | O(N + M) | AC | 0.109 s | 976 KB |
| [1280_graphs.go](1280_graphs.go) | Go 1.14 x64 | graphs | O(N + M) | AC | 0.125 s | 3416 KB |
| [1280_graphs.java](1280_graphs.java) | Java 1.8 | graphs | O(N + M) | AC | 0.140 s | 1324 KB |
| [1280_graphs.py](1280_graphs.py) | Python 3.12 x64 | graphs | O(N + M) | AC | 0.171 s | 24372 KB |
| [1280_graphs.rs](1280_graphs.rs) | Rust 1.75 x64 | graphs | O(N + M) | AC | 0.015 s | 3688 KB |
