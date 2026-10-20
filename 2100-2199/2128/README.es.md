# 2128. Solitario de filas a montones por palo como orden topológico

[Timus 2128](https://acm.timus.ru/problem.aspx?space=1&num=2128) · dificultad 998 · graphs

Problema original de Alexander Ipatov, preparado por Oleg Dolgorukov, del concurso «Más vale tarde que nunca».

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

Una baraja de m palos con valores 1 … n está dispuesta en k filas. Una
jugada toma la carta de más a la derecha de una fila y la pone en el
montón de su palo, lo que se permite cuando la carta superior del montón
vale uno menos, o el montón está vacío y la carta vale 1. Decidir si se
pueden pasar todas las cartas a los montones e imprimir un orden de
jugadas. Se acepta cualquier orden válido. Los límites son 1 segundo y
128 MB.

## Entrada

m, n y k, 1 ≤ n · m ≤ 10⁵, 1 ≤ k ≤ 10⁵, y luego las filas: aᵢ y aᵢ pares
(palo, valor) de izquierda a derecha.

## Salida

"NO", o "YES" y las cartas en el orden en que se mueven.

## Evaluación

Un comprobador reproduce las jugadas.

## Ejemplos

### Ejemplo 1

Entrada:

```
2 3 2
3 1 3 2 3 1 1
3 1 2 2 2 2 1
```

Salida:

```
YES
1 1
2 1
2 2
2 3
1 2
1 3
```

### Ejemplo 2

Entrada:

```
2 3 2
3 1 3 2 2 1 2
3 1 1 2 3 2 1
```

Salida:

```
NO
```

## Solución

Una carta solo puede moverse después de otras dos, cuando existen: la
carta del mismo palo con un valor menos, que debe estar en el montón, y
la carta a su derecha en la fila, que ya debe haberse ido. No hay más
condiciones, así que una sucesión de jugadas es válida exactamente
cuando pone cada carta después de sus dos predecesoras.

Eso es un orden topológico de un grafo con a lo sumo dos aristas
entrantes por carta. El algoritmo de Kahn empieza por las cartas sin
predecesora (los 1 al final derecho de su fila) y libera la siguiente
carta del palo y la vecina izquierda de la fila a medida que quedan
libres. Si llega a todas las cartas, el orden es la respuesta; si no, hay
un ciclo y la respuesta es NO. El trabajo es O(nm + k).

En el segundo ejemplo el 1 del palo 1 está tapado por el 3 del palo 2,
que necesita el 2 del palo 2; esa carta está tapada por el 2 del palo 1,
que necesita el 1 del palo 1: un ciclo.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2128_graphs.cpp](2128_graphs.cpp) | G++ 13.2 x64 | graphs | O(nm + k) | AC | 0.062 s | 1612 KB |
| [2128_graphs.go](2128_graphs.go) | Go 1.14 x64 | graphs | O(nm + k) | AC | 0.031 s | 8160 KB |
| [2128_graphs.java](2128_graphs.java) | Java 1.8 | graphs | O(nm + k) | AC | 0.109 s | 8788 KB |
| [2128_graphs.py](2128_graphs.py) | Python 3.12 x64 | graphs | O(nm + k) | AC | 0.312 s | 17992 KB |
| [2128_graphs.rs](2128_graphs.rs) | Rust 1.75 x64 | graphs | O(nm + k) | AC | 0.046 s | 4728 KB |
