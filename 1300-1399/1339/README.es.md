# 1339. Bebés

[Timus 1339](https://acm.timus.ru/problem.aspx?space=1&num=1339) · dificultad 856 · graphs

Problema original de Magaz Asanov, del USU Championship 2004.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una guardería tiene k niños y k niñas, k ≤ 250 000. A cada niño le
gusta como mucho una niña y ninguna niña le gusta a dos niños; del
mismo modo, a cada niña le gusta como mucho un niño y ningún niño le
gusta a dos niñas. Hay que repartir a los pequeños en k parejas
niño–niña de modo que, en cada pareja con alguien que quiere a otra
persona, al niño le guste la niña de la pareja o a la niña le guste el
niño. Se acepta cualquier reparto así.

Límite de tiempo: 1 segundo. Límite de memoria: 64 MB.

## Entrada

k, luego para cada niño el número de la niña que le gusta, o 0, y luego
para cada niña el número del niño que le gusta, o 0.

## Salida

Para cada niño, el número de la niña de su pareja.

## Comprobación

El comprobador acepta cualquier reparto en parejas que cumpla la regla.

## Ejemplos

### Ejemplo 1

Entrada:

```
3
3 0 0
0 2 0
```

Salida:

```
3 2 1
```

## Solución

Se traza una flecha desde cada pequeño hacia quien le gusta. De cada
pequeño sale como mucho una flecha y, como ningún pequeño le gusta a
dos, entra como mucho una, y las flechas siempre unen un niño y una niña. Así
que las flechas forman caminos y ciclos separados que alternan niños y
niñas.

Se recorre cada camino desde su inicio, el pequeño al que nadie quiere,
y se forman parejas de dos en dos a lo largo de él. A todos los del
camino salvo el último les gusta el siguiente, y solo sobra el último
pequeño de un camino de longitud impar, a quien no le gusta nadie. Un
ciclo alterna niños y niñas, así que tiene longitud par y se empareja
entero. Todas las parejas formadas así están unidas por una flecha, de
modo que cumplen la regla. A los que sobran no les gusta nadie, y sobran
tantos niños como niñas, así que pueden emparejarse de cualquier forma:
esa pareja no tiene a nadie que quiera a otra persona. `O(k)`.

Detalles a tener en cuenta:

- un camino de longitud impar debe dejar fuera su final, no su inicio:
  al primero del camino le gusta alguien y tiene que ir en pareja con
  esa persona (prueba 04);
- un único ciclo por los 500 000 pequeños no debe recorrerse con
  recursión (prueba gen2);
- los pequeños libres se emparejan niño con niña, y siempre salen en
  igual número.

Los repartos se comprobaron en 500 casos aleatorios de hasta 10
parejas.

## Notas por lenguaje

- CPython necesita unos 0,7 segundos para 250 000 parejas, demasiado
  cerca del límite de 1 segundo, así que la solución en Python se envía
  con PyPy 3.10, donde tarda unos 0,3 segundos.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [1339_graphs.cpp](1339_graphs.cpp) | G++ 13.2 x64 | graphs | O(k) | AC | 0.328 s | 6632 KB |
| [1339_graphs.go](1339_graphs.go) | Go 1.14 x64 | graphs | O(k) | AC | 0.078 s | 13600 KB |
| [1339_graphs.java](1339_graphs.java) | Java 1.8 | graphs | O(k) | AC | 0.156 s | 18876 KB |
| [1339_graphs.py](1339_graphs.py) | PyPy 3.10 x64 | graphs | O(k) | AC | 0.359 s | 52392 KB |
| [1339_graphs.rs](1339_graphs.rs) | Rust 1.75 x64 | graphs | O(k) | AC | 0.062 s | 31828 KB |
