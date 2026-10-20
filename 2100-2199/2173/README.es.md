# 2173. Contar repartos de patrocinadores, a lo sumo dos por problema

[Timus 2173](https://acm.timus.ru/problem.aspx?space=1&num=2173) · dificultad 831 · dp, combinatorics

Problema original de Vadim Barinov, del Concurso Escolar de Programación de los Urales 2022.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay M problemas y N patrocinadores; el patrocinador i debe aparecer en
exactamente sᵢ problemas distintos, y un problema puede mencionar a lo
sumo dos patrocinadores. Contar los repartos módulo 10⁹ + 7; dos
repartos difieren si algún problema recibe otro conjunto de
patrocinadores. Los límites son 2 segundos y 256 MB.

## Entrada

N y M, 1 ≤ N ≤ 1000, 1 ≤ M ≤ 2000, y luego s₁ … s_N con 1 ≤ sᵢ ≤ M y un
total de a lo sumo 2M.

## Salida

El número de repartos módulo 10⁹ + 7.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 2
1 1
```

Salida:

```
4
```

### Ejemplo 2

Entrada:

```
5 13
1 1 1 1 1
```

Salida:

```
351780
```

## Solución

Se añaden los patrocinadores uno a uno. Con t menciones colocadas, los
problemas quedan en tres grupos: j tienen un patrocinador, (t − j) / 2
tienen dos y el resto están vacíos. Para los siguientes patrocinadores
solo importa qué problema está en qué grupo, así que el estado es solo
j.

El siguiente patrocinador, con deseo s, toma a problemas que ya tienen
un patrocinador y s − a vacíos, lo que se elige de C(j, a) · C(e, s − a)
formas, siendo e el número de problemas vacíos. El nuevo estado es
j − a + (s − a). La respuesta es la suma sobre todos los estados
finales.

El estado tiene la paridad de t, así que hay a lo sumo M / 2 + 1 estados
vivos, y un patrocinador con deseo s cuesta O(M · s) transiciones. En
total es O(M · Σ sᵢ) = O(M²), con factoriales e inversos preparados una
vez.

En el primer ejemplo los dos patrocinadores comparten un problema (dos
formas) o toman uno cada uno (otras dos), cuatro en total.

## Notas por lenguaje

La solución en Python corre en PyPy 3.10; en CPython los 5 · 10⁶ pasos
interiores tardan alrededor de un segundo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2173_dp_combinatorics.cpp](2173_dp_combinatorics.cpp) | G++ 13.2 x64 | dp, combinatorics | O(M sum s) | AC | 0.031 s | 256 KB |
| [2173_dp_combinatorics.go](2173_dp_combinatorics.go) | Go 1.14 x64 | dp, combinatorics | O(M sum s) | AC | 0.062 s | 12392 KB |
| [2173_dp_combinatorics.java](2173_dp_combinatorics.java) | Java 1.8 | dp, combinatorics | O(M sum s) | AC | 0.375 s | 6288 KB |
| [2173_dp_combinatorics.py](2173_dp_combinatorics.py) | PyPy 3.10 x64 | dp, combinatorics | O(M sum s) | AC | 0.218 s | 6836 KB |
| [2173_dp_combinatorics.rs](2173_dp_combinatorics.rs) | Rust 1.75 x64 | dp, combinatorics | O(M sum s) | AC | 0.046 s | 312 KB |
