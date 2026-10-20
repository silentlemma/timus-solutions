# 2172. Menos problemas para colocar las menciones de todos los patrocinadores

[Timus 2172](https://acm.timus.ru/problem.aspx?space=1&num=2172) · dificultad 734 · greedy, constructive

Problema original de Valentin Zuev, del Concurso Escolar de Programación de los Urales 2022.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

El patrocinador i quiere aparecer en exactamente sᵢ problemas distintos,
y ningún problema puede mencionar a más de K patrocinadores distintos.
Hallar el menor número de problemas M y un plan con los patrocinadores
de cada problema. Se acepta cualquier plan válido. Los límites son 1
segundo y 256 MB.

## Entrada

N y K, 1 ≤ N, K ≤ 1000, y luego s₁ … s_N, 1 ≤ sᵢ ≤ 1000, con un total de
a lo sumo 10⁵.

## Salida

M, y luego para cada problema el número de sus patrocinadores y sus
números.

## Evaluación

Un comprobador verifica M y que el plan cumple todos los deseos y
límites.

## Ejemplos

### Ejemplo 1

Entrada:

```
5 2
1 1 1 1 1
```

Salida:

```
3
1 5
2 2 3
2 4 1
```

## Solución

Hay dos cotas inferiores claras: el patrocinador con el mayor deseo
necesita tantos problemas distintos, y las S = Σ sᵢ menciones necesitan
al menos ⌈S / K⌉ problemas. Así que M ≥ max(max sᵢ, ⌈S / K⌉), y con eso
basta.

Se escriben todas las menciones en fila, patrocinador tras patrocinador,
y se reparten a los problemas por turnos: la mención t va al problema
t mod M. Las menciones de un patrocinador son consecutivas y no pasan de
M, así que caen en problemas distintos. Cada problema recibe a lo sumo
⌈S / M⌉ ≤ K menciones. El trabajo es O(S).

En el ejemplo cinco patrocinadores con un deseo cada uno necesitan
⌈5 / 2⌉ = 3 problemas.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2172_greedy_constructive.cpp](2172_greedy_constructive.cpp) | G++ 13.2 x64 | greedy, constructive | O(S) | AC | 0.062 s | 3732 KB |
| [2172_greedy_constructive.go](2172_greedy_constructive.go) | Go 1.14 x64 | greedy, constructive | O(S) | AC | 0.031 s | 4724 KB |
| [2172_greedy_constructive.java](2172_greedy_constructive.java) | Java 1.8 | greedy, constructive | O(S) | AC | 0.156 s | 17408 KB |
| [2172_greedy_constructive.py](2172_greedy_constructive.py) | Python 3.12 x64 | greedy, constructive | O(S) | AC | 0.187 s | 18848 KB |
| [2172_greedy_constructive.rs](2172_greedy_constructive.rs) | Rust 1.75 x64 | greedy, constructive | O(S) | AC | 0.046 s | 8796 KB |
