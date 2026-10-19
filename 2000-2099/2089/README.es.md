# 2089. Elegir ganadores sin que ningún equipo gane dos veces

[Timus 2089](https://acm.timus.ru/problem.aspx?space=1&num=2089) · dificultad 949 · graphs, greedy

Problema original de Alexander Ipatov, preparado por Egor Shchelkonogov.

[English](README.md) · [Русский](README.ru.md) · [中文](README.zh.md) · **Español**

## Tarea

k equipos juegan n parejas; cada equipo juega de una a tres parejas.
Elegir el ganador de cada pareja, uno de sus dos equipos, de modo que
ningún equipo gane dos parejas, o informar de que es imposible. Se
acepta cualquier elección válida. Los límites son 2 segundos y 256 MB.

## Entrada

n y k, 1 ≤ n ≤ 10⁵, 2 ≤ k ≤ 10⁵, y después las n parejas.

## Salida

`Yes` y los ganadores de las parejas en orden, o `No`.

## Evaluación

Un comprobador acepta `No` solo cuando la salida esperada lo dice, y si
no comprueba que cada ganador juega en su pareja y gana una sola vez.

## Ejemplos

### Ejemplo 1

Entrada:

```
3 4
1 2
2 3
1 4
```

Salida:

```
Yes
1
2
4
```

### Ejemplo 2

Entrada:

```
6 4
1 2
1 3
1 4
2 3
2 4
3 4
```

Salida:

```
No
```

## Solución

Los equipos son vértices y las parejas aristas; elegir ganadores es
orientar cada arista hacia uno de sus extremos de modo que cada vértice
reciba a lo sumo una arista. Una parte conexa con más aristas que
vértices no se puede, y una con a lo sumo tantas sí: es un árbol, o un
árbol más una arista, que tiene exactamente un ciclo.

La construcción arranca hojas. Un equipo con una sola pareja sin decidir
la gana; eso nunca estorba, pues el equipo no tiene otro uso, y el otro
equipo de la pareja pierde una pareja sin decidir y quizá se vuelve hoja
a su vez. Cuando no quedan hojas, cada equipo restante tiene cero o al
menos dos parejas sin decidir. Si alguno aún tiene tres, su parte tiene
demasiadas aristas y la respuesta es No. Si no, las parejas restantes
forman ciclos disjuntos, y recorrer cada ciclo da cada pareja al equipo
al que lleva, así que cada equipo del ciclo gana exactamente una. Con
grados a lo sumo tres todo es O(n + k).

En el segundo ejemplo cuatro equipos juegan seis parejas, más de las que
pueden ganar, así que la respuesta es No.

## Soluciones

| Solución | Lenguaje | Enfoque | Complejidad | Veredicto | Tiempo | Memoria |
|----------|----------|---------|-------------|-----------|--------|---------|
| [2089_graphs_greedy.cpp](2089_graphs_greedy.cpp) | G++ 13.2 x64 | graphs, greedy | O(n + k) | AC | 0.234 s | 6492 KB |
| [2089_graphs_greedy.go](2089_graphs_greedy.go) | Go 1.14 x64 | graphs, greedy | O(n + k) | AC | 0.109 s | 13268 KB |
| [2089_graphs_greedy.java](2089_graphs_greedy.java) | Java 1.8 | graphs, greedy | O(n + k) | AC | 0.250 s | 20632 KB |
| [2089_graphs_greedy.py](2089_graphs_greedy.py) | Python 3.12 x64 | graphs, greedy | O(n + k) | AC | 0.578 s | 51484 KB |
| [2089_graphs_greedy.rs](2089_graphs_greedy.rs) | Rust 1.75 x64 | graphs, greedy | O(n + k) | AC | 0.093 s | 13104 KB |
