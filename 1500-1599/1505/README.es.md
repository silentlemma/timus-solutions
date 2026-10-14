# 1505. Bombeo de petróleo

[Timus 1505](https://acm.timus.ru/problem.aspx?space=1&num=1505) · dificultad 2815 · graphs

Problema original de Magaz Asanov y Evgeny Krokhalev, del cuarto de final de Ekaterimburgo del XXXI ACM ICPC, 2006.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

N estaciones de bombeo (1 ≤ N ≤ 10000) están unidas por como mucho
100000 oleoductos de un solo sentido. Un oleoducto de i a a tiene
capacidad b, flujo actual c (0 ≤ c ≤ b ≤ 10000) y un precio d
(0 ≤ d ≤ 10⁶) por cada unidad extra de capacidad. El petróleo sale de
la red solo por la estación N, que no tiene oleoductos de salida. Cada
otra estación recibe como mucho lo que envía; donde recibe menos, un
pozo cercano puede producir una unidad más. Hay que aumentar en una
unidad el flujo que entra en la estación N con el menor coste y
escribir el coste y los nuevos flujos, o «Impossible».

Límite de tiempo: 2 segundos. Límite de memoria: 64 MB.

## Entrada

N y luego una línea por estación: sus oleoductos como cuádruplas
a b c d separadas por comas y terminadas en punto; una estación sin
oleoductos tiene solo un punto.

## Salida

El coste mínimo y luego una línea por estación con sus oleoductos como
pares «a flujo» separados por comas y terminados en punto; o
«Impossible». Se acepta cualquier cambio de coste mínimo.

## Ejemplos

### Ejemplo 1

Entrada:

```
4
2 1 1 1, 3 1 1 3.
3 1 0 2, 4 1 1 2.
4 1 1 1.
.
```

Salida:

```
2
2 2, 3 1.
3 1, 4 1.
4 2.
.
```

## Solución

La unidad extra recorre un camino de una estación con pozo a la
estación N en la red residual. Por un oleoducto i → a puede ir hacia
delante gratis si le queda capacidad y por d si está lleno, porque
entonces su capacidad crece en uno. También puede ir hacia atrás, de a
a i, gratis siempre que el oleoducto lleve flujo: enviar una unidad
menos desde i la deja libre en i. Todos los precios son no negativos,
así que el algoritmo de Dijkstra desde todas las estaciones con pozo a
la vez halla el camino más barato; luego se vuelve desde N y se cambia
en uno el flujo de cada oleoducto del camino. `O((N + M) log N)` con M
oleoductos.

Si existe algún pozo, su excedente tiene que llegar a N por oleoductos
con flujo, lo cual es un camino, así que la respuesta es «Impossible»
justo cuando ninguna estación tiene pozo.

Detalles a tener en cuenta:

- el flujo que solo da vueltas por un ciclo no crea pozos, y no hay
  respuesta (prueba 03);
- la ruta más barata puede hacer retroceder el flujo de un oleoducto
  (prueba 04);
- ampliar un oleoducto lleno con d = 0 no cuesta nada (prueba 05);
- el coste puede llegar a 10⁴ · 10⁶ = 10¹⁰, más de 32 bits (gen5);
- los oleoductos de una estación terminan en punto, así que la entrada
  se lee mejor por su puntuación que por líneas (todas las pruebas);
- puede haber muchos cambios de coste mínimo, así que las pruebas usan
  un comprobador (todas las pruebas).

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1505_graphs.cpp](1505_graphs.cpp) | G++ 13.2 x64 | graphs | O((N + M) log N) | AC | 0.437 s | 11176 KB |
| [1505_graphs.go](1505_graphs.go) | Go 1.14 x64 | graphs | O((N + M) log N) | AC | 0.062 s | 22972 KB |
| [1505_graphs.java](1505_graphs.java) | Java 1.8 | graphs | O((N + M) log N) | AC | 0.218 s | 21788 KB |
| [1505_graphs.py](1505_graphs.py) | Python 3.12 x64 | graphs | O((N + M) log N) | AC | 0.500 s | 43480 KB |
| [1505_graphs.rs](1505_graphs.rs) | Rust 1.75 x64 | graphs | O((N + M) log N) | AC | 0.062 s | 14332 KB |
