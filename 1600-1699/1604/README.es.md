# 1604. En el País de los Tontos

[Timus 1604](https://acm.timus.ru/problem.aspx?space=1&num=1604) · dificultad 143 · greedy

Problema original de Alexander Ipatov (idea de Alexander Toropov), del IX Campeonato Abierto Individual de la Universidad Estatal de los Urales, 1 de marzo de 2008.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay k tipos de señales de límite de velocidad, nᵢ señales del tipo i y
como mucho 10000 señales en total. Hay que colocarlas todas a lo largo
de una carretera para que los conductores cambien de velocidad lo más a
menudo posible: hay un cambio en la primera señal y en cada señal
distinta de la anterior. Vale cualquier orden óptimo.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

k y luego n₁, …, nₖ.

## Salida

Los tipos de las señales en el orden de la carretera.

## Ejemplos

### Ejemplo 1

Entrada:

```
2
2 2
```

Salida:

```
1 2 1 2
```

## Solución

Cambiar de velocidad lo más a menudo posible significa tener los menos
vecinos iguales posibles. Sea m la mayor cantidad y n el total. Las
otras n − m señales parten las m señales del tipo más común en como
mucho n − m + 1 grupos, así que hay al menos max(0, 2m − n − 1) vecinos
iguales.

Un orden voraz alcanza esa cota: se coloca siempre el tipo con más
señales restantes, salvo que haya sido la señal anterior, y entonces el
tipo con la segunda mayor cantidad. Un montículo da ambos en
`O(log k)`, así que todo el orden cuesta `O(n log k)`.

Las pruebas usan un verificador que cuenta los vecinos iguales y los
compara con la cota. La cota se contrastó con una búsqueda exhaustiva
sobre todos los órdenes de conjuntos pequeños de señales.

Detalles a tener en cuenta:

- cuando un tipo tiene más de la mitad de las señales, los vecinos
  iguales no se pueden evitar, y el voraz los deja juntos al final
  (prueba 05);
- tomar siempre el tipo más común sin mirar la señal anterior lo repite;
  tomar los tipos por turnos sin mirar las cantidades puede agotar los
  otros tipos demasiado pronto (prueba 07).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1604_greedy.cpp](1604_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log k) | AC | 0.015 s | 292 KB |
| [1604_greedy.go](1604_greedy.go) | Go 1.14 x64 | greedy | O(n log k) | AC | 0.031 s | 2184 KB |
| [1604_greedy.java](1604_greedy.java) | Java 1.8 | greedy | O(n log k) | AC | 0.156 s | 3456 KB |
| [1604_greedy.py](1604_greedy.py) | Python 3.12 x64 | greedy | O(n log k) | AC | 0.093 s | 1776 KB |
| [1604_greedy.rs](1604_greedy.rs) | Rust 1.75 x64 | greedy | O(n log k) | AC | 0.015 s | 1044 KB |
