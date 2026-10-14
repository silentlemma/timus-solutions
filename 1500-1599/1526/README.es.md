# 1526. Platos marcianos

[Timus 1526](https://acm.timus.ru/problem.aspx?space=1&num=1526) · dificultad 1326 · dp

Problema original de Dmitry Gozman, del Dmitry Gozman Contest 1 en el campus de invierno de Petrozavodsk, enero de 2007.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una cena de fiesta tiene t/2 platos (2 ≤ t ≤ 200, t par) elegidos entre
n clases (1 ≤ n ≤ 10), con repeticiones. Un camarero trae platos y se
lleva los vacíos; se apilan, y solo se puede llevar el de arriba. m
pares (0 ≤ m ≤ 100) «i j» prohíben traer el plato j mientras haya en
cualquier lugar de la mesa un plato de i. Hay que contar los horarios
de t acciones (traer un plato de alguna clase o llevarse el de arriba)
módulo p (2 ≤ p ≤ 10⁴).

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

p, t, n y m, y luego los m pares.

## Salida

El número de horarios módulo p.

## Ejemplos

### Ejemplo 1

Entrada:

```
10000 4 2 1
1 2
```

Salida:

```
7
```

### Ejemplo 2

Entrada:

```
9999 6 10 2
2 3
6 7
```

Salida:

```
4866
```

## Solución

Un horario es un bosque de platos: sobre cada plato se anidan los
traídos mientras estaba en la mesa. Si un plato puede traerse depende
solo del conjunto de clases aún permitidas, que empieza con todas y,
sobre un plato de clase x, se reduce a su parte no prohibida por x. Sea
F[S][q] el número de horarios de q platos con el conjunto S permitido.
El primer plato es algún x de S con a platos encima, contados por
F[S ∩ after(x)][a], y los otros q − 1 − a platos le siguen con S aún
permitido: F[S][q] = Σ sobre a de G[S][a] · F[S][q − 1 − a], con
G[S][a] = Σ sobre x de S de F[S ∩ after(x)][a]. Solo hacen falta los
conjuntos alcanzables desde el completo; uno menor va antes, y un
conjunto puede referirse a sí mismo con un q menor. Como mucho 2¹⁰
conjuntos dan `O(2^n·t·(n+t))`.

Detalles a tener en cuenta:

- un par prohíbe el plato mientras el otro está en cualquier lugar de
  la mesa, no solo arriba (prueba 04, gen2);
- el par «i j» prohíbe traer j sobre i, no al revés (prueba 08);
- un plato puede estar prohibido sobre sí mismo, y entonces sus platos
  nunca se apilan (prueba 05);
- pueden aparecer los 1024 conjuntos de clases (prueba 04, gen2);
- el mismo par puede darse dos veces (prueba 07).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1526_dp.cpp](1526_dp.cpp) | G++ 13.2 x64 | dp | O(2^n * t * (n + t)) | AC | 0.001 s | 244 KB |
| [1526_dp.go](1526_dp.go) | Go 1.14 x64 | dp | O(2^n * t * (n + t)) | AC | 0.031 s | 1208 KB |
| [1526_dp.java](1526_dp.java) | Java 1.8 | dp | O(2^n * t * (n + t)) | AC | 0.140 s | 2992 KB |
| [1526_dp.py](1526_dp.py) | Python 3.12 x64 | dp | O(2^n * t * (n + t)) | AC | 0.109 s | 748 KB |
| [1526_dp.rs](1526_dp.rs) | Rust 1.75 x64 | dp | O(2^n * t * (n + t)) | AC | 0.015 s | 276 KB |
