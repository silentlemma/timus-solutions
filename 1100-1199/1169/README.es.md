# 1169. Una red conexa con exactamente K pares críticos de ordenadores

[Timus 1169](https://acm.timus.ru/problem.aspx?space=1&num=1169) · dificultad 728 · constructive

Problema original de Mugurel Ionut Andreica, del Romanian Open Contest de diciembre de 2001.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Hay que conectar `N ≤ 100` ordenadores con conexiones bidireccionales en
una sola red. Un par de ordenadores es crítico si quitar alguna conexión
los separa. Hay que construir una red con exactamente `K` pares críticos o
indicar que no existe.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

`N` y `K`.

## Salida

Las conexiones, un par de ordenadores por línea, o `-1`.

## Evaluación

Se acepta cualquier red cuyas conexiones sean distintas, unan ordenadores
distintos, los conecten todos y den exactamente `K` pares críticos; el
comprobador busca los puentes y cuenta los pares por sí mismo. `-1` debe
coincidir con la respuesta guardada.

## Ejemplos

### Ejemplo 1

Entrada:

```
7 12
```

Salida:

```
1 2
1 3
2 3
3 4
4 5
4 6
4 7
5 6
5 7
6 7
```

## Solución

Al quitar los puentes de una red conexa queda dividida en partes
2-arista-conexas, y dos ordenadores forman un par no crítico exactamente
cuando están en la misma parte. Una parte tiene un ordenador o al menos
tres (dos ordenadores necesitarían dos conexiones entre ellos), y
cualquier tamaño así se puede realizar: cada parte de tamaño `s ≥ 3` es un
ciclo y las partes se unen en cadena con conexiones sueltas, que son los
puentes. Así que la pregunta es si `N` se puede repartir en tamaños de
`{1, 3, 4, …}` con `Σ s·(s − 1)/2 = N·(N − 1)/2 − K`.

Es una mochila pequeña: `reach[m][t]` dice si `m` ordenadores se pueden
repartir con `t` pares no críticos. Añadir una parte de tamaño `s` lleva
`reach[m − s][t]` a `reach[m][t + s(s − 1)/2]`. Recorriendo hacia atrás
desde `reach[N][target]` se recuperan los tamaños. `O(N²·N²)` pasos de
bits en el peor caso, unos 50 millones, o muchos menos con conjuntos de
bits.

Detalles a tener en cuenta:

- no existe una parte de dos ordenadores, así que por ejemplo un triángulo
  más un árbol es posible, pero un único par no crítico no;
- con `N = 1` no hace falta ninguna conexión y el único `K` posible es 0;
- un árbol hace críticos todos los pares, un solo ciclo ninguno.

Todos los veredictos se compararon con una solución escrita aparte para
todo `K` con `N ≤ 12` y para 300 pares aleatorios hasta `N = 100`, y cada
red impresa pasó el comprobador.

## Notas por lenguaje

- C++ guarda cada `reach[m]` como bitset y Python como entero grande, así
  que una parte se añade con un desplazamiento; Go, Java y Rust usan
  tablas booleanas normales.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1169_constructive.cpp](1169_constructive.cpp) | G++ 13.2 x64 | constructive | O(N⁴) bit steps | AC | 0.015 s | 252 KB |
| [1169_constructive.go](1169_constructive.go) | Go 1.14 x64 | constructive | O(N⁴) bit steps | AC | 0.062 s | 1676 KB |
| [1169_constructive.java](1169_constructive.java) | Java 1.8 | constructive | O(N⁴) bit steps | AC | 0.250 s | 2152 KB |
| [1169_constructive.py](1169_constructive.py) | Python 3.12 x64 | constructive | O(N⁴) bit steps | AC | 0.093 s | 572 KB |
| [1169_constructive.rs](1169_constructive.rs) | Rust 1.75 x64 | constructive | O(N⁴) bit steps | AC | 0.046 s | 620 KB |
